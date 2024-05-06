from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime


@dataclass
class IlisMeta16AttrParent:
    class Meta:
        name = "IlisMeta16:AttrParent"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )
    ili_order_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "ili:order_pos",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Axis:
    class Meta:
        name = "IlisMeta16:Axis"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )
    ili_order_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "ili:order_pos",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16BaseType:
    class Meta:
        name = "IlisMeta16:BaseType"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Crt:
    class Meta:
        name = "IlisMeta16:CRT"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16ClassInBasket:
    class Meta:
        name = "IlisMeta16:ClassInBasket"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Constant:
    class Meta:
        name = "IlisMeta16:Constant"

    ilis_meta16_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Value",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16ElementInPackage:
    class Meta:
        name = "IlisMeta16:ElementInPackage"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Function:
    class Meta:
        name = "IlisMeta16:Function"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )
    ili_order_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "ili:order_pos",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Ili1RefAttr:
    class Meta:
        name = "IlisMeta16:Ili1RefAttr"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )
    ili_order_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "ili:order_pos",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Ili1TransferClass:
    class Meta:
        name = "IlisMeta16:Ili1TransferClass"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Lftparent:
    class Meta:
        name = "IlisMeta16:LFTParent"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Ltparent:
    class Meta:
        name = "IlisMeta16:LTParent"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16MetaDataTopic:
    class Meta:
        name = "IlisMeta16:MetaDataTopic"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Model:
    class Meta:
        name = "IlisMeta16:Model"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_ili_version: Optional[float] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:iliVersion",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_contracted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Contracted",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Kind",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Language",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_at: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:At",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Version",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Multiplicity:
    class Meta:
        name = "IlisMeta16:Multiplicity"

    ilis_meta16_min: Optional[int] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Min",
            "type": "Element",
        },
    )
    ilis_meta16_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Max",
            "type": "Element",
        },
    )
    ilis_meta16_multiplicity: Optional["IlisMeta16Multiplicity"] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Multiplicity",
            "type": "Element",
        },
    )


@dataclass
class IlisMeta16Of:
    class Meta:
        name = "IlisMeta16:Of"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16OfDataUnit:
    class Meta:
        name = "IlisMeta16:OfDataUnit"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16ParamParent:
    class Meta:
        name = "IlisMeta16:ParamParent"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )
    ili_order_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "ili:order_pos",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16ParentNode:
    class Meta:
        name = "IlisMeta16:ParentNode"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )
    ili_order_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "ili:order_pos",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16ResultType:
    class Meta:
        name = "IlisMeta16:ResultType"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Struct:
    class Meta:
        name = "IlisMeta16:Struct"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Structure:
    class Meta:
        name = "IlisMeta16:Structure"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Super:
    class Meta:
        name = "IlisMeta16:Super"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16TransferClass:
    class Meta:
        name = "IlisMeta16:TransferClass"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Type:
    class Meta:
        name = "IlisMeta16:Type"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IlisMeta16AllowedInBasket:
    class Meta:
        name = "IlisMeta16:AllowedInBasket"

    ilis_meta16_of_data_unit: Optional[IlisMeta16OfDataUnit] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:OfDataUnit",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_class_in_basket: Optional[IlisMeta16ClassInBasket] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:ClassInBasket",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16AnyOidtype:
    class Meta:
        name = "IlisMeta16:AnyOIDType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
                "required": True,
            },
        )
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Argument:
    class Meta:
        name = "IlisMeta16:Argument"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Kind",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_function: Optional[IlisMeta16Function] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Function",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_type: Optional[IlisMeta16Type] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Type",
            "type": "Element",
        },
    )


