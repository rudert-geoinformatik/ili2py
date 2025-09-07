from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.argument_type_1 import ArgumentType1

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Argument(ArgumentType1):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
