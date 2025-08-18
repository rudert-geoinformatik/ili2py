from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.constraint_type import ConstraintType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.set_constraint_type_constraint import SetConstraintTypeConstraint
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.set_constraint_type_where import SetConstraintTypeWhere

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class SetConstraintType(ConstraintType):
    where: Optional[SetConstraintTypeWhere] = field(
        default=None,
        metadata={
            "name": "Where",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    constraint: Optional[SetConstraintTypeConstraint] = field(
        default=None,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
