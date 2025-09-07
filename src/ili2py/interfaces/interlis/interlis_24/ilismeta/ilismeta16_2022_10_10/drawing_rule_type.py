from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.drawing_rule_type_class import DrawingRuleTypeClass
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.drawing_rule_type_graphic import DrawingRuleTypeGraphic
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.drawing_rule_type_rule import DrawingRuleTypeRule
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_metype import ExtendableMetype

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DrawingRuleType(ExtendableMetype):
    rule: list[DrawingRuleTypeRule] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_value: Optional[DrawingRuleTypeClass] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    graphic: Optional[DrawingRuleTypeGraphic] = field(
        default=None,
        metadata={
            "name": "Graphic",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
