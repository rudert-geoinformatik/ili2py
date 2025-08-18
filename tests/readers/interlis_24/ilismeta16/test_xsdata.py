import os

import pytest
from xsdata.formats.dataclass.parsers.config import ParserConfig

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer
from ili2py.readers.interlis_24.ilismeta16.xsdata import Reader


def test_init():
    reader = Reader()
    assert isinstance(reader.parser_config, ParserConfig)

@pytest.mark.parametrize('imd_path', [
    'models/DMAVTYM_Alles_V1_0/DMAVTYM_Alles_V1_0.imd',
    'models/Fruchtfolgeflaechen_V1/Fruchtfolgeflaechen_V1.imd',
    'models/Gewaesserraum_V1_1/Gewaesserraum_LegendeEintrag_V1_1.imd',
    'models/Gewaesserraum_V1_1/Gewaesserraum_V1_1.imd',
    'models/Hazard_Mapping_V1_3/Hazard_Mapping_V1_3.imd',
    'models/LWB_Bewirtschaftungseinheiten_V2_0/LWB_Bewirtschaftungseinheiten_V2_0.imd',
    'models/LWB_Bewirtschaftungseinheiten_V3_0/LWB_Bewirtschaftungseinheiten_V3_0.imd',
    'models/LWB_Biodiversitaetsfoerderflaechen_Qualitaet_II_und_Vernetzung_V2_0/LWB_Biodiversitaetsfoerderflaechen_Qualitaet_II_und_Vernetzung_V2_0.imd',
    'models/LWB_Nutzungsflaechen_V2_0/LWB_Nutzungsflaechen_V2_0.imd',
    'models/LWB_Nutzungsflaechen_V3_0/LWB_Nutzungsflaechen_V3_0.imd',
    'models/LWB_Perimeter_LandwirtschaftlicheNutzflaeche_Soemmerung_V2_0/LWB_Perimeter_LandwirtschaftlicheNutzflaeche_Soemmerung_V2_0.imd',
    'models/LWB_Perimeter_Terrassenreben_V2_0/LWB_Perimeter_Terrassenreben_V2_0.imd',
    'models/Nutzungsplanung_V1_2/Nutzungsplanung_V1_2.imd',
    'models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd',
    'models/Planungszonen_v1_1/Planungszonen_V1_1.imd',
    'models/SIA405_Abwasser_3D_2015_2_d-20211020/SIA405_Abwasser_3D_2015_2_d-20211020.imd',
    'models/SIA405_LKMap_3D_2015_2_d-20180427/SIA405_LKMap_3D_2015_2_d-20180427.imd',
    'models/SO_AFU_ABBAUSTELLEN_Publikation_20221103/SO_AFU_ABBAUSTELLEN_Publikation_20221103.imd',
    'models/SZ_Lebensraum_Fisch_V2/SZ_Lebensraum_Fisch_V2.imd',
    'models/SZ_Waldfeststellungen_V2/SZ_Waldfeststellungen_V2.imd',
    'models/SZ_Waldreservate_V3/SZ_Waldreservate_V3.imd'
])
def test_parsing(resource_path_root, imd_path):

    reader = Reader()
    metamodel = reader.read(os.path.join(resource_path_root, imd_path), create_index=False)
    assert isinstance(metamodel, ImdTransfer)