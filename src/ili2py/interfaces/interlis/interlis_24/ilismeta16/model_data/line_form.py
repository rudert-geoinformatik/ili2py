from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import imd_namespace_map
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.meta_element import MetaElement
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import HasRef, Ref


@dataclass
class LineForm(MetaElement):
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    Structure_ref: Optional[Ref] = field(
        metadata={
            "name": "Structure",
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )


@dataclass
class LinesForm(HasRef):
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    LineType_ref: Ref = field(
        metadata={
            "name": "LineType",
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    LineForm_ref: Ref = field(
        metadata={
            "name": "LineForm",
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