@dataclass
class IlisMeta16AttrOrParam:
    class Meta:
        name = "IlisMeta16:AttrOrParam"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_subdivision_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:SubdivisionKind",
            "type": "Element",
        },
    )
    ilis_meta16_transient: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Transient",
            "type": "Element",
        },
    )
    ilis_meta16_attr_parent: Optional[IlisMeta16AttrParent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:AttrParent",
            "type": "Element",
        },
    )
    ilis_meta16_super: Optional[IlisMeta16Super] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Super",
            "type": "Element",
        },
    )
    ilis_meta16_param_parent: Optional[IlisMeta16ParamParent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:ParamParent",
            "type": "Element",
        },
    )
    ilis_meta16_type: Optional[IlisMeta16Type] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16AttributeRefType:
    class Meta:
        name = "IlisMeta16:AttributeRefType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_lftparent: Optional[IlisMeta16Lftparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LFTParent",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_of: Optional[IlisMeta16Of] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Of",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16BaseClass:
    class Meta:
        name = "IlisMeta16:BaseClass"

    ilis_meta16_crt: Optional[IlisMeta16Crt] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:CRT",
            "type": "Element",
        },
    )
    ilis_meta16_base_class: Optional["IlisMeta16BaseClass"] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:BaseClass",
            "type": "Element",
        },
    )
    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
        },
    )


@dataclass
class IlisMeta16BooleanType:
    class Meta:
        name = "IlisMeta16:BooleanType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_lftparent: Optional[IlisMeta16Lftparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LFTParent",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Class:
    class Meta:
        name = "IlisMeta16:Class"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
            },
        )
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
        },
    )
    ilis_meta16_super: Optional[IlisMeta16Super] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Super",
            "type": "Element",
        },
    )
    ilis_meta16_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Kind",
            "type": "Element",
        },
    )
    ilis_meta16_embedded_role_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:EmbeddedRoleTransfer",
            "type": "Element",
        },
    )
    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
        },
    )


@dataclass
class IlisMeta16ClassRefType:
    class Meta:
        name = "IlisMeta16:ClassRefType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_ltparent: Optional[IlisMeta16Ltparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LTParent",
            "type": "Element",
        },
    )
    ilis_meta16_lftparent: Optional[IlisMeta16Lftparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LFTParent",
            "type": "Element",
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16CoordType:
    class Meta:
        name = "IlisMeta16:CoordType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
            },
        )
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
        },
    )
    ilis_meta16_multi: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Multi",
            "type": "Element",
        },
    )
    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
        },
    )


@dataclass
class IlisMeta16DataUnit:
    class Meta:
        name = "IlisMeta16:DataUnit"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
                "required": True,
            },
        )
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_view_unit: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:ViewUnit",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_data_unit_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:DataUnitName",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16EnumType:
    class Meta:
        name = "IlisMeta16:EnumType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
            },
        )
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
        },
    )
    ilis_meta16_order: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Order",
            "type": "Element",
        },
    )
    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
        },
    )
    ili_order_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "ili:order_pos",
            "type": "Attribute",
        },
    )


@dataclass
class IlisMeta16FormattedType:
    class Meta:
        name = "IlisMeta16:FormattedType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
                "required": True,
            },
        )
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_super: Optional[IlisMeta16Super] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Super",
            "type": "Element",
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_min: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Min",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_max: Optional[Union[XmlDateTime, XmlDate, XmlTime]] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Max",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Format",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_struct: Optional[IlisMeta16Struct] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Struct",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16FunctionDef:
    class Meta:
        name = "IlisMeta16:FunctionDef"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
                "required": True,
            },
        )
    )
    ilis_meta16_result_type: Optional[IlisMeta16ResultType] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:ResultType",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Ili1TransferElement:
    class Meta:
        name = "IlisMeta16:Ili1TransferElement"

    ilis_meta16_ili1_transfer_class: Optional[IlisMeta16Ili1TransferClass] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:Ili1TransferClass",
                "type": "Element",
                "required": True,
            },
        )
    )
    ilis_meta16_ili1_ref_attr: Optional[IlisMeta16Ili1RefAttr] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Ili1RefAttr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16LineForm:
    class Meta:
        name = "IlisMeta16:LineForm"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
                "required": True,
            },
        )
    )
    ilis_meta16_structure: Optional[IlisMeta16Structure] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Structure",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16LineType:
    class Meta:
        name = "IlisMeta16:LineType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_ltparent: Optional[IlisMeta16Ltparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LTParent",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Kind",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_multi: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Multi",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16MetaBasketDef:
    class Meta:
        name = "IlisMeta16:MetaBasketDef"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
            },
        )
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
        },
    )
    ilis_meta16_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Kind",
            "type": "Element",
        },
    )
    ilis_meta16_meta_data_topic: Optional[IlisMeta16MetaDataTopic] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:MetaDataTopic",
            "type": "Element",
        },
    )
    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
        },
    )


