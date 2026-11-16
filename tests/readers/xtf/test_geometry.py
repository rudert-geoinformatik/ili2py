import pickle
from array import array

import pytest

from ili2py.readers.xtf.geometry import Coord, CoordSpec, Polyline, Surface


@pytest.fixture
def lv95_spec() -> CoordSpec:
    return CoordSpec(
        tid="GeometryCHLV95_V1.Coord2",
        axes=("C1", "C2"),
        types=(float, float),
        precisions=(3, 3),
    )


@pytest.fixture
def polyline_with_arc() -> Polyline:
    # three vertices, the last one is the end point of an arc through (2.5, 1.5)
    return Polyline(array("d", [0.0, 0.0, 1.0, 1.0, 2.0, 0.0]), 2, {2: (2.5, 1.5)})


class TestGeometry:
    def test_same_values_are_equal(self):
        assert Coord((2600000.0, 1200000.0)) == Coord((2600000.0, 1200000.0))
        assert Coord((2600000.0, 1200000.0)) != Coord((2600000.0, 1200000.1))

    def test_repr_names_the_values(self):
        assert repr(Coord((1.0, 2.0))) == "Coord(values_=(1.0, 2.0))"

    def test_survives_pickling(self, polyline_with_arc):
        assert pickle.loads(pickle.dumps(polyline_with_arc)) == polyline_with_arc

    def test_with_spec_carries_the_spec_of_the_axes(self, lv95_spec):
        lv95_coord = Coord.with_spec(lv95_spec)
        # the subclass stays a Coord with the same name, only the spec is added
        assert issubclass(lv95_coord, Coord)
        assert lv95_coord.__name__ == "Coord"
        assert lv95_coord.spec == lv95_spec
        assert Coord.spec is None

    def test_with_spec_does_not_change_equality(self, lv95_spec):
        # the spec is a property of the type, the geometry is its values
        lv95_coord = Coord.with_spec(lv95_spec)
        assert lv95_coord((1.0, 2.0)) == Coord((1.0, 2.0))
        assert lv95_coord((1.0, 2.0)).fields() == ("values_",)


class TestPolyline:
    def test_vertices(self, polyline_with_arc):
        assert len(polyline_with_arc) == 3
        assert polyline_with_arc.vertex(0) == (0.0, 0.0)
        assert polyline_with_arc.vertex(2) == (2.0, 0.0)
        # the arc is kept apart from the vertices, by the index of its end point
        assert polyline_with_arc.arcs == {2: (2.5, 1.5)}

    def test_empty_polyline_has_no_vertices(self):
        assert len(Polyline(array("d"), 0, {})) == 0


class TestSurface:
    def test_boundaries(self, polyline_with_arc):
        surface = Surface([polyline_with_arc])
        assert surface.boundaries == [polyline_with_arc]
        assert surface == Surface([polyline_with_arc])
