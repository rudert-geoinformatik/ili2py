import os
import shutil
from pathlib import Path

import pytest
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from .helpers import GeneratedLibrary, find_xtf, generate_library


@pytest.fixture(scope="session")
def ilivalidator_jar() -> Path:
    """
    Provides the ilivalidator jar, `make test-e2e` sets it via ILIVALIDATOR_JAR. The tests are
    skipped if the jar or java is missing.

    Returns:
        The path of the ilivalidator jar.
    """
    jar = os.environ.get("ILIVALIDATOR_JAR")
    if not jar or not Path(jar).is_file():
        pytest.skip("ILIVALIDATOR_JAR not set or missing, run `make test-e2e`")
    if shutil.which("java") is None:
        pytest.skip("java not found")
    return Path(jar)


@pytest.fixture(scope="session")
def parser_config() -> ParserConfig:
    """
    The xsdata parser configuration of the tests. Unknown elements, attributes and converter
    warnings fail, so data the classes can not hold is not dropped silently.
    """
    return ParserConfig(
        fail_on_unknown_properties=True,
        fail_on_unknown_attributes=True,
        fail_on_converter_warnings=True,
    )


@pytest.fixture(scope="session")
def serializer_config() -> SerializerConfig:
    """The xsdata serializer configuration of the tests, indented as the XTF of the models."""
    return SerializerConfig(indent="  ", xml_declaration=True, encoding="UTF-8")


@pytest.fixture(
    params=[
        # a fast selection of 2.3 and 2.4 models to compare the rendered classes with and
        # without compact geometry, all models of test_roundtrip_xtf.py were checked once
        # (2026-10-31)
        "models/SZ_Lebensraum_Fisch_V2/SZ_Lebensraum_Fisch_V2.imd",
        "models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd",
        "models/Waldabstandslinien_V1_2/Waldabstandslinien_V1_2.imd",
        "models/Richtplan_erneuerbare_Energien_V1_0/PlanDirecteurEnergiesRenouvelables_V1.imd",
        "models/Leitungskataster/SIA405_LKMap_2015_2_d-20180427.imd",
        "models/SZ_Waldreservate_V3/SZ_Waldreservate_V3.imd",
        "models/DMAVTYM_Alles_V1_1/DMAVTYM_Alles_V1_1.imd",
        "models/IncrementalTransfer/DataTest1.imd",
        "models/Waldreservate_V2_0/Waldreservate_V2_0.imd",
    ]
)
def fast_imd(request, resource_path_root) -> Path:
    """The IMD of a model of the fast selection, the tests run once per model."""
    return Path(resource_path_root) / request.param


@pytest.fixture
def fast_library(fast_imd, tmp_path) -> GeneratedLibrary:
    """The python classes rendered out of the IMD of the fast selection."""
    return generate_library(fast_imd, tmp_path / "generated")


@pytest.fixture
def fast_xtf(fast_imd, fast_library, tmp_path) -> Path:
    """The XTF of the model of the fast selection, from its test data folder."""
    return find_xtf(fast_library.name, fast_library.models, fast_imd.parent, tmp_path / "data")
