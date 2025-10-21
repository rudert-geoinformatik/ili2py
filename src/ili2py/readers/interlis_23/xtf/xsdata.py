from typing import IO, AnyStr

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

from ili2py.interfaces.interlis.interlis_23 import TRANSFER
from ili2py.interfaces.interlis.interlis_23.generator import DataClassGenerator
from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer


class Reader:

    def __init__(
        self,
        meta_model: ImdTransfer,
        fail_on_unknown_properties: bool = False,
        namespace_map: dict | None = None,
    ):
        self.parser = XmlParser()
        self.parser.config = ParserConfig()
        self.parser.config.fail_on_unknown_properties = fail_on_unknown_properties
        self.namespace_map = namespace_map or {}
        self.parser.ns_map = self.namespace_map
        self.meta_model = meta_model

    def read(self, input_xtf: str | IO[AnyStr]):
        """
        Parses an XTF XML file into the dataclass objects for further usage.

        Args:
            input_xtf: The path or the file object to read the imd16 from
        """
        # we preparse the XTF to find out what model we are handling
        pre_xtf = self.parser.parse(input_xtf, TRANSFER)
        xtf_data = {}
        for model in pre_xtf.HEADERSECTION.MODELS:
            generated_dataclasses = DataClassGenerator(self.meta_model).generate(model.NAME)
            xtf_data[model.NAME] = self.parser.parse(input_xtf, generated_dataclasses)
        return xtf_data
