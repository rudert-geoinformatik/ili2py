import logging
from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Tuple, Optional, Union

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    AttrOrParam,
    AxisSpec,
    BlackboxType,
    BooleanType,
    EnumNode,
    EnumTreeValueType,
    EnumType,
    FormattedType,
    MetaElementTypeDocumentation,
    Model,
    ModelData,
    MultiValue,
    NumType,
    SubModel,
    TextType,
    MetaElementType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    Class as ImdClass,
    Role as ImdRole,
    CoordType as ImdCoordType,
    LineType as ImdLineType,
    MetaAttribute as ImdMetaAttribute,
)
from ili2py.mappers.helpers import Index

base_type_dictionary = {
    "TextType": "str",
    "FormattedType": "str",
    "BlackboxType": "bytes",
    "NumType": "float",
    "BooleanType": "bool",
}


@dataclass
class MetaAttribute:
    name: str
    value: str


@dataclass
class Base(ABC):
    name: str
    identifier: str
    doc: list[str]
    meta_attributes: list[MetaAttribute]

    @staticmethod
    def doc_string(documentation: list[MetaElementTypeDocumentation]):
        """
        Creates a list of documentation strings.
        Args:
            documentation: The documentation which will be flattened

        Returns:
            The flattened version of the given documentation.
        """
        return [item.doc_text.text for item in documentation]

    @staticmethod
    def get_element_of_type_from_list(
        element_type: Any,
        element_list: list[Any],
        kinds: list[str] | None = None,
    ) -> list[Any]:
        """
        Finds the elements which match the desired type.

        Args:
            element_type: The type to look for
            element_list: The list which should be scanned for the type.
            kind: Optional match parameter for kind (default: None).

        Returns:
            The list of elements which match the desired type. Will be empty list if no matches were found.
        """
        matching_elements = []
        for element in element_list:
            if isinstance(element, element_type):
                if kinds is not None:
                    if element.kind in kinds:
                        matching_elements.append(element)
                else:
                    matching_elements.append(element)
        return matching_elements

    @staticmethod
    def assemble_meta_attributes(index: Index, meta_element_tid: str) -> list[MetaAttribute]:
        meta_attributes = []
        if meta_element_tid in index.metaelement_metaattributes:
            for item in index.metaelement_metaattributes[meta_element_tid]:
                imd_meta_attribute: ImdMetaAttribute = index.index[item]
                meta_attributes.append(
                    MetaAttribute(name=imd_meta_attribute.name, value=imd_meta_attribute.value)
                )
        return meta_attributes


