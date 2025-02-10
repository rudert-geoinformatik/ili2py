from dataclasses import dataclass
from enum import StrEnum, auto
from typing import List


@dataclass(kw_only=True)
class Expression:
    pass


@dataclass
class UnaryExpr(Expression):
    class OperationEnum(StrEnum):
        Not = auto()
        Defined = auto()

    Operation: OperationEnum
    SubExpressions: List[Expression]


@dataclass
class CompoundExpr(Expression):
    class OperationEnum(StrEnum):
        Implication = "Implication"
        And = "And"
        Or = "Or"
        Mult = "Mult"
        Div = "Div"
        Relation_Equal = "Relation.Equal"
        Relation_NotEqual = "Relation.NotEqual"
        Relation_LessOrEqual = "Relation.LessOrEqual"
        Relation_GreaterOrEqual = "Relation.GreaterOrEqual"
        Relation_Less = "Relation.Less"
        Relation_Greater = "Relation.Greater"

    Operation: OperationEnum
    # TODO: Fix this, currently this fails while parsing the XML...
    # SubExpressions: List[Union[Constant, PathOrInspFactor]]
