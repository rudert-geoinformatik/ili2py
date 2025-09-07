from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_metype import ExtendableMetype
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.graphic_type_base import GraphicTypeBase
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.graphic_type_where import GraphicTypeWhere

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class GraphicType(ExtendableMetype):
    where: Optional[GraphicTypeWhere] = field(
        default=None,
        metadata={
            "name": "Where",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    base: Optional[GraphicTypeBase] = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
