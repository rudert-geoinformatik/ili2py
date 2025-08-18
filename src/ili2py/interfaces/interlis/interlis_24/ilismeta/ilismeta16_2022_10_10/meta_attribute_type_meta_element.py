from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_attributes import MetaAttributes

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaAttributeTypeMetaElement:
    class Meta:
        global_type = False

    meta_attributes: Optional[MetaAttributes] = field(
        default=None,
        metadata={
            "name": "MetaAttributes",
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
