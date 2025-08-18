from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.allowed_in_basket_type_class_in_basket import (
    AllowedInBasketTypeClassInBasket,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.allowed_in_basket_type_of_data_unit import (
    AllowedInBasketTypeOfDataUnit,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AllowedInBasketType:
    of_data_unit: Optional[AllowedInBasketTypeOfDataUnit] = field(
        default=None,
        metadata={
            "name": "OfDataUnit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    class_in_basket: Optional[AllowedInBasketTypeClassInBasket] = field(
        default=None,
        metadata={
            "name": "ClassInBasket",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