@dataclass
class Attribute(Base):
    """Represents imd AttrOrParam"""

    type: str
    type_restrictions: str = field(default_factory=list)
    enumeration: Optional["Enumeration"] = field(default=None)
    line_type: Optional["LineType"] = field(default=None)

    @staticmethod
    def check_float_kind(representation: str | None) -> bool:
        """
        Checks if a passed string of IMD16 number kinds can be interpreted as float.

        Args:
            representation: The numeric representation (e.g. 1000.00 or 1000 or -1000.000)

        Returns:
            True if it can be interpreted as float kind, False if not.
        """
        if representation:
            return len(representation.split(".")) == 2
        else:
            return False

    @staticmethod
    def handle_type_trail(
        imd_type: (
            TextType
            | FormattedType
            | BlackboxType
            | NumType
            | BooleanType
            | MultiValue
            | EnumType
            | ImdCoordType
            | ImdLineType
        ),
        index: Index,
    ) -> Tuple[str, bool]:
        """
        This method handles type resolution. When possible it returns a simple type name of Python (e.g. str,
        int, bool, etc.). When it is not possible to return a simple type, the OID of the linked type will
        be returned.

        Args:
            imd_type: The type which should be looked up
            index: The index which can be used to look up the type and maybe follow the path till the acutal
                type is found.

        Returns:
            The string representing the type and flag if returned string is a OID or not (might be looked up
            in index).
        """
        if isinstance(imd_type, TextType):
            return "str", False
        elif isinstance(imd_type, FormattedType):
            if imd_type.super and imd_type.name == "TYPE":
                return Attribute.handle_type_trail(index.index[imd_type.super.ref], index)
            else:
                return "str", False
        elif isinstance(imd_type, BlackboxType):
            return "str", False
        elif isinstance(imd_type, NumType):
            float_kind = Attribute.check_float_kind(imd_type.min) or Attribute.check_float_kind(
                imd_type.max
            )
            if float_kind:
                return "float", False
            else:
                return "int", False
        elif isinstance(imd_type, BooleanType):
            return "bool", False
        elif isinstance(imd_type, ImdCoordType):
            if imd_type.name == "TYPE" and imd_type.super:
                return Attribute.handle_type_trail(index.index[imd_type.super.ref], index)
            else:
                return imd_type.tid, True
        elif isinstance(imd_type, ImdLineType):
            if imd_type.name == "TYPE" and imd_type.super:
                return Attribute.handle_type_trail(index.index[imd_type.super.ref], index)
            else:
                return imd_type.tid, True
        elif isinstance(imd_type, MultiValue):
            return imd_type.base_type.ref, True
        elif isinstance(imd_type, EnumType):
            if imd_type.name == "TYPE" and imd_type.super:
                return Attribute.handle_type_trail(index.index[imd_type.super.ref], index)
            else:
                return imd_type.tid, True
        elif isinstance(imd_type, EnumTreeValueType):
            return imd_type.tid, True
        else:
            logging.debug(
                f"Type was not handled correctly for Python-Class-Generation preparation: {imd_type}"
            )
            return "UNKNOWN", False

    @staticmethod
    def derive_precision(representation: str) -> int:
        """
        Derives the precision of a float string representation (e.g. "1000.00" -> 2).
        Args:
            representation: The string representing a float.

        Returns:
            The preciscion of the float.
        """
        return len(representation.split(".")[1])

    @classmethod
    def construct_type_restrictions(
        cls,
        attribute_name: str,
        imd_type: (
            TextType
            | FormattedType
            | BlackboxType
            | NumType
            | BooleanType
            | MultiValue
            | EnumType
            | ImdCoordType
        ),
    ) -> str | None:
        if isinstance(imd_type, TextType):
            if imd_type.max_length is not None:
                return str({"max_length": imd_type.max_length})
        elif isinstance(imd_type, NumType):
            type_restrictions = {}
            float_kind = Attribute.check_float_kind(imd_type.min) or Attribute.check_float_kind(
                imd_type.max
            )
            if imd_type.min is not None:
                if float_kind:
                    min = float(imd_type.min)
                    type_restrictions["precision"] = Attribute.derive_precision(imd_type.min)
                else:
                    min = int(imd_type.min)
                type_restrictions["min"] = min
            if imd_type.max is not None:
                if float_kind:
                    max = float(imd_type.max)
                    max_precision = Attribute.derive_precision(imd_type.max)
                    if max_precision != type_restrictions["precision"]:
                        logging.debug(f"NumType precision was not as expected: {imd_type}")
                else:
                    max = int(imd_type.max)
                type_restrictions["max"] = max
            return str(type_restrictions) if type_restrictions else None
        else:
            logging.debug(f"Type was not handled by range assertions: {imd_type}")
            return None

    @staticmethod
    def handle_local_types_and_multivalues(
        index, resolved_type_name, referenced_type, attr_or_param, referenced_class
    ):
        local_type = None
        resolved_type = index.index.get(resolved_type_name)
        if not resolved_type:
            # type name is already a type which is not part of original imd tree, we manipulated it in
            # previous steps and assume here, that we can savely use it
            return resolved_type_name, local_type
        if isinstance(referenced_type, MultiValue):
            final_type_name = f"list['{resolved_type_name}']"
        elif isinstance(referenced_type, EnumType) and referenced_type.name == "TYPE":
            if referenced_type.name == resolved_type.name:
                class_name = f"{attr_or_param.name}Enum"
                final_type_name = f"'{referenced_class.name}.{class_name}'"
                local_type = Enumeration.from_imd(referenced_type, index)
                local_type.name = class_name
            else:
                final_type_name = resolved_type_name
        elif isinstance(referenced_type, ImdLineType) and referenced_type.name == "TYPE":
            if referenced_type.name == resolved_type.name:
                class_name = f"{attr_or_param.name}LineType"
                final_type_name = f"'{referenced_class.name}.{class_name}'"
                local_type = LineType.from_imd(referenced_type, index)
                local_type.name = class_name
            else:
                final_type_name = resolved_type_name
        else:
            final_type_name = resolved_type_name
        return final_type_name, local_type

    @classmethod
    def from_imd(
        cls,
        imd_attr_or_param: AttrOrParam,
        imd_model_data: ModelData,
        index: Index,
    ):
        referenced_type = index.index[imd_attr_or_param.type_value.ref]
        if imd_attr_or_param.attr_parent:
            referenced_class = index.index[imd_attr_or_param.attr_parent.ref]
        else:
            referenced_class = index.index[imd_attr_or_param.param_parent.ref]
        package = index.index[referenced_class.element_in_package.ref]
        sub_model = None
        if isinstance(package, SubModel):
            sub_model = package
            model = index.index[package.element_in_package.ref]
        else:
            model = package
        mapped_type, is_oid = cls.handle_type_trail(referenced_type, index)
        attribute_name = imd_attr_or_param.name
        meta_attributes = cls.assemble_meta_attributes(index, imd_attr_or_param.tid)
        resolved_type_name = Attribute.handle_type(
            index,
            mapped_type,
            imd_attr_or_param,
            referenced_class,
            model,
            referenced_type,
            is_oid=is_oid,
            sub_model=sub_model,
        )
        final_type_name, local_type = Attribute.handle_local_types_and_multivalues(
            index, resolved_type_name, referenced_type, imd_attr_or_param, referenced_class
        )
        return cls(
            identifier=imd_attr_or_param.tid,
            name=attribute_name,
            type=final_type_name,
            doc=cls.doc_string(imd_attr_or_param.documentation),
            type_restrictions=cls.construct_type_restrictions(attribute_name, referenced_type),
            meta_attributes=meta_attributes,
            enumeration=local_type if isinstance(local_type, Enumeration) else None,
            line_type=local_type if isinstance(local_type, LineType) else None,
        )

    @staticmethod
    def handle_type(
        index: Index,
        type_name: str,
        parent_attribute: AttrOrParam,
        parent_class: ImdClass,
        model: Model,
        referenced_type: (
            TextType
            | FormattedType
            | BlackboxType
            | NumType
            | BooleanType
            | MultiValue
            | EnumType
            | ImdCoordType
        ),
        is_oid: bool | None = None,
        sub_model: SubModel | None = None,
    ) -> str:
        if is_oid:
            imd_type = index.index[type_name]
            if imd_type.element_in_package:
                package_of_type_name = index.index[imd_type.element_in_package.ref].name
                if sub_model:
                    if sub_model.name == package_of_type_name:
                        type_name = imd_type.name
                else:
                    if model.name == package_of_type_name:
                        type_name = imd_type.name
            elif isinstance(imd_type, MultiValue):
                if imd_type.base_type:
                    return Attribute.handle_type(
                        index,
                        referenced_type.base_type.ref,
                        parent_attribute,
                        parent_class,
                        model,
                        referenced_type,
                        is_oid,
                        sub_model,
                    )
                else:
                    return Attribute.handle_type(
                        index,
                        imd_type.tid,
                        parent_attribute,
                        parent_class,
                        model,
                        referenced_type,
                        is_oid,
                        sub_model,
                    )
        return type_name


