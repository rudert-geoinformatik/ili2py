from dataclasses import field, dataclass
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16.shared import imd_namespace_map

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor import \
    Constant, UnitRef, UnitFunction
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.expression import \
    UnaryExpr, CompoundExpr

@dataclass
class ConstantElement:
    Constant: "Constant" = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )


@dataclass
class UnaryExprElement:
    UnaryExpr: "UnaryExpr" = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )


@dataclass
class UnitRefElement:
    UnitRef: "UnitRef" = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )


@dataclass
class CompoundExprElement:
    CompoundExpr: "CompoundExpr" = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )

@dataclass
class UnitFunctionElement:
    UnitFunction: "UnitFunction" = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )


@dataclass
class MultiplicityElement:

    # TODO: *Optional* seems to be wrong regarding to ilismeta model
    Min: Optional[int] = None
    Max: Optional[int] = None
