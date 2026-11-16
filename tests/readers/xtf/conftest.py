import pytest

from ili2py.readers.xtf.geometry import CoordSpec


@pytest.fixture
def integer_east_spec() -> CoordSpec:
    # a coord type with an integer first axis, e.g. COORD 0 .. 10 [m], 0.000 .. 10.000 [m]
    return CoordSpec(
        tid="Model.Coord",
        axes=("C1", "C2"),
        types=(int, float),
        precisions=(None, 3),
    )
