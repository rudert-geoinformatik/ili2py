from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.dependency_type_dependent import DependencyTypeDependent
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.dependency_type_using import DependencyTypeUsing

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DependencyType:
    using: Optional[DependencyTypeUsing] = field(
        default=None,
        metadata={
            "name": "Using",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    dependent: Optional[DependencyTypeDependent] = field(
        default=None,
        metadata={
            "name": "Dependent",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
