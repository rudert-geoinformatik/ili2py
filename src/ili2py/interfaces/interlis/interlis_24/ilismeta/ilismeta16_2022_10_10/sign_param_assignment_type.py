from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.sign_param_assignment_type_assignment import (
    SignParamAssignmentTypeAssignment,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.sign_param_assignment_type_param import (
    SignParamAssignmentTypeParam,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class SignParamAssignmentType:
    param: Optional[SignParamAssignmentTypeParam] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    assignment: Optional[SignParamAssignmentTypeAssignment] = field(
        default=None,
        metadata={
            "name": "Assignment",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
