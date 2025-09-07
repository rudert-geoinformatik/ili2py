from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.tree_value_type_of import TreeValueTypeOf

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class EnumTreeValueTypeTypeEt:
    class Meta:
        global_type = False

    tree_value_type_of: Optional[TreeValueTypeOf] = field(
        default=None,
        metadata={
            "name": "TreeValueTypeOf",
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
