from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.data_unit_type_oid import DataUnitTypeOid
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_metype import ExtendableMetype

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DataUnitType(ExtendableMetype):
    view_unit: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ViewUnit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    data_unit_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataUnitName",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    oid: Optional[DataUnitTypeOid] = field(
        default=None,
        metadata={
            "name": "Oid",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
