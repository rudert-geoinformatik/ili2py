from enum import Enum

from ili2py.mappers.internal.ilismeta16.model_data.domain import LengthRange
from ili2py.mappers.internal.ilismeta16.model_data.meta_elements import (
    DocText,
    ExtendableMe,
    MetaAttribute,
)
from ili2py.mappers.internal.ilismeta16.model_data.models import DomainType, Package
from ili2py.mappers.internal.ilismeta16.model_data.units import Unit


class TextTypeKind(Enum):
    MTEXT = "MText"
    TEXT = "Text"
    NAME = "Name"
    URI = "URI"


class TextType(DomainType):
    def __init__(
        self,
        tid: str,
        name: str,
        abstract: bool,
        final: bool,
        mandatory: bool,
        kind: TextTypeKind,
        generic: bool | None = None,
        documentation: list[DocText] | None = None,
        meta_attributes: list[MetaAttribute] | None = None,
        element_in_package: Package | None | None = None,
        sub: list[ExtendableMe] | None = None,
        super_class: ExtendableMe | None = None,
        max_length: int | None = None,
    ):
        if max_length is not None:
            LengthRange(max_length)
        super().__init__(
            tid,
            name,
            abstract,
            final,
            generic,
            mandatory,
            documentation=documentation,
            meta_attributes=meta_attributes,
            element_in_package=element_in_package,
            sub=sub,
            super_class=super_class,
        )
        self.kind = kind
        self.max_length = max_length


class NumType(DomainType):
    def __init__(
        self,
        tid: str,
        name: str,
        abstract: bool,
        final: bool,
        mandatory: bool,
        generic: bool | None = None,
        documentation: list[DocText] | None = None,
        meta_attributes: list[MetaAttribute] | None = None,
        element_in_package: Package | None | None = None,
        sub: list[ExtendableMe] | None = None,
        super_class: ExtendableMe | None = None,
        min: str | None = None,
        max: str | None = None,
        circular: bool | None = None,
        clockwise: bool | None = None,
        unit: Unit | None | None = None,
    ):
        super().__init__(
            tid,
            name,
            abstract,
            final,
            mandatory,
            generic,
            documentation=documentation,
            meta_attributes=meta_attributes,
            element_in_package=element_in_package,
            sub=sub,
            super_class=super_class,
        )
        self.min = min
        self.max = max
        self.circular = circular
        self.clockwise = clockwise
        self.unit = unit
