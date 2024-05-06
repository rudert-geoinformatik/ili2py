from dataclasses import dataclass, field
from typing import List, Optional

"""
SO_AFU_ABBAUSTELLEN_Publikation_20221103







                             Publikationsmodell der Abbaustellen.
                             Vereinigt die beiden Klassen des Editmodels in einer einzigen Klasse.
                            ------------------------------------------------------------------------------
                             Version | wer | Aenderung
                            ------------------------------------------------------------------------------
                             2021-06-30 | OJ | Initial erstellt.
                             2021-07-29 | OJ | Modellierung der Aufzaelungen (Codierungen)
                             2022-11-03 | SC | neuer Aufzähltyp StandRichtplan_Code
                        

"""


ns_map = {"ili": "http://www.interlis.ch/INTERLIS2.3"}


class ILI_META_BASE:
    namespace = ns_map["ili"]


@dataclass(kw_only=True)
class AbbaustelleClass:
    """




    Attribute der Abbaustelle (aus Fachapplikation).

        Attributes:


            bezeichnung (str): Sprechender Name der Abbaustelle
            aktennummer (str): AfU-interne Aktennummer der Abbaustelle
                                Immer in der Form xxx.xxx.xxx formatiert.

            gemeinde_name (str): Standortgemeinde der Abbaustelle - Name.
            gemeinde_bfs (int): Standortgemeinde der Abbaustelle - BFS-Nummer.




            richtplannummer (str): Nummer des Abbaugebeites im kant. Richtplan

            rrb_nr (str): Nummer des Regierungsratsbeschlusses zur Genehmigung des
                                Gestaltungsplans


    """

    tid: Optional[str] = field(
        default=None, metadata={"name": "TID", "type": "Attribute"}
    )

    bezeichnung: str = field(
        metadata={"name": "Bezeichnung", "type": "Element", "required": True}
    )

    aktennummer: str = field(
        metadata={"name": "Aktennummer", "type": "Element", "required": True}
    )

    gemeinde_name: str = field(
        metadata={"name": "Gemeinde_Name", "type": "Element", "required": True}
    )

    gemeinde_bfs: Optional[int] = field(
        default=None,
        metadata={"name": "Gemeinde_Bfs", "type": "Element", "required": False},
    )

    richtplannummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Richtplannummer",
            "type": "Element",
            "required": False,
        },
    )

    rrb_nr: Optional[str] = field(
        default=None,
        metadata={"name": "RRB_Nr", "type": "Element", "required": False},
    )


@dataclass(kw_only=True)
class AbbaustelleTopic:
    bid: str = field(metadata={"name": "BID", "type": "Attribute"})

    abbaustelle: List[AbbaustelleClass] = field(
        default_factory=list,
        metadata={
            "name": "SO_AFU_ABBAUSTELLEN_Publikation_20221103.Abbaustelle.Abbaustelle",
            "type": "Element",
            "default": None,
        },
    )


@dataclass
class Datasection:
    class Meta(ILI_META_BASE):
        name = "TRANSFER"

        abbaustelle: AbbaustelleTopic = field(
            metadata={
                "name": "SO_AFU_ABBAUSTELLEN_Publikation_20221103.Abbaustelle",
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

