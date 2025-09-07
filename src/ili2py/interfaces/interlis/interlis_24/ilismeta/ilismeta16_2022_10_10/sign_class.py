from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.sign_class_type import SignClassType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class SignClass(SignClassType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
