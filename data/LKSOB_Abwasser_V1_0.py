from dataclasses import dataclass, field
from typing import List, Optional

"""
LKSOB_Abwasser_V1_0


"""


ns_map = {"ili": "http://www.interlis.ch/INTERLIS2.3"}


class ILI_META_BASE:
    namespace = ns_map["ili"]


@dataclass(kw_only=True)
class SIA_Haltung_Material_ItemClass:
    """

    Attributes:

        name (str):
        code (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )

    code: Optional[str] = field(
        default=None,
        metadata={"name": "Code", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Deckel_Lagegenauigkeit_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Deckel_Deckelform_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Deckel_Verschluss_ItemClass:
    """

    Attributes:

        name (str):
        code (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )

    code: Optional[str] = field(
        default=None,
        metadata={"name": "Code", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Versickerungsanlage_Art_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Versickerungsanlage_Beschriftung_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Versickerungsanlage_Versickerungswasser_ItemClass:
    """

    Attributes:

        name (str):
        code (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )

    code: Optional[str] = field(
        default=None,
        metadata={"name": "Code", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Spezialbauwerk_Funktion_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Normschacht_Material_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Normschacht_Funktion_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Kanal_Nutzungsart_Ist_ItemClass:
    """

    Attributes:

        name (str):
        code (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )

    code: Optional[str] = field(
        default=None,
        metadata={"name": "Code", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Kanal_Funktion_Hierarchisch_ItemClass:
    """

    Attributes:

        name (str):
        code (str):
        typ (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )

    code: Optional[str] = field(
        default=None,
        metadata={"name": "Code", "type": "Element", "required": False},
    )

    typ: Optional[str] = field(
        default=None,
        metadata={"name": "Typ", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Haltungspunkt_Hoehengenauigkeit_ItemClass:
    """

    Attributes:

        name (str):
        code (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )

    code: Optional[str] = field(
        default=None,
        metadata={"name": "Code", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_Rohrprofil_Profiltyp_ItemClass:
    """

    Attributes:

        name (str):
        code (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )

    code: Optional[str] = field(
        default=None,
        metadata={"name": "Code", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SIA_KatalogTopic:
    bid: str = field(metadata={"name": "BID", "type": "Attribute"})

    sia_haltung_material_item: List[SIA_Haltung_Material_ItemClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Haltung_Material_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_deckel_lagegenauigkeit_item: List[
        SIA_Deckel_Lagegenauigkeit_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Deckel_Lagegenauigkeit_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_deckel_deckelform_item: List[SIA_Deckel_Deckelform_ItemClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Deckel_Deckelform_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_deckel_verschluss_item: List[SIA_Deckel_Verschluss_ItemClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Deckel_Verschluss_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_versickerungsanlage_art_item: List[
        SIA_Versickerungsanlage_Art_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Versickerungsanlage_Art_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_versickerungsanlage_beschriftung_item: List[
        SIA_Versickerungsanlage_Beschriftung_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Versickerungsanlage_Beschriftung_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_versickerungsanlage_versickerungswasser_item: List[
        SIA_Versickerungsanlage_Versickerungswasser_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Versickerungsanlage_Versickerungswasser_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_spezialbauwerk_funktion_item: List[
        SIA_Spezialbauwerk_Funktion_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Spezialbauwerk_Funktion_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_normschacht_material_item: List[SIA_Normschacht_Material_ItemClass] = (
        field(
            default_factory=list,
            metadata={
                "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Normschacht_Material_Item",
                "type": "Element",
                "default": None,
            },
        )
    )

    sia_normschacht_funktion_item: List[SIA_Normschacht_Funktion_ItemClass] = (
        field(
            default_factory=list,
            metadata={
                "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Normschacht_Funktion_Item",
                "type": "Element",
                "default": None,
            },
        )
    )

    sia_kanal_nutzungsart_ist_item: List[
        SIA_Kanal_Nutzungsart_Ist_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Kanal_Nutzungsart_Ist_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_kanal_funktion_hierarchisch_item: List[
        SIA_Kanal_Funktion_Hierarchisch_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Kanal_Funktion_Hierarchisch_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_haltungspunkt_hoehengenauigkeit_item: List[
        SIA_Haltungspunkt_Hoehengenauigkeit_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Haltungspunkt_Hoehengenauigkeit_Item",
            "type": "Element",
            "default": None,
        },
    )

    sia_rohrprofil_profiltyp_item: List[SIA_Rohrprofil_Profiltyp_ItemClass] = (
        field(
            default_factory=list,
            metadata={
                "name": "LKSOB_Abwasser_V1_0.SIA_Katalog.SIA_Rohrprofil_Profiltyp_Item",
                "type": "Element",
                "default": None,
            },
        )
    )


@dataclass(kw_only=True)
class SOB_Haltung_Durchleitung_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SOB_Deckel_Material_Deckelart_ItemClass:
    """

    Attributes:

        name (str):
        code (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )

    code: Optional[str] = field(
        default=None,
        metadata={"name": "Code", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SOB_EntwaesserungsTypItemClass:
    """

    Attributes:

        name (str):
        code (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )

    code: Optional[str] = field(
        default=None,
        metadata={"name": "Code", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SOB_Spezialbauwerk_Ausstattung_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SOB_Kanal_Entwaesserungstyp_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SOB_Position_Gleis_ItemClass:
    """

    Attributes:

        name (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    name: Optional[str] = field(
        default=None,
        metadata={"name": "Name", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class SOB_KatalogTopic:
    bid: str = field(metadata={"name": "BID", "type": "Attribute"})

    sob_haltung_durchleitung_item: List[SOB_Haltung_Durchleitung_ItemClass] = (
        field(
            default_factory=list,
            metadata={
                "name": "LKSOB_Abwasser_V1_0.SOB_Katalog.SOB_Haltung_Durchleitung_Item",
                "type": "Element",
                "default": None,
            },
        )
    )

    sob_deckel_material_deckelart_item: List[
        SOB_Deckel_Material_Deckelart_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SOB_Katalog.SOB_Deckel_Material_Deckelart_Item",
            "type": "Element",
            "default": None,
        },
    )

    sob_entwaesserungstypitem: List[SOB_EntwaesserungsTypItemClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SOB_Katalog.SOB_EntwaesserungsTypItem",
            "type": "Element",
            "default": None,
        },
    )

    sob_spezialbauwerk_ausstattung_item: List[
        SOB_Spezialbauwerk_Ausstattung_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SOB_Katalog.SOB_Spezialbauwerk_Ausstattung_Item",
            "type": "Element",
            "default": None,
        },
    )

    sob_kanal_entwaesserungstyp_item: List[
        SOB_Kanal_Entwaesserungstyp_ItemClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SOB_Katalog.SOB_Kanal_Entwaesserungstyp_Item",
            "type": "Element",
            "default": None,
        },
    )

    sob_position_gleis_item: List[SOB_Position_Gleis_ItemClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.SOB_Katalog.SOB_Position_Gleis_Item",
            "type": "Element",
            "default": None,
        },
    )


@dataclass(kw_only=True)
class SOB_Abwasser_Base_ClassClass:
    """

    Attributes:

        bemerkung (str):
        bezeichnung (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    bemerkung: Optional[str] = field(
        default=None,
        metadata={"name": "Bemerkung", "type": "Element", "required": False},
    )

    bezeichnung: str = field(
        metadata={"name": "Bezeichnung", "type": "Element", "required": True}
    )


@dataclass(kw_only=True)
class SOB_Abwasser_Base_Class_ExtendedClass:
    """

    Attributes:





    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class AbwasserbauwerkClass:
    """

    Attributes:




    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class AbwassernetzelementClass:
    """

    Attributes:

    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class HaltungspunktClass:
    """

    Attributes:




    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class RohrprofilClass:
    """

    Attributes:

        hoehenbreitenverhaeltnis (int):

    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    hoehenbreitenverhaeltnis: Optional[int] = field(
        default=None,
        metadata={
            "name": "HoehenBreitenverhaeltnis",
            "type": "Element",
            "required": False,
        },
    )


@dataclass(kw_only=True)
class AbwasserknotenClass:
    """

    Attributes:



    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class BauwerksTeilClass:
    """

    Attributes:

    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class EinleitstelleClass:
    """

    Attributes:



    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class HaltungClass:
    """

    Attributes:



        lichtehoehe (int):
        laengeeffektiv (int):





    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    lichtehoehe: Optional[int] = field(
        default=None,
        metadata={"name": "LichteHoehe", "type": "Element", "required": False},
    )

    laengeeffektiv: Optional[int] = field(
        default=None,
        metadata={
            "name": "LaengeEffektiv",
            "type": "Element",
            "required": False,
        },
    )


@dataclass(kw_only=True)
class KanalClass:
    """

    Attributes:



        rohrlaenge (int):

        sob_hinweiszurspuelung (str):

    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    rohrlaenge: Optional[int] = field(
        default=None,
        metadata={"name": "Rohrlaenge", "type": "Element", "required": False},
    )

    sob_hinweiszurspuelung: Optional[str] = field(
        default=None,
        metadata={
            "name": "SOB_HinweisZurSpuelung",
            "type": "Element",
            "required": False,
        },
    )


@dataclass(kw_only=True)
class NormschachtClass:
    """

    Attributes:










    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class SpezialbauwerkClass:
    """

    Attributes:






    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class VersickerungsanlageClass:
    """

    Attributes:







        schluckvermoegen (int):

        wirksameflaeche (int):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    schluckvermoegen: Optional[int] = field(
        default=None,
        metadata={
            "name": "Schluckvermoegen",
            "type": "Element",
            "required": False,
        },
    )

    wirksameflaeche: Optional[int] = field(
        default=None,
        metadata={
            "name": "Wirksameflaeche",
            "type": "Element",
            "required": False,
        },
    )


@dataclass(kw_only=True)
class DeckelClass:
    """

    Attributes:







        sob_belastbarkeit (int):

    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    sob_belastbarkeit: Optional[int] = field(
        default=None,
        metadata={
            "name": "SOB_Belastbarkeit",
            "type": "Element",
            "required": False,
        },
    )


@dataclass(kw_only=True)
class AbwasserTopic:
    bid: str = field(metadata={"name": "BID", "type": "Attribute"})

    sob_abwasser_base_class: List[SOB_Abwasser_Base_ClassClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.SOB_Abwasser_Base_Class",
            "type": "Element",
            "default": None,
        },
    )

    sob_abwasser_base_class_extended: List[
        SOB_Abwasser_Base_Class_ExtendedClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.SOB_Abwasser_Base_Class_Extended",
            "type": "Element",
            "default": None,
        },
    )

    abwasserbauwerk: List[AbwasserbauwerkClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Abwasserbauwerk",
            "type": "Element",
            "default": None,
        },
    )

    abwassernetzelement: List[AbwassernetzelementClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Abwassernetzelement",
            "type": "Element",
            "default": None,
        },
    )

    haltungspunkt: List[HaltungspunktClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Haltungspunkt",
            "type": "Element",
            "default": None,
        },
    )

    rohrprofil: List[RohrprofilClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Rohrprofil",
            "type": "Element",
            "default": None,
        },
    )

    abwasserknoten: List[AbwasserknotenClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Abwasserknoten",
            "type": "Element",
            "default": None,
        },
    )

    bauwerksteil: List[BauwerksTeilClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.BauwerksTeil",
            "type": "Element",
            "default": None,
        },
    )

    einleitstelle: List[EinleitstelleClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Einleitstelle",
            "type": "Element",
            "default": None,
        },
    )

    haltung: List[HaltungClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Haltung",
            "type": "Element",
            "default": None,
        },
    )

    kanal: List[KanalClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Kanal",
            "type": "Element",
            "default": None,
        },
    )

    normschacht: List[NormschachtClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Normschacht",
            "type": "Element",
            "default": None,
        },
    )

    spezialbauwerk: List[SpezialbauwerkClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Spezialbauwerk",
            "type": "Element",
            "default": None,
        },
    )

    versickerungsanlage: List[VersickerungsanlageClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Versickerungsanlage",
            "type": "Element",
            "default": None,
        },
    )

    deckel: List[DeckelClass] = field(
        default_factory=list,
        metadata={
            "name": "LKSOB_Abwasser_V1_0.Abwasser.Deckel",
            "type": "Element",
            "default": None,
        },
    )


@dataclass
class Datasection:
    class Meta(ILI_META_BASE):
        name = "TRANSFER"

        sia_katalog: SIA_KatalogTopic = field(
            metadata={
                "name": "LKSOB_Abwasser_V1_0.SIA_Katalog",
                "type": "Element",
                "default": None,
            }
        )
        sob_katalog: SOB_KatalogTopic = field(
            metadata={
                "name": "LKSOB_Abwasser_V1_0.SOB_Katalog",
                "type": "Element",
                "default": None,
            }
        )
        abwasser: AbwasserTopic = field(
            metadata={
                "name": "LKSOB_Abwasser_V1_0.Abwasser",
                "type": "Element",
                "default": None,
            }
        )


@dataclass(kw_only=True)
class Model:
    class Meta(ILI_META_BASE):
        name = "MODEL"

    name: str = field(
        metadata={
            "name": "NAME",
            "type": "Attribute",
            "required": False,
        },
    )
    version: str = field(
        metadata={
            "name": "VERSION",
            "type": "Attribute",
            "required": False,
        },
    )
    uri: str = field(
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": False,
        },
    )


@dataclass
class ModelItem:
    class Meta(ILI_META_BASE):
        name = "MODEL"

    model: Model = field(
        metadata={
            "name": "MODEL",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Headersection:
    class Meta(ILI_META_BASE):
        name = "HEADERSECTION"

    models: List[ModelItem] = field(
        metadata={
            "name": "MODELS",
            "type": "Element",
            "required": True,
        },
    )
    sender: str = field(
        default=None,
        metadata={
            "name": "SENDER",
            "type": "Attribute",
            "required": True,
        },
    )
    version: str = field(
        default=None,
        metadata={
            "name": "VERSION",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Transfer:
    class Meta(ILI_META_BASE):
        name = "TRANSFER"

    headersection: Headersection = field(
        metadata={
            "name": "HEADERSECTION",
            "type": "Element",
            "required": True,
        },
    )
    datasection: Datasection = field(
        metadata={
            "name": "DATASECTION",
            "type": "Element",
            "required": True,
        },
    )

