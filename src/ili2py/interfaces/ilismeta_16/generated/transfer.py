from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime


@dataclass
class Models:
    class Meta:
        name = "models"
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    model: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Association:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    order_pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class AttrParent:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    order_pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Axis:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    order_pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class BaseType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Crt:
    class Meta:
        name = "CRT"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Crtr:
    class Meta:
        name = "CRTR"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class ClassInBasket:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Constant:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    value: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Dependent:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class DocText:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ElementInPackage:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class FormalArgument:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Function:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    order_pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )


@dataclass
class Ili1RefAttr:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    order_pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Ili1TransferClass:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Lftparent:
    class Meta:
        name = "LFTParent"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Ltparent:
    class Meta:
        name = "LTParent"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class MetaDataTopic:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class MetaElement:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Multiplicity:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    min: Optional[int] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
        },
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
        },
    )
    multiplicity: Optional["Multiplicity"] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
        },
    )


@dataclass
class Of:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class OfDataUnit:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Oid:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class ParamParent:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    order_pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class ParentNode:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    order_pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Ref:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class ResultType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Struct:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Structure:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Super:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class ToClass:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class TransferClass:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class TypeType:
    class Meta:
        name = "Type"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Using:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )


@dataclass
class Headersection:
    class Meta:
        name = "headersection"
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    models: Optional[Models] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sender: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AllowedInBasket:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    of_data_unit: Optional[OfDataUnit] = field(
        default=None,
        metadata={
            "name": "OfDataUnit",
            "type": "Element",
            "required": True,
        },
    )
    class_in_basket: Optional[ClassInBasket] = field(
        default=None,
        metadata={
            "name": "ClassInBasket",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AnyOidtype:
    class Meta:
        name = "AnyOIDType"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Argument:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "required": True,
        },
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )


@dataclass
class AttributeRefType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    lftparent: Optional[Lftparent] = field(
        default=None,
        metadata={
            "name": "LFTParent",
            "type": "Element",
            "required": True,
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    of: Optional[Of] = field(
        default=None,
        metadata={
            "name": "Of",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BaseClass:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    crt: Optional[Crt] = field(
        default=None,
        metadata={
            "name": "CRT",
            "type": "Element",
        },
    )
    base_class: Optional["BaseClass"] = field(
        default=None,
        metadata={
            "name": "BaseClass",
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )


@dataclass
class BooleanType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    ltparent: Optional[Ltparent] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
        },
    )
    lftparent: Optional[Lftparent] = field(
        default=None,
        metadata={
            "name": "LFTParent",
            "type": "Element",
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ClassRefType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    ltparent: Optional[Ltparent] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
        },
    )
    lftparent: Optional[Lftparent] = field(
        default=None,
        metadata={
            "name": "LFTParent",
            "type": "Element",
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ClassRestriction:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    crtr: Optional[Crtr] = field(
        default=None,
        metadata={
            "name": "CRTR",
            "type": "Element",
        },
    )
    class_restriction: Optional["ClassRestriction"] = field(
        default=None,
        metadata={
            "name": "ClassRestriction",
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )


@dataclass
class CoordType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
        },
    )
    multi: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Multi",
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )


@dataclass
class DataUnit:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    view_unit: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ViewUnit",
            "type": "Element",
            "required": True,
        },
    )
    data_unit_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataUnitName",
            "type": "Element",
            "required": True,
        },
    )
    oid: Optional[Oid] = field(
        default=None,
        metadata={
            "name": "Oid",
            "type": "Element",
        },
    )


