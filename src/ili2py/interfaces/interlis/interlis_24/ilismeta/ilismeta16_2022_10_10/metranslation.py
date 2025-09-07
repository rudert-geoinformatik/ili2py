from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.metranslation_type import MetranslationType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Metranslation(MetranslationType):
    class Meta:
        name = "METranslation"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
