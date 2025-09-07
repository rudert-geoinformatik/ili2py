from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.formatted_type_type_struct import FormattedTypeTypeStruct
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.num_type_type import NumTypeType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class FormattedTypeType(NumTypeType):
    format: Optional[str] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    struct: Optional[FormattedTypeTypeStruct] = field(
        default=None,
        metadata={
            "name": "Struct",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
