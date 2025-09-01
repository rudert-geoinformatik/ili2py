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
    range_assertions: list[str] = field(default_factory=list)
    kind_assertions: list[str] = field(default_factory=list)
    enumeration: Optional["Enumeration"] = field(default=None)

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
    ) -> Union[str, "Enumeration"]:
        if isinstance(imd_type, TextType):
            return "str"
        elif isinstance(imd_type, FormattedType):
            if imd_type.super and imd_type.name == "TYPE":
                return Attribute.handle_type_trail(index.index[imd_type.super.ref], index)
            else:
                return "str"
        elif isinstance(imd_type, BlackboxType):
            return "str"
        elif isinstance(imd_type, NumType):
            return "float"
        elif isinstance(imd_type, BooleanType):
            return "bool"
        elif isinstance(imd_type, ImdCoordType):
            if imd_type.name == "TYPE" and imd_type.super:
                return Attribute.handle_type_trail(index.index[imd_type.super.ref], index)
            else:
                return imd_type.tid
        elif isinstance(imd_type, ImdLineType):
            if imd_type.name == "TYPE" and imd_type.super:
                return Attribute.handle_type_trail(index.index[imd_type.super.ref], index)
            else:
                return imd_type.tid
        elif isinstance(imd_type, MultiValue):
            return imd_type.base_type.ref
        elif isinstance(imd_type, EnumType):
            if imd_type.super:
                tid = Enumeration.prepare_tid(imd_type.super.ref)
            else:
                if imd_type.element_in_package:
                    # its a linked enumeration defined at package level
                    tid = Enumeration.prepare_tid(imd_type.tid)
                else:
                    # its an enumeration defined directly at attribute level in the interlis model
                    return Enumeration.from_imd(imd_type, index)
            return tid
        elif isinstance(imd_type, EnumTreeValueType):
            return imd_type.tid
        else:
            logging.debug(f"Type was not handled correctly for UML preparation: {imd_type}")
            return "UNKNOWN"

    @classmethod
    def construct_range_assertions(
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
    ) -> list[str]:
        if isinstance(imd_type, TextType):
            range_assertions = []
            if imd_type.max_length is not None:
                range_assertions.append(f"len(self.{attribute_name}) <= {imd_type.max_length}")
            return range_assertions
        elif isinstance(imd_type, NumType):
            range_assertions = []
            if imd_type.min is not None:
                range_assertions.append(f"self.{attribute_name} >= {imd_type.min}")
            if imd_type.max is not None:
                range_assertions.append(f"self.{attribute_name} <= {imd_type.max}")
            return range_assertions
        else:
            logging.debug(f"Type was not handled by range assertions: {imd_type}")
            return []

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
        mapped_type = cls.handle_type_trail(referenced_type, index)
        attribute_name = imd_attr_or_param.name
        meta_attributes = cls.assemble_meta_attributes(index, imd_attr_or_param.tid)
        final_type_name = Attribute.handle_type(
            mapped_type, imd_attr_or_param, referenced_class, model, referenced_type, sub_model
        )
        if isinstance(referenced_type, MultiValue):
            final_type_name = f"list[{final_type_name}]"
        return cls(
            identifier=imd_attr_or_param.tid,
            name=attribute_name,
            type=final_type_name,
            doc=cls.doc_string(imd_attr_or_param.documentation),
            range_assertions=cls.construct_range_assertions(attribute_name, referenced_type),
            meta_attributes=meta_attributes,
            enumeration=mapped_type if isinstance(mapped_type, Enumeration) else None,
        )

    @staticmethod
    def handle_type(
        type_name,
        parent_attribute: AttrOrParam,
        parent_class: ImdClass,
        model: Model,
        referenced_type,
        submodel: SubModel | None = None,
    ) -> Union[str, "Enumeration"]:
        if isinstance(type_name, Enumeration):
            return f'"{parent_class.name}.{type_name.name}"'
        if "." in type_name:
            type_name_parts = type_name.split(".")
            if type_name_parts[0] == model.name:
                # type is from the same model/package
                if submodel:
                    if type_name_parts[1] == submodel.name:
                        # type is from the same submodel/module
                        if type_name_parts[2] == parent_class.name:
                            # this is a class self reference
                            type_name = ".".join(type_name_parts[1:-1])
                            return f'"{type_name}"'
                        elif "ENUM" in type_name_parts[-1]:
                            return "".join(type_name_parts[-2:]).replace("_", "")
                        else:
                            return type_name_parts[-1]
                    else:
                        return type_name
                else:
                    # type is part of the __init__ of the package
                    if type_name_parts[1] == parent_class.name:
                        # this is a class self reference
                        type_name = ".".join(type_name_parts[1:-1])
                        return f'"{type_name}"'
                    return type_name_parts[-1]
            else:
                # it's a reference to an external, we return the full path
                return ".".join(type_name_parts)
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
                    (".".join(related_class.tid.split(".")[:-1]), related_class.tid.split(".")[-1])
                )
        meta_attributes = cls.assemble_meta_attributes(index, imd_class.tid)
        return cls(
            identifier=imd_class.tid,
            name=imd_class.name,
            super_class=(
                cls.decide_super_reference(imd_class.super.ref, imd_class.tid, index)
                if imd_class.super
                else None
            ),
            doc=cls.doc_string(imd_class.documentation),
            attributes=attributes,
            abstract=imd_class.abstract,
            related_class_imports=related_class_imports,
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

    @staticmethod
    def decide_super_reference(reference: str, class_tid: str, index: Index) -> str:
        if ".".join(class_tid.split(".")[:-1]) in reference:
            return index.index[reference].name
        else:
            return reference

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
                attributes.append(
                    CoordAttribute(
                        identifier=imd_axis.tid,
                        name=imd_axis.name,
                        doc=cls.doc_string(imd_axis.documentation),
                        type=Attribute.handle_type_trail(imd_axis, index),
                        reference_system=reference_system,
                        range_assertions=CoordAttribute.construct_range_assertions(
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
    def from_imd(cls, imd_line_type: ImdLineType, imd_model_data: ModelData, index: Index):
        attributes = []
        coord_type = index.index[imd_line_type.coord_type.ref]
        if imd_line_type.element_in_package.ref == coord_type.element_in_package.ref:
            # line_type and coordtype_reference in the same package
            type_name = coord_type.name.split(".")[-1]
        else:
            # line_type and coordtype_reference NOT in the same package
            type_name = imd_line_type.coord_type.ref
        meta_attributes = cls.assemble_meta_attributes(index, coord_type.tid)
        attribute = Attribute(
            identifier=coord_type.tid,
            name=imd_line_type.kind.upper(),
            doc=cls.doc_string(coord_type.documentation),
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
        imd_sub_model: SubModel,
        imported_packages: list[str],
        imd_model_data: ModelData,
        index: Index,
        library: str,
    ):
        classes = []
        related_class_imports = []
        for imd_class in cls.get_element_of_type_from_list(
            ImdClass, imd_model_data.choice, ["Class", "Structure"]
        ):
            if imd_class.element_in_package.ref == imd_sub_model.tid:
                class_instance = Class.from_imd(imd_class, imd_model_data, index)
                classes.append(class_instance)
                for module_path, class_name in class_instance.related_class_imports:
                    if module_path.split(".")[-1] != imd_sub_model.name:
                        if (module_path, class_name) not in related_class_imports:
                            related_class_imports.append((module_path, class_name))
        enumerations = []
        for imd_enumeration in index.types_bucket["EnumType"]:
            if imd_enumeration.element_in_package:
                if imd_enumeration.element_in_package.ref == imd_sub_model.tid:
                    enumerations.append(Enumeration.from_imd(imd_enumeration, index))
        coord_types = []
        for imd_coord_type in cls.get_element_of_type_from_list(
            ImdCoordType, imd_model_data.choice
        ):
            if imd_coord_type.element_in_package:
                if imd_coord_type.element_in_package.ref == imd_sub_model.tid:
                    coord_types.append(CoordType.from_imd(imd_coord_type, imd_model_data, index))
        line_types = []
        for imd_line_type in cls.get_element_of_type_from_list(ImdLineType, imd_model_data.choice):
            if imd_line_type.element_in_package:
                if imd_line_type.element_in_package.ref == imd_sub_model.tid:
                    line_types.append(LineType.from_imd(imd_line_type, imd_model_data, index))
        package = index.index[imd_sub_model.element_in_package.ref]
        meta_attributes = cls.assemble_meta_attributes(index, imd_sub_model.tid)
        return cls(
            identifier=imd_sub_model.tid,
            name=imd_sub_model.name,
            doc=cls.doc_string(imd_sub_model.documentation),
            classes=classes,
            enumerations=enumerations,
            coord_types=coord_types,
            line_types=line_types,
            imported_packages=imported_packages + [package.name],
            library=library,
            related_class_imports=related_class_imports,
            meta_attributes=meta_attributes,
        )


@dataclass
class Package(Base):
    """
    Represents a python package, this is a folder containing an __init__.py file. The folder gets the name of
    the model, the documentation goes into the __init__.py file.
    """

    version: str
    ili_version: str
    modules: list[Module] = field(default_factory=list)
    classes: list[Class] = field(default_factory=list)
    enumerations: list[Enumeration] = field(default_factory=list)
    coord_types: list[CoordType] = field(default_factory=list)
    line_types: list[LineType] = field(default_factory=list)
    imported_packages: list[str] = field(default_factory=list)
    related_class_imports: list[Tuple[str, str]] = field(default_factory=list)
    library: str = field(default=None)

    @classmethod
    def from_imd(cls, imd_model: Model, imd_model_data: ModelData, index: Index, library: str):
        modules = []
        imported_packages = index.importing_p[imd_model.tid]
        for imd_submodel in cls.get_element_of_type_from_list(SubModel, imd_model_data.choice):
            modules.append(
                Module.from_imd(imd_submodel, imported_packages, imd_model_data, index, library)
            )

        classes = []
        related_class_imports = []
        for imd_class in cls.get_element_of_type_from_list(
            ImdClass, imd_model_data.choice, ["Class", "Structure"]
        ):
            if imd_class.element_in_package.ref == imd_model.tid:
                class_instance = Class.from_imd(imd_class, imd_model_data, index)
                classes.append(class_instance)
                for module_path, class_name in class_instance.related_class_imports:
                    if module_path.split(".")[0] != imd_model.name:
                        if (module_path, class_name) not in related_class_imports:
                            related_class_imports.append((module_path, class_name))
        coord_types = []
        for imd_coord_type in cls.get_element_of_type_from_list(
            ImdCoordType, imd_model_data.choice
        ):
            if imd_coord_type.element_in_package:
                if imd_coord_type.element_in_package.ref == imd_model.tid:
                    coord_types.append(CoordType.from_imd(imd_coord_type, imd_model_data, index))
        line_types = []
        for imd_line_type in cls.get_element_of_type_from_list(ImdLineType, imd_model_data.choice):
            if imd_line_type.element_in_package:
                if imd_line_type.element_in_package.ref == imd_model.tid:
                    line_types.append(LineType.from_imd(imd_line_type, imd_model_data, index))
        enumerations = []
        for imd_enumeration in cls.get_element_of_type_from_list(EnumType, imd_model_data.choice):
            if imd_enumeration.element_in_package:
                if imd_enumeration.element_in_package.ref == imd_model.tid:
                    enumerations.append(Enumeration.from_imd(imd_enumeration, index))
        meta_attributes = cls.assemble_meta_attributes(index, imd_model.tid)
        return cls(
            identifier=imd_model.tid,
            name=imd_model.name,
            version=imd_model.version,
            ili_version=imd_model.ili_version,
            doc=cls.doc_string(imd_model.documentation),
            modules=modules,
            enumerations=enumerations,
            classes=classes,
            coord_types=coord_types,
            line_types=line_types,
            imported_packages=imported_packages,
            library=library,
            related_class_imports=related_class_imports,
            meta_attributes=meta_attributes,
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
