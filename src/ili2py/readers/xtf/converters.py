"""
xsdata converters for the special types of the python classes reading XTF, rendered (see
`writers.py.render`) or built at runtime (see `readers.xtf.runtime`).
"""

import importlib
from base64 import b64decode, b64encode
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

from xsdata.formats.converter import Converter, converter


class SpecialTypeConverter(Converter):
    """
    Converts the special str, int and float types of a library (e.g. INTERLIS.UUIDOID,
    INTERLIS.GregorianYear). The type is bound per instance, so every registered type gets its
    own converter.
    """

    def __init__(self, data_type: type):
        self.data_type = data_type

    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        return self.data_type(value) if value is not None else None

    def serialize(self, value: Any, **kwargs: Any) -> str | None:  # type: ignore[override]
        return str(value) if value is not None else None


class BinBlBoxConverter(Converter):
    """
    Converts the BLACKBOX BINARY type of a library, the XTF holds it base64 encoded.
    """

    def __init__(self, data_type: type):
        self.data_type = data_type

    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        return self.data_type(b64decode(value)) if value is not None else None

    def serialize(self, value: Any, **kwargs: Any) -> str | None:  # type: ignore[override]
        return b64encode(value).decode() if value is not None else None


@contextmanager
def registered_types(bin_bl_box: type, special_types: list[type]) -> Iterator[None]:
    """
    Registers the special types as xsdata converters and unregisters them on exit. xsdata
    supports only registered types, models and enums, without it e.g. a TID typed with
    INTERLIS.UUIDOID fails. Reading and writing have to happen inside, the parser and the
    serializer build their own context.

    The converter registry of xsdata is global per process, it is not thread safe.

    Args:
        bin_bl_box: The bytes type of BLACKBOX BINARY.
        special_types: The str, int and float types of the domains.
    """
    converters: dict[type, Converter] = {bin_bl_box: BinBlBoxConverter(bin_bl_box)}
    for special_type in special_types:
        converters[special_type] = SpecialTypeConverter(special_type)
    for data_type, type_converter in converters.items():
        converter.register_converter(data_type, type_converter)
    try:
        yield
    finally:
        for data_type in converters:
            converter.unregister_converter(data_type)


@contextmanager
def registered_converters(library_name: str) -> Iterator[None]:
    """
    Registers the special types of a rendered library as xsdata converters, see
    `registered_types`.

    Args:
        library_name: The name of the rendered library, it has to be importable.
    """
    convertable_types = importlib.import_module(f"{library_name}.convertable_types")
    references = importlib.import_module(f"{library_name}.references")
    # 2.3 wraps the bytes in the BinBlBoxType element, 2.4 uses BinBlBoxType directly
    bin_bl_box = getattr(references, "BinBlBox", references.BinBlBoxType)
    special_types = (
        convertable_types.get_special_str_types()
        + convertable_types.get_special_int_types()
        + convertable_types.get_special_float_types()
    )
    with registered_types(bin_bl_box, special_types):
        yield
