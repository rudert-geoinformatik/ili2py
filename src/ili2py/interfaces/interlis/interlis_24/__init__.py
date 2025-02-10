from dataclasses import dataclass
from typing import List

namespace_map = {
    "ili": "http://www.interlis.ch/xtf/2.4/INTERLIS",
    "geom": "http://www.interlis.ch/geometry/1.0",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance"
}

class ILI_META_BASE:
    namespace = namespace_map["ili"]


@dataclass
class Model:
    class Meta(ILI_META_BASE):
        pass

    model: str


@dataclass
class Headersection:
    class Meta(ILI_META_BASE):
        pass

    models: List[Model]
    sender: str = None


@dataclass
class Transfer:
    class Meta(ILI_META_BASE):
        pass

    headersection: Headersection
