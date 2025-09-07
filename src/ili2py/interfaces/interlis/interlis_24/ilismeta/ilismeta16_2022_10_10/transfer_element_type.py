from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.transfer_element_type_transfer_class import (
    TransferElementTypeTransferClass,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.transfer_element_type_transfer_element import (
    TransferElementTypeTransferElement,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TransferElementType:
    transfer_class: Optional[TransferElementTypeTransferClass] = field(
        default=None,
        metadata={
            "name": "TransferClass",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    transfer_element: Optional[TransferElementTypeTransferElement] = field(
        default=None,
        metadata={
            "name": "TransferElement",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
