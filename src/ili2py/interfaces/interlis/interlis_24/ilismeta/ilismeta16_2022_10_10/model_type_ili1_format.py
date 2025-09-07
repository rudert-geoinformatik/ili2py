from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.ili1_format import Ili1Format

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ModelTypeIli1Format:
    class Meta:
        global_type = False

    ili1_format: Optional[Ili1Format] = field(
        default=None,
        metadata={
            "name": "Ili1Format",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
