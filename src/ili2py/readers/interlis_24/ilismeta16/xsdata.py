from typing import AnyStr, IO

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer


class Reader:

    def __init__(self, fail_on_unknown_properties: bool = False, namespace_map: dict|None = None):
        self.parser = XmlParser()
        self.parser.config = ParserConfig()
        self.parser.config.fail_on_unknown_properties = fail_on_unknown_properties
        self.namespace_map = namespace_map or {}
        self.parser.ns_map = self.namespace_map

    def read(self, input_xtf: str|IO[AnyStr]) -> ImdTransfer:
        """
        Parses an IMD16 XML file into the dataclass objects for further usage.

        Args:
            input_meta_model: The path or the file object to read the imd16 from
        """
        xtf_data = self.parser.parse(input_xtf, ImdTransfer)
        return xtf_data
