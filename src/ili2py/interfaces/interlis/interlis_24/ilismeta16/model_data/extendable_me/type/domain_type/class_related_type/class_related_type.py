from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type import \
    DomainType


@dataclass
class ClassRelatedType(DomainType):
    pass


@dataclass
class ReferenceType(ClassRelatedType):
    External: bool


@dataclass
class ObjectType(ClassRelatedType):
    Multiple: bool


@dataclass
class ClassRefType(ClassRelatedType):
    pass