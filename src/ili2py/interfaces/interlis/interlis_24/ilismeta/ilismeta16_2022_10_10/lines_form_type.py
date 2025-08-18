from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.lines_form_type_line_form import LinesFormTypeLineForm
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.lines_form_type_line_type import LinesFormTypeLineType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LinesFormType:
    line_type: Optional[LinesFormTypeLineType] = field(
        default=None,
        metadata={
            "name": "LineType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    line_form: Optional[LinesFormTypeLineForm] = field(
        default=None,
        metadata={
            "name": "LineForm",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
