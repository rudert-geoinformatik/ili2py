from dataclasses import dataclass, field
from typing import Optional, List

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element import MetaAttributeElement
from ili2py.interfaces.interlis.interlis_24.ilismeta16.shared import imd_namespace_map
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
class ModelDataType:

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
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    AttrOrParam: List["AttrOrParam"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    TextType: Optional[List["TextType"]] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    EnumNode: List["EnumNode"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    EnumType: List["EnumType"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    NumType: Optional[List["NumType"]] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    AxisSpec: List["AxisSpec"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    CoordType: List["CoordType"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    BaseClass: List["BaseClass"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    ObjectType: List["ObjectType"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    ClassRefType: List["ClassRefType"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    MultiValue: Optional[List["MultiValue"]] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    BooleanType: List["BooleanType"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    FormattedType: List["FormattedType"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    LinesForm: List["LinesForm"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    LineType: List["LineType"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    LineForm: List["LineForm"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    Role: List["Role"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    SimpleConstraint: List["SimpleConstraint"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    ReferenceType: List["ReferenceType"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    BlackboxType: Optional[List["BlackboxType"]] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    Unit: List["Unit"] = field(
        default_factory=list,
        metadata={
            "namespace": imd_namespace_map["IlisMeta16"]
        }
    )
    # TODO: Add Views