@dataclass
class Dependency:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    using: Optional[Using] = field(
        default=None,
        metadata={
            "name": "Using",
            "type": "Element",
            "required": True,
        },
    )
    dependent: Optional[Dependent] = field(
        default=None,
        metadata={
            "name": "Dependent",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Derivates:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    constant: Optional[Constant] = field(
        default=None,
        metadata={
            "name": "Constant",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Documentation:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    doc_text: Optional[DocText] = field(
        default=None,
        metadata={
            "name": "DocText",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EnumType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
        },
    )
    ltparent: Optional[Ltparent] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
        },
    )
    order: Optional[str] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
    order_pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )


@dataclass
class FormattedType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    super: Optional[Super] = field(
        default=None,
        metadata={
            "name": "Super",
            "type": "Element",
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    min: Optional[str] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
            "required": True,
        },
    )
    max: Optional[Union[XmlDateTime, XmlDate, XmlTime]] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
            "required": True,
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "required": True,
        },
    )
    struct: Optional[Struct] = field(
        default=None,
        metadata={
            "name": "Struct",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class FunctionDef:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
            "required": True,
        },
    )
    result_type: Optional[ResultType] = field(
        default=None,
        metadata={
            "name": "ResultType",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ili1TransferElement:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ili1_transfer_class: Optional[Ili1TransferClass] = field(
        default=None,
        metadata={
            "name": "Ili1TransferClass",
            "type": "Element",
            "required": True,
        },
    )
    ili1_ref_attr: Optional[Ili1RefAttr] = field(
        default=None,
        metadata={
            "name": "Ili1RefAttr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LineForm:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
            "required": True,
        },
    )
    structure: Optional[Structure] = field(
        default=None,
        metadata={
            "name": "Structure",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LineType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    ltparent: Optional[Ltparent] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
            "required": True,
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "required": True,
        },
    )
    multi: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Multi",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MetaAttribute:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    meta_element: Optional[MetaElement] = field(
        default=None,
        metadata={
            "name": "MetaElement",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MetaBasketDef:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
        },
    )
    meta_data_topic: Optional[MetaDataTopic] = field(
        default=None,
        metadata={
            "name": "MetaDataTopic",
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )


@dataclass
class MultiValue:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    ltparent: Optional[Ltparent] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
        },
    )
    lftparent: Optional[Lftparent] = field(
        default=None,
        metadata={
            "name": "LFTParent",
            "type": "Element",
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    base_type: Optional[BaseType] = field(
        default=None,
        metadata={
            "name": "BaseType",
            "type": "Element",
            "required": True,
        },
    )
    ordered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ordered",
            "type": "Element",
            "required": True,
        },
    )
    multiplicity: Optional[Multiplicity] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ObjectType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    lftparent: Optional[Lftparent] = field(
        default=None,
        metadata={
            "name": "LFTParent",
            "type": "Element",
            "required": True,
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    multiple: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Multiple",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PathEl:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "required": True,
        },
    )
    ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ReferenceType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    ltparent: Optional[Ltparent] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
            "required": True,
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    external: Optional[bool] = field(
        default=None,
        metadata={
            "name": "External",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Role:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    external: Optional[bool] = field(
        default=None,
        metadata={
            "name": "External",
            "type": "Element",
            "required": True,
        },
    )
    strongness: Optional[str] = field(
        default=None,
        metadata={
            "name": "Strongness",
            "type": "Element",
            "required": True,
        },
    )
    ordered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ordered",
            "type": "Element",
            "required": True,
        },
    )
    multiplicity: Optional[Multiplicity] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "required": True,
        },
    )
    embedded_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EmbeddedTransfer",
            "type": "Element",
            "required": True,
        },
    )
    association: Optional[Association] = field(
        default=None,
        metadata={
            "name": "Association",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SubModel:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TextType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    super: Optional[Super] = field(
        default=None,
        metadata={
            "name": "Super",
            "type": "Element",
        },
    )
    ltparent: Optional[Ltparent] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
        },
    )
    lftparent: Optional[Lftparent] = field(
        default=None,
        metadata={
            "name": "LFTParent",
            "type": "Element",
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "required": True,
        },
    )
    max_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxLength",
            "type": "Element",
        },
    )


@dataclass
class TransferElement:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
    order_pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
    transfer_class: Optional[TransferClass] = field(
        default=None,
        metadata={
            "name": "TransferClass",
            "type": "Element",
        },
    )
    transfer_element: Optional["TransferElement"] = field(
        default=None,
        metadata={
            "name": "TransferElement",
            "type": "Element",
        },
    )


