from dataclasses import dataclass, field
from enum import auto, StrEnum
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class import Type
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import Ref, HasRef, OrderedRef
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.serialization_elements import MultiplicityElement


@dataclass(kw_only=True)
class DomainType(Type):
    Mandatory: bool


@dataclass
class BlackboxType(DomainType):
    class KindEnum(StrEnum):
        Binary = auto()
        Xml = auto()

    Kind: KindEnum


@dataclass
class CoordType(DomainType):

    NullAxis: Optional[int] = None
    PiHalfAxis: Optional[int] = None
    # Only available in interlis model_data since 2.4
    Multi: Optional[bool] = None


@dataclass
class AxisSpec(HasRef):
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    CoordType_ref: Ref = field(
        metadata={
            "name": "CoordType"
        },
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Axis_ref: OrderedRef = field(
        metadata={
            "name": "Axis"
        },
    )


@dataclass
class LineType(DomainType):
    class KindEnum(StrEnum):
        Polyline = auto()
        DirectedPolyline = auto()
        Area = auto()

    Kind: KindEnum
    # This is originally a string type in ilisMeta16.ili, but all actually
    #  occuring values are floats, so we assume that this was done to
    #  prevent limits of float definition in interlis 0.00 .. 1.00 since
    #  we need a simple arbitrary float value. Thats why we cast the value to
    #  float here silently
    MaxOverlap: Optional[float] = None
    Multi: Optional[bool] = None
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    CoordType_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "CoordType"
        },
    )


@dataclass
class TypeRelatedType(DomainType, HasRef):
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    BaseType_ref: Ref = field(
        metadata={
            "name": "BaseType"
        },
    )


@dataclass
class TextType(DomainType):
    class KindEnum(StrEnum):
        MText = auto()
        Text = auto()
        Name = auto()
        Uri = auto()

    Kind: KindEnum

    MaxLength: Optional[int] = field(
        default=None
    )


@dataclass(kw_only=True)
class NumType(DomainType, HasRef):
    Min: Optional[str] = None
    Max: Optional[str] = None
    Circular: Optional[bool] = None
    Clockwise: Optional[bool] = None
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Unit_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "Unit"
        }
    )
    # TODO: Implement RefSys attribute as association (called NumsRefSys in https://models.interlis.ch/core/IlisMeta16.ili)


@dataclass(kw_only=True)
class FormattedType(NumType):

    Format: str
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Struct_ref: Ref = field(
        metadata={
            "name": "Struct"
        }
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

    Order: OrderEnum


@dataclass
class MultiValue(TypeRelatedType):

    @dataclass
    class _Multiplicity:
        Multiplicity: MultiplicityElement = None

    Ordered: bool
    Multiplicity: Optional["MultiValue._Multiplicity"] = None