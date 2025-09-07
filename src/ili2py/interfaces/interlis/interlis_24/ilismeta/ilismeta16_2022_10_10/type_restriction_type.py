from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_restriction_type_trtr import TypeRestrictionTypeTrtr
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_restriction_type_type_restriction import (
    TypeRestrictionTypeTypeRestriction,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TypeRestrictionType:
    trtr: Optional[TypeRestrictionTypeTrtr] = field(
        default=None,
        metadata={
            "name": "TRTR",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    type_restriction: Optional[TypeRestrictionTypeTypeRestriction] = field(
        default=None,
        metadata={
            "name": "TypeRestriction",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
