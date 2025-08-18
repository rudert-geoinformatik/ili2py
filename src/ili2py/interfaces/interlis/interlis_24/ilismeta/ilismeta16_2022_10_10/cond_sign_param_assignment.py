from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.cond_sign_param_assignment_type import (
    CondSignParamAssignmentType,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class CondSignParamAssignment(CondSignParamAssignmentType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
