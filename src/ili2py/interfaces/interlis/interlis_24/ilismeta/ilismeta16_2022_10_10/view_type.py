from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_type import ClassType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.view_type_formation_parameter import ViewTypeFormationParameter
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.view_type_where import ViewTypeWhere

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ViewType(ClassType):
    formation_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "FormationKind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    formation_parameter: list[ViewTypeFormationParameter] = field(
        default_factory=list,
        metadata={
            "name": "FormationParameter",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    where: Optional[ViewTypeWhere] = field(
        default=None,
        metadata={
            "name": "Where",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    transient: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Transient",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