@dataclass
class Class(Base):
    """Represents imd Class"""

    super_class: str = field(default=None)
    attributes: list[Attribute] = field(default_factory=list)
    abstract: bool = field(default=False)
    related_class_imports: list[Tuple[str, str]] = field(default_factory=list)
    enumerations: list["Enumeration"] = field(default_factory=list)

    @classmethod
    def from_imd(cls, imd_class: ImdClass, imd_model_data: ModelData, index: Index):
        attributes = []
        for imd_attr_or_param in cls.get_element_of_type_from_list(
            AttrOrParam, imd_model_data.choice
        ):
            if imd_attr_or_param.attr_parent:
                if imd_attr_or_param.attr_parent.ref == imd_class.tid:
                    attribute = Attribute.from_imd(imd_attr_or_param, imd_model_data, index)
                    attributes.append(attribute)
        related_class_imports = []
        if imd_class.tid in index.association_to_class_ref_attributes:
            for role_tid, related_class_tid in index.association_to_class_ref_attributes[
                imd_class.tid
            ]:
                role: ImdRole = index.index[role_tid]
                related_class: ImdClass = index.index[related_class_tid]
                meta_attributes = cls.assemble_meta_attributes(index, role.tid)
                attributes.append(
                    Attribute(
                        name=role.name,
                        identifier=role.tid,
                        doc=cls.doc_string(role.documentation),
                        type=f'"{related_class.name}"',
                        meta_attributes=meta_attributes,
                    )
                )
                related_class_imports.append(
                    (
                        ".".join(related_class.tid.split(".")[:-1]),
                        related_class.tid.split(".")[-1],
                        "_".join(related_class.tid.split(".")),
                    )
                )
        meta_attributes = cls.assemble_meta_attributes(index, imd_class.tid)
        super_class_reference = None
        if imd_class.super:
            super_class_reference, super_class_reference_imports = cls.decide_super_reference(
                imd_class.super.ref, imd_class.tid, index
            )
            if super_class_reference_imports:
                related_class_imports.append(super_class_reference_imports)
        return cls(
            identifier=imd_class.tid,
            name=imd_class.name,
            super_class=super_class_reference,
            doc=cls.doc_string(imd_class.documentation),
            attributes=attributes,
            abstract=imd_class.abstract,
            related_class_imports=related_class_imports,
            meta_attributes=meta_attributes,
        )

    @staticmethod
    def decide_super_reference(
        reference: str, class_tid: str, index: Index
    ) -> Tuple[str, Union[Tuple[str, str, str], None]]:
        super_class = index.index[reference]
        super_class_package = index.index[super_class.element_in_package.ref]
        child_class = index.index[class_tid]
        child_class_package = index.index[child_class.element_in_package.ref]
        if isinstance(super_class_package, Model):
            if isinstance(child_class_package, Model):
                if super_class_package.name == child_class_package.name:
                    # both are from same model, so we can simply use the class name as super reference and
                    # dont need any additional imports
                    return super_class.name, None
                else:
                    # The reference is ok, it can be imported and used directly
                    return reference, (reference, None, None)
            elif isinstance(child_class_package, SubModel):
                return reference, (reference, None, None)
            else:
                logging.debug(
                    f"Unexpected type while handling super class constructs of class {child_class}"
                )
        elif isinstance(super_class_package, SubModel):
            super_class_model_package = index.index[super_class_package.element_in_package.ref]
            if isinstance(child_class_package, SubModel):
                child_class_model_package = index.index[child_class_package.element_in_package.ref]
                if (
                    child_class_package.name == super_class_package.name
                    and child_class_model_package.name == super_class_model_package.name
                ):
                    # Super class is from the same package
                    return super_class.name, None
                else:
                    super_class_model_package = index.index[
                        super_class_package.element_in_package.ref
                    ]
                    super_class_reference = f"{super_class_model_package.name}_{super_class_package.name}_{super_class.name}"
                    return super_class_reference, (
                        f"{super_class_model_package.name}.{super_class_package.name}",
                        super_class.name,
                        super_class_reference,
                    )
            else:
                super_class_model_package = index.index[super_class_package.element_in_package.ref]
                super_class_reference = f"{super_class_model_package.name}_{super_class_package.name}_{super_class.name}"
                return super_class_reference, (
                    f"{super_class_model_package.name}.{super_class_package.name}",
                    super_class.name,
                    super_class_reference,
                )
        else:
            logging.debug(
                f"Unexpected type while handling super class constructs of class {child_class}"
            )

    def get_class_name(self):
        return "_".join(self.name.split("."))

    def get_super_name(self):
        return "_".join(self.super_class.split("."))


