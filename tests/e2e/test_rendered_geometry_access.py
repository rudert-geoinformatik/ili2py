"""
The geometry access of the rendered classes (`ili2py.readers.xtf.access`), built by hand
without an XTF. That the access answers the same as the compact geometry for real data is in
`test_rendered_xtf.py`.
"""

import importlib
from pathlib import Path

import pytest

from ili2py.readers.xtf.access import (
    CoordAccess,
    MultiPolylineAccess,
    MultiSurfaceAccess,
    PolylineAccess,
    SurfaceAccess,
)

from .helpers import generate_library, imported_library


@pytest.fixture(scope="module")
def oereb(resource_path_root, tmp_path_factory):
    """The rendered library of the OeREB transfer model, INTERLIS 2.3."""
    imd = Path(resource_path_root) / "models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd"
    library = generate_library(imd, tmp_path_factory.mktemp("oereb"))
    with imported_library(library):
        yield importlib.import_module(f"{library.name}")


@pytest.fixture(scope="module")
def lv95_23(oereb):
    """The LV95 geometry of INTERLIS 2.3 (`GeometryCHLV95_V1`)."""
    return importlib.import_module(f"{oereb.__name__}.GeometryCHLV95_V1")


@pytest.fixture(scope="module")
def lv95_24(resource_path_root, tmp_path_factory):
    """The LV95 geometry of INTERLIS 2.4 (`GeometryCHLV95_V2`), it has the MULTI types."""
    imd = Path(resource_path_root) / "models/DMAVTYM_Alles_V1_1/DMAVTYM_Alles_V1_1.imd"
    library = generate_library(imd, tmp_path_factory.mktemp("dmav"))
    with imported_library(library):
        yield importlib.import_module(f"{library.name}.GeometryCHLV95_V2")


class TestRenderedCoordAccess:
    def test_coord(self, lv95_23):
        coord = lv95_23.Coord2(coord=lv95_23.Coord2Type(c1=2600000.0, c2=1200000.0))
        assert isinstance(coord, CoordAccess)
        assert coord.coordinates == (2600000.0, 1200000.0)

    def test_integer_axes_stay_integer(self, oereb):
        # INTERLIS.LineCoord has integer axes, the compact geometry answers the same with its
        # spec (see tests/readers/xtf/test_geometry.py)
        interlis = importlib.import_module(f"{oereb.__name__}.INTERLIS")
        coord = interlis.LineCoord(coord=interlis.LineCoordType(c1=1, c2=2))
        assert coord.coordinates == (1, 2)
        assert [type(value) for value in coord.coordinates] == [int, int]

    def test_empty_coord(self, lv95_23):
        # the compact geometry would be None, the rendered class can exist without values
        assert lv95_23.Coord2().coordinates == ()


class TestRenderedPolylineAccess:
    def test_line_with_arc(self, lv95_23):
        # a straight from (0, 0) to (2, 0), then an arc through (3, 1) to (2, 2)
        line = lv95_23.Line(
            polyline=lv95_23.Line.Segment(
                vertices=[
                    lv95_23.Coord2Type(c1=0.0, c2=0.0),
                    lv95_23.Coord2Type(c1=2.0, c2=0.0),
                    lv95_23.Coord2ARCType(c1=2.0, c2=2.0, a1=3.0, a2=1.0),
                ]
            )
        )
        assert isinstance(line, PolylineAccess)
        assert len(line) == 3
        assert list(line) == [(0.0, 0.0), (2.0, 0.0), (2.0, 2.0)]
        assert line.vertex(-1) == (2.0, 2.0)
        # the arc point belongs to the vertex ending the arc, the straights have none
        assert line.arc(2) == (3.0, 1.0)
        assert line.arc(1) is None

    def test_arc_with_radius(self, lv95_23):
        segment = lv95_23.Line.Segment(
            vertices=[
                lv95_23.Coord2Type(c1=0.0, c2=0.0),
                lv95_23.Coord2ARCType(c1=2.0, c2=0.0, a1=1.0, a2=1.0, r=1.0),
            ]
        )
        # the radius comes after the arc point, as the compact geometry keeps it
        assert segment.arc(1) == (1.0, 1.0, 1.0)

    def test_empty_line(self, lv95_23):
        line = lv95_23.Line()
        assert len(line) == 0
        assert list(line) == []
        # a vertex which is not there is loud, as in the compact geometry
        with pytest.raises(IndexError):
            line.vertex(0)
        with pytest.raises(IndexError):
            line.arc(0)


