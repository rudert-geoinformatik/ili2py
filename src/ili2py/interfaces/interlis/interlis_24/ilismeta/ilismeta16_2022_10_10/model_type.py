from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.model_type_ili1_format import ModelTypeIli1Format
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.package_type import PackageType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ModelType(PackageType):
    ili_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "iliVersion",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    contracted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Contracted",
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
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "max_length": 5,
        },
    )
    at: Optional[str] = field(
        default=None,
        metadata={
            "name": "At",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    no_incremental_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoIncrementalTransfer",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    char_set_iananame: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSetIANAName",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    xmlns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ili1_transfername: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili1Transfername",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ili1_format: Optional[ModelTypeIli1Format] = field(
        default=None,
        metadata={
            "name": "ili1Format",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
