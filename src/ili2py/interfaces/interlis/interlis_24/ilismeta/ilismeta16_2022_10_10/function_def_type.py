from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.function_def_type_result_type import FunctionDefTypeResultType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_element_type import MetaElementType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class FunctionDefType(MetaElementType):
    explanation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Explanation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    result_type: Optional[FunctionDefTypeResultType] = field(
        default=None,
        metadata={
            "name": "ResultType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
