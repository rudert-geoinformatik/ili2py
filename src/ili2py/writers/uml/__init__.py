from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.model_data import ModelData
from typing import List

from ili2py.writers.uml.interlis_23 import uml_diagram


def find_model_data_by_name(name: str, model_data: List[ModelData]) -> int:
    for index, item in enumerate(model_data):
        if item.Model.Name == name:
            return index
    raise AttributeError(f"No model found with name {name}")


def create_uml_diagram(model_names: List[str], transfer: ImdTransfer, flavour: str):
    # TODO: This is probably ugly (aka can we have mixed ili versions?
    if transfer.datasection.ModelData[-1].Model.Version == '2.3':
        return uml_diagram(transfer, model_names, flavour)
    else:
        raise NotImplemented
