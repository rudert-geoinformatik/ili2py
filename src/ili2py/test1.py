import os
import tempfile
from contextlib import contextmanager
from typing import Any, Optional, Type, Iterable, Tuple

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.converter import Converter, converter
from xsdata.formats.dataclass.parsers.config import ParserConfig
import logging

from xsdata.formats.dataclass.serializers import XmlSerializer

from ili2py.writers.uml import uml_diagram
from ili2py.writers.uml.interlis_23.uml import Diagram
from ili2py.writers.py.render import render_configuration, base_url_24

logging.getLogger().setLevel(logging.DEBUG)

from ili2py_interface.xtf_opening import Transfer
from ili2py_interface.convertable_types import (
    get_special_float_types,
    get_special_str_types,
    get_special_int_types,
    get_contained_model_names,
)
from ili2py_interface.references import XmlBlBoxType, BinBlBoxType

context = XmlContext()


@contextmanager
def temp_register():
    registered = []
    float_types = get_special_float_types()
    str_types = get_special_str_types()
    int_types = get_special_int_types()
    try:

        class Ili2PyConverterClassBinBlBoxType(Converter):
            def deserialize(self, value: Any, **kwargs: Any) -> bytes:
                from base64 import b64decode

                return b64decode(value)

            def serialize(self, value: Any, **kwargs: Any) -> Optional[str]:
                from base64 import b64encode

                if value:
                    return b64encode(value).decode()
                else:
                    return None

        converter.register_converter(BinBlBoxType, Ili2PyConverterClassBinBlBoxType())
        for float_type in float_types:

            def deserialize(self, value: Any, **kwargs: Any) -> Type[float_type]:
                return float_type(value) if value else None

            def serialize(self, value: Any, **kwargs: Any) -> Optional[str]:
                return str(value) if value else None

            Ili2PyConverterClass = type(
                f"Converter{float_type.__name__}",
                (Converter,),
                {"deserialize": deserialize, "serialize": serialize},
            )
            converter.register_converter(float_type, Ili2PyConverterClass())
            registered.append(float_type)
        for str_type in str_types:

            def deserialize(self, value: Any, **kwargs: Any) -> Type[str_type]:
                return str_type(value) if value else None

            def serialize(self, value: Any, **kwargs: Any) -> Optional[str]:
                return str(value) if value else None

            Ili2PyConverterClass = type(
                f"Converter{str_type.__name__}",
                (Converter,),
                {"deserialize": deserialize, "serialize": serialize},
            )
            converter.register_converter(str_type, Ili2PyConverterClass())
            registered.append(str_type)
        for int_type in int_types:

            def deserialize(self, value: Any, **kwargs: Any) -> Type[int_type]:
                return int_type(value) if value else None

            def serialize(self, value: Any, **kwargs: Any) -> Optional[str]:
                return str(value) if value else None

            Ili2PyConverterClass = type(
                f"Converter{int_type.__name__}",
                (Converter,),
                {"deserialize": deserialize, "serialize": serialize},
            )
            converter.register_converter(int_type, Ili2PyConverterClass())
            registered.append(int_type)

        yield
    finally:
        for tp in registered:
            try:
                converter.unregister_converter(tp)
            except KeyError:
                pass


parser_config = ParserConfig(
    fail_on_unknown_properties=False,
    fail_on_unknown_attributes=False,
)
with temp_register():
    parser = XmlParser(parser_config)
    ili_version = "2.3"
    xtf_path = "/home/kalle/projects/rudert-geoinformatik/ili2py/tests/data/models/OeREBKRMtrsfr_V2_0/ch.bazl.kataster-belasteter-standorte-zivilflugplaetze_v2_0.oereb.xtf"
    # xtf_path = "/home/kalle/projects/rudert-geoinformatik/ili2py/tests/data/models/Nutzungsplanung_V1_2/NE_073_plans_affectation_v1_2.xtf"
    # xtf_path = "/home/kalle/projects/rudert-geoinformatik/ili2py/tests/data/models/Waldreservate_V2_0/waldreservate_v2_0.xtf"
    # xtf_path = "/home/kalle/projects/rudert-geoinformatik/ili2py/tests/data/models/Waldreservate_V2_0/ur_uri_waldreservate_mgdm_v2_0.xtf"
    data = parser.parse(xtf_path, Transfer)
    xtf_path = os.path.join(tempfile.mkdtemp(prefix="ili2py"), "test.xtf")

    namespace_map = render_configuration[ili_version]["namespace_map"]
    if ili_version == "2.4":
        for name in get_contained_model_names():
            namespace_map[name] = f"{base_url_24}/{name}"
    with open(xtf_path, mode="w+") as f:
        # f.write(XmlSerializer().render(data, ns_map=namespace_map))
        pass
    x = 1
