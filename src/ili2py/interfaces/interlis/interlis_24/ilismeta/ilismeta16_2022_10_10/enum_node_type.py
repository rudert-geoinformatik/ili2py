from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.enum_node_type_enum_type import EnumNodeTypeEnumType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.enum_node_type_parent_node import EnumNodeTypeParentNode
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_metype import ExtendableMetype

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class EnumNodeType(ExtendableMetype):
    enum_type: Optional[EnumNodeTypeEnumType] = field(
        default=None,
        metadata={
            "name": "EnumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    parent_node: Optional[EnumNodeTypeParentNode] = field(
        default=None,
        metadata={
            "name": "ParentNode",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
