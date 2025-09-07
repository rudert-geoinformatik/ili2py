from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.local_ftype_type import LocalFtypeType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LocalFtype(LocalFtypeType):
    class Meta:
        name = "LocalFType"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
