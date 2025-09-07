from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.path_el import PathEl

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class PathOrInspFactorTypePathEls:
    class Meta:
        global_type = False

    path_el: Optional[PathEl] = field(
        default=None,
        metadata={
            "name": "PathEl",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
