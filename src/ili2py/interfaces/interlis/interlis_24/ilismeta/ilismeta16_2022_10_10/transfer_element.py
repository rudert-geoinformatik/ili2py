from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.transfer_element_type import TransferElementType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TransferElement(TransferElementType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
