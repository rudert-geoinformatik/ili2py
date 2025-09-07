from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.path_el_type_ref import PathElTypeRef

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class PathElType:
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ref: Optional[PathElTypeRef] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    num_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumIndex",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )
    spec_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecIndex",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
