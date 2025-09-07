from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_ref_type_ref import ClassRefTypeRef
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_ref_type_type import ClassRefTypeType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassRefType(ClassRefTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[ClassRefTypeRef] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )