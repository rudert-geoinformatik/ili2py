from dataclasses import dataclass, field
from typing import List, Optional

"""
OeREBKRMtrsfr_V2_0






Transferstruktur: Schnittstelle zwischen der für die Geobasisdaten zuständigen Stelle und der für den Kataster verantwortlichen Stelle des Kantons

"""


ns_map = {"ili": "http://www.interlis.ch/INTERLIS2.3"}


class ILI_META_BASE:
    namespace = ns_map["ili"]


@dataclass(kw_only=True)
class DarstellungsDienstClass:
    """




    Angaben zum Darstellungsdienst

        Attributes:


    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class EigentumsbeschraenkungClass:
    """




    Wurzelelement für Informationen über eine Beschränkung des Grundeigentums, die rechtskräftig, z.B. auf Grund einer Genehmigung oder eines richterlichen Entscheids, zustande gekommen ist

        Attributes:




    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )


@dataclass(kw_only=True)
class GeometrieClass:
    """




    Punkt-, linien-, oder flächenförmige Geometrie; neu zu definierende Eigentumsbeschränkungen sollten in der Regel flächenförmig sein

        Attributes:







            metadatengeobasisdaten (str): Verweis auf maschinenlesbare Metadaten (XML) der zugrundeliegenden Geobasisdaten, z.B. «http://www.geocat.ch/geonetwork/srv/deu/gm03.xml?id=705»
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    metadatengeobasisdaten: Optional[str] = field(
        default=None,
        metadata={
            "name": "MetadatenGeobasisdaten",
            "type": "Element",
            "required": False,
        },
    )


@dataclass(kw_only=True)
class LegendeEintragClass:
    """
    Ein Eintrag in der Planlegende

        Attributes:
            artcodeliste (str): Codeliste der Eigentumsbeschränkung, die durch diesen Legendeneintrag
                dargestellt wird
    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    artcodeliste: str = field(
        metadata={"name": "ArtCodeliste", "type": "Element", "required": True}
    )


@dataclass(kw_only=True)
class TransferstrukturTopic:
    bid: str = field(metadata={"name": "BID", "type": "Attribute"})

    darstellungsdienst: List[DarstellungsDienstClass] = field(
        default_factory=list,
        metadata={
            "name": "OeREBKRMtrsfr_V2_0.Transferstruktur.DarstellungsDienst",
            "type": "Element",
            "default": None,
        },
    )

    eigentumsbeschraenkung: List[EigentumsbeschraenkungClass] = field(
        default_factory=list,
        metadata={
            "name": "OeREBKRMtrsfr_V2_0.Transferstruktur.Eigentumsbeschraenkung",
            "type": "Element",
            "default": None,
        },
    )

    geometrie: List[GeometrieClass] = field(
        default_factory=list,
        metadata={
            "name": "OeREBKRMtrsfr_V2_0.Transferstruktur.Geometrie",
            "type": "Element",
            "default": None,
        },
    )

    legendeeintrag: List[LegendeEintragClass] = field(
        default_factory=list,
        metadata={
            "name": "OeREBKRMtrsfr_V2_0.Transferstruktur.LegendeEintrag",
            "type": "Element",
            "default": None,
        },
    )


@dataclass
class Datasection:
    class Meta(ILI_META_BASE):
        name = "TRANSFER"

        transferstruktur: TransferstrukturTopic = field(
            metadata={
                "name": "OeREBKRMtrsfr_V2_0.Transferstruktur",
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

