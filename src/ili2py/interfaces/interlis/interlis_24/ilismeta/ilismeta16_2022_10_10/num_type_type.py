from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.domain_type_type import DomainTypeType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.num_type_type_ref_sys import NumTypeTypeRefSys
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.num_type_type_unit import NumTypeTypeUnit

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class NumTypeType(DomainTypeType):
    min: Optional[str] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    max: Optional[str] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    circular: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Circular",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    clockwise: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Clockwise",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ref_sys: Optional[NumTypeTypeRefSys] = field(
        default=None,
        metadata={
            "name": "RefSys",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    unit: Optional[NumTypeTypeUnit] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
