from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Optional

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

    iliVersion: str
    Kind: KindEnum
    Contracted: Optional[bool] = None
    Language: Optional[str] = None
    At: Optional[str] = None
    Version: Optional[str] = None
    NoIncrementalTransfer: Optional[bool] = None
    CharSetIANAName: Optional[str] = None
    xmlns: Optional[str] = None
    ili1Transfername: Optional[str] = None
    ili1Format: Optional["Model._Ili1Format"] = None

    @dataclass
    class _Ili1Format:
        Ili1Format: Optional[Ili1FormatElement] = None


@dataclass
class SubModel(Package):
    pass

