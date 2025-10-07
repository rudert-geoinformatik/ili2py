import datetime
import tempfile

from ili2py.writers.uml.interlis_23 import uml_diagram

from ili2py.writers.uml.interlis_23.uml import Diagram

from ili2py.mappers.helpers import Index
from ili2py.writers.py.python_structure import Library
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.py.render import create_python_classes
import logging

logging.getLogger().setLevel(logging.DEBUG)

reader = Imd16Reader()

output_path = tempfile.mkdtemp(prefix="ili2py")

data = [
    {
        "imd": "../../tests/data/models/DMAVTYM_Alles_V1_0/DMAVTYM_Alles_V1_0.imd",
        "xtf": [],
    },
    {
        "imd": "../../tests/data/models/DMAVTYM_Tous_V1_0/DMAVTYM_Tous_V1_0.imd",
        "xtf": [],
    },
    {
        "imd": "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/ElektrischeAnlagenNennspannungUeber36kV_V1.imd",
        "xtf": [
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/arosaenergie.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/axpohydrosurselva.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/axpo.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/bkw.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/ckw.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/ekt.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/esb.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/ewb.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/ewdavos.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/ewn.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/ewo.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/fmv.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/groupe-e.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/ibc.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/iwb.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/khr.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/lagoule.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/primeo.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/regioenergie.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/ses.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/sgsw.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/sig.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/sil.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/swissgrid.xtf",
            "../../tests/data/models/Elektrische_Anlagen_Nennspannung_36kV_V1_0/yverdonenergies.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Fruchtfolgeflaechen_V1/Fruchtfolgeflaechen_V1.imd",
        "xtf": [
            "../../tests/data/models/Fruchtfolgeflaechen_V1/NE_068_surfaces_assolement_2024.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Gewaesserraum_V1_1/Gewaesserraum_LegendeEintrag_V1_1.imd",
        "xtf": [],
    },
    {
        "imd": "../../tests/data/models/Gewaesserraum_V1_1/Gewaesserraum_V1_1.imd",
        "xtf": ["../../tests/data/models/Gewaesserraum_V1_1/gewaesserraum_v1_1_be.xtf"],
    },
    {
        "imd": "../../tests/data/models/Grundwasservorkommen_V2_0/Grundwasservorkommen_V2_0.imd",
        "xtf": [
            "../../tests/data/models/Grundwasservorkommen_V2_0/grundwasservorkommen_v2_0_be.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/Hazard_Mapping_V1_3/Hazard_Mapping_V1_3.imd",
        "xtf": ["../../tests/data/models/Hazard_Mapping_V1_3/NE_166_dangers_nat_1_3_NE.xtf"],
    },
    {
        "imd": "../../tests/data/models/Holznutzungsbewilligung_V1/Holznutzungsbewilligung_V1_0.imd",
        "xtf": ["../../tests/data/models/Holznutzungsbewilligung_V1/Holznutzungsbewilligung.xtf"],
    },
    {
        "imd": "../../tests/data/models/Inventar_Wasserentnahmen_V1_1/InventarWasserentnahmen_V1_1.imd",
        "xtf": [
            "../../tests/data/models/Inventar_Wasserentnahmen_V1_1/InventarWasserentnahmen_V1_1.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/Kantonale_Ausnahmetransportrouten_V1_0/ExceptionalLoadsRoute_V1.imd",
        "xtf": [
            "../../tests/data/models/Kantonale_Ausnahmetransportrouten_V1_0/NE_184_transports_exceptionnels.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/Kataster_belasteter_Standorte_V1_5/KbS_V1_5.imd",
        "xtf": [
            "../../tests/data/models/Kataster_belasteter_Standorte_V1_5/NE_116_a_sites_pollues_1_5.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/Laermempfindlichkeitsstufen_V1_2/Laermempfindlichkeitsstufen_V1_2.imd",
        "xtf": [
            "../../tests/data/models/Laermempfindlichkeitsstufen_V1_2/NE_145_degre_sensiblite_bruit_1_2.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/Leitungskataster/SIA405_LKMap_2015_2_d-20180427.imd",
        "xtf": [
            "../../tests/data/models/Leitungskataster/SBB_SIA405_LKMap_AW_AG.xtf",
            "../../tests/data/models/Leitungskataster/SBB_SIA405_LKMap_EV_AG.xtf",
            "../../tests/data/models/Leitungskataster/SBB_SIA405_LKMap_FM_AG.xtf",
            "../../tests/data/models/Leitungskataster/SBB_SIA405_LKMap_WA_AG.xtf",
            "../../tests/data/models/Leitungskataster/SBB_SIA405_LKMap_WH_AG.xtf",
            "../../tests/data/models/Leitungskataster/SBB_SIA405_LKMap_WV_AG.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/LWB_Bewirtschaftungseinheiten_V2_0/LWB_Bewirtschaftungseinheiten_V2_0.imd",
        "xtf": ["../../tests/data/models/LWB_Bewirtschaftungseinheiten_V2_0/NE_a_153_6.xtf"],
    },
    {
        "imd": "../../tests/data/models/LWB_Bewirtschaftungseinheiten_V3_0/LWB_Bewirtschaftungseinheiten_V3_0.imd",
        "xtf": [],
    },
    {
        "imd": "../../tests/data/models/LWB_Biodiversitaetsfoerderflaechen_Qualitaet_II_und_Vernetzung_V2_0/LWB_Biodiversitaetsfoerderflaechen_Qualitaet_II_und_Vernetzung_V2_0.imd",
        "xtf": [
            "../../tests/data/models/LWB_Biodiversitaetsfoerderflaechen_Qualitaet_II_und_Vernetzung_V2_0/NE_153_3_biodiversite_qualite_II.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/LWB_Nutzungsflaechen_V2_0/LWB_Nutzungsflaechen_V2_0.imd",
        "xtf": [
            "../../tests/data/models/LWB_Nutzungsflaechen_V2_0/NE_a_153_6.xtf",
            "../../tests/data/models/LWB_Nutzungsflaechen_V2_0/NE_b_153_1.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/LWB_Nutzungsflaechen_V3_0/LWB_Nutzungsflaechen_V3_0.imd",
        "xtf": [],
    },
    {
        "imd": "../../tests/data/models/LWB_Perimeter_LandwirtschaftlicheNutzflaeche_Soemmerung_V2_0/LWB_Perimeter_LandwirtschaftlicheNutzflaeche_Soemmerung_V2_0.imd",
        "xtf": [
            "../../tests/data/models/LWB_Perimeter_LandwirtschaftlicheNutzflaeche_Soemmerung_V2_0/NE_a_153_5.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/LWB_Perimeter_Terrassenreben_V2_0/LWB_Perimeter_Terrassenreben_V2_0.imd",
        "xtf": ["../../tests/data/models/LWB_Perimeter_Terrassenreben_V2_0/NE_153_2.xtf"],
    },
    {
        "imd": "../../tests/data/models/Naturereigniskataster_V1_0/Naturereigniskataster_MGDM_V1.imd",
        "xtf": [
            "../../tests/data/models/Naturereigniskataster_V1_0/storme_interlis_export_MGDM_NE_20250728T024603.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/Nutzungsplanung_V1_2/Nutzungsplanung_V1_2.imd",
        "xtf": ["../../tests/data/models/Nutzungsplanung_V1_2/NE_073_plans_affectation_v1_2.xtf"],
    },
    {
        "imd": "../../tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd",
        "xtf": [
            "../../tests/data/models/OeREBKRMtrsfr_V2_0/ch.bazl.kataster-belasteter-standorte-zivilflugplaetze_v2_0.oereb.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/Planerischer_Gewaesserschutz_V1_2/PlanerischerGewaesserschutz_V1_2.imd",
        "xtf": [
            "../../tests/data/models/Planerischer_Gewaesserschutz_V1_2/ur_uri_gwszonen_mgdm_v1_2.xtf",
            "../../tests/data/models/Planerischer_Gewaesserschutz_V1_2/ur_uri_gsbereiche_mgdm_v1_2.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Planungszonen_v1_1/Planungszonen_V1_1.imd",
        "xtf": [
            "../../tests/data/models/Planungszonen_v1_1/ch.Planungszonen.sh.mgdm.v1_1.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Rebbaukataster_V2/LWB_Rebbaukataster_V2_0.imd",
        "xtf": [
            "../../tests/data/models/Rebbaukataster_V2/BL_a_151_1.xtf",
            "../../tests/data/models/Rebbaukataster_V2/NE_151_1.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Revitalisierungen_Fliessgewaesser_V1_2/Revitalisierung_Fliessgewaesser_V1_2.imd",
        "xtf": [
            "../../tests/data/models/Revitalisierungen_Fliessgewaesser_V1_2/revitalisierung_fliessgewaesser_v1_2_be.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Revitalisierung_Seeufer_V1_2/Revitalisierung_Seen_V1_2.imd",
        "xtf": [
            "../../tests/data/models/Revitalisierung_Seeufer_V1_2/revitalisierung_seen_v1_2_be.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Richtplan_erneuerbare_Energien_V1_0/RichtplanungErneuerbareEnergien_V1.imd",
        "xtf": [
            "../../tests/data/models/Richtplan_erneuerbare_Energien_V1_0/NE_PDER_FR.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Richtplan_erneuerbare_Energien_V1_0/SupplySecurity_RuledAreas_V1_2.imd",
        "xtf": [],
    },
    {
        "imd": "../../tests/data/models/Rodungen_Rodungsersatz_V1_1/Rodungen_V1_1.imd",
        "xtf": ["../../tests/data/models/Rodungen_Rodungsersatz_V1_1/Rodungen.xtf"],
    },
    {
        "imd": "../../tests/data/models/Sanierung_Wasserkraft_V1_2/SanierungWasserkraft_V1_2.imd",
        "xtf": [
            "../../tests/data/models/Sanierung_Wasserkraft_V1_2/NE_192_1_assainissement_force_hydraulique_v1_2.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/SIA405_Abwasser_3D_2015_2_d-20211020/SIA405_Abwasser_3D_2015_2_d-20211020.imd",
        "xtf": [],
    },
    {
        "imd": "../../tests/data/models/SIA405_LKMap_3D_2015_2_d-20180427/SIA405_LKMap_3D_2015_2_d-20180427.imd",
        "xtf": [],
    },
    {
        "imd": "../../tests/data/models/SIA405_Wasser_2015_2_d-20181005/SIA405_Wasser_2015_2_d-20181005.imd",
        "xtf": [],
    },
    {
        "imd": "../../tests/data/models/SO_AFU_ABBAUSTELLEN_Publikation_20221103/SO_AFU_ABBAUSTELLEN_Publikation_20221103.imd",
        "xtf": [
            "../../tests/data/models/SO_AFU_ABBAUSTELLEN_Publikation_20221103/ch.so.afu.abbaustellen.xtf"
        ],
    },
    {
        "imd": "../../tests/data/models/Statische_Waldgrenzen_v1_2/Waldgrenzen_V1_2.imd",
        "xtf": [
            "../../tests/data/models/Statische_Waldgrenzen_v1_2/NE_157_limites_forestieres_statiques_v1_2.xtf",
            "../../tests/data/models/Statische_Waldgrenzen_v1_2/npl_waldgrenzen_bl_mgdm_v1.2.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Stromversorgung_Netzgebiete_V1_2/stromversorgungssicherheit_netzgebiete_LV95_V1_2.imd",
        "xtf": [
            "../../tests/data/models/Stromversorgung_Netzgebiete_V1_2/SupplySecurity_RuledAreas_V1_2.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/SZ_Lebensraum_Fisch_V2/SZ_Lebensraum_Fisch_V2.imd",
        "xtf": [
            "../../tests/data/models/SZ_Lebensraum_Fisch_V2/SZ_Lebensraum_Fisch_V2.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/SZ_Waldfeststellungen_V2/SZ_Waldfeststellungen_V2.imd",
        "xtf": [
            "../../tests/data/models/SZ_Waldfeststellungen_V2/SZ_Waldfeststellungen_V2.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/SZ_Waldreservate_V3/SZ_Waldreservate_V3.imd",
        "xtf": [
            "../../tests/data/models/SZ_Waldreservate_V3/SZ_Waldreservate_V3.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Waldabstandslinien_V1_2/Waldabstandslinien_V1_2.imd",
        "xtf": [
            "../../tests/data/models/Waldabstandslinien_V1_2/2761_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2762_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2763_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2764_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2765_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2766_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2767_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2768_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2769_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2770_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2771_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2772_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2773_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2774_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2775_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2781_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2782_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2783_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2784_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2785_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2786_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2787_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2788_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2789_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2790_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2791_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2792_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2793_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2821_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2822_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2823_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2824_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2825_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2826_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2827_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2828_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2829_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2830_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2831_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2832_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2833_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2834_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2841_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2842_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2843_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2844_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2845_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2846_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2847_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2848_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2849_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2850_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2851_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2852_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2853_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2854_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2855_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2856_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2857_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2858_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2859_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2860_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2861_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2862_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2863_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2864_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2865_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2866_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2867_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2868_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2869_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2881_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2882_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2883_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2884_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2885_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2886_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2887_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2888_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2889_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2890_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2891_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2892_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2893_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2894_BL_Waldabstandslinien_V1_2.xtf",
            "../../tests/data/models/Waldabstandslinien_V1_2/2895_BL_Waldabstandslinien_V1_2.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Waldabstandslinien_V1_2/DistancesParRapportALaForet_V1_2.imd",
        "xtf": [
            "../../tests/data/models/Waldabstandslinien_V1_2/NE_159_distance_par_rapport_a_la_foret_v1_2.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Waldreservate_V1_1/Waldreservate_V1_1.imd",
        "xtf": [
            "../../tests/data/models/Waldreservate_V1_1/160_1_reserves_forestieres.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Waldreservate_V2_0/Waldreservate_V2_0.imd",
        "xtf": [
            "../../tests/data/models/Waldreservate_V2_0/waldreservate_v2_0.xtf",
        ],
    },
    {
        "imd": "../../tests/data/models/Wildruhezonen_V2_1_1/Wildruhezonen_V2_1.imd",
        "xtf": [
            "../../tests/data/models/Wildruhezonen_V2_1_1/mgdm_Wildruhezonen_LV95_V2_1_BL.xtf",
        ],
    },
]

diagram_config = [
    {
        "flavour": "plantuml",
        "direction": "top to bottom",
        "linetype": "polyline",
        "postfix": "puml",
    },
    {"flavour": "plantuml", "direction": "top to bottom", "linetype": "ortho", "postfix": "puml"},
    {"flavour": "plantuml", "direction": "top to bottom", "linetype": "spline", "postfix": "puml"},
    {
        "flavour": "plantuml",
        "direction": "left to right",
        "linetype": "polyline",
        "postfix": "puml",
    },
    {"flavour": "plantuml", "direction": "left to right", "linetype": "ortho", "postfix": "puml"},
    {"flavour": "plantuml", "direction": "left to right", "linetype": "spline", "postfix": "puml"},
    {"flavour": "mermaid", "direction": "LR", "linetype": None, "postfix": "md"},
    {"flavour": "mermaid", "direction": "RL", "linetype": None, "postfix": "md"},
    {"flavour": "mermaid", "direction": "TD", "linetype": None, "postfix": "md"},
    {"flavour": "mermaid", "direction": "DT", "linetype": None, "postfix": "md"},
]

for test_set in data:
    metamodel = reader.read(test_set["imd"])
    index = Index(metamodel.datasection)
    library_name = f'{index.types_bucket["Model"][-1].name}'
    library = Library.from_imd(metamodel.datasection.ModelData, index, library_name)
    create_python_classes(library, index, output_path)
    diagram = Diagram.from_imd(index)
    for configuration in diagram_config:
        uml_diagram(
            diagram,
            index,
            [library_name],
            configuration["flavour"],
            ".".join(
                [
                    library_name,
                    configuration["flavour"],
                    configuration["direction"],
                    configuration["linetype"] if configuration["linetype"] else "_",
                    configuration["postfix"],
                ]
            ),
            output_path,
            linetype=configuration["linetype"],
            direction=configuration["direction"],
        )

"""
run in bash afterwards:
find /tmp/ili2pyirc98n2_/mermaid/ -type f -name "*.md" | parallel -j 14 'mmdc -i {} -o {.}.png
plantuml -tpng /tmp/ili2pyirc98n2_/plantuml/*.puml
"""
