import os

import pytest

from ili2py.mappers.helpers import Index
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.py.python_structure import Class, Library, Module, Package
from ili2py.writers.py.transfer_names import translate_transfer_names

TRANSLATED_IMD = (
    "models/Richtplan_erneuerbare_Energien_V1_0/PlanDirecteurEnergiesRenouvelables_V1.imd"
)
ORIGINAL_IMD = "models/Richtplan_erneuerbare_Energien_V1_0/RichtplanungErneuerbareEnergien_V1.imd"


def build_library(resource_path_root, imd_path) -> tuple[Library, Index]:
    reader = Imd16Reader()
    metamodel = reader.read(os.path.join(resource_path_root, imd_path))
    index = Index(metamodel.datasection)
    library = Library.from_imd(metamodel.datasection.ModelData, index, "test")
    return library, index


def find_package(library: Library, name: str) -> Package:
    return next(package for package in library.packages if package.name == name)


def find_module(package: Package, name: str) -> Module:
    return next(module for module in package.modules if module.name == name)


def find_class(module: Module, name: str) -> Class:
    return next(class_item for class_item in module.classes if class_item.name == name)


@pytest.fixture
def translated(resource_path_root) -> Library:
    library, index = build_library(resource_path_root, TRANSLATED_IMD)
    translate_transfer_names(library, index)
    return library


def test_module_and_class(translated):
    package = find_package(translated, "RichtplanungErneuerbareEnergien_V1")
    module = find_module(package, "Objekte")
    # python names and identifiers stay original
    assert module.name == "Objekte"
    assert module.identifier == "RichtplanungErneuerbareEnergien_V1.Objekte"
    assert module.tag == "PlanDirecteurEnergiesRenouvelables_V1.Objets"
    assert module.translations == {"de": "Objekte"}
    class_definition = find_class(module, "Objekt")
    assert class_definition.identifier == "RichtplanungErneuerbareEnergien_V1.Objekte.Objekt"
    assert class_definition.tag == "PlanDirecteurEnergiesRenouvelables_V1.Objets.Objet"
    assert class_definition.translations == {"de": "Objekt"}


def test_attribute_and_enumeration(translated):
    package = find_package(translated, "RichtplanungErneuerbareEnergien_V1")
    class_definition = find_class(find_module(package, "Objekte"), "Objekt")
    attribute = next(item for item in class_definition.attributes if item.name == "Objektart")
    assert attribute.tag == "TypeObjet"
    assert attribute.translations == {"de": "Objektart"}
    enumeration = next(item for item in package.enumerations if item.name == "Objektart")
    assert enumeration.values[0] == "Ausgangslage"
    assert enumeration.value_tags["Ausgangslage"] == "Donnees_de_base"
    assert enumeration.value_translations["Ausgangslage"] == {"de": "Ausgangslage"}
    assert (
        enumeration.value_tags["Richtplaninhalt.Festsetzung"]
        == "ContenuPlanDirecteur.Coordination_reglee"
    )


def test_choices(translated):
    choices = {choice.identifier: choice.tag for choice in translated.topic_choices}
    assert (
        choices["RichtplanungErneuerbareEnergien_V1.Objekte"]
        == "PlanDirecteurEnergiesRenouvelables_V1.Objets"
    )
    # imported untranslated models keep their tags
    assert choices["CoordSys.CoordsysTopic"] == "CoordSys.CoordsysTopic"
    package = find_package(translated, "RichtplanungErneuerbareEnergien_V1")
    basket_choices = {
        choice.identifier: choice.tag
        for choice in mandatory_basket(find_module(package, "Objekte")).choices
    }
    assert (
        basket_choices["RichtplanungErneuerbareEnergien_V1.Objekte.Flaeche"]
        == "PlanDirecteurEnergiesRenouvelables_V1.Objets.Surface"
    )


def mandatory_basket(module: Module):
    assert module.basket is not None
    return module.basket


def test_untranslated_unchanged(resource_path_root):
    library, index = build_library(resource_path_root, ORIGINAL_IMD)
    before = repr(library)
    translate_transfer_names(library, index)
    assert repr(library) == before
