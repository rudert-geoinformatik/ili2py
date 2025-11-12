import os

import pytest
from xsdata.formats.dataclass.parsers.config import ParserConfig

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader


def test_init():
    reader = Imd16Reader()
    assert isinstance(reader.parser_config, ParserConfig)


@pytest.mark.parametrize(
    "imd_path",
    [
        "models/Planerischer_Gewaesserschutz_V1_2/PlanerischerGewaesserschutz_V1_2.imd",
        "models/Kataster_belasteter_Standorte_V1_5/KbS_V1_5.imd",
        "models/Nutzungsplanung_V1_2/Nutzungsplanung_V1_2.imd",
        "models/Revitalisierungen_Fliessgewaesser_V1_2/Revitalisierung_Fliessgewaesser_V1_2.imd",
        "models/Waldreservate_V2_0/Waldreservate_V2_0.imd",
        "models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/ElektrischeAnlagenNennspannungUeber36kV_V1.imd",
        "models/LWB_Bewirtschaftungseinheiten_V3_0/LWB_Bewirtschaftungseinheiten_V3_0.imd",
        "models/Wildruhezonen_V2_1_1/Wildruhezonen_V2_1.imd",
        "models/SZ_Lebensraum_Fisch_V2/SZ_Lebensraum_Fisch_V2.imd",
        "models/LWB_Biodiversitaetsfoerderflaechen_Qualitaet_II_und_Vernetzung_V2_0/LWB_Biodiversitaetsfoerderflaechen_Qualitaet_II_und_Vernetzung_V2_0.imd",
        "models/SZ_Waldreservate_V3/SZ_Waldreservate_V3.imd",
        "models/Naturereigniskataster_V1_0/Naturereigniskataster_MGDM_V1.imd",
        "models/Grundwasservorkommen_V2_0/Grundwasservorkommen_V2_0.imd",
        "models/Laermempfindlichkeitsstufen_V1_2/Laermempfindlichkeitsstufen_V1_2.imd",
        "models/LWB_Perimeter_Terrassenreben_V2_0/LWB_Perimeter_Terrassenreben_V2_0.imd",
        "models/SIA405_Abwasser_3D_2015_2_d-20211020/SIA405_Abwasser_3D_2015_2_d-20211020.imd",
        "models/Statische_Waldgrenzen_v1_2/Waldgrenzen_V1_2.imd",
        "models/SZ_Waldfeststellungen_V2/SZ_Waldfeststellungen_V2.imd",
        "models/Revitalisierung_Seeufer_V1_2/Revitalisierung_Seen_V1_2.imd",
        "models/Gewaesserraum_V1_1/Gewaesserraum_V1_1.imd",
        "models/Gewaesserraum_V1_1/Gewaesserraum_LegendeEintrag_V1_1.imd",
        "models/SupplySecurity_RuledAreas_V1_2/SupplySecurity_RuledAreas_V1_2.imd",
        "models/Richtplan_erneuerbare_Energien_V1_0/RichtplanungErneuerbareEnergien_V1.imd",
        "models/SO_AFU_ABBAUSTELLEN_Publikation_20221103/SO_AFU_ABBAUSTELLEN_Publikation_20221103.imd",
        "models/Waldreservate_V1_1/Waldreservate_V1_1.imd",
        "models/Leitungskataster/SIA405_LKMap_2015_2_d-20180427.imd",
        "models/Inventar_Wasserentnahmen_V1_1/InventarWasserentnahmen_V1_1.imd",
        "models/Sanierung_Wasserkraft_V1_2/SanierungWasserkraft_V1_2.imd",
        "models/Fruchtfolgeflaechen_V1/Fruchtfolgeflaechen_V1.imd",
        "models/LWB_Bewirtschaftungseinheiten_V2_0/LWB_Bewirtschaftungseinheiten_V2_0.imd",
        "models/Hazard_Mapping_V1_3/Hazard_Mapping_V1_3.imd",
        "models/SIA405_LKMap_3D_2015_2_d-20180427/SIA405_LKMap_3D_2015_2_d-20180427.imd",
        "models/LWB_Nutzungsflaechen_V3_0/LWB_Nutzungsflaechen_V3_0.imd",
        "models/LWB_Nutzungsflaechen_V2_0/LWB_Nutzungsflaechen_V2_0.imd",
        "models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd",
        "models/Holznutzungsbewilligung_V1/Holznutzungsbewilligung_V1_0.imd",
        "models/DMAVTYM_Alles_V1_0/DMAVTYM_Alles_V1_0.imd",
        "models/Planungszonen_v1_1/Planungszonen_V1_1.imd",
        "models/SIA405_Wasser_2015_2_d-20181005/SIA405_Wasser_2015_2_d-20181005.imd",
        "models/LWB_Perimeter_LandwirtschaftlicheNutzflaeche_Soemmerung_V2_0/LWB_Perimeter_LandwirtschaftlicheNutzflaeche_Soemmerung_V2_0.imd",
        "models/Kantonale_Ausnahmetransportrouten_V1_0/ExceptionalLoadsRoute_V1.imd",
        "models/Rodungen_Rodungsersatz_V1_1/Rodungen_V1_1.imd",
    ],
)
def test_parsing(resource_path_root, imd_path):

    reader = Imd16Reader()
    metamodel = reader.read(os.path.join(resource_path_root, imd_path))
    assert isinstance(metamodel, ImdTransfer)
