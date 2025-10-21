from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import imd_namespace_map
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class import (
    Type,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import (
    HasRef,
    OrderedRef,
    Ref,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.serialization_elements import (
    MultiplicityElement,
)


@dataclass(kw_only=True)
class DomainType(Type):
    Mandatory: bool = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})


@dataclass
class BlackboxType(DomainType):
    class KindEnum(StrEnum):
        Binary = auto()
        Xml = auto()

    Kind: KindEnum = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})


@dataclass
class CoordType(DomainType):

    NullAxis: Optional[int] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )
    PiHalfAxis: Optional[int] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )
    # Only available in interlis model_data since 2.4
    Multi: Optional[bool] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )


@dataclass
class AxisSpec(HasRef):
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    CoordType_ref: Ref = field(
        metadata={"name": "CoordType", "namespace": imd_namespace_map["IlisMeta16"]},
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Axis_ref: OrderedRef = field(
        metadata={"name": "Axis", "namespace": imd_namespace_map["IlisMeta16"]},
    )


@dataclass
class LineType(DomainType):
    class KindEnum(StrEnum):
        Polyline = auto()
        DirectedPolyline = auto()
        Area = auto()

    Kind: KindEnum = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    # This is originally a string type in ilisMeta16.ili, but all actually
    #  occuring values are floats, so we assume that this was done to
    #  prevent limits of float definition in interlis 0.00 .. 1.00 since
    #  we need a simple arbitrary float value. Thats why we cast the value to
    #  float here silently
    MaxOverlap: Optional[float] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )
    Multi: Optional[bool] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    CoordType_ref: Optional[Ref] = field(
        default=None,
        metadata={"name": "CoordType", "namespace": imd_namespace_map["IlisMeta16"]},
    )


@dataclass
class TypeRelatedType(DomainType, HasRef):
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    BaseType_ref: Ref = field(
        metadata={"name": "BaseType", "namespace": imd_namespace_map["IlisMeta16"]},
    )


@dataclass
class TextType(DomainType):
    class KindEnum(StrEnum):
        MText = auto()
        Text = auto()
        Name = auto()
        Uri = auto()

    Kind: KindEnum = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})

    MaxLength: Optional[int] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )


@dataclass(kw_only=True)
class NumType(DomainType, HasRef):
    Min: Optional[str] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )
    Max: Optional[str] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )
    Circular: Optional[bool] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )
    Clockwise: Optional[bool] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Unit_ref: Optional[Ref] = field(
        default=None, metadata={"name": "Unit", "namespace": imd_namespace_map["IlisMeta16"]}
    )
    # TODO: Implement RefSys attribute as association (called NumsRefSys in https://models.interlis.ch/core/IlisMeta16.ili)


@dataclass(kw_only=True)
class FormattedType(NumType):

    Format: str = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Struct_ref: Ref = field(
        metadata={"name": "Struct", "namespace": imd_namespace_map["IlisMeta16"]}
    )


@dataclass
class BooleanType(DomainType):
    pass


@dataclass
class EnumType(DomainType):

    class OrderEnum(StrEnum):
        Unordered = auto()
        Ordered = auto()
        Circular = auto()

    Order: OrderEnum = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})


@dataclass
class MultiValue(TypeRelatedType):

    @dataclass
    class _Multiplicity:
        Multiplicity: MultiplicityElement = field(
            default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
        )

    Ordered: bool = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    Multiplicity: Optional["MultiValue._Multiplicity"] = field(
        default=None, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )
