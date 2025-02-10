from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional, List

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.meta_element import MetaElement
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.expression import \
    Expression
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import Ref
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import OrderedRef


@dataclass(kw_only=True)
class ExtendableMe(MetaElement):

    Abstract: bool
    Final: bool
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Super_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "Super"
        },
    )
    # Only available in interlis model_data since 2.4
    # TODO: Find way to create class according to the parsed version in imd
    Generic: bool = field(
        default=None
    )
    # TODO: implement association Inheritance super/Subclass


@dataclass
class Unit(ExtendableMe):

    class KindEnum(StrEnum):
        BaseU = auto()
        DerivedU = auto()
        ComposedU = auto()

    Kind: KindEnum
    # TODO: MANDATORY CONSTRAINT ((Kind != #BaseU) == DEFINED(Definition));
    # TODO: Fix this, currently this fails while parsing the XML...
    # Definition: Optional[List[Union[CompoundExprElement,UnitFunctionElement]]] = None


@dataclass
class DataUnit(ExtendableMe):
    name = "BASKET"
    ViewUnit: bool
    DataUnitName: str
    # TODO: Implement ASSOCIATION Dependency
    # TODO: Implement ASSOCIATION AllowedInBasket


@dataclass
class AttrOrParam(ExtendableMe):

    class SubdivisionKindEnum(StrEnum):
        NoSubDiv = auto()
        SubDiv = auto()
        ContSubDiv = auto()

    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Type_ref: Ref = field(
        metadata={
            "name": "Type"
        }
    )
    SubdivisionKind: SubdivisionKindEnum = None
    Transient: Optional[bool] = None
    Derivates: Optional[List[Expression]] = field(
        default_factory=list
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    AttrParent_ref: Optional[OrderedRef] = field(
        default=None,
        metadata={
            "name": "AttrParent"
        },
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    ParamParent_ref: Optional[OrderedRef] = field(
        default=None,
        metadata={
            "name": "ParamParent"
        },
    )


@dataclass
class EnumNode(ExtendableMe):

    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    EnumType_ref: Optional[OrderedRef] = field(
        default=None,
        metadata={
            "name": "EnumType"
        }
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    ParentNode_ref: Optional[OrderedRef] = field(
        default=None,
        metadata={
            "name": "ParentNode"
        }
    )


