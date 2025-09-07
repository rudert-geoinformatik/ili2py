from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.multi_value_type_multiplicity import MultiValueTypeMultiplicity
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_related_type_type import TypeRelatedTypeType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MultiValueType(TypeRelatedTypeType):
    ordered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ordered",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    multiplicity: Optional[MultiValueTypeMultiplicity] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
