from dataclasses import dataclass, field

from ili2py.interfaces.interlis.interlis_24 import Transfer
from ili2py.interfaces.interlis.interlis_24.ilismeta16.shared import imd_namespace_map
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import ModelData as Imd_ModelData


@dataclass(kw_only=True)
class DataSection:

    ModelData: list["Imd_ModelData"] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {"name": "ModelData", "type": Imd_ModelData, "namespace": imd_namespace_map['IlisMeta16']},
            )
        }
    )


@dataclass(kw_only=True)
class ImdTransfer(Transfer):

    datasection: DataSection = field(
        metadata={
            "namespace": imd_namespace_map['ili']
        }
    )
