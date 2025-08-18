from abc import ABC
from typing import AnyStr, IO

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer


class Reader(ABC):
    _reader_class = None

    def __init__(self, fail_on_unknown_properties: bool = False, fail_on_unknown_attributes: bool = False, namespace_map: dict|None = None):
        self.parser_config = ParserConfig(
            fail_on_unknown_properties=fail_on_unknown_properties,
            fail_on_unknown_attributes= fail_on_unknown_attributes
        )
        self.parser = XmlParser(self.parser_config)
        self.namespace_map = namespace_map or {}
        self.parser.ns_map = self.namespace_map

    def read(self, input_xtf: str|IO[AnyStr]) -> ImdTransfer:
        """
        Parses an IMD16 XML file into the dataclass objects for further usage.

        Args:
            input_xtf: The path or the file object to read the imd16 from
        Returns:
            The tree of IMD16 definitions.
        """
        return self.parser.parse(input_xtf, self._reader_class)


class Imd16Reader(Reader):
    _reader_class = ImdTransfer