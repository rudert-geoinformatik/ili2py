from dataclasses import dataclass, field
from typing import Optional, List

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.model_data import imd_namespace_map, \
    MetaAttributeElement
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element import AbstractElement, \
    DocTextElement
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import HasRef, Ref


@dataclass(kw_only=True)
class MetaElement(HasRef, AbstractElement):
    Name: str = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    tid: str = field(
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["ili"]
        }
    )
    Documentation: Optional[List["MetaElement._Documentation"]] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    MetaAttribute: Optional[List[MetaAttributeElement]] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"],
        }
    )
    # use the metadata.name to fetch the element from XML but store it
    #   as `*_ref` instance variable to resolve soft reference to actual object
    ElementInPackage_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "ElementInPackage"
        },
    )

    @dataclass
    class _Documentation:
        DocText: DocTextElement = field(
            metadata={
                "name": "DocText",
                "type": "Element",
                "namespace": imd_namespace_map["IlisMeta16"],
            },
        )
