from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.doc_text_translation import DocTextTranslation

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetranslationTypeTranslatedDoc:
    class Meta:
        global_type = False

    doc_text_translation: Optional[DocTextTranslation] = field(
        default=None,
        metadata={
            "name": "DocTextTranslation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
