from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.explicit_assoc_access_type_assoc_acc_of import (
    ExplicitAssocAccessTypeAssocAccOf,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.explicit_assoc_access_type_origin_role import (
    ExplicitAssocAccessTypeOriginRole,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.explicit_assoc_access_type_target_role import (
    ExplicitAssocAccessTypeTargetRole,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_metype import ExtendableMetype

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ExplicitAssocAccessType(ExtendableMetype):
    assoc_acc_of: Optional[ExplicitAssocAccessTypeAssocAccOf] = field(
        default=None,
        metadata={
            "name": "AssocAccOf",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    origin_role: Optional[ExplicitAssocAccessTypeOriginRole] = field(
        default=None,
        metadata={
            "name": "OriginRole",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    target_role: Optional[ExplicitAssocAccessTypeTargetRole] = field(
        default=None,
        metadata={
            "name": "TargetRole",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
