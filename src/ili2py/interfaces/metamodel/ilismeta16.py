from enum import StrEnum, auto

from ili2py.interfaces.metamodel import ns_map
from dataclasses import dataclass, field
from typing import List, Optional


class META_BASE:
    namespace = ns_map["IlisMeta16"]


@dataclass(kw_only=True)
class Ref:
    ref: str = field(
        metadata={
            "type": "Attribute",
            "namespace": ns_map["ili"],
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderedRef(Ref):
    order_pos: str = field(
        metadata={
            "type": "Attribute",
            "namespace": ns_map["ili"],
            "required": True,
        },
    )


@dataclass
class Ili1FormatStruct:

    class TidKind(StrEnum):
        TID_I16 = auto()
        TID_I32 = auto()
        TID_ANY = auto()
        TID_EXPLANATION = auto()

    is_free: bool = field(
        metadata={
            "name": "isFree",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    blank_code: int = field(
        metadata={
            "name": "blankCode",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )
    undefined_code: int = field(
        metadata={
            "name": "undefinedCode",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )
    continue_code: int = field(
        metadata={
            "name": "continueCode",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )
    font: str = field(
        metadata={
            "name": "Font",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    tid_kind: TidKind = field(
        metadata={
            "name": "tidKind",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    line_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "LineSize",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "min_inclusive": 1,
            "max_inclusive": 2147483647,
        },
    )
    tid_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "tidSize",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "min_inclusive": 1,
            "max_inclusive": 2147483647,
        },
    )
    tid_explanation: Optional[str] = field(
        default=None,
        metadata={
            "name": "tidExplanation",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )


@dataclass
class DocText:
    class Meta(META_BASE):
        name = "datasection"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"]
        },
    )
    text: str = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True
        },
    )


@dataclass
class MetaElementRef:
    class Meta(META_BASE):
        pass

    ref: str = field(
        metadata={
            "type": "Attribute",
            "namespace": ns_map["ili"],
            "required": True,
        },
    )


@dataclass
class MetaAttribute:
    class Meta(META_BASE):
        pass

    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    value: str = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    tid: str = field(
        metadata={
            "type": "Attribute",
            "namespace": ns_map["ili"],
            "required": True,
        },
    )
    meta_element_ref: Ref = field(
        metadata={
            "name": "MetaElement",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MetaElement:
    class Meta(META_BASE):
        pass

    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    tid: str = field(
        metadata={
            "type": "Attribute",
            "namespace": ns_map["ili"],
            "required": True,
        },
    )
    documentation: Optional[List["MetaElement.Documentation"]] = field(
        default_factory=list,
        metadata={
            "name": "Documentation",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    meta_attributes: Optional[List[MetaAttribute]] = field(
        default_factory=list,
        metadata={
            "name": "MetaAttribute",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )

    @dataclass
    class Documentation:
        doc_text: DocText = field(
            metadata={
                "name": "DocText",
                "type": "Element",
                "namespace": ns_map["IlisMeta16"],
                "required": True,
            },
        )


@dataclass(kw_only=True)
class Package(MetaElement):
    pass
    # TODO implement ASSOCIATION PackageElements


@dataclass
class Model(Package):
    class Kind(StrEnum):
        NormalM = auto()
        TypeM = auto()
        RefSystemM = auto()
        SymbologyM = auto()

    ili_version: str = field(
        metadata={
            "name": "iliVersion",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    kind: Kind = field(
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    contracted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Contracted",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "max_length": 5,
        },
    )
    at: Optional[str] = field(
        default=None,
        metadata={
            "name": "At",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    no_incremental_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoIncrementalTransfer",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    char_set_iananame: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSetIANAName",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    xmlns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    ili1_transfername: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili1Transfername",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    ili1_format: Optional["Model.Ili1Format"] = field(
        default=None,
        metadata={
            "name": "ili1Format",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )

    @dataclass
    class Ili1Format:
        ili1_format: Optional[Ili1FormatStruct] = field(
            default=None,
            metadata={
                "name": "Ili1Format",
                "type": "Element",
                "namespace": ns_map["IlisMeta16"],
                "required": True,
            },
        )


@dataclass
class SubModel(Package):
    pass


@dataclass(kw_only=True)
class ExtendableMe(MetaElement):
    class Meta:
        name = "ExtendableME"

    abstract: bool = field(
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    generic: bool = field(
        # TODO: This seems wrong. It was only done because some types were missing the "generic keyword"
        default=False,
        metadata={
            "name": "Generic",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    final: bool = field(
        metadata={
            "name": "Final",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    # TODO: implement association Inheritance super/Subclass


@dataclass
class DataUnit(ExtendableMe):
    name = "BASKET"
    view_unit: bool = field(
        metadata={
            "name": "ViewUnit",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    data_unit_name: str = field(
        metadata={
            "name": "DataUnitName",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    # TODO: Implement ASSOCIATION Dependency
    # TODO: Implement ASSOCIATION AllowedInBasket


@dataclass(kw_only=True)
class Type(ExtendableMe):
    class Meta(META_BASE):
        name = "Type"


@dataclass
class DomainType(Type):
    class Meta(META_BASE):
        name = "DomainType"

    mandatory: bool = field(
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )


@dataclass
class TextType(DomainType):
    class Kind(StrEnum):
        MText = auto()
        Text = auto()
        Name = auto()
        Uri = auto()

    kind: Kind = field(
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    lt_parent: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    max_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxLength",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "min_inclusive": 1,
            "max_inclusive": 2147483647,
        },
    )


@dataclass
class NumType(DomainType):
    min: Optional[str] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    max: Optional[str] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    circular: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Circular",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    clockwise: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Clockwise",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )


@dataclass
class TypeRelatedType(DomainType):
    class Meta(META_BASE):
        name = "TypeRelatedType"

    base_type: Ref = field(
        metadata={
            "name": "BaseType",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )


@dataclass
class Multiplicity:
    class Meta(META_BASE):
        name = "Multiplicity"

    min: int = field(
        metadata={
            "name": "Min",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )


@dataclass
class MultiValue(TypeRelatedType):
    class Meta(META_BASE):
        name = "MultiValue"

    ordered: bool = field(
        metadata={
            "name": "Ordered",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    multiplicity: Optional["MultiValue.Multiplicity"] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    lt_parent: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )

    @dataclass
    class Multiplicity:
        multiplicity: Optional[Multiplicity] = field(
            default=None,
            metadata={
                "name": "Multiplicity",
                "type": "Element",
                "namespace": ns_map["IlisMeta16"],
                "required": True,
            },
        )


@dataclass
class Class(Type):
    class Meta(META_BASE):
        name = "Class"

    class Kind(StrEnum):
        Structure = auto()
        Class = auto()
        View = auto()
        Association = auto()

    kind: Kind = field(
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    embedded_role_transfer: bool = field(
        metadata={
            "name": "EmbeddedRoleTransfer",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    ili1_optional_table: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ili1OptionalTable",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    multiplicity: Optional["Class.Multiplicity"] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    element_in_package: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )

    @dataclass
    class Multiplicity:
        multiplicity: Optional[Multiplicity] = field(
            default=None,
            metadata={
                "name": "Multiplicity",
                "type": "Element",
                "namespace": ns_map["IlisMeta16"],
                "required": True,
            },
        )

    oid: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "Oid",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )

    # TODO: implement ASSOCIATION ClassConstraint
    # TODO: implement ASSOCIATION ClassAttr
    # TODO: implement ASSOCIATION ClassParam
    # TODO: implement ASSOCIATION BaseClass


@dataclass(kw_only=True)
class Expression:
    class Meta(META_BASE):
        name = "Expression"


@dataclass
class AttrOrParam(ExtendableMe):
    class Meta(META_BASE):
        name = "AttrOrParam"

    class SubdivisionKind(StrEnum):
        NoSubDiv = auto()
        SubDiv = auto()
        ContSubDiv = auto()

    type: Ref = field(
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )

    subdivision_kind: Optional[SubdivisionKind] = field(
        default=None,
        metadata={
            "name": "SubdivisionKind",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    transient: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Transient",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    derivates: Optional[List[Expression]] = field(
        default_factory=list,
        metadata={
            "name": "Derivates",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    attr_parent: Optional[OrderedRef] = field(
        default=None,
        metadata={
            "name": "AttrParent",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    param_parent: Optional[OrderedRef] = field(
        default=None,
        metadata={
            "name": "ParamParent",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )


@dataclass
class ModelData:
    class Meta(META_BASE):
        name = "ModelData"

    bid: str = field(
        metadata={
            "type": "Attribute",
            "namespace": ns_map["ili"],
            "required": True,
        },
    )
    model: Model = field(
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "required": True,
        },
    )
    # TODO: Keep an eye on requested list length (as of meta model docs list of sub_model has to
    #  be at least 1)
    sub_model: List[SubModel] = field(
        default_factory=list,
        metadata={
            "name": "SubModel",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    data_unit: List[DataUnit] = field(
        default=None,
        metadata={
            "name": "DataUnit",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )

    meta_attributes: Optional[List[MetaAttribute]] = field(
        default_factory=list,
        metadata={
            "name": "MetaAttribute",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    consistency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": ns_map["ili"],
        },
    )
    classes: Optional[List[Class]] = field(
        default_factory=list,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    attr_or_param: List[AttrOrParam] = field(
        default_factory=list,
        metadata={
            "name": "AttrOrParam",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    text_types: Optional[List[TextType]] = field(
        default_factory=list,
        metadata={
            "name": "TextType",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    num_types: Optional[List[NumType]] = field(
        default_factory=list,
        metadata={
            "name": "NumType",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )
    multi_values: Optional[List[MultiValue]] = field(
        default_factory=list,
        metadata={
            "name": "MultiValue",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
        },
    )




