from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DocTextTranslationType:
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
