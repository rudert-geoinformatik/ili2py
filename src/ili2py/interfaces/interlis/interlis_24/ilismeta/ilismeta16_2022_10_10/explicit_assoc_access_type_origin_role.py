from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.assoc_acc_origin import AssocAccOrigin

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ExplicitAssocAccessTypeOriginRole:
    class Meta:
        global_type = False

    assoc_acc_origin: Optional[AssocAccOrigin] = field(
        default=None,
        metadata={
            "name": "AssocAccOrigin",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
