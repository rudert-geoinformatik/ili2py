from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.factor_type import FactorType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.path_or_insp_factor_type_inspection import (
    PathOrInspFactorTypeInspection,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.path_or_insp_factor_type_path_els import (
    PathOrInspFactorTypePathEls,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class PathOrInspFactorType(FactorType):
    path_els: list[PathOrInspFactorTypePathEls] = field(
        default_factory=list,
        metadata={
            "name": "PathEls",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    inspection: Optional[PathOrInspFactorTypeInspection] = field(
        default=None,
        metadata={
            "name": "Inspection",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
