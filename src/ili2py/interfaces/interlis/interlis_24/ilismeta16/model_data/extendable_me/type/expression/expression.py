from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import List, Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import imd_namespace_map


@dataclass(kw_only=True)
class Expression:
    pass


@dataclass
class UnaryExpr(Expression):
    class OperationEnum(StrEnum):
        Not = auto()
        Defined = auto()

    Operation: OperationEnum = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    SubExpressions: List[Expression] = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )


@dataclass
class CompoundExpr(Expression):
    class OperationEnum(StrEnum):
        Implication = "Implication" # 2.4!
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

    Operation: Optional[OperationEnum] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    # TODO: Fix this, currently this fails while parsing the XML...
    # SubExpressions: List[Union[Constant, PathOrInspFactor]]