@dataclass
class CoordAttribute(Attribute):
    reference_system: str = field(default=None)


@dataclass
class CoordType(Base):
    attributes: list[Attribute] = field(default_factory=list)

    @classmethod
    def from_imd(cls, imd_coord_type: ImdCoordType, imd_model_data: ModelData, index: Index):
        attributes = []
        for imd_axis_spec in cls.get_element_of_type_from_list(AxisSpec, imd_model_data.choice):
            if imd_axis_spec.coord_type.ref == imd_coord_type.tid:
                imd_axis = index.index[imd_axis_spec.axis.ref]
                reference_system = None
                if imd_axis.ref_sys:
                    reference_system = index.index[imd_axis.ref_sys.ref].tid
                meta_attributes = cls.assemble_meta_attributes(index, imd_axis.tid)
                mapped_type, is_tid = Attribute.handle_type_trail(imd_axis, index)
                attributes.append(
                    CoordAttribute(
                        identifier=imd_axis.tid,
                        name=imd_axis.name,
                        doc=cls.doc_string(imd_axis.documentation),
                        type=mapped_type,
                        reference_system=reference_system,
                        type_restrictions=CoordAttribute.construct_type_restrictions(
                            imd_axis.name, imd_axis
                        ),
                        meta_attributes=meta_attributes,
                    )
                )
        meta_attributes = cls.assemble_meta_attributes(index, imd_coord_type.tid)
        return cls(
            identifier=imd_coord_type.tid,
            name=imd_coord_type.name,
            doc=cls.doc_string(imd_coord_type.documentation),
            attributes=attributes,
            meta_attributes=meta_attributes,
        )

    @property
    def range_assertions(self) -> list[str]:
        """
        Collects all range assertions of the class and returns it as a plain list.
        Returns:
            Tha flat list of range assertions for the whole class.
        """
        range_assertions = []
        for attribute in self.attributes:
            range_assertions = range_assertions + attribute.range_assertions
        return range_assertions


