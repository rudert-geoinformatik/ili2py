from dataclasses import dataclass, field
from typing import Optional, List

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element import MetaAttributeElement
from ili2py.interfaces.interlis.interlis_24.ilismeta16.shared import IMD_META_BASE, imd_namespace_map
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.package.package import Model, SubModel
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me import DataUnit, Unit
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class import Class, BaseClass
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me import AttrOrParam, EnumNode
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type import \
    TextType, EnumType, NumType, BooleanType, FormattedType, LineType, AxisSpec, CoordType, MultiValue, BlackboxType
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type import \
    ObjectType, ClassRefType, ReferenceType
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.role import Role
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.line_form import LineForm, LinesForm
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.constraints import SimpleConstraint


@dataclass
class ModelData:
    class Meta(IMD_META_BASE):
        name = "ModelData"

    bid: str = field(
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["ili"]
        }
    )
    Model: "Model" = field(
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    # TODO: Keep an eye on requested list length (as of meta model docs list of sub_model has to
    #  be at least 1)
    SubModel: List["SubModel"] = field(
        default_factory=list
    )
    DataUnit: List["DataUnit"] = None
    MetaAttribute: Optional[List[MetaAttributeElement]] = field(
        default_factory=list
    )
    consistency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["ili"],
        },
    )
    Class: Optional[List["Class"]] = field(
        default_factory=list
    )
    AttrOrParam: List["AttrOrParam"] = field(
        default_factory=list
    )
    TextType: Optional[List["TextType"]] = field(
        default_factory=list
    )
    EnumNode: List["EnumNode"] = field(
        default_factory=list
    )
    EnumType: List["EnumType"] = field(
        default_factory=list
    )
    NumType: Optional[List["NumType"]] = field(
        default_factory=list
    )
    AxisSpec: List["AxisSpec"] = field(
        default_factory=list
    )
    CoordType: List["CoordType"] = field(
        default_factory=list
    )
    BaseClass: List["BaseClass"] = field(
        default_factory=list
    )
    ObjectType: List["ObjectType"] = field(
        default_factory=list
    )
    ClassRefType: List["ClassRefType"] = field(
        default_factory=list
    )
    MultiValue: Optional[List["MultiValue"]] = field(
        default_factory=list
    )
    BooleanType: List["BooleanType"] = field(
        default_factory=list
    )
    FormattedType: List["FormattedType"] = field(
        default_factory=list
    )
    LinesForm: List["LinesForm"] = field(
        default_factory=list
    )
    LineType: List["LineType"] = field(
        default_factory=list
    )
    LineForm: List["LineForm"] = field(
        default_factory=list
    )
    Role: List["Role"] = field(
        default_factory=list
    )
    SimpleConstraint: List["SimpleConstraint"] = field(
        default_factory=list
    )
    ReferenceType: List["ReferenceType"] = field(
        default_factory=list
    )
    BlackboxType: Optional[List["BlackboxType"]] = field(
        default_factory=list
    )
    Unit: List["Unit"] = field(
        default_factory=list
    )
    # TODO: Add Views
