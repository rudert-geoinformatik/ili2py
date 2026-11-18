from array import array

import pytest
from lxml import etree  # type: ignore[import-untyped]

from ili2py.interfaces.interlis.interlis_23 import TRANSFER, Ili23GeometryTags
from ili2py.interfaces.interlis.interlis_24 import Ili24GeometryTags
from ili2py.readers.xtf.backend import XtfBackend
from ili2py.readers.xtf.geometry import (
    Coord,
    MultiPolyline,
    MultiSurface,
    Polyline,
    Surface,
)
from ili2py.readers.xtf.xsdata_backend import (
    CompactGeometryBuilder,
    GeometryReader,
    GeometryText,
    GeometryWriter,
    XsdataBackend,
)


@pytest.fixture
def ili23_reader() -> GeometryReader:
    return GeometryReader(Ili23GeometryTags())


@pytest.fixture
def ili24_reader() -> GeometryReader:
    return GeometryReader(Ili24GeometryTags())


class TestXsdataBackend:
    def test_is_a_backend(self):
        assert isinstance(XsdataBackend(), XtfBackend)

    def test_geometry_tags_of_a_2_3_transfer(self):
        assert isinstance(XsdataBackend.geometry_tags(TRANSFER), Ili23GeometryTags)

    def test_geometry_tags_of_a_2_4_transfer(self):
        # the rendered Transfer of a 2.4 library carries the namespace of INTERLIS in its Meta
        class Transfer:
            class Meta:
                namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

        assert isinstance(XsdataBackend.geometry_tags(Transfer), Ili24GeometryTags)

    def test_geometry_tags_of_an_unknown_transfer_fail(self):
        # without the namespace of a transfer version there is no guess
        class Transfer:
            pass

        with pytest.raises(ValueError, match="no transfer of INTERLIS 2.3 or 2.4"):
            XsdataBackend.geometry_tags(Transfer)

    def test_library_name(self):
        # the rendered Transfer is in `<library>.xtf_opening`
        class Transfer:
            pass

        Transfer.__module__ = "oereb.xtf_opening"
        assert XsdataBackend.library_name(Transfer) == "oereb"


class TestGeometryReader:
    def test_coord(self, ili23_reader):
        element = etree.fromstring(
            b'<COORD xmlns="http://www.interlis.ch/INTERLIS2.3">'
            b"<C1>2600000.123</C1><C2>1200000.456</C2>"
            b"</COORD>"
        )
        assert ili23_reader.geometry(element) == Coord((2600000.123, 1200000.456))

    def test_polyline_of_straights(self, ili23_reader):
        element = etree.fromstring(
            b'<POLYLINE xmlns="http://www.interlis.ch/INTERLIS2.3">'
            b"<COORD><C1>0</C1><C2>0</C2></COORD>"
            b"<COORD><C1>1</C1><C2>1</C2></COORD>"
            b"</POLYLINE>"
        )
        # the vertices are flat, two axes each
        assert ili23_reader.geometry(element) == Polyline(
            array("d", [0.0, 0.0, 1.0, 1.0]), 2, {}
        )

    def test_polyline_with_arc(self, ili23_reader):
        element = etree.fromstring(
            b'<POLYLINE xmlns="http://www.interlis.ch/INTERLIS2.3">'
            b"<COORD><C1>0</C1><C2>0</C2></COORD>"
            b"<ARC><C1>2</C1><C2>0</C2><A1>1</A1><A2>1</A2></ARC>"
            b"</POLYLINE>"
        )
        polyline = ili23_reader.geometry(element)
        # the end point of the arc is a vertex, the intermediate point is kept by its index
        assert polyline == Polyline(array("d", [0.0, 0.0, 2.0, 0.0]), 2, {1: (1.0, 1.0)})

    def test_empty_polyline(self, ili23_reader):
        element = etree.fromstring(b'<POLYLINE xmlns="http://www.interlis.ch/INTERLIS2.3"/>')
        assert len(ili23_reader.geometry(element)) == 0

    def test_surface_with_exterior_and_interior(self, ili24_reader):
        element = etree.fromstring(
            b'<surface xmlns="http://www.interlis.ch/geometry/1.0">'
            b"<exterior><polyline>"
            b"<coord><c1>0</c1><c2>0</c2></coord><coord><c1>9</c1><c2>0</c2></coord>"
            b"</polyline></exterior>"
            b"<interior><polyline>"
            b"<coord><c1>1</c1><c2>1</c2></coord><coord><c1>2</c1><c2>1</c2></coord>"
            b"</polyline></interior>"
            b"</surface>"
        )
        # the exterior is the first boundary
        assert ili24_reader.geometry(element) == Surface(
            [
                Polyline(array("d", [0.0, 0.0, 9.0, 0.0]), 2, {}),
                Polyline(array("d", [1.0, 1.0, 2.0, 1.0]), 2, {}),
            ]
        )

    def test_unknown_element_fails(self, ili24_reader):
        element = etree.fromstring(b'<point xmlns="http://www.interlis.ch/geometry/1.0"/>')
        with pytest.raises(ValueError, match="unknown geometry element"):
            ili24_reader.geometry(element)


