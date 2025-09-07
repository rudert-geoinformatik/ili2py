from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.any_oidtype_type import AnyOidtypeType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AnyOidtype(AnyOidtypeType):
    class Meta:
        name = "AnyOIDType"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
