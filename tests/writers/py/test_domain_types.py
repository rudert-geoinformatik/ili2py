import os

import pytest

from ili2py.mappers.helpers import Index
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.py.python_structure import Library
from ili2py.writers.py.render import create_python_classes


@pytest.fixture(scope="module")
def generated(resource_path_root, tmp_path_factory):
    reader = Imd16Reader()
    metamodel = reader.read(
        os.path.join(resource_path_root, "models/DMAVTYM_Tous_V1_1/DMAVTYM_Tous_V1_1.imd")
    )
    index = Index(metamodel.datasection)
    library = Library.from_imd(metamodel.datasection.ModelData, index, "tous")
    output_path = tmp_path_factory.mktemp("ili2py")
    create_python_classes(library, index, str(output_path), beautify=False)
    return library, output_path / "tous"


def test_boolean_domain(generated):
    library, output_path = generated
    package = next(item for item in library.packages if item.name == "DMAVTYM_Qualitaet_V1_0")
    definition = next(
        item for item in package.type_definitions if item["name"] == "Zuverlaessigkeit"
    )
    # bool can not be subclassed, the domain class has no base
    assert definition["kind"] == "bool"
    assert definition["reference"] is None
    content = (output_path / "DMAVTYM_Qualitaet_V1_0" / "__init__.py").read_text(
        encoding="utf-8"
    )
    assert "class Zuverlaessigkeit:" in content
    compile(content, "DMAVTYM_Qualitaet_V1_0/__init__.py", "exec")


def test_coord_type_kind(generated):
    _, output_path = generated
    content = (output_path / "GeometryCHLV95_V2" / "__init__.py").read_text(encoding="utf-8")
    coord_metadata = content.split('"oid": "GeometryCHLV95_V2.Coord2",')[1].split("}")[0]
    assert '"kind": "CoordType"' in coord_metadata
