from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.model_data_basket_oidtype import ModelDataBasketOidtype

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ModelDataBasketOid(ModelDataBasketOidtype):
    class Meta:
        name = "ModelData.BasketOID"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
