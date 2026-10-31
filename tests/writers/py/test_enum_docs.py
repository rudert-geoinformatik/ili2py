import ast
import os

import pytest

from ili2py.mappers.helpers import Index
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.py.python_structure import Enumeration, Library
from ili2py.writers.py.render import create_python_classes


def generate(resource_path_root, tmp_path_factory, imd_name: str):
    reader = Imd16Reader()
    metamodel = reader.read(
        os.path.join(resource_path_root, f"models/EnumDocs_V1/{imd_name}")
    )
    index = Index(metamodel.datasection)
    library = Library.from_imd(metamodel.datasection.ModelData, index, "enumdocs")
    output_path = tmp_path_factory.mktemp("ili2py")
    create_python_classes(library, index, str(output_path), beautify=False)
    return library, output_path / "enumdocs" / "EnumDocs_V1"


@pytest.fixture(scope="module")
def generated(resource_path_root, tmp_path_factory):
    # ili2c does not write the documentation of enumeration elements, see Readme.md of the model
    return generate(resource_path_root, tmp_path_factory, "EnumDocs_V1_EnumNodeDoc.imd")


def find_enumeration(library: Library, name: str) -> Enumeration:
    package = next(item for item in library.packages if item.name == "EnumDocs_V1")
    return next(item for item in package.enumerations if item.name == name)


def find_class(tree: ast.Module, name: str) -> ast.ClassDef:
    return next(
        node for node in ast.walk(tree) if isinstance(node, ast.ClassDef) and node.name == name
    )


def member_docs(class_node: ast.ClassDef) -> dict[str, str]:
    # attribute docstrings are the string expressions directly following an assignment
    docs = {}
    for previous, current in zip(class_node.body, class_node.body[1:]):
        if (
            isinstance(previous, ast.Assign)
            and isinstance(current, ast.Expr)
            and isinstance(current.value, ast.Constant)
        ):
            docs[previous.targets[0].id] = current.value.value
    return docs


def test_value_docs(generated):
    library, _ = generated
    assert find_enumeration(library, "Zustand").value_docs == {
        "aktiv": ["In Betrieb"],
        "inaktiv": ["Ausser Betrieb"],
    }
    # enum tree (ALL OF), only the documentation of the last segment is taken
    assert find_enumeration(library, "Kategorie").value_docs == {
        "rot": ["Signalfarbe"],
        "gruen.hell": ["Helles Gruen"],
    }


def test_rendered_enumeration(generated):
    _, output_path = generated
    content = (output_path / "__init__.py").read_text(encoding="utf-8")
    tree = ast.parse(content)
    zustand = find_class(tree, "Zustand")
    docstring = ast.get_docstring(zustand)
    assert "Attributes:\n    AKTIV: In Betrieb\n    INAKTIV: Ausser Betrieb" in docstring
    assert member_docs(zustand) == {"AKTIV": "In Betrieb", "INAKTIV": "Ausser Betrieb"}
    assert member_docs(find_class(tree, "Kategorie")) == {
        "ROT": "Signalfarbe",
        "GRUEN_HELL": "Helles Gruen",
    }


def test_rendered_class(generated):
    _, output_path = generated
    content = (output_path / "Objekte.py").read_text(encoding="utf-8")
    tree = ast.parse(content)
    objekt = find_class(tree, "Objekt")
    # docstring has to be the first statement, before class Meta
    assert ast.get_docstring(objekt).startswith("Ein Objekt\n\nArgs:\n    Farbe: Farbe des Objekts")
    assert ast.get_docstring(find_class(objekt, "ObjektArtEnum")) == "Attributes:\n    A: Erste Art"
    # class without own documentation still documents its attributes
    assert ast.get_docstring(find_class(tree, "OhneDoku")) == (
        "Args:\n    Bemerkung: Bemerkung zum Objekt"
    )


def test_without_value_docs(resource_path_root, tmp_path_factory):
    library, output_path = generate(resource_path_root, tmp_path_factory, "EnumDocs_V1.imd")
    assert find_enumeration(library, "Zustand").value_docs == {}
    tree = ast.parse((output_path / "__init__.py").read_text(encoding="utf-8"))
    zustand = find_class(tree, "Zustand")
    assert ast.get_docstring(zustand) is None
    assert member_docs(zustand) == {}
