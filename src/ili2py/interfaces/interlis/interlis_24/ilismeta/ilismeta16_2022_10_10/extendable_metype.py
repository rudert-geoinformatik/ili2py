from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_metype_super import ExtendableMetypeSuper
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_element_type import MetaElementType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ExtendableMetype(MetaElementType):
    class Meta:
        name = "ExtendableMEType"

    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    super: Optional[ExtendableMetypeSuper] = field(
        default=None,
        metadata={
            "name": "Super",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
