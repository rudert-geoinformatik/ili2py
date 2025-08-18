from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.axis_spec_type_axis import AxisSpecTypeAxis
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.axis_spec_type_coord_type import AxisSpecTypeCoordType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AxisSpecType:
    coord_type: Optional[AxisSpecTypeCoordType] = field(
        default=None,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    axis: Optional[AxisSpecTypeAxis] = field(
        default=None,
        metadata={
            "name": "Axis",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
