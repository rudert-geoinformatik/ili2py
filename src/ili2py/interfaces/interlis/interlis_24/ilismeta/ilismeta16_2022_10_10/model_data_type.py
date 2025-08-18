from dataclasses import dataclass, field
from typing import Optional, Union

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.allowed_in_basket import AllowedInBasket
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.any_oidtype import AnyOidtype
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.aref_restriction import ArefRestriction
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.argument import Argument
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.assoc_acc import AssocAcc
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.attr_or_param import AttrOrParam
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.attribute_ref_type import AttributeRefType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.axis_spec import AxisSpec
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.base_class import BaseClass
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.blackbox_type import BlackboxType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.boolean_type import BooleanType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_mod import Class
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_ref_type import ClassRefType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_related_type import ClassRelatedType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_restriction import ClassRestriction
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.concrete_for_generic import ConcreteForGeneric
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.constraint import Constraint
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.context import Context
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.coord_type import CoordType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.data_unit import DataUnit
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.dependency import Dependency
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.domain_type import DomainType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.drawing_rule import DrawingRule
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.enum_node import EnumNode
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.enum_tree_value_type import EnumTreeValueType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.enum_type import EnumType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.existence_constraint import ExistenceConstraint
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.explicit_assoc_access import ExplicitAssocAccess
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.extendable_me import ExtendableMe
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.formatted_type import FormattedType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.function_def import FunctionDef
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.graphic import Graphic
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.ili1_transfer_element import Ili1TransferElement
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.import_mod import Import
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.line_form import LineForm
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.line_type import LineType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.lines_form import LinesForm
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_attribute import MetaAttribute
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_basket_def import MetaBasketDef
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_element import MetaElement
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.meta_object_def import MetaObjectDef
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.model import Model
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.multi_value import MultiValue
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.num_type import NumType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.object_type import ObjectType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.package import Package
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.reference_type import ReferenceType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.renamed_base_view import RenamedBaseView
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.role import Role
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.set_constraint import SetConstraint
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.simple_constraint import SimpleConstraint
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.sub_model import SubModel
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.text_type import TextType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.transfer_element import TransferElement
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_mod import Type
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_related_type import TypeRelatedType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.type_restriction import TypeRestriction
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.unique_constraint import UniqueConstraint
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.unit import Unit
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.view import View

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ModelDataType:
    choice: list[
        Union[
            LineForm,
            Argument,
            FunctionDef,
            MetaObjectDef,
            Context,
            SetConstraint,
            UniqueConstraint,
            ExistenceConstraint,
            SimpleConstraint,
            Constraint,
            SubModel,
            Model,
            Package,
            DrawingRule,
            Graphic,
            RenamedBaseView,
            EnumNode,
            MetaBasketDef,
            Unit,
            DataUnit,
            ExplicitAssocAccess,
            AttrOrParam,
            View,
            Class,
            LineType,
            EnumTreeValueType,
            EnumType,
            AttributeRefType,
            AnyOidtype,
            CoordType,
            FormattedType,
            NumType,
            BlackboxType,
            TextType,
            BooleanType,
            ObjectType,
            Role,
            ReferenceType,
            ClassRefType,
            ClassRelatedType,
            MultiValue,
            TypeRelatedType,
            DomainType,
            Type,
            ExtendableMe,
            MetaElement,
            MetaAttribute,
            Import,
            TypeRestriction,
            BaseClass,
            ClassRestriction,
            AssocAcc,
            TransferElement,
            Ili1TransferElement,
            Dependency,
            AllowedInBasket,
            ConcreteForGeneric,
            AxisSpec,
            ArefRestriction,
            LinesForm,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LineForm",
                    "type": LineForm,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Argument",
                    "type": Argument,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "FunctionDef",
                    "type": FunctionDef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "MetaObjectDef",
                    "type": MetaObjectDef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Context",
                    "type": Context,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "SetConstraint",
                    "type": SetConstraint,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "UniqueConstraint",
                    "type": UniqueConstraint,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ExistenceConstraint",
                    "type": ExistenceConstraint,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "SimpleConstraint",
                    "type": SimpleConstraint,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Constraint",
                    "type": Constraint,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "SubModel",
                    "type": SubModel,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Model",
                    "type": Model,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Package",
                    "type": Package,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "DrawingRule",
                    "type": DrawingRule,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Graphic",
                    "type": Graphic,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "RenamedBaseView",
                    "type": RenamedBaseView,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "EnumNode",
                    "type": EnumNode,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "MetaBasketDef",
                    "type": MetaBasketDef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Unit",
                    "type": Unit,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "DataUnit",
                    "type": DataUnit,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ExplicitAssocAccess",
                    "type": ExplicitAssocAccess,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "AttrOrParam",
                    "type": AttrOrParam,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "View",
                    "type": View,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Class",
                    "type": Class,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "LineType",
                    "type": LineType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "EnumTreeValueType",
                    "type": EnumTreeValueType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "EnumType",
                    "type": EnumType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "AttributeRefType",
                    "type": AttributeRefType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "AnyOIDType",
                    "type": AnyOidtype,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "CoordType",
                    "type": CoordType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "FormattedType",
                    "type": FormattedType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "NumType",
                    "type": NumType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "BlackboxType",
                    "type": BlackboxType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "TextType",
                    "type": TextType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "BooleanType",
                    "type": BooleanType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ObjectType",
                    "type": ObjectType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Role",
                    "type": Role,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ReferenceType",
                    "type": ReferenceType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ClassRefType",
                    "type": ClassRefType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ClassRelatedType",
                    "type": ClassRelatedType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "MultiValue",
                    "type": MultiValue,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "TypeRelatedType",
                    "type": TypeRelatedType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "DomainType",
                    "type": DomainType,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Type",
                    "type": Type,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ExtendableME",
                    "type": ExtendableMe,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "MetaElement",
                    "type": MetaElement,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "MetaAttribute",
                    "type": MetaAttribute,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Import",
                    "type": Import,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "TypeRestriction",
                    "type": TypeRestriction,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "BaseClass",
                    "type": BaseClass,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ClassRestriction",
                    "type": ClassRestriction,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "AssocAcc",
                    "type": AssocAcc,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "TransferElement",
                    "type": TransferElement,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Ili1TransferElement",
                    "type": Ili1TransferElement,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Dependency",
                    "type": Dependency,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "AllowedInBasket",
                    "type": AllowedInBasket,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ConcreteForGeneric",
                    "type": ConcreteForGeneric,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "AxisSpec",
                    "type": AxisSpec,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ARefRestriction",
                    "type": ArefRestriction,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "LinesForm",
                    "type": LinesForm,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
            ),
        },
    )
    bid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )
    consistency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
