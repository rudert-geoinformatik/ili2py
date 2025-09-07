from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.sign_param_assignment import SignParamAssignment

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class CondSignParamAssignmentTypeAssignments:
    class Meta:
        global_type = False

    sign_param_assignment: Optional[SignParamAssignment] = field(
        default=None,
        metadata={
            "name": "SignParamAssignment",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
