from abc import ABC
from enum import Enum
from typing import Optional

from ili2py.mappers.internal.ilismeta16.domain import LanguageCode
from ili2py.mappers.internal.ilismeta16.model_data.domain import Code, LengthRange, MultRange

# MetaElements definition of ilisMeta16.ili


class DocText:

    def __init__(self, text: str, name: str | None = None):
        self.text = text
        self.name = name


class MetaAttribute:

    def __init__(self, name: str, value: str, meta_element: Optional["MetaElement"] = None):
        self.name = name
        self.value = value
        self.meta_element = meta_element


class MetaElement(ABC):
    def __init__(
        self,
        tid: str,
        name: str,
        documentation: list[DocText] | None = None,
        meta_attributes: list[MetaAttribute] | None = None,
        element_in_package: Optional["Package"] | None = None,
    ):
        self.tid = tid
        self.name = name
        self.documentation = documentation or []
        self.meta_attributes = meta_attributes or []
        # CONTSTRAINT
        if element_in_package:
            assert not isinstance(element_in_package, Model)
        self.element_in_package = element_in_package


class ExtendableMe(ABC, MetaElement):

    def __init__(
        self,
        tid: str,
        name: str,
        abstract: bool,
        final: bool,
        generic: bool | None = None,
        documentation: list[DocText] | None = None,
        meta_attributes: list[MetaAttribute] | None = None,
        element_in_package: Optional["Package"] | None = None,
        sub: list["ExtendableMe"] | None = None,
        super_class: Optional["ExtendableMe"] = None,
    ):
        super().__init__(
            tid,
            name,
            documentation=documentation,
            meta_attributes=meta_attributes,
            element_in_package=element_in_package,
        )
        self.abstract = abstract
        self.final = final
        self.generic = generic
        self.sub = sub or []
        self.super = super_class


# Models definition of ilisMeta16.ili


class Package(ABC, MetaElement):
    def __init__(
        self,
        tid: str,
        name: str,
        documentation: list[DocText] | None = None,
        meta_attributes: list[MetaAttribute] | None = None,
        element_in_package: Optional["Package"] | None = None,
        imports: list["Package"] | None | None = None,
    ):
        super().__init__(
            tid,
            name,
            documentation=documentation,
            meta_attributes=meta_attributes,
            element_in_package=element_in_package,
        )
        self.imports = imports or []


class TidKind(Enum):
    TID_I16 = "TID_I16"
    TID_I32 = "TID_I32"
    TID_ANY = "TID_ANY"
    TID_EXPLANATION = "TID_EXPLANATION"


class Ili1Format:
    """
    Structure
    """

    def __init__(
        self,
        is_free: bool,
        blank_code: int,
        undefined_code: int,
        continue_code: int,
        font: str,
        tid_kind: TidKind,
        line_size: int | None = None,
        tid_size: int | None = None,
        tid_explantation: str | None = None,
    ):
        Code(blank_code)
        Code(undefined_code)
        Code(continue_code)
        if line_size is not None:
            LengthRange(line_size)
        if tid_size is not None:
            LengthRange(tid_size)
        self.is_free = is_free
        self.blank_code = blank_code
        self.undefined_code = undefined_code
        self.continue_code = continue_code
        self.font = font
        self.tid_kind = tid_kind
        self.line_size = line_size
        self.tid_size = tid_size
        self.tid_explantation = tid_explantation


class ModelKind(Enum):
    NORMALM = "NormalM"
    TYPEM = "TypeM"
    REFSYSTEMM = "RefSystemM"
    SYMBOLOGYM = "SymbologyM"


class Model(Package):
    """
    Represents an INTERLIS Model
    """

    def __init__(
        self,
        tid: str,
        name: str,
        ili_version: str,
        kind: ModelKind,
        documentation: list[DocText] | None = None,
        meta_attributes: list[MetaAttribute] | None = None,
        element_in_package: Optional["Package"] | None = None,
        contracted: bool | None = None,
        language: str | None = None,
        at: str | None = None,
        version: str | None = None,
        no_incremental_transfer: bool | None = None,
        char_set_iana_name: str | None = None,
        xmlns: str | None = None,
        ili1_transfer_name: str | None = None,
        ili1_format: Ili1Format | None = None,
    ):
        if language is not None:
            LanguageCode(language)
        super().__init__(
            tid,
            name,
            documentation=documentation,
            meta_attributes=meta_attributes,
            element_in_package=element_in_package,
        )
        self.ili_version = ili_version
        self.kind = kind
        self.contracted = contracted
        self.language = language
        self.at = at
        self.version = version
        self.no_incremental_transfer = no_incremental_transfer
        self.char_set_iana_name = char_set_iana_name
        self.xmlns = xmlns
        self.ili1_transfer = ili1_transfer_name
        self.ili1_format = ili1_format


