from dataclasses import dataclass, field

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import imd_namespace_map
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type import (
    DomainType,
)


@dataclass
class ClassRelatedType(DomainType):
    pass


@dataclass
class ReferenceType(ClassRelatedType):
    External: bool = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})


@dataclass
class ObjectType(ClassRelatedType):
    Multiple: bool = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})


@dataclass
class ClassRefType(ClassRelatedType):
    pass
