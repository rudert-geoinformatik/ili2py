from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.allowed_in_basket_type import AllowedInBasketType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AllowedInBasket(AllowedInBasketType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
