from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.domain_type_type import DomainTypeType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_related_type_type_base_type import (
    TypeRelatedTypeTypeBaseType,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TypeRelatedTypeType(DomainTypeType):
    base_type: Optional[TypeRelatedTypeTypeBaseType] = field(
        default=None,
        metadata={
            "name": "BaseType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
