from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type import \
    ReferenceType
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import OrderedRef
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.serialization_elements import MultiplicityElement


@dataclass
class Role(ReferenceType):

    class StrongnessEnum(StrEnum):
        Assoc = auto()
        Aggr = auto()
        Comp = auto()

    @dataclass
    class _Multiplicity:
        multiplicity: Optional[MultiplicityElement] = None

    Strongness: StrongnessEnum
    Ordered: bool
    EmbeddedTransfer: bool
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Association_ref: OrderedRef = field(
        metadata={
            "name": "Association"
        }
    )
    Multiplicity: Optional["Role._Multiplicity"] = None