class TestRenderedSurfaceAccess:
    def test_surface_with_hole(self, lv95_23):
        Boundary = lv95_23.Surface.SurfaceBOUNDARY
        Polyline = Boundary.SurfacePOLYLINE
        square = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 0.0)]
        hole = [(1.0, 1.0), (2.0, 1.0), (2.0, 2.0), (1.0, 1.0)]
        surface = lv95_23.Surface(
            surface=Boundary(
                boundaries=[
                    Polyline(
                        polyline=Polyline.Segment(
                            vertices=[lv95_23.Coord2Type(c1=x, c2=y) for x, y in square]
                        )
                    ),
                    Polyline(
                        polyline=Polyline.Segment(
                            vertices=[lv95_23.Coord2Type(c1=x, c2=y) for x, y in hole]
                        )
                    ),
                ]
            )
        )
        assert isinstance(surface, SurfaceAccess)
        # the exterior comes first, then the hole
        exterior, interior = surface.boundaries
        assert list(exterior) == square
        assert list(interior) == hole
        assert isinstance(exterior, PolylineAccess)

    def test_empty_surface(self, lv95_23):
        assert lv95_23.Surface().boundaries == []


class TestRenderedMultiAccess:
    def test_multi_line(self, lv95_24):
        Polylines = lv95_24.MultiLine.Polylines
        multi_line = lv95_24.MultiLine(
            multipolyline=Polylines(
                parts=[
                    Polylines.Segment(
                        vertices=[
                            lv95_24.Coord2Type(c1=0.0, c2=0.0),
                            lv95_24.Coord2Type(c1=1.0, c2=1.0),
                        ]
                    ),
                    Polylines.Segment(
                        vertices=[
                            lv95_24.Coord2Type(c1=5.0, c2=5.0),
                            lv95_24.Coord2Type(c1=6.0, c2=5.0),
                        ]
                    ),
                ]
            )
        )
        assert isinstance(multi_line, MultiPolylineAccess)
        # the parts are polylines on their own
        first, second = multi_line.polylines
        assert isinstance(first, PolylineAccess)
        assert list(first) == [(0.0, 0.0), (1.0, 1.0)]
        assert second.vertex(-1) == (6.0, 5.0)

    def test_multi_surface(self, lv95_24):
        Surfaces = lv95_24.MultiSurface.Surfaces
        Boundary = Surfaces.MultiSurfaceBoundary
        Polyline = Boundary.MultiSurfacePolyline
        triangle = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (0.0, 0.0)]
        multi_surface = lv95_24.MultiSurface(
            multisurface=Surfaces(
                parts=[
                    Boundary(
                        boundaries=[
                            Polyline(
                                polyline=Polyline.Segment(
                                    vertices=[lv95_24.Coord2Type(c1=x, c2=y) for x, y in triangle]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        assert isinstance(multi_surface, MultiSurfaceAccess)
        # each surface of the multi surface answers as a surface
        (surface,) = multi_surface.surfaces
        assert isinstance(surface, SurfaceAccess)
        assert list(surface.boundaries[0]) == triangle

    def test_empty_multi_geometries(self, lv95_24):
        assert lv95_24.MultiLine().polylines == []
        assert lv95_24.MultiSurface().surfaces == []
