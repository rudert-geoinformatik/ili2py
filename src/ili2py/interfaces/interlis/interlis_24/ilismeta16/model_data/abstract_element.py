from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import HasRef, Ref
from ili2py.interfaces.interlis.interlis_24.ilismeta16.shared import imd_namespace_map


@dataclass
class AbstractElement:
    pass


@dataclass
class Ili1FormatElement(AbstractElement):

    class TidKind(StrEnum):
        TID_I16 = auto()
        TID_I32 = auto()
        TID_ANY = auto()
        TID_EXPLANATION = auto()

    isFree: bool = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    blankCode: int = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    undefinedCode: int = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    continueCode: int = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    Font: str = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    tidKind: TidKind = field(metadata={"namespace": imd_namespace_map["IlisMeta16"]})
    LineSize: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["IlisMeta16"],
        },
    )
    tidSize: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["IlisMeta16"],
        },
    )
    tidExplanation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["IlisMeta16"],
        },
    )


@dataclass
class DocTextElement(AbstractElement):

    Text: str = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        },
    )
    Name: Optional[str] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        },
    )


@dataclass
class MetaAttributeElement(HasRef, AbstractElement):

    Name: str = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        },
    )
    Value: str = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        },
    )
    tid: str = field(metadata={"type": "Attribute", "namespace": imd_namespace_map["ili"]})
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    MetaElement_ref: Ref = field(
        metadata={
            "name": "MetaElement",
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
