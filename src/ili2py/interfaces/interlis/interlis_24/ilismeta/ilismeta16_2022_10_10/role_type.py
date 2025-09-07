from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.reference_type_type import ReferenceTypeType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.role_type_association import RoleTypeAssociation
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.role_type_derivates import RoleTypeDerivates
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.role_type_multiplicity import RoleTypeMultiplicity

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class RoleType(ReferenceTypeType):
    strongness: Optional[str] = field(
        default=None,
        metadata={
            "name": "Strongness",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    ordered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ordered",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    multiplicity: Optional[RoleTypeMultiplicity] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    derivates: list[RoleTypeDerivates] = field(
        default_factory=list,
        metadata={
            "name": "Derivates",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    embedded_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EmbeddedTransfer",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    association: Optional[RoleTypeAssociation] = field(
        default=None,
        metadata={
            "name": "Association",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
