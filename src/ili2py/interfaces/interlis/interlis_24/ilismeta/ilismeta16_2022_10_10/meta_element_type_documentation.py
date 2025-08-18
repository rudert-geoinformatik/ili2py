from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.doc_text import DocText

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaElementTypeDocumentation:
    class Meta:
        global_type = False

    doc_text: Optional[DocText] = field(
        default=None,
        metadata={
            "name": "DocText",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
