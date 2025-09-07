from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Ili1FormatType:
    is_free: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isFree",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    line_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "LineSize",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 2147483647,
        },
    )
    tid_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "tidSize",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 2147483647,
        },
    )
    blank_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "blankCode",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )
    undefined_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "undefinedCode",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )
    continue_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "continueCode",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )
    font: Optional[str] = field(
        default=None,
        metadata={
            "name": "Font",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    tid_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "tidKind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    tid_explanation: Optional[str] = field(
        default=None,
        metadata={
            "name": "tidExplanation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