class SubModel(Package):
    """
    Represents an INTERLIS Topic
    """


class Type(ABC):
    pass


class Expression(ABC):
    pass


class Multiplicity:
    def __init__(self, minimum: int, maximum: int | None = None):
        MultRange(minimum)
        MultRange(maximum)
        self.minimum = minimum
        self.maximum = maximum


class Constraint(ABC, MetaElement):
    pass


class DomainType(ABC, Type):
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
        constraints: list[Constraint] | None = None,
    ):
        super().__init__(
            tid,
            name,
            abstract,
            final,
            generic,
            documentation=documentation,
            meta_attributes=meta_attributes,
            element_in_package=element_in_package,
            sub=sub,
            super_class=super_class,
        )
        self.mandatory = mandatory
        # association DomainConstraint
        self.constraints = constraints or []


# Classes definition of ilisMeta16.ili


class ClassKind(Enum):
    STRUCTURE = "Structure"
    CLASS = "Class"
    VIEW = "View"
    ASSOCIATION = "Association"


class Class(Type):
    def __init__(
        self,
        kind: ClassKind,
        embedded_role_transfer: bool,
        attributes: list["AttrOrParam"] | None = None,
        parameters: list["AttrOrParam"] | None = None,
        multiplicity: Multiplicity | None = None,
        ili1_optional_table: bool | None = None,
        constraints: list[Constraint] | None = None,
    ):
        self.kind = kind
        self.embedded_role_transfer = embedded_role_transfer
        self.attributes = attributes or []
        self.parameters = parameters or []
        # enforce ilismeta16
        if self.kind == ClassKind.ASSOCIATION:
            assert multiplicity is not None
        self.multiplicity = multiplicity
        self.ili1_optional_table = ili1_optional_table
        self.constraints = constraints or []


class SubdivisionKind(Enum):
    NOSUBDIV = "NoSubDiv"
    SUBDIV = "SubDiv"
    CONTSUBDIV = "ContSubDiv"


class AttrOrParam(ExtendableMe):
    def __init__(
        self,
        tid: str,
        name: str,
        abstract: bool,
        final: bool,
        subdivision_kind: SubdivisionKind,
        attr_type: Type,
        generic: bool | None = None,
        documentation: list[DocText] | None = None,
        meta_attributes: list[MetaAttribute] | None = None,
        sub: list["ExtendableMe"] | None = None,
        super_class: Optional["ExtendableMe"] = None,
        transient: bool | None = None,
        derivates: list[Expression] | None = None,
        local_type: list[Type] | None = None,
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
        self.subdivision_kind = subdivision_kind
        self.transient = transient
        self.derivates = derivates or []
        self.local_type = local_type or []
        self.type = attr_type


# Types related to other types of ilisMeta16.ili


class TypeRelatedType(ABC, DomainType):
    def __init__(
        self,
        tid: str,
        name: str,
        abstract: bool,
        final: bool,
        mandatory: bool,
        base_type: Type,
        generic: bool | None = None,
        documentation: list[DocText] | None = None,
        meta_attributes: list[MetaAttribute] | None = None,
        element_in_package: Package | None | None = None,
        sub: list[ExtendableMe] | None = None,
        super_class: ExtendableMe | None = None,
        type_restrictions: list[Type] | None = None,
    ):
        super().__init__(
            tid,
            name,
            abstract,
            final,
            mandatory,
            generic=generic,
            documentation=documentation,
            meta_attributes=meta_attributes,
            element_in_package=element_in_package,
            sub=sub,
            super_class=super_class,
        )
        self.base_type = base_type
        # TODO: How to implement external reference? aka what does that mean actually in this context?
        #  Just, that it can be from another model?
        self.type_restrictions = type_restrictions or []


# Bag type of ilisMeta16.ili


class MultiValue(TypeRelatedType):
    def __init__(
        self,
        tid: str,
        name: str,
        abstract: bool,
        final: bool,
        mandatory: bool,
        base_type: Type,
        ordered: bool,
        generic: bool | None = None,
        documentation: list[DocText] | None = None,
        meta_attributes: list[MetaAttribute] | None = None,
        element_in_package: Package | None | None = None,
        sub: list[ExtendableMe] | None = None,
        super_class: ExtendableMe | None = None,
        type_restrictions: list[Type] | None = None,
        multiplicity: Multiplicity | None = None,
    ):
        super().__init__(
            tid,
            name,
            abstract,
            final,
            mandatory,
            base_type,
            generic=generic,
            documentation=documentation,
            meta_attributes=meta_attributes,
            element_in_package=element_in_package,
            sub=sub,
            super_class=super_class,
            type_restrictions=type_restrictions,
        )
        self.ordered = ordered
        self.multiplicity = multiplicity
