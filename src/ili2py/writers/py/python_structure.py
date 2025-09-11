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
    NumTypeType,
    TypeType,
    ClassRefType,
    DataUnit,
    TypeRelatedTypeType,
    ReferenceType,
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
    type_restrictions: dict = field(default_factory=dict)
    enumeration: Optional["Enumeration"] = field(default=None)
    line_type: Optional["LineType"] = field(default=None)
    type_related_type_class: Optional["Class"] = field(default=None)

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
    def check_type_float(type_definition: NumType) -> bool:
        return Attribute.check_float_kind(type_definition.min) or Attribute.check_float_kind(
            type_definition.max
        )

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
            | TypeType
            | ClassRefType
            | ReferenceType
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
            if imd_type.super:
                if imd_type.name == "TYPE":
                    return imd_type.super.ref, True
                else:
                    return imd_type.tid, True
            else:
                return "str", False
        elif isinstance(imd_type, FormattedType):
            if imd_type.super:
                if imd_type.name == "TYPE":
                    return imd_type.super.ref, True
                else:
                    return imd_type.tid, True
            else:
                return "str", False
        elif isinstance(imd_type, ClassRefType):
            if imd_type.ref:
                return imd_type.ref.ref, True
            else:
                return "Any", False
        elif isinstance(imd_type, BlackboxType):
            if imd_type.kind.upper() == "BINARY":
                return "BinBlBox", False
            elif imd_type.kind.upper() == "XML":
                return "XmlBlBox", False
            else:
                logging.debug(f"Binary type was not handled correctly {imd_type}")
                return "str", False
        elif isinstance(imd_type, NumType):
            float_kind = Attribute.check_type_float(imd_type)
            if imd_type.super:
                if imd_type.name == "TYPE":
                    referenced_super = index.index[imd_type.super.ref]
                    if referenced_super.name != "TYPE":
                        return imd_type.super.ref, True
                else:
                    return imd_type.tid, True
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
        elif isinstance(imd_type, ReferenceType):
            return "Ref", False
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
        imd_type: (
            TextType
            | FormattedType
            | BlackboxType
            | NumType
            | BooleanType
            | MultiValue
            | EnumType
            | ImdCoordType
            | ImdRole
            | TypeType
        ),
        type_related_type: bool = False,
    ) -> dict:
        type_restrictions = {
            "mandatory": imd_type.mandatory,
            "kind": None,
            "format": None,
            "unit": None,
            "ref_sys": None,
            "clockwise": None,
            "circular": None,
            "abstract": imd_type.abstract,
            "final": imd_type.final,
            "generic": imd_type.generic,
            "super": imd_type.super.ref if imd_type.super else imd_type.super,
            "type_related_type": type_related_type,
        }
        if imd_type.mandatory:
            type_restrictions["multiplicity"] = {"min": 1, "max": 1}
        else:
            type_restrictions["multiplicity"] = {"min": 0, "max": 1}
        if isinstance(imd_type, TextType):
            if imd_type.max_length is not None:
                type_restrictions.update(**{"max_length": imd_type.max_length})
        elif isinstance(imd_type, NumTypeType):
            if imd_type.unit:
                type_restrictions["unit"] = imd_type.unit.ref
            type_restrictions["circular"] = imd_type.circular
            type_restrictions["clockwise"] = imd_type.clockwise
            if imd_type.ref_sys:
                type_restrictions["ref_sys"] = imd_type.ref_sys.ref
            float_kind = Attribute.check_float_kind(imd_type.min) or Attribute.check_float_kind(
                imd_type.max
            )
            if isinstance(imd_type, NumType):
                if imd_type.min is not None:
                    if float_kind:
                        min_value = float(imd_type.min)
                        type_restrictions["precision"] = Attribute.derive_precision(imd_type.min)
                    else:
                        min_value = int(imd_type.min)
                    type_restrictions["min"] = min_value
                if imd_type.max is not None:
                    if float_kind:
                        max_value = float(imd_type.max)
                        max_precision = Attribute.derive_precision(imd_type.max)
                        if max_precision != type_restrictions["precision"]:
                            logging.debug(f"NumType precision was not as expected: {imd_type}")
                    else:
                        max_value = int(imd_type.max)
                    type_restrictions["max"] = max_value
            elif isinstance(imd_type, FormattedType):
                type_restrictions["format"] = f'"{imd_type.format}"'
                type_restrictions["struct"] = imd_type.struct.ref
                type_restrictions["min"] = imd_type.min
                type_restrictions["max"] = imd_type.max

            else:
                logging.debug(
                    logging.debug(
                        f"SubType of NumTypeType was not handled by range assertions: {imd_type}"
                    )
                )
        elif isinstance(imd_type, ImdRole):
            type_restrictions["multiplicity"] = {
                "min": imd_type.multiplicity.multiplicity.min,
                "max": imd_type.multiplicity.multiplicity.max,
            }
            type_restrictions["association_strongness"] = imd_type.strongness
        elif isinstance(imd_type, MultiValue):
            type_restrictions["multiplicity"] = {
                "min": imd_type.multiplicity.multiplicity.min,
                "max": imd_type.multiplicity.multiplicity.max,
            }
        elif isinstance(imd_type, BlackboxType):
            type_restrictions["kind"] = imd_type.kind
        else:
            logging.debug(f"Type was not handled by range assertions: {imd_type}")
        return type_restrictions

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
            if referenced_type.multiplicity.multiplicity.max is None:
                final_type_name = f"list['{resolved_type_name}']"
            elif referenced_type.multiplicity.multiplicity.max > 1:
                final_type_name = f"list['{resolved_type_name}']"
            else:
                final_type_name = resolved_type_name
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
        imd_type_oid = imd_attr_or_param.type_value.ref
        imd_type_object = index.index[imd_type_oid]
        type_related_type_class = None
        if isinstance(imd_type_object, MultiValue):
            related_type_oid = imd_type_object.base_type.ref
            related_type_object = index.index[related_type_oid]
            if related_type_object.element_in_package:
                related_type_object_package = index.index[
                    related_type_object.element_in_package.ref
                ]
                type_reference = None
                type_reference_imports = []
                if (
                    related_type_object.element_in_package.ref
                    == index.index[imd_attr_or_param.attr_parent.ref].element_in_package.ref
                ):
                    type_reference = related_type_object.name
                else:
                    if isinstance(related_type_object_package, SubModel):
                        related_type_object_model = index.index[
                            related_type_object_package.element_in_package.ref
                        ]
                        type_reference = f"{related_type_object_model.name}_{related_type_object_package.name}_{related_type_object.name}"
                        type_reference_imports.append(
                            (
                                f"{related_type_object_model.name}.{related_type_object_package.name}",
                                related_type_object.name,
                                type_reference,
                            )
                        )
                    elif isinstance(related_type_object_package, Model):
                        type_reference = (
                            f"{related_type_object_package.name}_{related_type_object.name}"
                        )
                        type_reference_imports.append(
                            (
                                f"{related_type_object_package.name}",
                                related_type_object.name,
                                type_reference,
                            )
                        )
                    else:
                        logging.debug(
                            f"MultiValue Type was not handled correctly {imd_type_object}"
                        )
                list_type = False
                if imd_type_object.multiplicity:
                    if imd_type_object.multiplicity.multiplicity.max is None:
                        list_type = True
                    elif imd_type_object.multiplicity.multiplicity.max > 1:
                        list_type = True
                if list_type:
                    if type_reference == related_type_object.name:
                        type_reference = f"list['{type_reference}']"
                    else:
                        type_reference = f"list[{type_reference}]"

                type_related_type_class = Class(
                    name=f"{imd_attr_or_param.name}Type",
                    identifier=imd_type_object.tid,
                    doc=["This is a class inserted by ili2py for correctly parsing multi types."],
                    meta_attributes=cls.assemble_meta_attributes(index, imd_type_object.tid),
                    super_class=None,
                    attributes=[
                        Attribute(
                            name=related_type_object.name,
                            identifier=f"ili2py.{related_type_object.tid}",
                            doc=["This attribute is a HOP-Type to correctly parse XTF."],
                            meta_attributes=[],
                            type=type_reference,
                            type_restrictions=cls.construct_type_restrictions(
                                imd_type_object, type_related_type=True
                            ),
                            enumeration=None,
                            line_type=None,
                            type_related_type_class=None,
                        )
                    ],
                    abstract=False,
                    related_class_imports=type_reference_imports,
                )
            else:
                logging.debug(f"MultiValue Type was not handled as expected {imd_type_object}")
        return cls(
            identifier=imd_attr_or_param.tid,
            name=attribute_name,
            type=type_related_type_class.name if type_related_type_class else final_type_name,
            doc=cls.doc_string(imd_attr_or_param.documentation),
            type_restrictions=cls.construct_type_restrictions(referenced_type),
            meta_attributes=meta_attributes,
            enumeration=local_type if isinstance(local_type, Enumeration) else None,
            line_type=local_type if isinstance(local_type, LineType) else None,
            type_related_type_class=type_related_type_class,
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

    oid: Attribute | None = field(default=None)
    super_class: str | None = field(default=None)
    attributes: list[Attribute] = field(default_factory=list)
    abstract: bool = field(default=False)
    related_class_imports: list[Tuple[str, str]] = field(default_factory=list)
    enumerations: list["Enumeration"] = field(default_factory=list)
    kind: Optional[str] = field(default=None)

    @classmethod
    def from_imd(cls, imd_class: ImdClass, imd_model_data: ModelData, index: Index):
        attributes = []
        related_class_imports = []
        oid_attribute = None
        if imd_class.oid:
            oid_type_object = index.index[imd_class.oid.ref]
            if oid_type_object.element_in_package.ref == imd_class.element_in_package.ref:
                oid_type_name = oid_type_object.name
            else:
                oid_type_object_package = index.index[oid_type_object.element_in_package.ref]
                if isinstance(oid_type_object_package, SubModel):
                    oid_type_object_model = index.index[
                        oid_type_object_package.element_in_package.ref
                    ]
                    oid_type_name = f"{oid_type_object_model.name}_{oid_type_object_package.name}_{oid_type_object.name}"
                    related_class_imports.append(
                        (
                            f"{oid_type_object_model.name}.{oid_type_object_package.name}",
                            oid_type_object.name,
                            oid_type_name,
                        )
                    )
                else:
                    oid_type_name = f"{oid_type_object_package.name}_{oid_type_object.name}"
                    related_class_imports.append(
                        (
                            f"{oid_type_object_package.name}",
                            oid_type_object.name,
                            oid_type_name,
                        )
                    )
            oid_attribute = Attribute(
                "tid",
                identifier=f"ili2py.{imd_class.tid}.tid",
                doc=[
                    "This attribute is generated by ili2py based on the OID definition in the underlying model."
                ],
                meta_attributes=[],
                type=oid_type_name,
                type_restrictions=Attribute.construct_type_restrictions(oid_type_object),
                enumeration=None,
                line_type=None,
                type_related_type_class=None,
            )
        if index.class_class_attribute.get(imd_class.tid):
            for imd_attr_or_param_oid in index.class_class_attribute[imd_class.tid]:
                attribute = Attribute.from_imd(
                    index.index[imd_attr_or_param_oid], imd_model_data, index
                )
                attributes.append(attribute)
        if imd_class.tid in index.association_to_class_ref_attributes:
            for role_tid, related_class_tid in index.association_to_class_ref_attributes[
                imd_class.tid
            ]:
                role: ImdRole = index.index[role_tid]
                related_class: ImdClass = index.index[related_class_tid]
                type_reference, type_reference_imports = cls.decide_type_reference(
                    related_class.tid, imd_class.tid, index
                )
                if type_reference_imports:
                    related_class_imports.append(type_reference_imports)
                meta_attributes = cls.assemble_meta_attributes(index, role.tid)
                type_restrictions = Attribute.construct_type_restrictions(role)
                attributes.append(
                    Attribute(
                        name=role.name,
                        identifier=role.tid,
                        doc=cls.doc_string(role.documentation),
                        type="Ref",
                        meta_attributes=meta_attributes,
                        type_restrictions=type_restrictions,
                    )
                )
        meta_attributes = cls.assemble_meta_attributes(index, imd_class.tid)
        super_class_reference = None
        if imd_class.super:
            super_class_reference, super_class_reference_imports = cls.decide_type_reference(
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
            kind=imd_class.kind,
            oid=oid_attribute,
        )

    @staticmethod
    def decide_type_reference(
        reference: str, class_tid: str, index: Index
    ) -> Tuple[str, Union[Tuple[str, str | None, str | None], None]] | None:
        super_class = index.index[reference]
        if super_class.element_in_package:
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
                    child_class_model_package = index.index[
                        child_class_package.element_in_package.ref
                    ]
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
                logging.debug(
                    f"Unexpected type while handling super class constructs of class {child_class}"
                )
        else:
            return None


@dataclass
class Choice:
    type_reference: str = field()
    name: str = field()
    identifier: str = field()
    model_name: str = field()


@dataclass
class Basket:
    choices: list[Choice] = field(default_factory=list)
    related_class_imports: list[Tuple[str, str]] = field(default_factory=list)

    @classmethod
    def from_imd(cls, imd_class: DataUnit, index: Index):
        choices = []
        related_class_imports = []
        for type_oid in index.allowed_in_basket_of_data_unit[imd_class.tid]:
            type_object = index.index[type_oid]
            if type_object.element_in_package.ref == imd_class.element_in_package.ref:
                type_reference = type_object.name
            else:
                type_reference, type_reference_imports = Class.decide_type_reference(
                    type_object.tid, imd_class.tid, index
                )
                if type_reference_imports:
                    related_class_imports.append(type_reference_imports)
            type_model_object = index.index[type_object.element_in_package.ref]
            if isinstance(type_model_object, SubModel):
                type_model_object = index.index[type_model_object.element_in_package.ref]
            choices.append(
                Choice(
                    type_reference=type_reference,
                    name=type_object.name,
                    identifier=type_object.tid,
                    model_name=type_model_object.name,
                )
            )
        return cls(choices=choices, related_class_imports=related_class_imports)


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
                        type_restrictions=CoordAttribute.construct_type_restrictions(imd_axis),
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
    type_definitions: list[dict] = field(default_factory=list)
    basket: Basket = field(default=None)

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
                for attribute in class_instance.attributes:
                    if attribute.type_related_type_class:
                        classes.append(attribute.type_related_type_class)
                        related_class_imports = (
                            related_class_imports
                            + attribute.type_related_type_class.related_class_imports
                        )
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
        type_definitions = []
        elements = index.elements_in_package.get(imd_instance.tid, [])
        if not elements:
            logging.debug(f"No elements in package {imd_instance}")
        else:
            for element_tid in index.elements_in_package.get(imd_instance.tid, []):
                element = index.index[element_tid]
                if (
                    isinstance(element, TextType)
                    or isinstance(element, NumType)
                    or isinstance(element, FormattedType)
                ):
                    reference, is_oid = Attribute.handle_type_trail(element, index)
                    if element.tid == reference:
                        reference = element.super.ref
                    if is_oid:
                        referenced_element = index.index[reference]
                        if referenced_element.element_in_package:
                            if referenced_element.element_in_package.ref == imd_instance.tid:
                                reference = referenced_element.name
                    kind = "text"
                    if isinstance(element, NumType):
                        float_kind = Attribute.check_type_float(element)
                        if float_kind:
                            kind = "float"
                        else:
                            kind = "int"
                    type_definitions.append(
                        {
                            "oid": element.tid,
                            "name": element.name,
                            "restrictions": Attribute.construct_type_restrictions(element),
                            "reference": reference,
                            "kind": kind,
                        }
                    )
        basket = None
        basket_ref = index.topic_basket.get(imd_instance.tid)
        if basket_ref:
            basket = Basket.from_imd(index.index[basket_ref], index)
            related_class_imports = related_class_imports + basket.related_class_imports
        association_oids = index.elements_in_package_class_association.get(imd_instance.tid)
        if association_oids:
            for association_oid in association_oids:
                association_object = index.index[association_oid]
                association_construct = index.association_bucket.get(association_oid)
                own_class = False
                attributes = []
                # https://github.com/rudert-geoinformatik/ili2py/blob/master/tests/data/ilismeta16/ili2-refman_2006-04-13_d.pdf
                # chapter 3.3.9 (page 87)
                if association_construct:
                    logging.debug(
                        f"Deciding if association is embedded or own class {association_object}"
                    )
                    if len(association_construct) > 2:
                        logging.debug("    Association has > 2 roles => own class")
                        own_class = True
                    elif all(
                        index.index[role_oid].multiplicity.multiplicity.max is None
                        or index.index[role_oid].multiplicity.multiplicity.max > 1
                        for role_oid, referenced_class_oid in association_construct
                    ):
                        logging.debug("    Association roles multiplicities are > 1 => own class")
                        own_class = True
                    elif all(
                        hasattr(index.index[role_oid], "oid")
                        and index.index[role_oid].oid is not None
                        for role_oid, referenced_class_oid in association_construct
                    ):
                        logging.debug("    Association has OID => own class")
                        own_class = True
                    # special check for own association class based on external references
                    elif len(association_construct) == 2:
                        logging.debug(
                            "   Association has 2 Role definitions, checking how to embedd..."
                        )
                        same_topic2 = (
                            index.index[association_construct[1][1]].element_in_package.ref
                            == imd_instance.tid
                        )
                        same_topic1 = (
                            index.index[association_construct[0][1]].element_in_package.ref
                            == imd_instance.tid
                        )
                        if not same_topic1 and not same_topic2:
                            logging.debug(
                                "       Embedding Association: Both referenced classes are in a different "
                                f"topic, we need a own class for the association {association_object}"
                            )
                            own_class = True
                        else:
                            if same_topic2:
                                logging.debug(
                                    "       Embedding Association: Referenced Class of second role is in same topic, "
                                    "assuming the association is embedded there and we dont need an own class "
                                    f"for {association_object}"
                                )
                                own_class = False
                            elif same_topic1:
                                logging.debug(
                                    "       Embedding Association: Referenced Class of first role is in same topic, "
                                    "assuming the association is embedded there and we dont need an own class "
                                    f"for {association_object}"
                                )
                                own_class = False

                    if len(index.class_subclassed_by.get(association_object.tid, [])) > 0:
                        logging.debug(
                            f"    Associaction has Subclasses, we construct a class for validity reason "
                            f"(Dataclasses) {association_object}"
                        )
                        own_class = True

                    if own_class:
                        for role_oid, referenced_class_oid in association_construct:
                            role_object: ImdRole = index.index[role_oid]
                            referenced_class_object: ImdClass = index.index[referenced_class_oid]
                            attributes.append(
                                Attribute(
                                    name=role_object.name,
                                    identifier=role_object.tid,
                                    doc=cls.doc_string(role_object.documentation),
                                    meta_attributes=cls.assemble_meta_attributes(
                                        index, role_object.tid
                                    ),
                                    type="Ref",
                                    type_restrictions=Attribute.construct_type_restrictions(
                                        role_object
                                    ),
                                    enumeration=None,
                                    line_type=None,
                                )
                            )
                super_reference = None
                type_reference_imports = []
                if association_object.super:
                    super_reference, type_reference_imports = Class.decide_type_reference(
                        association_object.super.ref, association_object.tid, index
                    )
                    if type_reference_imports:
                        related_class_imports.append(type_reference_imports)
                if super_reference or attributes:
                    classes.append(
                        Class(
                            name=association_object.name,
                            identifier=association_object.tid,
                            doc=cls.doc_string(association_object.documentation),
                            meta_attributes=cls.assemble_meta_attributes(
                                index, association_object.tid
                            ),
                            super_class=super_reference,
                            attributes=attributes,
                            abstract=association_object.abstract,
                            related_class_imports=type_reference_imports,
                            enumerations=[],
                            kind="Association",
                        )
                    )
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
            type_definitions=type_definitions,
            basket=basket,
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
            type_definitions=partialy_initialized_package.type_definitions,
        )


