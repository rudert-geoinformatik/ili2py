from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.path_or_insp_factor import PathOrInspFactor

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ExistenceConstraintTypeAttr:
    class Meta:
        global_type = False

    path_or_insp_factor: Optional[PathOrInspFactor] = field(
        default=None,
        metadata={
            "name": "PathOrInspFactor",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
