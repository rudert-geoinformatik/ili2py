from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.domain_type_type import DomainTypeType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class CoordTypeType(DomainTypeType):
    null_axis: Optional[int] = field(
        default=None,
        metadata={
            "name": "NullAxis",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 3,
        },
    )
    pi_half_axis: Optional[int] = field(
        default=None,
        metadata={
            "name": "PiHalfAxis",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 3,
        },
    )
    multi: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Multi",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
