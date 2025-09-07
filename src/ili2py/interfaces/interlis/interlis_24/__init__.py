from dataclasses import dataclass, field
from typing import List, Optional

namespace_map = {
    "ili": "http://www.interlis.ch/xtf/2.4/INTERLIS",
    "geom": "http://www.interlis.ch/geometry/1.0",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance"
}


@dataclass
class Model:

    model: str = field(
        metadata={
            "namespace": namespace_map["ili"]
        }
    )


@dataclass
class Models:
    elements: List[Model] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {"name": "model", "type": Model, "namespace": namespace_map["ili"]},
            )
        }
    )


@dataclass
class HeaderSection:

    models: Models = field(
        metadata={
            "namespace": namespace_map["ili"]
        }
    )
    sender: Optional[str] = field(
        default=None,
        metadata={"namespace": namespace_map["ili"]},
    )


@dataclass
class Transfer:

    headersection: HeaderSection = field(
        metadata={
            "namespace": namespace_map["ili"]
        }
    )
