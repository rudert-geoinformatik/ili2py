from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import List, Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import imd_namespace_map
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.expression import (
    Expression,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.meta_element import MetaElement
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import OrderedRef, Ref


@dataclass(kw_only=True)
class ExtendableMe(MetaElement):

    Abstract: bool = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    Final: bool = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Super_ref: Optional[Ref] = field(
        default=None,
        metadata={"name": "Super", "namespace": imd_namespace_map["IlisMeta16"]},
    )
    # Only available in interlis model_data since 2.4
    # TODO: Find way to create class according to the parsed version in imd
    Generic: bool = field(
        default=None,
        metadata={"namespace": imd_namespace_map["IlisMeta16"]},
    )
    # TODO: implement association Inheritance super/Subclass


@dataclass
class Unit(ExtendableMe):

    class KindEnum(StrEnum):
        BaseU = auto()
        DerivedU = auto()
        ComposedU = auto()

    Kind: KindEnum = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    # TODO: MANDATORY CONSTRAINT ((Kind != #BaseU) == DEFINED(Definition));
    # TODO: Fix this, currently this fails while parsing the XML...
    # Definition: Optional[List[Union[CompoundExprElement,UnitFunctionElement]]] = None


@dataclass
class DataUnit(ExtendableMe):
    name = "BASKET"
    ViewUnit: bool = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    DataUnitName: str = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
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
    Type_ref: Ref = field(metadata={"name": "Type", "namespace": imd_namespace_map["IlisMeta16"]})
    SubdivisionKind: SubdivisionKindEnum = None
    Transient: Optional[bool] = None
    Derivates: Optional[List[Expression]] = field(
        default_factory=list, metadata={"namespace": imd_namespace_map["IlisMeta16"]}
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    AttrParent_ref: Optional[OrderedRef] = field(
        default=None,
        metadata={"name": "AttrParent", "namespace": imd_namespace_map["IlisMeta16"]},
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    ParamParent_ref: Optional[OrderedRef] = field(
        default=None,
        metadata={"name": "ParamParent", "namespace": imd_namespace_map["IlisMeta16"]},
    )


@dataclass
class EnumNode(ExtendableMe):

    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    EnumType_ref: Optional[OrderedRef] = field(
        default=None, metadata={"name": "EnumType", "namespace": imd_namespace_map["IlisMeta16"]}
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    ParentNode_ref: Optional[OrderedRef] = field(
        default=None, metadata={"name": "ParentNode", "namespace": imd_namespace_map["IlisMeta16"]}
    )
