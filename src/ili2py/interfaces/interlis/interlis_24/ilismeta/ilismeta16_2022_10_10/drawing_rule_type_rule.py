from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.cond_sign_param_assignment import CondSignParamAssignment

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DrawingRuleTypeRule:
    class Meta:
        global_type = False

    cond_sign_param_assignment: Optional[CondSignParamAssignment] = field(
        default=None,
        metadata={
            "name": "CondSignParamAssignment",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
