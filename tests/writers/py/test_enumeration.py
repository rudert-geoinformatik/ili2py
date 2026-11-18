import os

import pytest

from ili2py.mappers.helpers import Index
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.py.python_structure import Enumeration


@pytest.fixture(scope="module")
def sia405_wasser_index(resource_path_root) -> Index:
    metamodel = Imd16Reader().read(
        os.path.join(
            resource_path_root,
            "models/SIA405_Wasser_2015_2_d-20181005/SIA405_Wasser_2015_2_d-20181005.imd",
        )
    )
    return Index(metamodel.datasection)


class TestEnumTreeValueType:
    def test_the_domain_wins_over_the_type_of_an_attribute(self, sia405_wasser_index):
        # SIA405_Wasser has the domain `Status = ALL OF Statuswerte` and the attribute
        # `Leitung.Status`, whose type is an own ALL OF Statuswerte, so two candidates
        candidates = [
            enum_tree_value_type.tid
            for enum_tree_value_type in sia405_wasser_index.types_bucket["EnumTreeValueType"]
            if enum_tree_value_type.et.ref == "SIA405_WASSER_2015.SIA405_Wasser.Statuswerte"
        ]
        assert candidates == [
            "SIA405_WASSER_2015.SIA405_Wasser.Status",
            "SIA405_WASSER_2015.SIA405_Wasser.Leitung.Status.TYPE",
        ]
        # the enumeration and the attribute agree on the domain as identifier
        matched = Enumeration.enum_tree_value_type(
            "SIA405_WASSER_2015.SIA405_Wasser.Statuswerte", sia405_wasser_index
        )
        assert matched.tid == "SIA405_WASSER_2015.SIA405_Wasser.Status"

    def test_an_enumeration_not_used_as_tree_has_none(self, sia405_wasser_index):
        # no ALL OF refers to it, so the enumeration is rendered on its own tid
        assert (
            Enumeration.enum_tree_value_type("SIA405_WASSER_2015.Unknown", sia405_wasser_index)
            is None
        )
