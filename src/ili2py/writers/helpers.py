import logging
import os
from pathlib import Path

from ili2py.mappers.helpers import Index


def handle_model_versions(index: Index) -> str:
    ili_version = None
    for model in index.types_bucket["Model"]:
        if model.name == "INTERLIS":
            logging.debug(
                "INTERLIS package is ignored for version check due "
                "to https://github.com/claeis/ili2c/issues/146"
            )
        else:
            if not ili_version:
                ili_version = model.ili_version
            if model.ili_version != ili_version:
                logging.error(f"General version {ili_version} does not match package {model}")
                raise RuntimeError(
                    "Different ili versions in one library are not supported "
                    "(enable debug and check logs for details). Please have also a look at "
                    "https://interlis.discourse.group/t/gibt-es-gruende-weshalb-man-ili2-3-und-ili2-4-nicht-mischen-sollte/78"
                )
    return ili_version


def create_file(output_path: str, model_name: str, file_name: str):
    output_file = Path(os.path.join(output_path, model_name, file_name))
    output_file.parent.mkdir(exist_ok=True, parents=True)
    return output_file
