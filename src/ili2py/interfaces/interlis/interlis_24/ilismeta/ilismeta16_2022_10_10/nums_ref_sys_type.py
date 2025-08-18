from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class NumsRefSysType:
    axis: Optional[int] = field(
        default=None,
        metadata={
            "name": "Axis",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 3,
        },
    )
