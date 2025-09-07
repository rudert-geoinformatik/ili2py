from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.constraint_type import ConstraintType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.unique_constraint_type_unique_def import (
    UniqueConstraintTypeUniqueDef,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.unique_constraint_type_where import UniqueConstraintTypeWhere

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class UniqueConstraintType(ConstraintType):
    where: Optional[UniqueConstraintTypeWhere] = field(
        default=None,
        metadata={
            "name": "Where",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    unique_def: list[UniqueConstraintTypeUniqueDef] = field(
        default_factory=list,
        metadata={
            "name": "UniqueDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_occurs": 1,
        },
    )
