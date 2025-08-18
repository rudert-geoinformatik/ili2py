from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.constraint_type_to_class import ConstraintTypeToClass
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.constraint_type_to_domain import ConstraintTypeToDomain
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_element_type import MetaElementType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ConstraintType(MetaElementType):
    to_class: Optional[ConstraintTypeToClass] = field(
        default=None,
        metadata={
            "name": "ToClass",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    to_domain: Optional[ConstraintTypeToDomain] = field(
        default=None,
        metadata={
            "name": "ToDomain",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
