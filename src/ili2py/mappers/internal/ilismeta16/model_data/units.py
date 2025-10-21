from enum import Enum
from typing import Optional

from ili2py.mappers.internal.ilismeta16.model_data.meta_elements import (
    DocText,
    ExtendableMe,
    MetaAttribute,
)
from ili2py.mappers.internal.ilismeta16.model_data.models import Expression


class UnitKind(Enum):
    BASEU = "BaseU"
    DERIVEDU = "DerivedU"
    COMPOSEDU = "ComposedU"


class Unit(ExtendableMe):
    def __init__(
        self,
        tid: str,
        name: str,
        abstract: bool,
        final: bool,
        kind: UnitKind,
        generic: bool | None = None,
        documentation: list[DocText] | None = None,
        meta_attributes: list[MetaAttribute] | None = None,
        sub: list["ExtendableMe"] | None = None,
        super_class: Optional["ExtendableMe"] = None,
        definition: Expression | None = None,
    ):
        super().__init__(
            tid,
            name,
            abstract,
            final,
            generic,
            documentation=documentation,
            meta_attributes=meta_attributes,
            sub=sub,
            super_class=super_class,
        )
        self.kind = kind
        self.definition = definition
        self.constraint()

    def constraint(self):
        assert self.kind != UnitKind.BASEU and self.definition is not None
