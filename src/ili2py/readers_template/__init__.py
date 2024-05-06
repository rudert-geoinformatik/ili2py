from ili2py.interfaces.metamodel.ili import Transfer, ModelData
from typing import List

from ili2py.readers_template.interlis_23 import reader_classes


def find_model_data_by_name(name: str, model_data: List[ModelData]) -> int:
    for index, item in enumerate(model_data):
        if item.model.name == name:
            return index
    raise AttributeError(f"No model found with name {name}")


def create_reader_classes(model_name: str, transfer: Transfer):
    model_data = transfer.datasection.model_data[
        find_model_data_by_name(model_name, transfer.datasection.model_data)
    ]
    if model_data.model.ili_version == '2.3':
        return reader_classes(model_data, transfer.datasection.model_data)
    else:
        raise NotImplemented
