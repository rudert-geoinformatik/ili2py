import os

import pytest

from ili2py.mappers.helpers import Index
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.py.python_structure import Library

ELEMENTS = "DMAV_Einzelobjekte_V1_1.Einzelobjekte"


@pytest.fixture(scope="module")
def attributes(resource_path_root):
    metamodel = Imd16Reader().read(
        os.path.join(resource_path_root, "models/DMAVTYM_Alles_V1_1/DMAVTYM_Alles_V1_1.imd")
    )
    index = Index(metamodel.datasection)
    library = Library.from_imd(metamodel.datasection.ModelData, index, "alles")
    return {
        attribute.identifier: attribute
        for package in library.packages
        for cls in classes(package)
        for attribute in cls.attributes
    }


def classes(package):
    # its own, and those of its topics
    yield from package.classes
    for module in package.modules:
        yield from module.classes


@pytest.mark.parametrize(
    ("attribute", "arcs"),
    [
        # a domain, GeometryCHLV95_V2.Line, POLYLINE WITH (STRAIGHTS, ARCS): no line_type
        (f"{ELEMENTS}.Linienelement.Geometrie", True),
        # its own SURFACE WITH (STRAIGHTS, ARCS)
        (f"{ELEMENTS}.Flaechenelement.Geometrie", True),
        (f"{ELEMENTS}.Punktelement.Geometrie", False),
    ],
)
def test_the_arcs_of_a_geometry(attributes, attribute, arcs):
    assert attributes[attribute].geometric_arcs is arcs
