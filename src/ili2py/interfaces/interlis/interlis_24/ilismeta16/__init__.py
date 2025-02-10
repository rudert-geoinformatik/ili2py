from dataclasses import dataclass, field
from typing import List

from ili2py.interfaces.interlis.interlis_24 import ILI_META_BASE, Transfer
from ili2py.interfaces.interlis.interlis_24.ilismeta16.shared import imd_namespace_map
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.model_data import ModelData


@dataclass(kw_only=True)
class Datasection:
    class Meta(ILI_META_BASE):
        pass

    ModelData: List["ModelData"] = field(
        metadata={
            "namespace": imd_namespace_map['IlisMeta16']
        }
    )


@dataclass(kw_only=True)
class ImdTransfer(Transfer):
    class Meta(ILI_META_BASE):
        pass

    datasection: Datasection

