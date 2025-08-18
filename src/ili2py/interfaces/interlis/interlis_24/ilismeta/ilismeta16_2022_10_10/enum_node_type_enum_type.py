from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.top_node import TopNode

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class EnumNodeTypeEnumType:
    class Meta:
        global_type = False

    top_node: Optional[TopNode] = field(
        default=None,
        metadata={
            "name": "TopNode",
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
    order_pos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
