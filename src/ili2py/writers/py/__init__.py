from ili2py.mappers.helpers import Index
from ili2py.writers.py.interlis23.python import Library
from ili2py.writers import handle_model_versions
from ili2py.writers.py.interlis23 import reader_classes


def create_python_classes(library: Library, index: Index, output_path: str):
    ili_version = handle_model_versions(index)
    if ili_version == "2.3":
        reader_classes(library, output_path)
    else:
        raise NotImplementedError(f"ili version '{ili_version}' not supported")
