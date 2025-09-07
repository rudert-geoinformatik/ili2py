from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.domain_type_type import DomainTypeType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.line_type_type_coord_type import LineTypeTypeCoordType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.line_type_type_lastructure import LineTypeTypeLastructure

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LineTypeType(DomainTypeType):
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    max_overlap: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxOverlap",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    multi: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Multi",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    coord_type: Optional[LineTypeTypeCoordType] = field(
        default=None,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    lastructure: Optional[LineTypeTypeLastructure] = field(
        default=None,
        metadata={
            "name": "LAStructure",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
