from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.ili1_format_type import Ili1FormatType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Ili1Format(Ili1FormatType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
