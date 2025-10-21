from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type import (
    ReferenceType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import OrderedRef
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.serialization_elements import (
    MultiplicityElement,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta16.shared import imd_namespace_map


@dataclass
class Role(ReferenceType):

    class StrongnessEnum(StrEnum):
        Assoc = auto()
        Aggr = auto()
        Comp = auto()

    @dataclass
    class _Multiplicity:
        Multiplicity: Optional[MultiplicityElement] = field(
            default=None,
            metadata={
                "namespace": imd_namespace_map["IlisMeta16"],
            },
        )

    Strongness: StrongnessEnum = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    Ordered: bool = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    EmbeddedTransfer: bool = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Association_ref: OrderedRef = field(
        metadata={"name": "Association", "namespace": imd_namespace_map["IlisMeta16"]}
    )
    Multiplicity: Optional["Role._Multiplicity"] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        },
    )
