from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_restriction_type_class_restriction import (
    ClassRestrictionTypeClassRestriction,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_restriction_type_crtr import ClassRestrictionTypeCrtr

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassRestrictionType:
    crtr: Optional[ClassRestrictionTypeCrtr] = field(
        default=None,
        metadata={
            "name": "CRTR",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    class_restriction: Optional[ClassRestrictionTypeClassRestriction] = field(
        default=None,
        metadata={
            "name": "ClassRestriction",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