@dataclass
class Library(Base):
    packages: list[Package] = field(default_factory=list)
    topic_choices: list[Choice] = field(default_factory=list)
    related_class_imports: list[Tuple[str, str, str]] = field(default_factory=list)

    @classmethod
    def from_imd(cls, imd_model_data_list: list[ModelData], index: Index, name):
        packages = []
        topic_choices = []
        related_class_imports = []
        for imd_model_data in imd_model_data_list:
            for model in cls.get_element_of_type_from_list(Model, imd_model_data.choice):
                package = Package.from_imd(model, imd_model_data, index, name)
                packages.append(package)
                for module in package.modules:
                    if module.basket:
                        if module.basket.choices:
                            basket_reference = f"{package.name}_{module.name}_{module.name}TOPIC"
                            related_class_imports.append(
                                (
                                    f"{package.name}.{module.name}",
                                    f"{module.name}TOPIC",
                                    basket_reference,
                                )
                            )
                            topic_choices.append(
                                Choice(
                                    type_reference=basket_reference,
                                    name=module.name,
                                    model_name=package.name,
                                    identifier=module.identifier,
                                )
                            )

        return cls(
            name=name,
            doc=["This library was created with ili2py"],
            packages=packages,
            identifier=name,
            meta_attributes=[],
            topic_choices=topic_choices,
            related_class_imports=related_class_imports,
        )