@dataclass
class IlisMeta16MultiValue:
    class Meta:
        name = "IlisMeta16:MultiValue"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_ltparent: Optional[IlisMeta16Ltparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LTParent",
            "type": "Element",
        },
    )
    ilis_meta16_lftparent: Optional[IlisMeta16Lftparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LFTParent",
            "type": "Element",
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_base_type: Optional[IlisMeta16BaseType] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:BaseType",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_ordered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Ordered",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_multiplicity: Optional[IlisMeta16Multiplicity] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Multiplicity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16ObjectType:
    class Meta:
        name = "IlisMeta16:ObjectType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_lftparent: Optional[IlisMeta16Lftparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LFTParent",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_multiple: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Multiple",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16SubExpressions:
    class Meta:
        name = "IlisMeta16:SubExpressions"

    ilis_meta16_constant: Optional[IlisMeta16Constant] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Constant",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16SubModel:
    class Meta:
        name = "IlisMeta16:SubModel"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
                "required": True,
            },
        )
    )


@dataclass
class IlisMeta16TextType:
    class Meta:
        name = "IlisMeta16:TextType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
            },
        )
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_ltparent: Optional[IlisMeta16Ltparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LTParent",
            "type": "Element",
        },
    )
    ilis_meta16_lftparent: Optional[IlisMeta16Lftparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LFTParent",
            "type": "Element",
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Kind",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_max_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:MaxLength",
            "type": "Element",
        },
    )


@dataclass
class IlisMeta16TransferElement:
    class Meta:
        name = "IlisMeta16:TransferElement"

    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
        },
    )
    ili_order_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "ili:order_pos",
            "type": "Attribute",
        },
    )
    ilis_meta16_transfer_class: Optional[IlisMeta16TransferClass] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:TransferClass",
            "type": "Element",
        },
    )
    ilis_meta16_transfer_element: Optional["IlisMeta16TransferElement"] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:TransferElement",
                "type": "Element",
            },
        )
    )


@dataclass
class IlisMeta16AxisSpec:
    class Meta:
        name = "IlisMeta16:AxisSpec"

    ilis_meta16_coord_type: Optional[IlisMeta16CoordType] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:CoordType",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_axis: Optional[IlisMeta16Axis] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Axis",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16CompoundExpr:
    class Meta:
        name = "IlisMeta16:CompoundExpr"

    ilis_meta16_operation: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Operation",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_sub_expressions: Optional[IlisMeta16SubExpressions] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:SubExpressions",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16EnumNode:
    class Meta:
        name = "IlisMeta16:EnumNode"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[Union[str, bool]] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_parent_node: Optional[IlisMeta16ParentNode] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:ParentNode",
            "type": "Element",
        },
    )
    ilis_meta16_enum_type: Optional[IlisMeta16EnumType] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:EnumType",
            "type": "Element",
        },
    )


@dataclass
class IlisMeta16MetaObjectDef:
    class Meta:
        name = "IlisMeta16:MetaObjectDef"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_is_ref_system: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:IsRefSystem",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_class: Optional[IlisMeta16Class] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Class",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_meta_basket_def: Optional[IlisMeta16MetaBasketDef] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:MetaBasketDef",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Definition:
    class Meta:
        name = "IlisMeta16:Definition"

    ilis_meta16_compound_expr: Optional[IlisMeta16CompoundExpr] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:CompoundExpr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IlisMeta16Unit:
    class Meta:
        name = "IlisMeta16:Unit"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
            },
        )
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
        },
    )
    ilis_meta16_super: Optional[IlisMeta16Super] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Super",
            "type": "Element",
        },
    )
    ilis_meta16_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Kind",
            "type": "Element",
        },
    )
    ilis_meta16_definition: Optional[IlisMeta16Definition] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Definition",
            "type": "Element",
        },
    )
    ili_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:ref",
            "type": "Attribute",
        },
    )


