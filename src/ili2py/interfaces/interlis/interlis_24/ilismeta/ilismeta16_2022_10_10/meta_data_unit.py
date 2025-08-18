from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_data_unit_type import MetaDataUnitType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaDataUnit(MetaDataUnitType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
