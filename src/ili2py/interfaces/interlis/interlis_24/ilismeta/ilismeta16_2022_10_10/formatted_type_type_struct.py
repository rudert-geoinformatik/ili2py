from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.struct_of_format import StructOfFormat

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class FormattedTypeTypeStruct:
    class Meta:
        global_type = False

    struct_of_format: Optional[StructOfFormat] = field(
        default=None,
        metadata={
            "name": "StructOfFormat",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
