from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.formal_argument_type import FormalArgumentType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class FormalArgument(FormalArgumentType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
