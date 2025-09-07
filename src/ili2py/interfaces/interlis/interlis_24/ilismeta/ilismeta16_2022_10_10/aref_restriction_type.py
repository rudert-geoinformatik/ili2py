from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.aref_restriction_type_aref import ArefRestrictionTypeAref
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.aref_restriction_type_type import ArefRestrictionTypeType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ArefRestrictionType:
    class Meta:
        name = "ARefRestrictionType"

    aref: Optional[ArefRestrictionTypeAref] = field(
        default=None,
        metadata={
            "name": "ARef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    type_value: Optional[ArefRestrictionTypeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
