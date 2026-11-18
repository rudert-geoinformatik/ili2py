"""
xsdata converters for the special types of the python classes reading XTF, rendered (see
`writers.py.render`).
"""

import importlib
from base64 import b64decode, b64encode
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

from xsdata.formats.converter import Converter, converter


class TypeConverter(Converter):
    """
    Base of the converters of a library type. The type is bound per instance, so every
    registered type gets its own converter.
    """

    def __init__(self, data_type: type):
        """
        Args:
            data_type: The type of the library the converter is responsible for.
        """
        self.data_type = data_type


class SpecialTypeConverter(TypeConverter):
    """
    Converts the special str, int and float types of a library (e.g. INTERLIS.UUIDOID,
    INTERLIS.GregorianYear).
    """

    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        """The text of the XTF as the special type, so the value keeps knowing what it is."""
        return self.data_type(value) if value is not None else None

    def serialize(self, value: Any, **kwargs: Any) -> str | None:  # type: ignore[override]
        """The value as text, the special type is a str, int or float underneath anyway."""
        return str(value) if value is not None else None


class BinBlBoxConverter(TypeConverter):
    """
    Converts the BLACKBOX BINARY type of a library, the XTF holds it base64 encoded.
    """

    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        """The base64 text of the XTF as the bytes it stands for."""
        return self.data_type(b64decode(value)) if value is not None else None

    def serialize(self, value: Any, **kwargs: Any) -> str | None:  # type: ignore[override]
        """The bytes back as base64 text."""
        return b64encode(value).decode() if value is not None else None


@contextmanager
def registered_types(
    bin_bl_box: type,
    special_types: list[type],
    converters: dict[type, Converter] | None = None,
) -> Iterator[None]:
    """
    Registers the special types as xsdata converters and unregisters them on exit. xsdata
    supports only registered types, models and enums, without it e.g. a TID typed with
    INTERLIS.UUIDOID fails. Reading and writing have to happen inside, the parser and the
    serializer build their own context.

    Types registered already (e.g. by an enclosing block) are left to their owner, so the
    blocks can be nested. The converter registry of xsdata is global per process, it is not
    thread safe.

    Args:
        bin_bl_box: The bytes type of BLACKBOX BINARY.
        special_types: The str, int and float types of the domains.
        converters: Further converters, key is the type.
    """
    converters = {bin_bl_box: BinBlBoxConverter(bin_bl_box)} | (converters or {})
    for special_type in special_types:
        converters[special_type] = SpecialTypeConverter(special_type)
    converters = {
        data_type: type_converter
        for data_type, type_converter in converters.items()
        if data_type not in converter.registry
    }
    for data_type, type_converter in converters.items():
        converter.register_converter(data_type, type_converter)
    try:
        yield
    finally:
        for data_type in converters:
            converter.unregister_converter(data_type)


@contextmanager
def registered_converters(
    library_name: str, converters: dict[type, Converter] | None = None
) -> Iterator[None]:
    """
    Registers the special types of a rendered library as xsdata converters, see
    `registered_types`.

    Args:
        library_name: The name of the rendered library, it has to be importable.
        converters: Further converters, key is the type.
    """
    importlib.import_module(f"{library_name}.xtf_opening")
    convertable_types = importlib.import_module(f"{library_name}.convertable_types")
    references = importlib.import_module(f"{library_name}.references")
    # 2.3 wraps the bytes in the BinBlBoxType element, 2.4 uses BinBlBoxType directly
    bin_bl_box = getattr(references, "BinBlBox", references.BinBlBoxType)
    special_types = (
        convertable_types.get_special_str_types()
        + convertable_types.get_special_int_types()
        + convertable_types.get_special_float_types()
    )
    with registered_types(bin_bl_box, special_types, converters):
        yield
