import pytest

from ili2py.interfaces.interlis import GeometryTags
from ili2py.interfaces.interlis.interlis_23 import TRANSFER, Ili23GeometryTags
from ili2py.interfaces.interlis.interlis_24 import Ili24GeometryTags


@pytest.fixture
def ili23_tags() -> Ili23GeometryTags:
    return Ili23GeometryTags()


@pytest.fixture
def ili24_tags() -> Ili24GeometryTags:
    return Ili24GeometryTags()


@pytest.fixture
def ili24_transfer_class() -> type:
    # the rendered Transfer of a 2.4 library carries the namespace of INTERLIS in its Meta
    class Transfer:
        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    return Transfer


class TestIli23GeometryTags:
    def test_element_names_are_in_the_one_namespace(self, ili23_tags):
        # 2.3 knows a single namespace for the transfer and the geometry
        assert ili23_tags.coord == "{http://www.interlis.ch/INTERLIS2.3}COORD"
        assert ili23_tags.arc == "{http://www.interlis.ch/INTERLIS2.3}ARC"
        assert ili23_tags.polyline == "{http://www.interlis.ch/INTERLIS2.3}POLYLINE"
        assert ili23_tags.surface == "{http://www.interlis.ch/INTERLIS2.3}SURFACE"
        assert ili23_tags.axes == (
            "{http://www.interlis.ch/INTERLIS2.3}C1",
            "{http://www.interlis.ch/INTERLIS2.3}C2",
            "{http://www.interlis.ch/INTERLIS2.3}C3",
        )
        assert ili23_tags.arc_points == (
            "{http://www.interlis.ch/INTERLIS2.3}A1",
            "{http://www.interlis.ch/INTERLIS2.3}A2",
            "{http://www.interlis.ch/INTERLIS2.3}R",
        )

    def test_there_are_no_multi_geometries(self, ili23_tags):
        assert ili23_tags.multipolyline is None
        assert ili23_tags.multisurface is None
        # so they are not part of the geometries either
        assert ili23_tags.geometries == frozenset(
            {
                "{http://www.interlis.ch/INTERLIS2.3}COORD",
                "{http://www.interlis.ch/INTERLIS2.3}POLYLINE",
                "{http://www.interlis.ch/INTERLIS2.3}SURFACE",
            }
        )

    @pytest.mark.parametrize("index", [0, 1, 5])
    def test_every_boundary_is_a_boundary(self, ili23_tags, index):
        # 2.3 does not tell the exterior from the interiors
        assert ili23_tags.boundary(index) == "{http://www.interlis.ch/INTERLIS2.3}BOUNDARY"

    def test_reads_the_transfer_of_its_version_only(self, ili24_transfer_class):
        assert Ili23GeometryTags.reads(TRANSFER)
        assert not Ili23GeometryTags.reads(ili24_transfer_class)


class TestIli24GeometryTags:
    def test_element_names_are_in_the_geometry_namespace(self, ili24_tags):
        # the geometry has its own namespace, apart from the one of INTERLIS
        assert ili24_tags.namespace == "http://www.interlis.ch/geometry/1.0"
        assert ili24_tags.coord == "{http://www.interlis.ch/geometry/1.0}coord"
        assert ili24_tags.polyline == "{http://www.interlis.ch/geometry/1.0}polyline"
        assert ili24_tags.axes == (
            "{http://www.interlis.ch/geometry/1.0}c1",
            "{http://www.interlis.ch/geometry/1.0}c2",
            "{http://www.interlis.ch/geometry/1.0}c3",
        )

    def test_multi_geometries_are_geometries(self, ili24_tags):
        assert ili24_tags.multipolyline == "{http://www.interlis.ch/geometry/1.0}multipolyline"
        assert ili24_tags.multisurface == "{http://www.interlis.ch/geometry/1.0}multisurface"
        assert ili24_tags.multipolyline in ili24_tags.geometries
        assert ili24_tags.multisurface in ili24_tags.geometries

    @pytest.mark.parametrize(
        "index, boundary",
        [
            # the first boundary is the exterior, all following ones are interiors
            (0, "{http://www.interlis.ch/geometry/1.0}exterior"),
            (1, "{http://www.interlis.ch/geometry/1.0}interior"),
            (5, "{http://www.interlis.ch/geometry/1.0}interior"),
        ],
    )
    def test_boundary(self, ili24_tags, index, boundary):
        assert ili24_tags.boundary(index) == boundary

    def test_reads_the_transfer_of_its_version_only(self, ili24_transfer_class):
        assert Ili24GeometryTags.reads(ili24_transfer_class)
        assert not Ili24GeometryTags.reads(TRANSFER)


class TestGeometryTags:
    @pytest.mark.parametrize(
        "tag, local_name",
        [
            ("{http://www.interlis.ch/geometry/1.0}coord", "coord"),
            ("COORD", "COORD"),
        ],
    )
    def test_local_name(self, tag, local_name):
        assert GeometryTags.local_name(tag) == local_name
