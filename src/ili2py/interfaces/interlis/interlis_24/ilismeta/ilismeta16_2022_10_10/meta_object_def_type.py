from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_element_type import MetaElementType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_object_def_type_class import MetaObjectDefTypeClass
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_object_def_type_meta_basket_def import (
    MetaObjectDefTypeMetaBasketDef,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaObjectDefType(MetaElementType):
    is_ref_system: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRefSystem",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    class_value: Optional[MetaObjectDefTypeClass] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    meta_basket_def: Optional[MetaObjectDefTypeMetaBasketDef] = field(
        default=None,
        metadata={
            "name": "MetaBasketDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
