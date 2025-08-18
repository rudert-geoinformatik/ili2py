from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.aref_of_type import ArefOfType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ArefOf(ArefOfType):
    class Meta:
        name = "ARefOf"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