@dataclass
class AttrOrParam:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    documentation: Optional[Documentation] = field(
        default=None,
        metadata={
            "name": "Documentation",
            "type": "Element",
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    super: Optional[Super] = field(
        default=None,
        metadata={
            "name": "Super",
            "type": "Element",
        },
    )
    subdivision_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubdivisionKind",
            "type": "Element",
        },
    )
    transient: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Transient",
            "type": "Element",
        },
    )
    derivates: Optional[Derivates] = field(
        default=None,
        metadata={
            "name": "Derivates",
            "type": "Element",
        },
    )
    attr_parent: Optional[AttrParent] = field(
        default=None,
        metadata={
            "name": "AttrParent",
            "type": "Element",
        },
    )
    param_parent: Optional[ParamParent] = field(
        default=None,
        metadata={
            "name": "ParamParent",
            "type": "Element",
        },
    )
    type_value: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AxisSpec:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    coord_type: Optional[CoordType] = field(
        default=None,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "required": True,
        },
    )
    axis: Optional[Axis] = field(
        default=None,
        metadata={
            "name": "Axis",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Class:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    documentation: Optional[Documentation] = field(
        default=None,
        metadata={
            "name": "Documentation",
            "type": "Element",
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
        },
    )
    super: Optional[Super] = field(
        default=None,
        metadata={
            "name": "Super",
            "type": "Element",
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
        },
    )
    embedded_role_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EmbeddedRoleTransfer",
            "type": "Element",
        },
    )
    oid: Optional[Oid] = field(
        default=None,
        metadata={
            "name": "Oid",
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )


@dataclass
class EnumNode:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[Union[str, bool]] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    parent_node: Optional[ParentNode] = field(
        default=None,
        metadata={
            "name": "ParentNode",
            "type": "Element",
        },
    )
    enum_type: Optional[EnumType] = field(
        default=None,
        metadata={
            "name": "EnumType",
            "type": "Element",
        },
    )


@dataclass
class Model:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    documentation: Optional[Documentation] = field(
        default=None,
        metadata={
            "name": "Documentation",
            "type": "Element",
        },
    )
    ili_version: Optional[float] = field(
        default=None,
        metadata={
            "name": "iliVersion",
            "type": "Element",
            "required": True,
        },
    )
    contracted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Contracted",
            "type": "Element",
            "required": True,
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "required": True,
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        },
    )
    at: Optional[str] = field(
        default=None,
        metadata={
            "name": "At",
            "type": "Element",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
        },
    )


@dataclass
class PathEls:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    path_el: List[PathEl] = field(
        default_factory=list,
        metadata={
            "name": "PathEl",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class MetaObjectDef:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    is_ref_system: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRefSystem",
            "type": "Element",
            "required": True,
        },
    )
    class_value: Optional[Class] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "required": True,
        },
    )
    meta_basket_def: Optional[MetaBasketDef] = field(
        default=None,
        metadata={
            "name": "MetaBasketDef",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PathOrInspFactor:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    path_els: Optional[PathEls] = field(
        default=None,
        metadata={
            "name": "PathEls",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Expression:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    constant: Optional[Constant] = field(
        default=None,
        metadata={
            "name": "Constant",
            "type": "Element",
        },
    )
    path_or_insp_factor: Optional[PathOrInspFactor] = field(
        default=None,
        metadata={
            "name": "PathOrInspFactor",
            "type": "Element",
        },
    )


@dataclass
class ActualArgument:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    formal_argument: Optional[FormalArgument] = field(
        default=None,
        metadata={
            "name": "FormalArgument",
            "type": "Element",
            "required": True,
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "required": True,
        },
    )
    expression: Optional[Expression] = field(
        default=None,
        metadata={
            "name": "Expression",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Arguments:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    actual_argument: List[ActualArgument] = field(
        default_factory=list,
        metadata={
            "name": "ActualArgument",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class FunctionCall:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "required": True,
        },
    )
    arguments: Optional[Arguments] = field(
        default=None,
        metadata={
            "name": "Arguments",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SubExpression:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    path_or_insp_factor: Optional[PathOrInspFactor] = field(
        default=None,
        metadata={
            "name": "PathOrInspFactor",
            "type": "Element",
        },
    )
    compound_expr: Optional["CompoundExpr"] = field(
        default=None,
        metadata={
            "name": "CompoundExpr",
            "type": "Element",
        },
    )
    function_call: Optional[FunctionCall] = field(
        default=None,
        metadata={
            "name": "FunctionCall",
            "type": "Element",
        },
    )


@dataclass
class UnaryExpr:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Element",
            "required": True,
        },
    )
    sub_expression: Optional[SubExpression] = field(
        default=None,
        metadata={
            "name": "SubExpression",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SubExpressions:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    path_or_insp_factor: Optional[PathOrInspFactor] = field(
        default=None,
        metadata={
            "name": "PathOrInspFactor",
            "type": "Element",
        },
    )
    constant: Optional[Constant] = field(
        default=None,
        metadata={
            "name": "Constant",
            "type": "Element",
        },
    )
    compound_expr: List["CompoundExpr"] = field(
        default_factory=list,
        metadata={
            "name": "CompoundExpr",
            "type": "Element",
        },
    )
    unary_expr: List[UnaryExpr] = field(
        default_factory=list,
        metadata={
            "name": "UnaryExpr",
            "type": "Element",
        },
    )


@dataclass
class CompoundExpr:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Element",
            "required": True,
        },
    )
    sub_expressions: Optional[SubExpressions] = field(
        default=None,
        metadata={
            "name": "SubExpressions",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Definition:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    compound_expr: Optional[CompoundExpr] = field(
        default=None,
        metadata={
            "name": "CompoundExpr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicalExpression:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    compound_expr: Optional[CompoundExpr] = field(
        default=None,
        metadata={
            "name": "CompoundExpr",
            "type": "Element",
        },
    )
    path_or_insp_factor: Optional[PathOrInspFactor] = field(
        default=None,
        metadata={
            "name": "PathOrInspFactor",
            "type": "Element",
        },
    )
    unary_expr: Optional[UnaryExpr] = field(
        default=None,
        metadata={
            "name": "UnaryExpr",
            "type": "Element",
        },
    )


@dataclass
class SimpleConstraint:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    to_class: Optional[ToClass] = field(
        default=None,
        metadata={
            "name": "ToClass",
            "type": "Element",
            "required": True,
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "required": True,
        },
    )
    logical_expression: Optional[LogicalExpression] = field(
        default=None,
        metadata={
            "name": "LogicalExpression",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Unit:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
        },
    )
    super: Optional[Super] = field(
        default=None,
        metadata={
            "name": "Super",
            "type": "Element",
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
        },
    )
    definition: Optional[Definition] = field(
        default=None,
        metadata={
            "name": "Definition",
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )


@dataclass
class NumType:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    element_in_package: Optional[ElementInPackage] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
        },
    )
    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    super: Optional[Super] = field(
        default=None,
        metadata={
            "name": "Super",
            "type": "Element",
        },
    )
    ltparent: Optional[Ltparent] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
        },
    )
    lftparent: Optional[Lftparent] = field(
        default=None,
        metadata={
            "name": "LFTParent",
            "type": "Element",
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    min: Optional[Union[int, Decimal]] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
        },
    )
    max: Optional[Union[int, float, Decimal]] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
        },
    )
    circular: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Circular",
            "type": "Element",
            "required": True,
        },
    )
    unit: Optional[Unit] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
        },
    )


