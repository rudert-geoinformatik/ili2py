from ili2py.interfaces.metamodel import ns_map
from dataclasses import dataclass, field
from typing import List, Optional
from ili2py.interfaces.metamodel.ilismeta16 import ModelData


class ILI_META_BASE:
    namespace = ns_map["ili"]


@dataclass(kw_only=True)
class Datasection:
    class Meta(ILI_META_BASE):
        name = "datasection"

    model_data: List[ModelData] = field(
        metadata={
            "name": "ModelData",
            "type": "Element",
            "namespace": ns_map["IlisMeta16"],
            "min_occurs": 1
        },
    )


@dataclass
class Model:
    class Meta(ILI_META_BASE):
        pass

    model: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "min_occurs": 1,
            "namespace": ns_map["ili"],
        },
    )


@dataclass
class Headersection:
    class Meta(ILI_META_BASE):
        name = "headersection"

    models: List[Model] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sender: str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Transfer:
    class Meta(ILI_META_BASE):
        name = "transfer"

    headersection: Headersection = field(
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    datasection: Datasection = field(
        metadata={
            "type": "Element",
            "required": True,
        },
    )