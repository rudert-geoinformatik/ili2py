from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me import \
    ExtendableMe
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import Ref, HasRef
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.serialization_elements import MultiplicityElement


@dataclass(kw_only=True)
class Type(ExtendableMe):
    LTParent_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "LTParent"
        },
    )


@dataclass
class Class(Type):

    class KindEnum(StrEnum):
        Structure = auto()
        Class = auto()
        View = auto()
        Association = auto()

    @dataclass
    class _Multiplicity:
        multiplicity: Optional[MultiplicityElement] = None

    Kind: KindEnum
    EmbeddedRoleTransfer: bool
    ili1OptionalTable: Optional[bool] = None
    Multiplicity: Optional["Class._Multiplicity"] = None
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Oid_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "Oid"
        }
    )

    # TODO: implement ASSOCIATION ClassConstraint
    # TODO: implement ASSOCIATION ClassAttr
    # TODO: implement ASSOCIATION ClassParam
    # TODO: implement ASSOCIATION BaseClass




@dataclass
class BaseClass(HasRef):

    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    CRT_ref: Ref = field(
        metadata={
            "name": "CRT"
        }
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    BaseClass_ref: Ref = field(
        metadata={
            "name": "BaseClass"
        }
    )