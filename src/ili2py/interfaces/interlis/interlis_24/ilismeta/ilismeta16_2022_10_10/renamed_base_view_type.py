from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_metype import ExtendableMetype
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.renamed_base_view_type_base_view import (
    RenamedBaseViewTypeBaseView,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.renamed_base_view_type_view import RenamedBaseViewTypeView

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class RenamedBaseViewType(ExtendableMetype):
    or_null: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OrNull",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    base_view: Optional[RenamedBaseViewTypeBaseView] = field(
        default=None,
        metadata={
            "name": "BaseView",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    view: Optional[RenamedBaseViewTypeView] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
