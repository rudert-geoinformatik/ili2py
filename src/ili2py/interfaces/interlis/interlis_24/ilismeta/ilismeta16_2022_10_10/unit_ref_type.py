from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.factor_type import FactorType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.unit_ref_type_unit import UnitRefTypeUnit

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class UnitRefType(FactorType):
    unit: Optional[UnitRefTypeUnit] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
