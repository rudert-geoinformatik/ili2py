from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.ili1_transfer_element_type_ili1_ref_attr import (
    Ili1TransferElementTypeIli1RefAttr,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.ili1_transfer_element_type_ili1_transfer_class import (
    Ili1TransferElementTypeIli1TransferClass,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Ili1TransferElementType:
    ili1_transfer_class: Optional[Ili1TransferElementTypeIli1TransferClass] = (
        field(
            default=None,
            metadata={
                "name": "Ili1TransferClass",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )
    )
    ili1_ref_attr: Optional[Ili1TransferElementTypeIli1RefAttr] = field(
        default=None,
        metadata={
            "name": "Ili1RefAttr",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
