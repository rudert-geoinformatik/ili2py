import logging

from ili2py.mappers.python import Library

from ili2py.writers.py.interlis23 import reader_classes


def create_python_classes(library: Library, output_path: str):
    # TODO: This is probably ugly (aka can we have mixed ili versions?
    ili_version = None
    for package in library.packages:
        if package.identifier == "INTERLIS":
            logging.debug(
                "INTERLIS package is ignored for version check due "
                "to https://github.com/claeis/ili2c/issues/146"
            )
        else:
            if not ili_version:
                ili_version = package.ili_version
            if package.ili_version != ili_version:
                logging.error(f"General version {ili_version} does not match package {package}")
                raise RuntimeError(
                    "Different ili versions in one library are not supported "
                    "(enable debug and check logs for details). Please have also a look at "
                    "https://interlis.discourse.group/t/gibt-es-gruende-weshalb-man-ili2-3-und-ili2-4-nicht-mischen-sollte/78"
                )
    if ili_version == "2.3":
        reader_classes(library, output_path)
    else:
        raise NotImplementedError(f"ili version '{ili_version}' not supportes")
