from dataclasses import dataclass, field
from typing import List, Optional

"""
Planungszonen_V1_1






Minimales Geodatenmodell "Planungszonen"
Geobasisdatensatz Nr. 76
TRANSLATION OF-Modelle: Zones_reservees_V1_1.ili, ZoneDiPianificazione_V1_1.ili

"""


ns_map = {"ili": "http://www.interlis.ch/INTERLIS2.3"}


class ILI_META_BASE:
    namespace = ns_map["ili"]


@dataclass(kw_only=True)
class DokumentClass:
    """

    Attributes:








        auszugindex (int):



    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    auszugindex: int = field(
        metadata={"name": "AuszugIndex", "type": "Element", "required": True}
    )


@dataclass(kw_only=True)
class RechtsvorschriftenTopic:
    bid: str = field(metadata={"name": "BID", "type": "Attribute"})

    dokument: List[DokumentClass] = field(
        default_factory=list,
        metadata={
            "name": "Planungszonen_V1_1.Rechtsvorschriften.Dokument",
            "type": "Element",
            "default": None,
        },
    )


@dataclass(kw_only=True)
class PlanungszoneClass:
    """

    Attributes:





        bemerkungen (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    bemerkungen: Optional[str] = field(
        default=None,
        metadata={"name": "Bemerkungen", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class Typ_PlanungszoneClass:
    """

    Attributes:

        code (str):
        bezeichnung (str):
        abkuerzung (str):

        bemerkungen (str):

    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    code: str = field(
        metadata={"name": "Code", "type": "Element", "required": True}
    )

    bezeichnung: str = field(
        metadata={"name": "Bezeichnung", "type": "Element", "required": True}
    )

    abkuerzung: Optional[str] = field(
        default=None,
        metadata={"name": "Abkuerzung", "type": "Element", "required": False},
    )

    bemerkungen: Optional[str] = field(
        default=None,
        metadata={"name": "Bemerkungen", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class GeobasisdatenTopic:
    bid: str = field(metadata={"name": "BID", "type": "Attribute"})

    planungszone: List[PlanungszoneClass] = field(
        default_factory=list,
        metadata={
            "name": "Planungszonen_V1_1.Geobasisdaten.Planungszone",
            "type": "Element",
            "default": None,
        },
    )

    typ_planungszone: List[Typ_PlanungszoneClass] = field(
        default_factory=list,
        metadata={
            "name": "Planungszonen_V1_1.Geobasisdaten.Typ_Planungszone",
            "type": "Element",
            "default": None,
        },
    )


@dataclass(kw_only=True)
class AmtClass:
    """

    Attributes:



        uid (str):
        zeile1 (str):
        zeile2 (str):
        strasse (str):
        hausnr (str):
        plz (str):
        ort (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    uid: Optional[str] = field(
        default=None,
        metadata={"name": "UID", "type": "Element", "required": False},
    )

    zeile1: Optional[str] = field(
        default=None,
        metadata={"name": "Zeile1", "type": "Element", "required": False},
    )

    zeile2: Optional[str] = field(
        default=None,
        metadata={"name": "Zeile2", "type": "Element", "required": False},
    )

    strasse: Optional[str] = field(
        default=None,
        metadata={"name": "Strasse", "type": "Element", "required": False},
    )

    hausnr: Optional[str] = field(
        default=None,
        metadata={"name": "Hausnr", "type": "Element", "required": False},
    )

    plz: Optional[str] = field(
        default=None,
        metadata={"name": "PLZ", "type": "Element", "required": False},
    )

    ort: Optional[str] = field(
        default=None,
        metadata={"name": "Ort", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class DatenbestandClass:
    """

    Attributes:

        basketid (str):


        bemerkungen (str):
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    basketid: Optional[str] = field(
        default=None,
        metadata={"name": "BasketID", "type": "Element", "required": False},
    )

    bemerkungen: Optional[str] = field(
        default=None,
        metadata={"name": "Bemerkungen", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class TransferMetadatenTopic:
    bid: str = field(metadata={"name": "BID", "type": "Attribute"})

    amt: List[AmtClass] = field(
        default_factory=list,
        metadata={
            "name": "Planungszonen_V1_1.TransferMetadaten.Amt",
            "type": "Element",
            "default": None,
        },
    )

    datenbestand: List[DatenbestandClass] = field(
        default_factory=list,
        metadata={
            "name": "Planungszonen_V1_1.TransferMetadaten.Datenbestand",
            "type": "Element",
            "default": None,
        },
    )


@dataclass
class Datasection:
    class Meta(ILI_META_BASE):
        name = "TRANSFER"

        rechtsvorschriften: RechtsvorschriftenTopic = field(
            metadata={
                "name": "Planungszonen_V1_1.Rechtsvorschriften",
                "type": "Element",
                "default": None,
            }
        )
        geobasisdaten: GeobasisdatenTopic = field(
            metadata={
                "name": "Planungszonen_V1_1.Geobasisdaten",
                "type": "Element",
                "default": None,
            }
        )
        transfermetadaten: TransferMetadatenTopic = field(
            metadata={
                "name": "Planungszonen_V1_1.TransferMetadaten",
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

