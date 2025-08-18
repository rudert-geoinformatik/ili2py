from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import imd_namespace_map
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.meta_element import MetaElement
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import Ref
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.serialization_elements import CompoundExprElement


@dataclass
class Constraint(MetaElement):
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    ToClass_ref: Ref = field(
        metadata={
            "name": "ToClass",
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )


@dataclass
class SimpleConstraint(Constraint):
    class KindEnum(StrEnum):
        MandC = auto()
        LowPercC = auto()
        HighPercC = auto()
    Kind: KindEnum = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    LogicalExpression: CompoundExprElement = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    Percentage: Optional[float] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
