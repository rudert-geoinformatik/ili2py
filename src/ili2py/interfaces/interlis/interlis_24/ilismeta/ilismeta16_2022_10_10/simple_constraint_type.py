from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.constraint_type import ConstraintType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.simple_constraint_type_logical_expression import (
    SimpleConstraintTypeLogicalExpression,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class SimpleConstraintType(ConstraintType):
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("100.00"),
        },
    )
    logical_expression: Optional[SimpleConstraintTypeLogicalExpression] = (
        field(
            default=None,
            metadata={
                "name": "LogicalExpression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
    )
