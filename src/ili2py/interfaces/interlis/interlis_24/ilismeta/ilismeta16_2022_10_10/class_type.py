from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_type_existence_constraint import (
    ClassTypeExistenceConstraint,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_type_multiplicity import ClassTypeMultiplicity
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_type_oid import ClassTypeOid
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_type_view import ClassTypeView
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_type import TypeType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassType(TypeType):
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    multiplicity: Optional[ClassTypeMultiplicity] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    embedded_role_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EmbeddedRoleTransfer",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    ili1_optional_table: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ili1OptionalTable",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    existence_constraint: Optional[ClassTypeExistenceConstraint] = field(
        default=None,
        metadata={
            "name": "ExistenceConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    oid: Optional[ClassTypeOid] = field(
        default=None,
        metadata={
            "name": "Oid",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    view: Optional[ClassTypeView] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
