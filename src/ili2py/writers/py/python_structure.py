import logging
from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Optional, Tuple, Union

from xsdata.formats.dataclass.serializers import DictEncoder

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    ActualArgumentType,
    AttributeConstType,
    AttrOrParam,
    AxisSpec,
    BlackboxType,
    BooleanType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import Class as ImdClass
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    ClassConstType,
    ClassRefType,
    CompoundExprType,
    ConstantType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    CoordType as ImdCoordType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    DataUnit,
    EnumAssignment,
    EnumAssignmentType,
    EnumMappingType,
    EnumNode,
    EnumTreeValueType,
    EnumType,
    ExistenceConstraintType,
    FormattedType,
    FunctionCallType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    LineType as ImdLineType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    MetaAttribute as ImdMetaAttribute,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    MetaElementType,
    MetaElementTypeDocumentation,
    Model,
    ModelData,
    MultiValue,
    MultiValueType,
    NumType,
    NumTypeType,
    PathOrInspFactorType,
    PathOrInspFactorTypePathEls,
    ReferenceType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import Role as ImdRole
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    RuntimeParamRefType,
    SetConstraintType,
    SimpleConstraintType,
    SubModel,
    TextType,
    TypeType,
    UnaryExprType,
    UniqueConstraintType,
    UnitFunctionType,
    UnitRefType,
)
from ili2py.mappers.helpers import Index
from ili2py.writers.py.constraints import (
    ActualArgument,
    AttributeConst,
    ClassConst,
    CompoundExpr,
    Constant,
    EnumMapping,
    ExistenceConstraint,
    ExpressionType,
    FunctionCall,
    PathEl,
    PathOrInspFactor,
    RuntimeParamRef,
    SetConstraint,
    SimpleConstraint,
    UnaryExpr,
    UniqueConstraint,
    UnitFunction,
    UnitRef,
)

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
    # See chapter 2.1.2 Klasse MetaElement in [IlisMeta16 Documentation](https://github.com/rudert-geoinformatik/ili2py/blob/master/tests/data/ilismeta16/ili24-metamodel_2022-06-17_d.pdf))
    OID_SEPARATOR = "."
    PYTHON_NAME_SEPARATOR = ""
    name: str
    identifier: str
    doc: list[str]
    meta_attributes: list[MetaAttribute]

    @staticmethod
    def doc_string(documentation: list[MetaElementTypeDocumentation]) -> list[str]:
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

    @staticmethod
    def pythonize_oid_global(oid: str) -> str:
        """
        Central method to create a pythonic name out of the passed oid. It can be used to derive IMD wide unique names
        which are save to be used in python as e.g. class names.

        The default behaiour is:
            'LocalisationCH_V1.MultilingualText.LocalisedText.TYPE' => 'LocalisationCH_V1MultilingualTextLocalisedTextTYPE'
        Args:
            oid: The OID string which is split by the oid_separator.
            python_separator: The separator which is used to join the pythonic name.

        Returns:
            The pythonized version of the OID.
        """
        oid_parts = oid.split(Base.OID_SEPARATOR)
        return Base.PYTHON_NAME_SEPARATOR.join(oid_parts)


