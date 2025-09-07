from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.attribute_const_type_attribute import AttributeConstTypeAttribute
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.factor_type import FactorType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AttributeConstType(FactorType):
    attribute: Optional[AttributeConstTypeAttribute] = field(
        default=None,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