class TestCompactGeometryBuilder:
    def test_the_parts_carry_the_spec_as_well(self, integer_east_spec):
        builder = CompactGeometryBuilder(Ili24GeometryTags())
        boundary = Polyline(array("d", [1.0, 0.5, 2.0, 0.5, 1.0, 0.5]), 2, {})
        multi_surface = builder.typed(MultiSurface([Surface([boundary])]), integer_east_spec)
        # not only the geometry of the field, a boundary on its own knows its axes too, so it
        # answers with the int axis as the rendered dataclasses do
        surface = multi_surface.surfaces[0]
        assert surface.spec == integer_east_spec
        assert surface.boundaries[0].spec == integer_east_spec
        assert surface.boundaries[0].vertex(0) == (1, 0.5)
        assert type(surface.boundaries[0].vertex(0)[0]) is int
        # the values are the same as before
        assert multi_surface == MultiSurface([Surface([boundary])])

    def test_a_typed_type_is_created_once(self, integer_east_spec):
        builder = CompactGeometryBuilder(Ili24GeometryTags())
        first = builder.typed(Coord((1.0, 2.0)), integer_east_spec)
        second = builder.typed(Coord((3.0, 4.0)), integer_east_spec)
        # a type per geometry and spec, not one per geometry read
        assert type(first) is type(second)


class TestGeometryWriter:
    @pytest.mark.parametrize(
        "value, text",
        [
            (1.0, "1.0"),
            (2600000.123, "2600000.123"),
            # exponents, nan and inf are written as xsdata writes them
            (1e-07, "1E-07"),
            (1e20, "1E20"),
            (float("nan"), "NaN"),
            (float("inf"), "INF"),
            (float("-inf"), "-INF"),
        ],
    )
    def test_format_float(self, value, text):
        assert GeometryWriter.format_float(value) == text


class TestGeometryText:
    def test_polyline_with_arc_in_2_3(self):
        text = GeometryText(GeometryWriter(Ili23GeometryTags()), None, 2, "  ")
        polyline = Polyline(array("d", [0.0, 0.0, 2.0, 0.0]), 2, {1: (1.0, 1.0)})
        # indented at depth 2 as the xsdata writer would do it, without namespace prefix
        assert text.text(polyline) == (
            "\n    <POLYLINE>"
            "\n      <COORD>"
            "\n        <C1>0.0</C1>"
            "\n        <C2>0.0</C2>"
            "\n      </COORD>"
            "\n      <ARC>"
            "\n        <C1>2.0</C1>"
            "\n        <C2>0.0</C2>"
            "\n        <A1>1.0</A1>"
            "\n        <A2>1.0</A2>"
            "\n      </ARC>"
            "\n    </POLYLINE>"
        )

    def test_integer_axis_in_2_4(self, integer_east_spec):
        text = GeometryText(GeometryWriter(Ili24GeometryTags()), "geom", 1, "  ")
        coord = Coord.with_spec(integer_east_spec)((2600000.0, 1e-07))
        # the integer axis is written without decimals, with the prefix of the geometry
        assert text.text(coord) == (
            "\n  <geom:coord>"
            "\n    <geom:c1>2600000</geom:c1>"
            "\n    <geom:c2>1E-07</geom:c2>"
            "\n  </geom:coord>"
        )

    def test_empty_multipolyline(self):
        text = GeometryText(GeometryWriter(Ili24GeometryTags()), "geom", 1, "  ")
        assert text.text(MultiPolyline([])) == "\n  <geom:multipolyline/>"

    def test_multi_geometry_in_2_3_fails(self):
        # INTERLIS 2.3 has no MULTI geometries, there is nothing to write them as
        text = GeometryText(GeometryWriter(Ili23GeometryTags()), None, 1, "  ")
        with pytest.raises(TypeError, match="no multi geometries"):
            text.text(MultiPolyline([]))
