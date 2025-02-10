from dataclasses import dataclass, field
from enum import StrEnum

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.expression import \
    Expression
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import Ref
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.path_elements import PathElsElement



@dataclass(kw_only=True)
class Factor(Expression):
    pass


@dataclass
class PathOrInspFactor(Factor):

    PathEls: PathElsElement


@dataclass
class Constant(Factor):
    class TypeKind(StrEnum):
        Undefined = "Undefined"
        Numeric = "Numeric"
        Text = "Text"
        Enumeration = "Enumeration"

    Value: str
    Type: TypeKind


@dataclass
class UnitRef(Factor):
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Unit_ref: Ref = field(
        metadata={
            "name": "Unit"
        },
    )



@dataclass
class UnitFunction(Factor):

    Explanation: str