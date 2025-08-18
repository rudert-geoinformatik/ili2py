from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.metranslation_type_of import MetranslationTypeOf
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.metranslation_type_translated_doc import (
    MetranslationTypeTranslatedDoc,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetranslationType:
    class Meta:
        name = "METranslationType"

    of: Optional[MetranslationTypeOf] = field(
        default=None,
        metadata={
            "name": "Of",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    translated_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TranslatedName",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    translated_doc: list[MetranslationTypeTranslatedDoc] = field(
        default_factory=list,
        metadata={
            "name": "TranslatedDoc",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
