from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_metype import ExtendableMetype
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_type_lftparent import TypeTypeLftparent
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_type_ltparent import TypeTypeLtparent

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TypeType(ExtendableMetype):
    lftparent: Optional[TypeTypeLftparent] = field(
        default=None,
        metadata={
            "name": "LFTParent",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ltparent: Optional[TypeTypeLtparent] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
