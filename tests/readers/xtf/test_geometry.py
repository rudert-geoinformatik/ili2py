import pickle
from array import array

import pytest

from ili2py.readers.xtf.access import (
    CoordAccess,
    MultiPolylineAccess,
    MultiSurfaceAccess,
    PolylineAccess,
    SurfaceAccess,
)
from ili2py.readers.xtf.geometry import (
    Coord,
    CoordSpec,
    MultiPolyline,
    MultiSurface,
    Polyline,
    Surface,
)


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


class TestCoord:
    def test_coordinates_without_spec_are_floats(self):
        # without a spec nobody knows better, the values stay as they were read
        assert Coord((2600000.0, 1200000.0)).coordinates == (2600000.0, 1200000.0)

    def test_coordinates_come_in_the_types_of_the_axes(self, integer_east_spec):
        # the compact geometry stores floats, the rendered dataclasses hold the first axis as
        # int, so the access has to answer with an int as well
        coord = Coord.with_spec(integer_east_spec)((2600000.0, 1.5))
        assert coord.coordinates == (2600000, 1.5)
        assert [type(value) for value in coord.coordinates] == [int, float]
        # what is stored does not change, the writer relies on it
        assert coord.values_ == (2600000.0, 1.5)


class TestPolyline:
    def test_vertices(self, polyline_with_arc):
        assert len(polyline_with_arc) == 3
        assert polyline_with_arc.vertex(0) == (0.0, 0.0)
        assert polyline_with_arc.vertex(2) == (2.0, 0.0)
        # the arc is kept apart from the vertices, by the index of its end point
        assert polyline_with_arc.arcs == {2: (2.5, 1.5)}

    def test_empty_polyline_has_no_vertices(self):
        assert len(Polyline(array("d"), 0, {})) == 0
        assert list(Polyline(array("d"), 0, {})) == []

    def test_iterating_gives_the_vertices(self, polyline_with_arc):
        # one tuple of axis values per vertex, the arc point is not one of them
        assert list(polyline_with_arc) == [(0.0, 0.0), (1.0, 1.0), (2.0, 0.0)]

    def test_negative_index_counts_from_the_end(self, polyline_with_arc):
        # as in a list, the rendered dataclasses hold their vertices in one
        assert polyline_with_arc.vertex(-1) == (2.0, 0.0)
        assert polyline_with_arc.vertex(-3) == (0.0, 0.0)

    @pytest.mark.parametrize("index", [3, -4])
    def test_vertex_out_of_range_fails(self, polyline_with_arc, index):
        # a slice would answer with an empty tuple, a missing vertex has to be loud
        with pytest.raises(IndexError, match="out of 3"):
            polyline_with_arc.vertex(index)
        with pytest.raises(IndexError, match="out of 3"):
            polyline_with_arc.arc(index)

    def test_arc_of_a_vertex(self, polyline_with_arc):
        # the vertex 2 ends the arc, the vertices before end a straight
        assert polyline_with_arc.arc(2) == (2.5, 1.5)
        assert polyline_with_arc.arc(-1) == (2.5, 1.5)
        assert polyline_with_arc.arc(1) is None
        assert polyline_with_arc.arc(0) is None

    def test_vertices_come_in_the_types_of_the_axes(self, integer_east_spec):
        polyline = Polyline.with_spec(integer_east_spec)(array("d", [1.0, 0.5, 2.0, 0.25]), 2, {})
        # the first axis is an int, by index and by iterating
        assert polyline.vertex(0) == (1, 0.5)
        assert [type(value) for value in polyline.vertex(0)] == [int, float]
        assert list(polyline) == [(1, 0.5), (2, 0.25)]
        assert [type(value) for value in list(polyline)[1]] == [int, float]


class TestSurface:
    def test_boundaries(self, polyline_with_arc):
        surface = Surface([polyline_with_arc])
        assert surface.boundaries == [polyline_with_arc]
        assert surface == Surface([polyline_with_arc])


class TestAccess:
    def test_coord(self):
        assert isinstance(Coord((1.0, 2.0)), CoordAccess)

    def test_polyline(self, polyline_with_arc):
        assert isinstance(polyline_with_arc, PolylineAccess)

    def test_surface(self, polyline_with_arc):
        assert isinstance(Surface([polyline_with_arc]), SurfaceAccess)

    def test_multi_polyline(self, polyline_with_arc):
        assert isinstance(MultiPolyline([polyline_with_arc]), MultiPolylineAccess)

    def test_multi_surface(self, polyline_with_arc):
        assert isinstance(MultiSurface([Surface([polyline_with_arc])]), MultiSurfaceAccess)

    def test_a_coord_is_no_polyline(self):
        # the protocols tell the geometries apart, tools can ask which one they have
        assert not isinstance(Coord((1.0, 2.0)), PolylineAccess)
        assert not isinstance(Coord((1.0, 2.0)), SurfaceAccess)