@dataclass
class LineType(Base):
    attribute: Attribute = field(default_factory=list)
    max_overlap: float = field(default=None)
    straights: bool = field(default=False)
    arcs: bool = field(default=False)

    @classmethod
    def from_imd(cls, imd_line_type: ImdLineType, index: Index):
        attributes = []
        attribute_doc = []
        meta_attributes = []
        if imd_line_type.coord_type:
            coord_type = index.index[imd_line_type.coord_type.ref]
            attribute_doc = cls.doc_string(coord_type.documentation)
            if imd_line_type.element_in_package:
                if imd_line_type.element_in_package.ref == coord_type.element_in_package.ref:
                    # line_type and coordtype_reference in the same package
                    type_name = coord_type.name.split(".")[-1]
                else:
                    # line_type and coordtype_reference NOT in the same package
                    type_name = imd_line_type.coord_type.ref
            else:
                # line_type and coordtype_reference NOT in the same package
                type_name = imd_line_type.coord_type.ref
            meta_attributes = cls.assemble_meta_attributes(index, coord_type.tid)
        else:
            type_name = "Any"
        attribute = Attribute(
            identifier=f"{imd_line_type.tid}_attribute",
            name=imd_line_type.kind.upper(),
            doc=attribute_doc,
            type=type_name,
            meta_attributes=meta_attributes,
        )
        if imd_line_type.kind not in ["Polyline", "DirectedPolyline", "Surface", "Area"]:
            logging.debug(f"LineType kind not recognized {imd_line_type.kind}, {imd_line_type}")
        meta_attributes = cls.assemble_meta_attributes(index, imd_line_type.tid)
        return cls(
            identifier=imd_line_type.tid,
            name=imd_line_type.name,
            doc=cls.doc_string(imd_line_type.documentation),
            attribute=attribute,
            max_overlap=float(imd_line_type.max_overlap) if imd_line_type.max_overlap else None,
            straights=imd_line_type.tid in index.line_form["INTERLIS.STRAIGHTS"],
            arcs=imd_line_type.tid in index.line_form["INTERLIS.ARCS"],
            meta_attributes=meta_attributes,
        )


