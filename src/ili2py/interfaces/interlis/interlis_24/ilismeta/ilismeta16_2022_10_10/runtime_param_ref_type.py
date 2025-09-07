from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.factor_type import FactorType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.runtime_param_ref_type_runtime_param import (
    RuntimeParamRefTypeRuntimeParam,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class RuntimeParamRefType(FactorType):
    runtime_param: Optional[RuntimeParamRefTypeRuntimeParam] = field(
        default=None,
        metadata={
            "name": "RuntimeParam",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
