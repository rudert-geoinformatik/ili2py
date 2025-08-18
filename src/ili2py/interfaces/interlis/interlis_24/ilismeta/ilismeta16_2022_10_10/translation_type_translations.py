from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.metranslation import Metranslation

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TranslationTypeTranslations:
    class Meta:
        global_type = False

    metranslation: Optional[Metranslation] = field(
        default=None,
        metadata={
            "name": "METranslation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
