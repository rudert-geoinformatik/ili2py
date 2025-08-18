from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.aref_restriction_type import ArefRestrictionType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ArefRestriction(ArefRestrictionType):
    class Meta:
        name = "ARefRestriction"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
