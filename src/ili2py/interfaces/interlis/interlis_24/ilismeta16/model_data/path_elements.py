from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import List, Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import HasRef, Ref
from ili2py.interfaces.interlis.interlis_24.ilismeta16.shared import imd_namespace_map


@dataclass
class PathElElement(HasRef):
    # TODO: MANDATORY CONSTRAINT (Kind >= #ReferenceAttr) == DEFINED(Ref);
    class KindEnum(StrEnum):
        This = auto()
        ThisArea = auto()
        ThatArea = auto()
        Parent = auto()
        ReferenceAttr = auto()
        AssocPath = auto()
        Role = auto()
        ViewBase = auto()
        Attribute = auto()
        MetaObject = auto()

    Kind: KindEnum
    NumIndex: Optional[int] = None
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Ref_ref: Optional[Ref] = field(
        default=None,
        metadata={"name": "Ref"},
    )


@dataclass
class PathElsElement:
    PathEl: List[PathElElement] = field(default_factory=list)


@dataclass
class PathOrInspFactorElement:
    PathOrInspFactor: "PathOrInspFactor" = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
