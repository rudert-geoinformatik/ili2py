import os

import pytest

from ili2py.mappers.helpers import Index, TranslatedModel
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader


def read_index(resource_path_root, imd_path) -> Index:
    reader = Imd16Reader()
    metamodel = reader.read(os.path.join(resource_path_root, imd_path))
    return Index(metamodel.datasection)


def test_translated_models_single(resource_path_root):
    index = read_index(
        resource_path_root,
        "models/Richtplan_erneuerbare_Energien_V1_0/PlanDirecteurEnergiesRenouvelables_V1.imd",
    )
    assert index.translated_models == {
        "RichtplanungErneuerbareEnergien_V1": [
            TranslatedModel(
                name="PlanDirecteurEnergiesRenouvelables_V1",
                language="fr",
                original="RichtplanungErneuerbareEnergien_V1",
                original_language="de",
            )
        ]
    }
    # the translation of the model name is kept like the one of every other element
    assert index.model_translations["RichtplanungErneuerbareEnergien_V1"] == {
        "fr": "PlanDirecteurEnergiesRenouvelables_V1"
    }
    assert index.model_translations["RichtplanungErneuerbareEnergien_V1.Objekte"] == {
        "fr": "Objets"
    }
    assert index.model_translations[
        "RichtplanungErneuerbareEnergien_V1.Objektart.TOP.Ausgangslage"
    ] == {"fr": "Donnees_de_base"}


def test_translated_models_imported(resource_path_root):
    # DMAVTYM_Tous_V1_1 is a translation and imports translated models only, every one of
    # them has its own ModelTranslation basket
    index = read_index(resource_path_root, "models/DMAVTYM_Tous_V1_1/DMAVTYM_Tous_V1_1.imd")
    assert len(index.translated_models) == 20
    assert index.translated_models["DMAVTYM_Geometrie_V1_0"] == [
        TranslatedModel(
            name="DMAVTYM_Geometrie_FR_V1_0",
            language="fr",
            original="DMAVTYM_Geometrie_V1_0",
            original_language="de",
        )
    ]
    # DMAVTYM_Tous_V1_1.ili declares MODEL DMAVTYM_Tous_V1_1 (de) instead of (fr), the
    # index takes the language as it is
    assert index.translated_models["DMAVTYM_Alles_V1_1"] == [
        TranslatedModel(
            name="DMAVTYM_Tous_V1_1",
            language="de",
            original="DMAVTYM_Alles_V1_1",
            original_language="de",
        )
    ]
    # untranslated imports are not in there
    assert "INTERLIS" not in index.translated_models
    assert "GeometryCHLV95_V2" not in index.translated_models


def test_translated_models_none(resource_path_root):
    index = read_index(
        resource_path_root,
        "models/Richtplan_erneuerbare_Energien_V1_0/RichtplanungErneuerbareEnergien_V1.imd",
    )
    assert index.translated_models == {}
    assert index.model_translations == {}


@pytest.mark.parametrize(
    "name, original",
    [
        ("PlanDirecteurEnergiesRenouvelables_V1", "RichtplanungErneuerbareEnergien_V1"),
        ("RichtplanungErneuerbareEnergien_V1", None),
        ("Unknown", None),
    ],
)
def test_translated_model(resource_path_root, name, original):
    index = read_index(
        resource_path_root,
        "models/Richtplan_erneuerbare_Energien_V1_0/PlanDirecteurEnergiesRenouvelables_V1.imd",
    )
    translated = index.translated_model(name)
    assert (translated.original if translated else None) == original
