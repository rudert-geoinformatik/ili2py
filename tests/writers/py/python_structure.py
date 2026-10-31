import pytest

from ili2py.writers.py.python_structure import Attribute, Base, Class


@pytest.mark.parametrize(
    "oid, result",
    [
        (
            "LocalisationCH_V1.MultilingualText.LocalisedText.TYPE",
            "LocalisationCH_V1MultilingualTextLocalisedTextTYPE",
        ),
        (
            "LocalisationCH_V1.MultilingualText.LocalisedText",
            "LocalisationCH_V1MultilingualTextLocalisedText",
        ),
    ],
)
def test_base_pythonize_oid_global(oid, result):
    assert Base.pythonize_oid_global(oid) == result


def test_class_default_tag():
    # the tag of a class in the 2.3 transfer is its qualified name
    class_definition = Class(
        name="Objekt",
        identifier="RichtplanungErneuerbareEnergien_V1.Objekte.Objekt",
        doc=[],
        meta_attributes=[],
        translations={},
    )
    assert class_definition.tag == "RichtplanungErneuerbareEnergien_V1.Objekte.Objekt"


def test_class_explicit_tag():
    class_definition = Class(
        name="Objekt",
        identifier="RichtplanungErneuerbareEnergien_V1.Objekte.Objekt",
        doc=[],
        meta_attributes=[],
        translations={},
        tag="PlanDirecteurEnergiesRenouvelables_V1.Objets.Objet",
    )
    assert class_definition.tag == "PlanDirecteurEnergiesRenouvelables_V1.Objets.Objet"


def test_attribute_default_tag():
    # the tag of an attribute is its name
    attribute = Attribute(
        name="Objektart",
        identifier="RichtplanungErneuerbareEnergien_V1.Objekte.Objekt.Objektart",
        doc=[],
        meta_attributes=[],
        translations={},
        types=["str"],
    )
    assert attribute.tag == "Objektart"


def test_attribute_default_tag_structure():
    # the HOP attribute of a structure attribute is tagged with the qualified name of the
    # structure, see Attribute.handle_local_types
    attribute = Attribute(
        name="struct_content",
        identifier="ili2py.RichtplanungErneuerbareEnergien_V1.MultiPoint",
        doc=[],
        meta_attributes=[],
        translations={},
        types=["RichtplanungErneuerbareEnergien_V1MultiPoint"],
        type_restrictions={"type_related_type": True},
    )
    assert attribute.tag == "RichtplanungErneuerbareEnergien_V1.MultiPoint"