@dataclass
class Value(Base):
    value: str
    children: list["Value"] = field(default_factory=list)

    @classmethod
    def from_imd(cls, imd_enum_node: EnumNode, index: Index):
        return cls(
            identifier=imd_enum_node.tid,
            name=imd_enum_node.name,
            value=imd_enum_node.name,
            doc=cls.doc_string(imd_enum_node.documentation),
            meta_attributes=[],
        )

    def get_enum_values(self, values: list, current_path: list, tree: bool = False):
        if tree or len(self.children) == 0:
            values.append(".".join(current_path + [self.value]))
        for child in self.children:
            child.get_enum_values(values, current_path + [self.value], tree=tree)
        return values


@dataclass
class Enumeration(Base):
    values: list[str] = field(default_factory=list)
    super_class: str = field(default=None)
    tree: bool = field(default=False)

    @classmethod
    def get_related_enum_nodes(cls, imd_enum_node: EnumNode, index: Index):
        related_enum_nodes = []
        for found_enum_node in index.types_bucket["EnumNode"]:
            if found_enum_node.parent_node is not None:
                if found_enum_node.parent_node.ref == imd_enum_node.tid:
                    child_enum_nodes = cls.get_related_enum_nodes(found_enum_node, index)
                    enum_value = Value.from_imd(found_enum_node, index)
                    enum_value.children = child_enum_nodes
                    related_enum_nodes.append(enum_value)
        return related_enum_nodes

    @classmethod
    def from_imd(cls, imd_enum_type: EnumType, index: Index):
        top_enum_node = index.index[f"{imd_enum_type.tid}.TOP"]
        enum_hirarchie = cls.get_related_enum_nodes(top_enum_node, index)
        matched_imd_enum_tree_value_type = None
        for imd_enum_tree_value_type in index.types_bucket.get("EnumTreeValueType", []):
            if imd_enum_tree_value_type.et.ref == imd_enum_type.tid:
                matched_imd_enum_tree_value_type = imd_enum_tree_value_type
        tree = matched_imd_enum_tree_value_type is not None
        values = []
        for node in enum_hirarchie:
            values = values + node.get_enum_values([], [], tree=tree)
        # Shortening the relation between AttrOrParam.type and EnumTreeValueType.tid to the actual
        # EnumType.tid because an EnumTreeValueType is a EnumType of all nodes and leafs in the enum tree
        # see https://www.interlis.ch/download/interlis2/ili2-refman_2006-04-13_d.pdf 2.8.2 Aufzählungen
        # and this is resolved already Values.get_related_enum_nodes
        if matched_imd_enum_tree_value_type:
            tid = matched_imd_enum_tree_value_type.tid
            name = matched_imd_enum_tree_value_type.name
        else:
            tid = cls.prepare_tid(imd_enum_type.tid)
            name = imd_enum_type.name
        meta_attributes = cls.assemble_meta_attributes(index, imd_enum_type.tid)
        return cls(
            identifier=tid,
            name=cls.get_name(name, tid),
            doc=cls.doc_string(imd_enum_type.documentation),
            super_class=imd_enum_type.super.ref if imd_enum_type.super else None,
            values=values,
            tree=tree,
            meta_attributes=meta_attributes,
        )

    @staticmethod
    def prepare_tid(tid: str) -> str:
        return tid.replace(".TYPE", "_ENUM")

    @staticmethod
    def get_name(name, identifier) -> str:
        if name == "TYPE":
            return "".join(identifier.split(".")[-2:]).replace("_", "")
        else:
            return name


