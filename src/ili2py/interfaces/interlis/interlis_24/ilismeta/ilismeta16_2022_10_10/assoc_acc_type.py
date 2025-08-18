from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.assoc_acc_type_assoc_acc import AssocAccTypeAssocAcc
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.assoc_acc_type_class import AssocAccTypeClass

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AssocAccType:
    class_value: Optional[AssocAccTypeClass] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    assoc_acc: Optional[AssocAccTypeAssocAcc] = field(
        default=None,
        metadata={
            "name": "AssocAcc",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
