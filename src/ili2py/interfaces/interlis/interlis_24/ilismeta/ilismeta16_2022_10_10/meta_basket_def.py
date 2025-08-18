from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_basket_def_type import MetaBasketDefType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaBasketDef(MetaBasketDefType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
