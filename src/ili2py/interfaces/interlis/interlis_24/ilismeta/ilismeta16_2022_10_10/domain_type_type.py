from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.domain_type_type_context import DomainTypeTypeContext
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_type import TypeType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DomainTypeType(TypeType):
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    context: Optional[DomainTypeTypeContext] = field(
        default=None,
        metadata={
            "name": "Context",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
