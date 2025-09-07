from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.import_type_imported_p import ImportTypeImportedP
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.import_type_importing_p import ImportTypeImportingP

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ImportType:
    importing_p: Optional[ImportTypeImportingP] = field(
        default=None,
        metadata={
            "name": "ImportingP",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    imported_p: Optional[ImportTypeImportedP] = field(
        default=None,
        metadata={
            "name": "ImportedP",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
