"""
The rendered classes (writers/py/render.py) read the XTF of a model and write it again.
Read with compact geometry, the rendered classes have to write the same XTF. Validation of
the written XTF with ilivalidator is in `test_roundtrip_xtf.py`.

Sections: `pytest -m rendered_read`, `pytest -m rendered_write`.
"""

from io import StringIO

import pytest
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from ili2py.readers.xtf.converters import registered_converters
from ili2py.readers.xtf.xsdata_backend import XsdataBackend

from .helpers import geometries_by_access, imported_library, xtf_header


class TestRenderedXtf:
    @pytest.mark.rendered_read
    @pytest.mark.parametrize("compact_geometry", [False, True], ids=["dataclasses", "compact"])
    def test_rendered_classes_read_the_xtf(
        self, fast_library, fast_xtf, parser_config, compact_geometry
    ):
        backend = XsdataBackend(parser_config=parser_config, compact_geometry=compact_geometry)
        with imported_library(fast_library) as xtf_opening:
            transfer = backend.read(fast_xtf, xtf_opening.Transfer)
            # the root is the Transfer of the rendered library and it holds the data
            assert isinstance(transfer, xtf_opening.Transfer)
            assert transfer.datasection.baskets

    @pytest.mark.rendered_read
    def test_geometry_access_is_the_same_compact_or_not(
        self, fast_library, fast_xtf, parser_config
    ):
        with imported_library(fast_library) as xtf_opening:
            # we read the XTF twice, once with the geometry as the rendered dataclasses and
            # once compact
            as_dataclasses = XsdataBackend(parser_config=parser_config).read(
                fast_xtf, xtf_opening.Transfer
            )
            as_compact = XsdataBackend(
                parser_config=parser_config, compact_geometry=True
            ).read(fast_xtf, xtf_opening.Transfer)

        # a tool reading the geometry through the access must not see a difference: same
        # attributes, same vertices and arcs, the axis values in the same python types
        assert geometries_by_access(as_dataclasses) == geometries_by_access(as_compact)

    @pytest.mark.rendered_write
    def test_compact_geometry_writes_what_xsdata_writes(
        self, fast_library, fast_xtf, parser_config, serializer_config
    ):
        ns_map = xtf_header(fast_xtf).ns_map()
        with imported_library(fast_library) as xtf_opening:
            # xsdata on its own reads and writes the geometry element by element, this is the
            # XTF we expect
            with registered_converters(fast_library.name):
                transfer = XmlParser(config=parser_config).parse(
                    str(fast_xtf), xtf_opening.Transfer
                )
                expected = StringIO()
                XmlSerializer(config=serializer_config).write(
                    expected, transfer, ns_map=ns_map
                )
            assert expected.getvalue().startswith("<?xml")

            # the backend reads the geometry compact and writes it as text, the XTF must not
            # differ by a single character
            backend = XsdataBackend(
                parser_config=parser_config,
                serializer_config=serializer_config,
                compact_geometry=True,
            )
            transfer = backend.read(fast_xtf, xtf_opening.Transfer)
            written = StringIO()
            backend.write(transfer, written, ns_map)
            assert written.getvalue() == expected.getvalue()
