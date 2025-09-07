from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.cond_sign_param_assignment_type_assignments import (
    CondSignParamAssignmentTypeAssignments,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.cond_sign_param_assignment_type_where import (
    CondSignParamAssignmentTypeWhere,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class CondSignParamAssignmentType:
    where: Optional[CondSignParamAssignmentTypeWhere] = field(
        default=None,
        metadata={
            "name": "Where",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    assignments: list[CondSignParamAssignmentTypeAssignments] = field(
        default_factory=list,
        metadata={
            "name": "Assignments",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
