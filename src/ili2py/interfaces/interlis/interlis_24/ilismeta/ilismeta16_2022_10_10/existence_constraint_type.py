from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.constraint_type import ConstraintType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.existence_constraint_type_attr import ExistenceConstraintTypeAttr

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ExistenceConstraintType(ConstraintType):
    attr: Optional[ExistenceConstraintTypeAttr] = field(
        default=None,
        metadata={
            "name": "Attr",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
