from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import imd_namespace_map
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me import \
    ExtendableMe
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import Ref, HasRef
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.serialization_elements import MultiplicityElement


@dataclass(kw_only=True)
class Type(ExtendableMe):
    LTParent_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "namespace": imd_namespace_map["IlisMeta16"]
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
        multiplicity: Optional[MultiplicityElement] = field(
            default=None,
            metadata={
                "name": "LTParent",
                "namespace": imd_namespace_map["IlisMeta16"]
            },
        )

    Kind: KindEnum = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    EmbeddedRoleTransfer: bool = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    ili1OptionalTable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["IlisMeta16"],
        },
    )
    Multiplicity: Optional["Class._Multiplicity"] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["IlisMeta16"],
        },
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Oid_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "Oid",
            "namespace": imd_namespace_map["IlisMeta16"]
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
            "name": "CRT",
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    BaseClass_ref: Ref = field(
        metadata={
            "name": "BaseClass",
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )