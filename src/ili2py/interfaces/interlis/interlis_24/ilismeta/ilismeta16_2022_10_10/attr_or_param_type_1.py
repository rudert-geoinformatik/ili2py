from dataclasses import dataclass, field
from typing import Optional

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.attr_or_param_type_attr_parent import AttrOrParamTypeAttrParent
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.attr_or_param_type_derivates import AttrOrParamTypeDerivates
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.attr_or_param_type_param_parent import AttrOrParamTypeParamParent
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_metype import ExtendableMetype

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AttrOrParamType1(ExtendableMetype):
    class Meta:
        name = "AttrOrParamType"

    subdivision_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubdivisionKind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    transient: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Transient",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    derivates: list[AttrOrParamTypeDerivates] = field(
        default_factory=list,
        metadata={
            "name": "Derivates",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    attr_parent: Optional[AttrOrParamTypeAttrParent] = field(
        default=None,
        metadata={
            "name": "AttrParent",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    param_parent: Optional[AttrOrParamTypeParamParent] = field(
        default=None,
        metadata={
            "name": "ParamParent",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_value: Optional["AttrOrParamTypeType2"] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class AttrOrParamTypeType2:
    class Meta:
        global_type = False

    attr_or_param_type: Optional[AttrOrParamType1] = field(
        default=None,
        metadata={
            "name": "AttrOrParamType",
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