@dataclass
class Module(Base):
    """Represents imd:SubModel aka ili:Topic"""

    classes: list[Class] = field(default_factory=list)
    enumerations: list[Enumeration] = field(default_factory=list)
    coord_types: list[CoordType] = field(default_factory=list)
    line_types: list[LineType] = field(default_factory=list)
    imported_packages: list[str] = field(default_factory=list)
    related_class_imports: list[Tuple[str, str]] = field(default_factory=list)
    library: str = field(default=None)

    @classmethod
    def from_imd(
        cls,
        imd_instance: MetaElementType,
        imd_model_data: ModelData,
        index: Index,
        library: str,
    ):
        classes = []
        related_class_imports = []
        for imd_class in cls.get_element_of_type_from_list(
            ImdClass, imd_model_data.choice, ["Class", "Structure"]
        ):
            if imd_class.element_in_package.ref == imd_instance.tid:
                class_instance = Class.from_imd(imd_class, imd_model_data, index)
                classes.append(class_instance)
                for module_path, class_name, alias in class_instance.related_class_imports:
                    if (module_path, class_name, alias) not in related_class_imports:
                        related_class_imports.append((module_path, class_name, alias))
        enumerations = []
        for imd_enumeration in index.types_bucket["EnumType"]:
            if imd_enumeration.element_in_package:
                if imd_enumeration.element_in_package.ref == imd_instance.tid:
                    enumerations.append(Enumeration.from_imd(imd_enumeration, index))
        coord_types = []
        for imd_coord_type in cls.get_element_of_type_from_list(
            ImdCoordType, imd_model_data.choice
        ):
            if imd_coord_type.element_in_package:
                if imd_coord_type.element_in_package.ref == imd_instance.tid:
                    coord_types.append(CoordType.from_imd(imd_coord_type, imd_model_data, index))
        line_types = []
        for imd_line_type in cls.get_element_of_type_from_list(ImdLineType, imd_model_data.choice):
            if imd_line_type.element_in_package:
                if imd_line_type.element_in_package.ref == imd_instance.tid:
                    line_types.append(LineType.from_imd(imd_line_type, index))
        meta_attributes = cls.assemble_meta_attributes(index, imd_instance.tid)
        return cls(
            identifier=imd_instance.tid,
            name=imd_instance.name,
            doc=cls.doc_string(imd_instance.documentation),
            classes=classes,
            enumerations=enumerations,
            coord_types=coord_types,
            line_types=line_types,
            imported_packages=[],
            library=library,
            related_class_imports=related_class_imports,
            meta_attributes=meta_attributes,
        )


@dataclass
class Package(Module):
    """
    Represents a python package, this is a folder containing an __init__.py file. The folder gets the name of
    the model, the documentation goes into the __init__.py file.
    """

    version: str = field(default=None)
    ili_version: str = field(default=None)
    modules: list[Module] = field(default_factory=list)

    @classmethod
    def from_imd(
        cls, imd_instance: MetaElementType, imd_model_data: ModelData, index: Index, library: str
    ):
        if not isinstance(imd_instance, Model):
            raise TypeError(f'imd_instance has to be of type "Model" but was {imd_instance}')
        # set correct typing
        imd_model: Model = imd_instance

        # call Module function to initialize
        partialy_initialized_package = super(Package, cls).from_imd(
            imd_instance, imd_model_data, index, library
        )
        modules = []
        imported_packages = index.importing_p[imd_instance.tid]
        for imd_submodel in cls.get_element_of_type_from_list(SubModel, imd_model_data.choice):
            module = Module.from_imd(imd_submodel, imd_model_data, index, library)
            # we add imported packages from module level here too, this is necessary since we split things into
            # nested files (python style)
            module.imported_packages = imported_packages + [partialy_initialized_package.name]
            modules.append(module)
        return cls(
            identifier=imd_model.tid,
            name=imd_model.name,
            version=imd_model.version,
            ili_version=imd_model.ili_version,
            doc=cls.doc_string(imd_model.documentation),
            modules=modules,
            enumerations=partialy_initialized_package.enumerations,
            classes=partialy_initialized_package.classes,
            coord_types=partialy_initialized_package.coord_types,
            line_types=partialy_initialized_package.line_types,
            imported_packages=imported_packages,
            library=library,
            related_class_imports=partialy_initialized_package.related_class_imports,
            meta_attributes=partialy_initialized_package.meta_attributes,
        )


@dataclass
class Library(Base):
    packages: list[Package] = field(default_factory=list)

    @classmethod
    def from_imd(cls, imd_model_data_list: list[ModelData], index: Index, name):
        packages = []
        for imd_model_data in imd_model_data_list:
            for model in cls.get_element_of_type_from_list(Model, imd_model_data.choice):
                packages.append(Package.from_imd(model, imd_model_data, index, name))
        return cls(
            name=name,
            doc=["This library was created with ili2py"],
            packages=packages,
            identifier=name,
            meta_attributes=[],
        )
