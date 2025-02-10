from dataclasses import dataclass
from typing import List, Type


# the common name space used in an INTERLIS 2.3 XTF
namespace_map = {
    "ili": "http://www.interlis.ch/INTERLIS2.3"
}


class ILI_META_BASE:
    namespace = namespace_map["ili"]



@dataclass(kw_only=True)
class MODEL:
    class Meta(ILI_META_BASE):
        pass

    NAME: str
    VERSION: str
    URI: str

@dataclass
class HeaderSection:
    class Meta(ILI_META_BASE):
        pass

    MODELS: List[MODEL]
    SENDER: str
    VERSION: str

@dataclass
class TRANSFER:
    class Meta(ILI_META_BASE):
        pass

    HEADERSECTION: HeaderSection
