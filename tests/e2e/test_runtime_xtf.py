"""
The runtime classes (readers/xtf/runtime.py) have a structure of their own, but they have to
read and write the same XTF as the rendered classes (writers/py/render.py): the XTF of a model
is read with both and written again, the results have to be equal.
"""

import io
import pickle
from pathlib import Path

import pytest
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from ili2py.readers.xtf.runtime import RuntimeLibrary, slug

from .helpers import (
    find_xtf,
    generate_library,
    imported_library,
    read_xtf,
    registered_types,
    xtf_header,
)

PARSER_CONFIG = ParserConfig(
    fail_on_unknown_properties=True,
    fail_on_unknown_attributes=True,
    fail_on_converter_warnings=True,
)
SERIALIZER_CONFIG = SerializerConfig(indent="  ", xml_declaration=True, encoding="UTF-8")

IMD_PATHS = [
    # 2.3
    "models/SZ_Lebensraum_Fisch_V2/SZ_Lebensraum_Fisch_V2.imd",
    "models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd",
    "models/Nutzungsplanung_V1_2/Nutzungsplanung_V1_2.imd",
    "models/Richtplan_erneuerbare_Energien_V1_0/PlanDirecteurEnergiesRenouvelables_V1.imd",
    "models/Leitungskataster/SIA405_LKMap_2015_2_d-20180427.imd",
    # 2.4
    "models/SZ_Waldreservate_V3/SZ_Waldreservate_V3.imd",
    "models/DMAVTYM_Alles_V1_1/DMAVTYM_Alles_V1_1.imd",
    "models/IncrementalTransfer/DataTest1.imd",
    "models/Hazard_Mapping_V1_3/Hazard_Mapping_V1_3.imd",
]


@pytest.mark.parametrize("imd_path", IMD_PATHS)
def test_runtime_writes_what_rendered_writes(resource_path_root, tmp_path, imd_path):
    imd = Path(resource_path_root) / imd_path
    rendered = generate_library(imd, tmp_path / "generated")
    xtf = find_xtf(rendered, imd.parent, tmp_path / "data")
    ns_map: dict[str | None, str] = {
        (prefix or None): uri for prefix, uri in xtf_header(xtf).namespaces.items()
    }
    serializer = XmlSerializer(config=SERIALIZER_CONFIG)
    with imported_library(rendered) as xtf_opening, registered_types(rendered):
        rendered_xtf = serializer.render(read_xtf(xtf, xtf_opening.Transfer), ns_map=ns_map)

    with RuntimeLibrary.from_imd(imd) as runtime:
        transfer = runtime.read(xtf, PARSER_CONFIG)
        assert isinstance(transfer, runtime.transfer)
        assert transfer.datasection.baskets
        out = io.StringIO()
        runtime.write(transfer, out, ns_map=ns_map, config=SERIALIZER_CONFIG)
        assert out.getvalue() == rendered_xtf
        # the classes are reachable through their module, the objects can be pickled
        basket = transfer.datasection.baskets[0]
        assert pickle.loads(pickle.dumps(basket)) == basket


def test_registry(resource_path_root):
    imd = Path(resource_path_root) / IMD_PATHS[0]
    with RuntimeLibrary.from_imd(imd, "runtime_registry") as runtime:
        for imd_class in runtime.index.types_bucket["Class"]:
            if runtime.is_built_class(imd_class.tid):
                built = runtime.classes[imd_class.tid]
                assert built.__name__ == slug(imd_class.tid)
                assert getattr(runtime.module, built.__name__) is built
        assert runtime.classes["SZ_Lebensraum_Fisch_V2.Metadaten.Datenstand"].Meta.name == (
            "SZ_Lebensraum_Fisch_V2.Metadaten.Datenstand"
        )
    with pytest.raises(ImportError):
        RuntimeLibrary.from_imd(imd, "sys").build()
