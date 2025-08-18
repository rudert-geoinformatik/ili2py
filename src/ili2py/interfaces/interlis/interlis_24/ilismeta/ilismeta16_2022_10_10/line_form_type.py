from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.line_form_type_structure import LineFormTypeStructure
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_element_type import MetaElementType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LineFormType(MetaElementType):
    structure: Optional[LineFormTypeStructure] = field(
        default=None,
        metadata={
            "name": "Structure",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
