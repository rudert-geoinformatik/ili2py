import pytest

from ili2py.writers.py.python_structure import Base


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