@dataclass
class Attribute(Base):
    """Represents imd AttrOrParam"""

    types: list[str]
    type_restrictions: dict = field(default_factory=dict)
    enumeration: Optional["Enumeration"] = field(default=None)
    line_type: Optional["LineType"] = field(default=None)
    type_related_type_class: Optional["Class"] = field(default=None)
    reference_targets: list[str] = field(default_factory=list)
    is_list_type: bool = field(default=False)
    geometric: bool = field(default=False)
    geometric_multi: bool = field(default=False)
    geometric_is_point_like: bool = field(default=False)
    geometric_is_line_like: bool = field(default=False)
    geometric_is_polygon_like: bool = field(default=False)
    type_related_imports: list[Tuple[str, Union[Tuple[str, str | None, str | None], None]]] = field(
        default_factory=list
    )
    namespace_package: str | None = field(default=None)
    kind: str | None = field(default=None)

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
            return "str", False
        elif isinstance(imd_type, FormattedType):
            return "str", False
        elif isinstance(imd_type, ClassRefType):
            if imd_type.ref:
                return imd_type.ref.ref, True
            else:
                return "Any", False
        elif isinstance(imd_type, BlackboxType):
            if imd_type.kind.upper() == "BINARY":
                return "BinBlBoxType", False
            elif imd_type.kind.upper() == "XML":
                return "XmlBlBoxType", False
            else:
                logging.debug(f"Binary type was not handled correctly {imd_type}")
                return "str", False
        elif isinstance(imd_type, NumType):
            float_kind = Attribute.check_type_float(imd_type)
            if float_kind:
                return "float", False
            else:
                return "int", False
        elif isinstance(imd_type, BooleanType):
            return "bool", False
        elif isinstance(imd_type, ImdCoordType):
            if imd_type.name == "TYPE":
                if imd_type.super:
                    return imd_type.super.ref, True
                else:
                    return imd_type.tid, True
            else:
                return imd_type.tid, True
        elif isinstance(imd_type, ImdLineType):
            if imd_type.name == "TYPE":
                if imd_type.super:
                    return imd_type.super.ref, True
                else:
                    return imd_type.tid, True
            else:
                return imd_type.tid, True
        elif isinstance(imd_type, MultiValue):
            if isinstance(index.index[imd_type.base_type.ref], ImdClass):
                # we directly return the original base type ref here, this means its the oid of a structure class
                # we expect that class to exist in the right place (see class.from_imd)
                return imd_type.base_type.ref, True
            else:
                return imd_type.tid, True
        elif isinstance(imd_type, EnumType):
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
    def handle_local_types(
        index, resolved_type_name, referenced_type, attr_or_param, referenced_class
    ):
        local_type = None
        resolved_type = index.index.get(resolved_type_name)
        if not resolved_type:
            # type name is already a type which is not part of original imd tree, we manipulated it in
            # previous steps and assume here, that we can savely use it
            return resolved_type_name, local_type
        if isinstance(referenced_type, EnumType) and referenced_type.name == "TYPE":
            if referenced_type.name == resolved_type.name:
                class_name = f"{referenced_class.name}{attr_or_param.name}Enum"
                final_type_name = class_name
                local_type = Enumeration.from_imd(referenced_type, index)
                local_type.name = class_name
            else:
                final_type_name = resolved_type_name
        elif isinstance(referenced_type, ImdLineType) and referenced_type.name == "TYPE":
            if referenced_type.name == resolved_type.name:
                class_name = f"{referenced_class.name}{attr_or_param.name}LineType"
                final_type_name = class_name
                local_type = LineType.from_imd(referenced_type, index)
                local_type.name = class_name
            else:
                final_type_name = resolved_type_name
        elif isinstance(referenced_type, MultiValueType) and referenced_type.name in [
            "TYPE",
            "MVT",
        ]:
            multi_value_base_type = index.index[referenced_type.base_type.ref]
            imports = []
            if referenced_type.name == "MVT":
                multi_value_base_type_name, is_oid = Attribute.handle_type_trail(
                    multi_value_base_type, index
                )
                if is_oid:
                    # the multi field is not a simple type but links to a complex one
                    multi_value_base_type_name, multi_value_base_type_import = (
                        Attribute.decide_type_reference(
                            referenced_class, multi_value_base_type.tid, index
                        )
                    )
                    if multi_value_base_type_import:
                        imports.append(multi_value_base_type_import)
                type_restrictions = Attribute.construct_type_restrictions(multi_value_base_type)
                model_name = Attribute.get_model_name_from_type(referenced_type, index)
                list_type = Attribute.decide_list_type(multi_value_base_type)
            else:
                multi_value_base_type_name, multi_value_base_type_import = (
                    Attribute.decide_type_reference(
                        referenced_class, multi_value_base_type.tid, index
                    )
                )
                if multi_value_base_type_import:
                    imports.append(multi_value_base_type_import)
                type_restrictions = {"type_related_type": True}
                model_name = Attribute.get_model_name_from_type(multi_value_base_type, index)
                list_type = Attribute.decide_list_type(referenced_type)
            local_type = Class(
                name=f"{referenced_class.name}{attr_or_param.name}Struct",
                identifier=referenced_type.tid,
                doc=["This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py"],
                meta_attributes=Attribute.assemble_meta_attributes(index, referenced_type.tid),
                super_class=None,
                attributes=[
                    Attribute(
                        name="struct_content",
                        identifier=f"ili2py.{multi_value_base_type.tid}",
                        doc=["This attribute is a HOP-Type to correctly parse XTF."],
                        meta_attributes=[],
                        types=[multi_value_base_type_name],
                        type_restrictions=type_restrictions,
                        enumeration=None,
                        line_type=None,
                        type_related_type_class=None,
                        is_list_type=list_type,
                        namespace_package=model_name,
                        kind=referenced_type.name,
                    )
                ],
                abstract=False,
                related_class_imports=imports,
            )
            final_type_name = local_type.name
        else:
            final_type_name = resolved_type_name
        return final_type_name, local_type

    @staticmethod
    def decide_list_type(imd_type_object: MultiValueType):
        list_type = False
        if isinstance(imd_type_object, MultiValueType):
            # we act only if passed type was really a candidate to be a list type
            if imd_type_object.multiplicity:
                if imd_type_object.multiplicity.multiplicity:
                    if imd_type_object.multiplicity.multiplicity.max is None:
                        list_type = True
                    elif imd_type_object.multiplicity.multiplicity.max > 1:
                        list_type = True
                else:
                    logging.warning(
                        f"MultiValueType had multiplicity.multiplicity => None, this is unusual: {imd_type_object}"
                    )
            else:
                logging.warning(
                    f"MultiValueType had multiplicity => None, this is unusual: {imd_type_object}"
                )
        return list_type

    @staticmethod
    def get_referenced_class(imd_attr_or_param: AttrOrParam, index: Index) -> ImdClass:
        if imd_attr_or_param.attr_parent:
            referenced_class = index.index[imd_attr_or_param.attr_parent.ref]
        else:
            referenced_class = index.index[imd_attr_or_param.param_parent.ref]
        return referenced_class

    @staticmethod
    def get_class_location(
        class_definition: ImdClass, index: Index
    ) -> Tuple[Model, Union[SubModel, None]]:
        package = index.index[class_definition.element_in_package.ref]
        sub_model = None
        if isinstance(package, SubModel):
            sub_model = package
            model = index.index[package.element_in_package.ref]
        else:
            model = package
        return model, sub_model

    @staticmethod
    def attribute_name(attribute: AttrOrParam):
        return attribute.name.lower()

    @classmethod
    def from_imd(
        cls,
        imd_attr_or_param: AttrOrParam,
        imd_model_data: ModelData,
        index: Index,
    ):
        referenced_type = index.index[imd_attr_or_param.type_value.ref]
        referenced_class = Attribute.get_referenced_class(imd_attr_or_param, index)
        mapped_type, is_oid = cls.handle_type_trail(referenced_type, index)
        meta_attributes = cls.assemble_meta_attributes(index, imd_attr_or_param.tid)
        final_type_name, local_type = Attribute.handle_local_types(
            index, mapped_type, referenced_type, imd_attr_or_param, referenced_class
        )
        type_related_imports = []
        if is_oid and not local_type:
            decided_type_name, type_related_import = Attribute.decide_type_reference(
                referenced_class, final_type_name, index
            )
            if decided_type_name:
                final_type_name = decided_type_name
            if type_related_import:
                type_related_imports.append(type_related_import)
        return cls(
            identifier=imd_attr_or_param.tid,
            name=imd_attr_or_param.name,
            types=[final_type_name],
            doc=cls.doc_string(imd_attr_or_param.documentation),
            type_restrictions=cls.construct_type_restrictions(referenced_type),
            meta_attributes=meta_attributes,
            enumeration=local_type if isinstance(local_type, Enumeration) else None,
            line_type=local_type if isinstance(local_type, LineType) else None,
            type_related_type_class=local_type if isinstance(local_type, Class) else None,
            is_list_type=Attribute.decide_list_type(referenced_type),
            geometric=imd_attr_or_param.tid in index.geometric_attributes,
            geometric_multi=imd_attr_or_param.tid in index.geometric_attributes_multi,
            geometric_is_point_like=imd_attr_or_param.tid in index.geometric_attributes_point_like,
            geometric_is_line_like=imd_attr_or_param.tid in index.geometric_attributes_line_like,
            geometric_is_polygon_like=imd_attr_or_param.tid
            in index.geometric_attributes_polygon_like,
            type_related_imports=type_related_imports,
            namespace_package=Attribute.get_last_super_model_name_from_attribute(
                imd_attr_or_param, index
            ),
        )

    @staticmethod
    def get_model_name_from_type(type_definition: TypeType, index: Index):
        if type_definition.element_in_package:
            package = index.index[type_definition.element_in_package.ref]
            if isinstance(package, SubModel):
                package = index.index[package.element_in_package.ref]
            return package.name
        else:
            attribute = index.index[type_definition.ltparent.ref]
            return Attribute.get_model_name_from_attribute(attribute, index)

    @staticmethod
    def get_model_name_from_attribute(attribute: AttrOrParam, index: Index) -> str:
        if attribute.attr_parent:
            parent: ImdClass = index.index[attribute.attr_parent.ref]
        else:
            parent: ImdClass = index.index[attribute.param_parent.ref]
        package = index.index[parent.element_in_package.ref]
        if isinstance(package, SubModel):
            package = index.index[package.element_in_package.ref]
        return package.name

    @staticmethod
    def get_last_super_model_name_from_attribute(attribute: AttrOrParam, index: Index) -> str:
        """
        This method derives the package which the attribute is from. It uses the maybe existing super definition to
        adjust the package to the highest super class. This is because a inherited/extended attribute has its origin
        back from the package/model where it first was defined.
        See: https://interlis.discourse.group/t/multilingual-elemente-aus-localisationch-v2-localisation-v2-in-interlis-2-4/423

        Args:
            attribute:
            index:

        Returns:

        """
        if attribute.tid in index.type_super_classes:
            # here we reset the attribute variable to the highest (last) available element from the inheritance chain!
            attribute = index.index[index.type_super_classes[attribute.tid][-1]]
        return Attribute.get_model_name_from_attribute(attribute, index)

    @staticmethod
    def decide_type_references(source_class: ImdClass, target_type_oids: list[str], index: Index):
        types = []
        imports = []
        for super_reference in target_type_oids:
            super_type_name, type_reference_import = Attribute.decide_type_reference(
                source_class, super_reference, index
            )
            if super_type_name not in types:
                types.append(super_type_name)
            if type_reference_import:
                if type_reference_import not in imports:
                    imports.append(type_reference_import)
        return types, imports

    @staticmethod
    def decide_type_reference(source_class: ImdClass, target_type_oid: str, index: Index):
        target_type = index.index[target_type_oid]
        local_type = False
        if target_type.element_in_package:
            # this is a type which is defined as a own class
            target_referenced_class = target_type
        else:
            # this is a type which is defined inline directly with the corresponding attribute
            target_attr_or_param = index.index[target_type.ltparent.ref]
            target_referenced_class = Attribute.get_referenced_class(target_attr_or_param, index)
            local_type = True
        target_model, target_sub_model = Attribute.get_class_location(
            target_referenced_class, index
        )
        if source_class.element_in_package.ref == target_referenced_class.element_in_package.ref:
            # source and target in the same package
            if local_type:
                if target_referenced_class.tid != source_class.tid:
                    return f"{target_referenced_class.name}.{target_attr_or_param.name}", None
                else:
                    return None, None
            else:
                return f"{target_referenced_class.name}", None
        else:
            if target_sub_model:
                package_import_part = f"{target_model.name}.{target_sub_model.name}"
            else:
                package_import_part = f"{target_model.name}"
            if local_type:
                # its a type directly from an attribute of a class, we link to that attribute
                reference_name = Attribute.pythonize_oid_global(target_referenced_class.tid)
                return f"{reference_name}.{target_attr_or_param.name}", (
                    package_import_part,
                    target_referenced_class.name,
                    reference_name,
                )
            else:
                # its a dedicated type class, we link to that class
                reference_name = Attribute.pythonize_oid_global(target_type.tid)
                return f"{reference_name}", (
                    package_import_part,
                    target_type.name,
                    reference_name,
                )


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
    existence_constraints: list[dict] = field(default_factory=list)
    set_constraints: list[dict] = field(default_factory=list)
    simple_constraints: list[dict] = field(default_factory=list)
    unique_constraints: list[dict] = field(default_factory=list)
    geom_point_like_attributes: list[Attribute] = field(default_factory=list)
    geom_line_like_attributes: list[Attribute] = field(default_factory=list)
    geom_polygon_like_attributes: list[Attribute] = field(default_factory=list)

    @property
    def geom_attributes(self):
        return (
            self.geom_polygon_like_attributes
            + self.geom_line_like_attributes
            + self.geom_point_like_attributes
        )

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
                types=[oid_type_name],
                type_restrictions=Attribute.construct_type_restrictions(oid_type_object),
                enumeration=None,
                line_type=None,
                type_related_type_class=None,
            )
        point_like_attributes = []
        line_like_attributes = []
        polygon_like_attributes = []
        if index.class_class_attribute.get(imd_class.tid):
            for imd_attr_or_param_oid in index.class_class_attribute[imd_class.tid]:
                attribute = Attribute.from_imd(
                    index.index[imd_attr_or_param_oid], imd_model_data, index
                )
                attributes.append(attribute)
                if attribute.geometric_is_point_like:
                    point_like_attributes.append(attribute)
                if attribute.geometric_is_line_like:
                    line_like_attributes.append(attribute)
                if attribute.geometric_is_polygon_like:
                    polygon_like_attributes.append(attribute)
                related_class_imports += attribute.type_related_imports
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
                package_name = Attribute.get_model_name_from_type(imd_class, index)
                attributes.append(
                    Attribute(
                        name=role.name,
                        identifier=role.tid,
                        doc=cls.doc_string(role.documentation),
                        types=["Ref"],
                        meta_attributes=meta_attributes,
                        type_restrictions=type_restrictions,
                        reference_targets=[related_class_tid],
                        namespace_package=package_name,
                    )
                )
        meta_attributes = cls.assemble_meta_attributes(index, imd_class.tid)
        super_class_reference = None
        if imd_class.super:
            super_class_reference, super_class_reference_imports = cls.decide_type_reference(
                imd_class.super.ref, imd_class.tid, index
            )
            if super_class_reference_imports:
                if (
                    len(super_class_reference_imports[0].split(".")) > 1
                    and super_class_reference_imports[1] is None
                    and super_class_reference_imports[2] is None
                ):
                    logging.debug(
                        f"Import was skipped, since it has too many dots: {super_class_reference_imports[0]}"
                    )
                else:
                    related_class_imports.append(super_class_reference_imports)
        return cls(
            identifier=imd_class.tid,
            name=Class.class_name(imd_class),
            super_class=super_class_reference,
            doc=cls.doc_string(imd_class.documentation),
            attributes=attributes,
            abstract=imd_class.abstract,
            related_class_imports=related_class_imports,
            meta_attributes=meta_attributes,
            kind=imd_class.kind,
            oid=oid_attribute,
            existence_constraints=Class.translate_existence_constraint(
                index.class_with_existence_constraints.get(imd_class.tid, []), index
            ),
            set_constraints=Class.translate_set_constraint(
                index.class_with_set_constraints.get(imd_class.tid, []), index
            ),
            simple_constraints=Class.translate_simple_constraint(
                index.class_with_simple_constraints.get(imd_class.tid, []), index
            ),
            unique_constraints=Class.translate_unique_constraint(
                index.class_with_unique_constraints.get(imd_class.tid, []), index
            ),
            geom_point_like_attributes=point_like_attributes,
            geom_line_like_attributes=line_like_attributes,
            geom_polygon_like_attributes=polygon_like_attributes,
        )

    @staticmethod
    def class_name(imd_class: ImdClass) -> str:
        return imd_class.name

    @staticmethod
    def translate_path_els(path_els_imd: list[PathOrInspFactorTypePathEls]) -> list[PathEl]:
        translated_path_els = []
        for path_el_imd in path_els_imd:
            translated_path_els.append(
                PathEl(
                    kind=path_el_imd.path_el.kind,
                    ref=path_el_imd.path_el.ref.ref if path_el_imd.path_el.ref else None,
                    num_index=path_el_imd.path_el.num_index,
                    spec_index=path_el_imd.path_el.spec_index,
                )
            )
        return translated_path_els

    @staticmethod
    def translate_actual_argument(imd_element: ActualArgumentType) -> ActualArgument:
        object_classes = []
        for object_class in imd_element.object_classes:
            if object_class.class_ref:
                object_classes.append(object_class.class_ref.ref)
        return ActualArgument(
            formal_argument=(
                imd_element.formal_argument.ref if imd_element.formal_argument else None
            ),
            kind=imd_element.kind,
            object_classes=object_classes,
            expression=(
                Class.translate_expression(imd_element.expression.choice)
                if imd_element.expression
                else None
            ),
        )

    @staticmethod
    def translate_path_or_insp_factor(imd_element: PathOrInspFactorType) -> PathOrInspFactor:
        translated_element = PathOrInspFactor(
            path_els=Class.translate_path_els(imd_element.path_els),
            inspection=imd_element.inspection.ref if imd_element.inspection else None,
        )
        return translated_element

    @staticmethod
    def translate_unit_function(imd_element: UnitFunctionType) -> UnitFunction:
        return UnitFunction(explanation=imd_element.explanation)

    @staticmethod
    def translate_unit_ref(imd_element: UnitRefType) -> UnitRef:
        return UnitRef(unit=imd_element.unit.ref if imd_element.unit else None)

    @staticmethod
    def translate_attribute_const(imd_element: AttributeConstType) -> AttributeConst:
        return AttributeConst(
            attribute=imd_element.attribute.ref if imd_element.attribute else None
        )

    @staticmethod
    def translate_class_const(imd_element: ClassConstType) -> ClassConst:
        return ClassConst(
            class_value=imd_element.class_value.ref if imd_element.class_value else None
        )

    @staticmethod
    def translate_constant(imd_element: ConstantType):
        return Constant(value=imd_element.value, type=imd_element.type_value)

    @staticmethod
    def translate_runtime_param(imd_element: RuntimeParamRefType) -> RuntimeParamRef:
        return RuntimeParamRef(
            runtime_param=imd_element.runtime_param.ref if imd_element.runtime_param else None
        )

    @staticmethod
    def translate_function_call(imd_element: FunctionCallType) -> FunctionCall:
        return FunctionCall(
            function=imd_element.function.ref if imd_element.function else None,
            arguments=[
                Class.translate_actual_argument(function_call_argument.actual_argument)
                for function_call_argument in imd_element.arguments
            ],
        )

    @staticmethod
    def translate_enum_assignment(imd_element: EnumAssignmentType) -> EnumAssignment:
        return EnumAssignment(
            min_enum_value=imd_element.min_enum_value.ref if imd_element.min_enum_value else None,
            max_enum_value=imd_element.max_enum_value.ref if imd_element.max_enum_value else None,
            value_to_assign=Class.translate_expression(imd_element.value_to_assign.choice),
        )

    @staticmethod
    def translate_enum_mapping(imd_element: EnumMappingType) -> EnumMapping:
        translated_element = EnumMapping(
            enum_value=Class.translate_path_or_insp_factor(
                imd_element.enum_value.path_or_insp_factor
            ),
            cases=[
                Class.translate_enum_assignment(case.enum_assignment) for case in imd_element.cases
            ],
        )
        return translated_element

    @staticmethod
    def translate_compound_expression(imd_element: CompoundExprType) -> CompoundExpr:
        translated_sub_expressions = []
        for sub_expressions in imd_element.sub_expressions:
            for expression in sub_expressions.choice:
                translated_sub_expressions.append(Class.translate_expression(expression))
        return CompoundExpr(
            operation=imd_element.operation, sub_expressions=translated_sub_expressions
        )

    @staticmethod
    def translate_unary_expression(imd_element: UnaryExprType) -> UnaryExpr:
        return UnaryExpr(
            operation=imd_element.operation,
            sub_expression=Class.translate_expression(imd_element.sub_expression.choice),
        )

    @staticmethod
    def translate_expression(
        expression_imd: (
            UnitFunctionType
            | UnitRefType
            | AttributeConstType
            | ClassConstType
            | ConstantType
            | RuntimeParamRefType
            | FunctionCallType
            | EnumMappingType
            | PathOrInspFactorType
            | CompoundExprType
            | UnaryExprType
        ),
    ) -> ExpressionType | None:
        if isinstance(expression_imd, UnitFunctionType):
            return ExpressionType(choice=Class.translate_unit_function(expression_imd))
        elif isinstance(expression_imd, UnitRefType):
            return ExpressionType(choice=Class.translate_unit_ref(expression_imd))
        elif isinstance(expression_imd, AttributeConstType):
            return ExpressionType(choice=Class.translate_attribute_const(expression_imd))
        elif isinstance(expression_imd, ClassConstType):
            return ExpressionType(choice=Class.translate_class_const(expression_imd))
        elif isinstance(expression_imd, ConstantType):
            return ExpressionType(choice=Class.translate_constant(expression_imd))
        elif isinstance(expression_imd, RuntimeParamRefType):
            return ExpressionType(choice=Class.translate_runtime_param(expression_imd))
        elif isinstance(expression_imd, FunctionCallType):
            return ExpressionType(choice=Class.translate_function_call(expression_imd))
        elif isinstance(expression_imd, EnumMappingType):
            return ExpressionType(choice=Class.translate_enum_mapping(expression_imd))
        elif isinstance(expression_imd, PathOrInspFactorType):
            return ExpressionType(choice=Class.translate_path_or_insp_factor(expression_imd))
        elif isinstance(expression_imd, CompoundExprType):
            return ExpressionType(choice=Class.translate_compound_expression(expression_imd))
        elif isinstance(expression_imd, UnaryExprType):
            return ExpressionType(choice=Class.translate_unary_expression(expression_imd))
        else:
            logging.debug(f"passed type was: {expression_imd}")
            return None

    @staticmethod
    def translate_existence_constraint(constraint_oids: list[str], index: Index) -> list[dict]:
        translated_constraints = []
        for oid in constraint_oids:
            constraint: ExistenceConstraintType = index.index[oid]
            translated_constraints.append(
                DictEncoder().encode(
                    ExistenceConstraint(
                        id=constraint.tid,
                        name=constraint.name,
                        documentation=Class.doc_string(constraint.documentation),
                        to_class=constraint.to_class.ref if constraint.to_class else None,
                        to_domain=constraint.to_domain.ref if constraint.to_domain else None,
                        attr=Class.translate_path_or_insp_factor(
                            constraint.attr.path_or_insp_factor
                        ),
                    )
                )
            )
        return translated_constraints

    @staticmethod
    def translate_set_constraint(constraint_oids: list[str], index: Index) -> list[dict]:
        translated_constraints = []
        for oid in constraint_oids:
            constraint: SetConstraintType = index.index[oid]
            translated_constraint = SetConstraint(
                id=constraint.tid,
                name=constraint.name,
                documentation=Class.doc_string(constraint.documentation),
                to_class=constraint.to_class.ref if constraint.to_class else None,
                to_domain=constraint.to_domain.ref if constraint.to_domain else None,
                where=(
                    Class.translate_expression(constraint.where.choice)
                    if constraint.where
                    else None
                ),
                constraint=(
                    Class.translate_expression(constraint.constraint.choice)
                    if constraint.constraint
                    else None
                ),
            )
            translated_constraints.append(DictEncoder().encode(translated_constraint))
        return translated_constraints

    @staticmethod
    def translate_simple_constraint(constraint_oids: list[str], index: Index) -> list[dict]:
        translated_constraints = []
        for oid in constraint_oids:
            constraint: SimpleConstraintType = index.index[oid]
            translated_constraint = SimpleConstraint(
                id=constraint.tid,
                name=constraint.name,
                documentation=Class.doc_string(constraint.documentation),
                to_class=constraint.to_class.ref if constraint.to_class else None,
                to_domain=constraint.to_domain.ref if constraint.to_domain else None,
                kind=constraint.kind,
                percentage=constraint.percentage,
                logical_expression=Class.translate_expression(constraint.logical_expression.choice),
            )
            translated_constraints.append(DictEncoder().encode(translated_constraint))
        return translated_constraints

    @staticmethod
    def translate_unique_constraint(constraint_oids: list[str], index: Index) -> list[dict]:
        translated_constraints = []
        for oid in constraint_oids:
            constraint: UniqueConstraintType = index.index[oid]
            unique_def = []
            for unique_def_imd in constraint.unique_def:
                unique_def.append(
                    Class.translate_path_or_insp_factor(unique_def_imd.path_or_insp_factor)
                )
            translated_constraints.append(
                DictEncoder().encode(
                    UniqueConstraint(
                        id=constraint.tid,
                        name=constraint.name,
                        documentation=Class.doc_string(constraint.documentation),
                        to_class=constraint.to_class.ref if constraint.to_class else None,
                        to_domain=constraint.to_domain.ref if constraint.to_domain else None,
                        kind=constraint.kind,
                        unique_def=unique_def,
                        where=(
                            Class.translate_expression(constraint.where.choice)
                            if constraint.where
                            else None
                        ),
                    )
                )
            )
        return translated_constraints

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
    multi: bool = field(default=False)

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
                        types=[mapped_type],
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
            multi=imd_coord_type.multi if imd_coord_type.multi else False,
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
    is_line_like: bool = field(default=False)
    is_polygon_like: bool = field(default=False)
    multi: bool = field(default=False)

    @classmethod
    def from_imd(cls, imd_line_type: ImdLineType, index: Index):
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
            types=[type_name],
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
            is_line_like=imd_line_type.kind in ["Polyline", "DirectedPolyline"],
            is_polygon_like=imd_line_type.kind in ["Surface", "Area"],
            multi=imd_line_type.multi if imd_line_type.multi else False,
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
            for element in index.types_in_domain.get(imd_instance.tid, []):
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
                            "existence_constraints": Class.translate_existence_constraint(
                                index.domain_with_existence_constraints.get(element.tid, []), index
                            ),
                            "set_constraints": Class.translate_set_constraint(
                                index.domain_with_set_constraints.get(element.tid, []), index
                            ),
                            "simple_constraints": Class.translate_simple_constraint(
                                index.domain_with_simple_constraints.get(element.tid, []), index
                            ),
                            "unique_constraints": Class.translate_unique_constraint(
                                index.domain_with_unique_constraints.get(element.tid, []), index
                            ),
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
                        association_attribute_names = []
                        for role_oid, referenced_class_oid in association_construct:
                            role_object: ImdRole = index.index[role_oid]
                            if role_object.name in association_attribute_names:
                                logging.debug(
                                    f"We skip association attribute. Attribute with same name was added "
                                    f"already (this is likely due to an OR role combination in "
                                    f"{association_object.tid}) => {role_object}"
                                )
                                attributes[
                                    association_attribute_names.index(role_object.name)
                                ].reference_targets.append(referenced_class_oid)
                                continue
                            association_attribute_names.append(role_object.name)
                            package_name = Attribute.get_model_name_from_type(
                                association_object, index
                            )
                            attributes.append(
                                Attribute(
                                    name=role_object.name,
                                    identifier=role_object.tid,
                                    doc=cls.doc_string(role_object.documentation),
                                    meta_attributes=cls.assemble_meta_attributes(
                                        index, role_object.tid
                                    ),
                                    types=["Ref"],
                                    type_restrictions=Attribute.construct_type_restrictions(
                                        role_object
                                    ),
                                    enumeration=None,
                                    line_type=None,
                                    reference_targets=[referenced_class_oid],
                                    namespace_package=package_name,
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
        partialy_initialized_package = super().from_imd(
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
