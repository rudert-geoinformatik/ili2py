from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.object_oidtype import ObjectOidtype

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ObjectOid(ObjectOidtype):
    class Meta:
        name = "ObjectOID"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
