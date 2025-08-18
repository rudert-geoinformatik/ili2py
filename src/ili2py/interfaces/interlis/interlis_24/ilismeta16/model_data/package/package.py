from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import imd_namespace_map
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element import Ili1FormatElement
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.meta_element import MetaElement


@dataclass(kw_only=True)
class Package(MetaElement):
    pass


@dataclass
class Model(Package):
    class KindEnum(StrEnum):
        NormalM = auto()
        TypeM = auto()
        RefSystemM = auto()
        SymbologyM = auto()

    iliVersion: str = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    Kind: KindEnum = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    Contracted: Optional[bool] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    Language: Optional[str] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    At: Optional[str] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    Version: Optional[str] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    NoIncrementalTransfer: Optional[bool] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    CharSetIANAName: Optional[str] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    xmlns: Optional[str] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    ili1Transfername: Optional[str] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    ili1Format: Optional["Model._Ili1Format"] = field(
        default=None,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )

    @dataclass
    class _Ili1Format:
        Ili1Format: Optional[Ili1FormatElement] = None


@dataclass
class SubModel(Package):
    pass

