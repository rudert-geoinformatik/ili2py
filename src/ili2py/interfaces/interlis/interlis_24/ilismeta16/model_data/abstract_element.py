from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import HasRef, Ref
from ili2py.interfaces.interlis.interlis_24.ilismeta16.shared import IMD_META_BASE, imd_namespace_map


@dataclass
class AbstractElement:
    class Meta(IMD_META_BASE):
        pass


@dataclass
class Ili1FormatElement(AbstractElement):

    class TidKind(StrEnum):
        TID_I16 = auto()
        TID_I32 = auto()
        TID_ANY = auto()
        TID_EXPLANATION = auto()

    isFree: bool
    blankCode: int
    undefinedCode: int
    continueCode: int
    Font: str
    tidKind: TidKind
    LineSize: Optional[int] = None
    tidSize: Optional[int] = None
    tidExplanation: Optional[str] = None


@dataclass
class DocTextElement(AbstractElement):

    Text: str
    Name: Optional[str] = None


@dataclass
class MetaAttributeElement(HasRef,AbstractElement):

    Name: str
    Value: str
    tid: str = field(
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["ili"]
        }
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    MetaElement_ref: Ref = field(
        metadata={
            "name": "MetaElement"
        }
    )

