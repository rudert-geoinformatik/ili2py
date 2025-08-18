from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_metype import ExtendableMetype

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ExtendableMe(ExtendableMetype):
    class Meta:
        name = "ExtendableME"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
