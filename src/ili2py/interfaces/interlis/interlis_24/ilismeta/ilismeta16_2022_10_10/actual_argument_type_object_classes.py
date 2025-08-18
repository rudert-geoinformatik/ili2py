from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_ref import ClassRef

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ActualArgumentTypeObjectClasses:
    class Meta:
        global_type = False

    class_ref: Optional[ClassRef] = field(
        default=None,
        metadata={
            "name": "ClassRef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