@dataclass
class ModelData:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

    bid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    model: Optional[Model] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "required": True,
        },
    )
    line_form: List[LineForm] = field(
        default_factory=list,
        metadata={
            "name": "LineForm",
            "type": "Element",
            "sequence": 1,
        },
    )
    unit: List[Unit] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "sequence": 2,
        },
    )
    meta_attribute: Optional[MetaAttribute] = field(
        default=None,
        metadata={
            "name": "MetaAttribute",
            "type": "Element",
        },
    )
    text_type: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "TextType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    enum_node: List[EnumNode] = field(
        default_factory=list,
        metadata={
            "name": "EnumNode",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    enum_type: List[EnumType] = field(
        default_factory=list,
        metadata={
            "name": "EnumType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    any_oidtype: List[AnyOidtype] = field(
        default_factory=list,
        metadata={
            "name": "AnyOIDType",
            "type": "Element",
            "sequence": 2,
        },
    )
    num_type: List[NumType] = field(
        default_factory=list,
        metadata={
            "name": "NumType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    axis_spec: List[AxisSpec] = field(
        default_factory=list,
        metadata={
            "name": "AxisSpec",
            "type": "Element",
            "sequence": 2,
        },
    )
    coord_type: List[CoordType] = field(
        default_factory=list,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "sequence": 2,
        },
    )
    base_class: List[BaseClass] = field(
        default_factory=list,
        metadata={
            "name": "BaseClass",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    class_ref_type: List[ClassRefType] = field(
        default_factory=list,
        metadata={
            "name": "ClassRefType",
            "type": "Element",
            "sequence": 2,
        },
    )
    object_type: List[ObjectType] = field(
        default_factory=list,
        metadata={
            "name": "ObjectType",
            "type": "Element",
            "sequence": 2,
        },
    )
    argument: List[Argument] = field(
        default_factory=list,
        metadata={
            "name": "Argument",
            "type": "Element",
            "sequence": 2,
        },
    )
    function_def: List[FunctionDef] = field(
        default_factory=list,
        metadata={
            "name": "FunctionDef",
            "type": "Element",
            "sequence": 2,
        },
    )
    role: List[Role] = field(
        default_factory=list,
        metadata={
            "name": "Role",
            "type": "Element",
            "sequence": 1,
        },
    )
    boolean_type: List[BooleanType] = field(
        default_factory=list,
        metadata={
            "name": "BooleanType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    multi_value: List[MultiValue] = field(
        default_factory=list,
        metadata={
            "name": "MultiValue",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    attribute_ref_type: List[AttributeRefType] = field(
        default_factory=list,
        metadata={
            "name": "AttributeRefType",
            "type": "Element",
            "sequence": 2,
        },
    )
    class_value: List[Class] = field(
        default_factory=list,
        metadata={
            "name": "Class",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    attr_or_param: List[AttrOrParam] = field(
        default_factory=list,
        metadata={
            "name": "AttrOrParam",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    transfer_element: List[TransferElement] = field(
        default_factory=list,
        metadata={
            "name": "TransferElement",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    ili1_transfer_element: List[Ili1TransferElement] = field(
        default_factory=list,
        metadata={
            "name": "Ili1TransferElement",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    sub_model: List[SubModel] = field(
        default_factory=list,
        metadata={
            "name": "SubModel",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    data_unit: List[DataUnit] = field(
        default_factory=list,
        metadata={
            "name": "DataUnit",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    allowed_in_basket: List[AllowedInBasket] = field(
        default_factory=list,
        metadata={
            "name": "AllowedInBasket",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 2,
        },
    )
    meta_basket_def: List[MetaBasketDef] = field(
        default_factory=list,
        metadata={
            "name": "MetaBasketDef",
            "type": "Element",
            "sequence": 2,
        },
    )
    meta_object_def: List[MetaObjectDef] = field(
        default_factory=list,
        metadata={
            "name": "MetaObjectDef",
            "type": "Element",
            "sequence": 2,
        },
    )
    formatted_type: List[FormattedType] = field(
        default_factory=list,
        metadata={
            "name": "FormattedType",
            "type": "Element",
            "sequence": 2,
        },
    )
    line_type: List[LineType] = field(
        default_factory=list,
        metadata={
            "name": "LineType",
            "type": "Element",
            "sequence": 2,
        },
    )
    simple_constraint: List[SimpleConstraint] = field(
        default_factory=list,
        metadata={
            "name": "SimpleConstraint",
            "type": "Element",
            "sequence": 1,
        },
    )
    class_restriction: List[ClassRestriction] = field(
        default_factory=list,
        metadata={
            "name": "ClassRestriction",
            "type": "Element",
            "sequence": 1,
        },
    )
    reference_type: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceType",
            "type": "Element",
            "sequence": 1,
        },
    )
    dependency: List[Dependency] = field(
        default_factory=list,
        metadata={
            "name": "Dependency",
            "type": "Element",
            "sequence": 1,
        },
    )


@dataclass
class Datasection:
    class Meta:
        name = "datasection"
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    model_data: List[ModelData] = field(
        default_factory=list,
        metadata={
            "name": "ModelData",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_occurs": 1,
        },
    )


@dataclass
class Transfer:
    class Meta:
        name = "transfer"
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    headersection: Optional[Headersection] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    datasection: Optional[Datasection] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
