from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.base_class_type_base_class import BaseClassTypeBaseClass
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.base_class_type_crt import BaseClassTypeCrt

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class BaseClassType:
    crt: Optional[BaseClassTypeCrt] = field(
        default=None,
        metadata={
            "name": "CRT",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    base_class: Optional[BaseClassTypeBaseClass] = field(
        default=None,
        metadata={
            "name": "BaseClass",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
