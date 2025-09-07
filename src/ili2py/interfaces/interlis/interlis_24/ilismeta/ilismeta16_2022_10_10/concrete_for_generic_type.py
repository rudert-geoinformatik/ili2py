from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.concrete_for_generic_type_concrete_domain import (
    ConcreteForGenericTypeConcreteDomain,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.concrete_for_generic_type_generic_def import (
    ConcreteForGenericTypeGenericDef,
)

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ConcreteForGenericType:
    generic_def: Optional[ConcreteForGenericTypeGenericDef] = field(
        default=None,
        metadata={
            "name": "GenericDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    concrete_domain: Optional[ConcreteForGenericTypeConcreteDomain] = field(
        default=None,
        metadata={
            "name": "ConcreteDomain",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
