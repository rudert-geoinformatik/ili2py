from dataclasses import dataclass, field
from typing import Optional, Union, List

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.actual_argument_type_formal_argument import (
    ActualArgumentTypeFormalArgument,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.actual_argument_type_object_classes import (
    ActualArgumentTypeObjectClasses,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.attribute_const import AttributeConst
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_const import ClassConst
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.constant import Constant
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.enum_assignment_type_max_enum_value import (
    EnumAssignmentTypeMaxEnumValue,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.enum_assignment_type_min_enum_value import (
    EnumAssignmentTypeMinEnumValue,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.enum_mapping_type_enum_value import EnumMappingTypeEnumValue
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.expression import Expression
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.expression_type import ExpressionType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.factor import Factor
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.factor_type import FactorType
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.function_call_type_function import FunctionCallTypeFunction
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.path_or_insp_factor import PathOrInspFactor
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.runtime_param_ref import RuntimeParamRef
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.unit_function import UnitFunction
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.unit_ref import UnitRef

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ActualArgumentType:
    formal_argument: Optional[ActualArgumentTypeFormalArgument] = field(
        default=None,
        metadata={
            "name": "FormalArgument",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    expression: Optional["ActualArgumentTypeExpression"] = field(
        default=None,
        metadata={
            "name": "Expression",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    object_classes: list[ActualArgumentTypeObjectClasses] = field(
        default_factory=list,
        metadata={
            "name": "ObjectClasses",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )


@dataclass
class CompoundExprType(ExpressionType):
    operation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    sub_expressions: list["CompoundExprTypeSubExpressions"] = field(
        default_factory=list,
        metadata={
            "name": "SubExpressions",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )


@dataclass
class EnumAssignmentType:
    value_to_assign: Optional["EnumAssignmentTypeValueToAssign"] = field(
        default=None,
        metadata={
            "name": "ValueToAssign",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    min_enum_value: Optional[EnumAssignmentTypeMinEnumValue] = field(
        default=None,
        metadata={
            "name": "MinEnumValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    max_enum_value: Optional[EnumAssignmentTypeMaxEnumValue] = field(
        default=None,
        metadata={
            "name": "MaxEnumValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )


@dataclass
class UnaryExprType(ExpressionType):
    operation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    sub_expression: Optional["UnaryExprTypeSubExpression"] = field(
        default=None,
        metadata={
            "name": "SubExpression",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )


@dataclass
class ActualArgument(ActualArgumentType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class CompoundExpr(CompoundExprType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class EnumAssignment(EnumAssignmentType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class UnaryExpr(UnaryExprType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class EnumMappingTypeCases:
    class Meta:
        global_type = False

    enum_assignment: Optional[EnumAssignment] = field(
        default=None,
        metadata={
            "name": "EnumAssignment",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class FunctionCallTypeArguments:
    class Meta:
        global_type = False

    actual_argument: Optional[ActualArgument] = field(
        default=None,
        metadata={
            "name": "ActualArgument",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class EnumMappingType(FactorType):
    enum_value: Optional[EnumMappingTypeEnumValue] = field(
        default=None,
        metadata={
            "name": "EnumValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    cases: list[EnumMappingTypeCases] = field(
        default_factory=list,
        metadata={
            "name": "Cases",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )


@dataclass
class FunctionCallType(FactorType):
    function: Optional[FunctionCallTypeFunction] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    arguments: list[FunctionCallTypeArguments] = field(
        default_factory=list,
        metadata={
            "name": "Arguments",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )


@dataclass
class EnumMapping(EnumMappingType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class FunctionCall(FunctionCallType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ActualArgumentTypeExpression:
    class Meta:
        global_type = False

    choice: Optional[
        Union[
            UnitFunction,
            UnitRef,
            AttributeConst,
            ClassConst,
            Constant,
            RuntimeParamRef,
            FunctionCall,
            EnumMapping,
            PathOrInspFactor,
            Factor,
            CompoundExpr,
            UnaryExpr,
            Expression,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UnitFunction",
                    "type": UnitFunction,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "UnitRef",
                    "type": UnitRef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "AttributeConst",
                    "type": AttributeConst,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ClassConst",
                    "type": ClassConst,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Constant",
                    "type": Constant,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "RuntimeParamRef",
                    "type": RuntimeParamRef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "FunctionCall",
                    "type": FunctionCall,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "EnumMapping",
                    "type": EnumMapping,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "PathOrInspFactor",
                    "type": PathOrInspFactor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Factor",
                    "type": Factor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "CompoundExpr",
                    "type": CompoundExpr,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "UnaryExpr",
                    "type": UnaryExpr,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Expression",
                    "type": Expression,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
            ),
        },
    )


@dataclass
class CompoundExprTypeSubExpressions:
    class Meta:
        global_type = False

    choice: Optional[List[
        Union[
            UnitFunction,
            UnitRef,
            AttributeConst,
            ClassConst,
            Constant,
            RuntimeParamRef,
            FunctionCall,
            EnumMapping,
            PathOrInspFactor,
            Factor,
            CompoundExpr,
            UnaryExpr,
            Expression,
        ]
    ]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UnitFunction",
                    "type": UnitFunction,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "UnitRef",
                    "type": UnitRef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "AttributeConst",
                    "type": AttributeConst,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ClassConst",
                    "type": ClassConst,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Constant",
                    "type": Constant,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "RuntimeParamRef",
                    "type": RuntimeParamRef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "FunctionCall",
                    "type": FunctionCall,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "EnumMapping",
                    "type": EnumMapping,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "PathOrInspFactor",
                    "type": PathOrInspFactor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Factor",
                    "type": Factor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "CompoundExpr",
                    "type": CompoundExpr,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "UnaryExpr",
                    "type": UnaryExpr,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Expression",
                    "type": Expression,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
            ),
        },
    )


@dataclass
class EnumAssignmentTypeValueToAssign:
    class Meta:
        global_type = False

    choice: Optional[
        Union[
            UnitFunction,
            UnitRef,
            AttributeConst,
            ClassConst,
            Constant,
            RuntimeParamRef,
            FunctionCall,
            EnumMapping,
            PathOrInspFactor,
            Factor,
            CompoundExpr,
            UnaryExpr,
            Expression,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UnitFunction",
                    "type": UnitFunction,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "UnitRef",
                    "type": UnitRef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "AttributeConst",
                    "type": AttributeConst,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ClassConst",
                    "type": ClassConst,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Constant",
                    "type": Constant,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "RuntimeParamRef",
                    "type": RuntimeParamRef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "FunctionCall",
                    "type": FunctionCall,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "EnumMapping",
                    "type": EnumMapping,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "PathOrInspFactor",
                    "type": PathOrInspFactor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Factor",
                    "type": Factor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "CompoundExpr",
                    "type": CompoundExpr,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "UnaryExpr",
                    "type": UnaryExpr,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Expression",
                    "type": Expression,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
            ),
        },
    )


@dataclass
class UnaryExprTypeSubExpression:
    class Meta:
        global_type = False

    choice: Optional[
        Union[
            UnitFunction,
            UnitRef,
            AttributeConst,
            ClassConst,
            Constant,
            RuntimeParamRef,
            FunctionCall,
            EnumMapping,
            PathOrInspFactor,
            Factor,
            CompoundExpr,
            UnaryExpr,
            Expression,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UnitFunction",
                    "type": UnitFunction,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "UnitRef",
                    "type": UnitRef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "AttributeConst",
                    "type": AttributeConst,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "ClassConst",
                    "type": ClassConst,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Constant",
                    "type": Constant,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "RuntimeParamRef",
                    "type": RuntimeParamRef,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "FunctionCall",
                    "type": FunctionCall,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "EnumMapping",
                    "type": EnumMapping,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "PathOrInspFactor",
                    "type": PathOrInspFactor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Factor",
                    "type": Factor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "CompoundExpr",
                    "type": CompoundExpr,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "UnaryExpr",
                    "type": UnaryExpr,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
                {
                    "name": "Expression",
                    "type": Expression,
                    "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                },
            ),
        },
    )