@dataclass
class IlisMeta16NumType:
    class Meta:
        name = "IlisMeta16:NumType"

    ili_tid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:tid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Name",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_element_in_package: Optional[IlisMeta16ElementInPackage] = (
        field(
            default=None,
            metadata={
                "name": "IlisMeta16:ElementInPackage",
                "type": "Element",
            },
        )
    )
    ilis_meta16_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Abstract",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Generic",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Final",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_super: Optional[IlisMeta16Super] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Super",
            "type": "Element",
        },
    )
    ilis_meta16_ltparent: Optional[IlisMeta16Ltparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LTParent",
            "type": "Element",
        },
    )
    ilis_meta16_lftparent: Optional[IlisMeta16Lftparent] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:LFTParent",
            "type": "Element",
        },
    )
    ilis_meta16_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Mandatory",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_min: Optional[Union[Decimal, int]] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Min",
            "type": "Element",
        },
    )
    ilis_meta16_max: Optional[Union[float, int]] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Max",
            "type": "Element",
        },
    )
    ilis_meta16_circular: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Circular",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_unit: Optional[IlisMeta16Unit] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Unit",
            "type": "Element",
        },
    )


@dataclass
class IlisMeta16ModelData:
    class Meta:
        name = "IlisMeta16:ModelData"

    ili_bid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili:bid",
            "type": "Attribute",
            "required": True,
        },
    )
    ilis_meta16_model: Optional[IlisMeta16Model] = field(
        default=None,
        metadata={
            "name": "IlisMeta16:Model",
            "type": "Element",
            "required": True,
        },
    )
    ilis_meta16_line_form: List[IlisMeta16LineForm] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:LineForm",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    ilis_meta16_unit: List[IlisMeta16Unit] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:Unit",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_text_type: List[IlisMeta16TextType] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:TextType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_enum_node: List[IlisMeta16EnumNode] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:EnumNode",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_enum_type: List[IlisMeta16EnumType] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:EnumType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_any_oidtype: List[IlisMeta16AnyOidtype] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:AnyOIDType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_num_type: List[IlisMeta16NumType] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:NumType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_axis_spec: List[IlisMeta16AxisSpec] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:AxisSpec",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_coord_type: List[IlisMeta16CoordType] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:CoordType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_base_class: List[IlisMeta16BaseClass] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:BaseClass",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_class_ref_type: List[IlisMeta16ClassRefType] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:ClassRefType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_object_type: List[IlisMeta16ObjectType] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:ObjectType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_argument: List[IlisMeta16Argument] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:Argument",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_function_def: List[IlisMeta16FunctionDef] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:FunctionDef",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_boolean_type: List[IlisMeta16BooleanType] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:BooleanType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_multi_value: List[IlisMeta16MultiValue] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:MultiValue",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_attribute_ref_type: List[IlisMeta16AttributeRefType] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:AttributeRefType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_class: List[IlisMeta16Class] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:Class",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_attr_or_param: List[IlisMeta16AttrOrParam] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:AttrOrParam",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_transfer_element: List[IlisMeta16TransferElement] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:TransferElement",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_ili1_transfer_element: List[IlisMeta16Ili1TransferElement] = (
        field(
            default_factory=list,
            metadata={
                "name": "IlisMeta16:Ili1TransferElement",
                "type": "Element",
                "min_occurs": 1,
                "sequence": 1,
            },
        )
    )
    ilis_meta16_sub_model: List[IlisMeta16SubModel] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:SubModel",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_data_unit: List[IlisMeta16DataUnit] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:DataUnit",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_allowed_in_basket: List[IlisMeta16AllowedInBasket] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:AllowedInBasket",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_meta_basket_def: List[IlisMeta16MetaBasketDef] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:MetaBasketDef",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_meta_object_def: List[IlisMeta16MetaObjectDef] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:MetaObjectDef",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_formatted_type: List[IlisMeta16FormattedType] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:FormattedType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ilis_meta16_line_type: List[IlisMeta16LineType] = field(
        default_factory=list,
        metadata={
            "name": "IlisMeta16:LineType",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
