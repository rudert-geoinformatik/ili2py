from dataclasses import dataclass, field
from typing import Optional, Union

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.actual_argument_type import (
    CompoundExpr,
    EnumMapping,
    FunctionCall,
    UnaryExpr,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.attribute_const import AttributeConst
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_const import ClassConst
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.constant import Constant
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.expression import Expression
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.factor import Factor
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.path_or_insp_factor import PathOrInspFactor
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.runtime_param_ref import RuntimeParamRef
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.unit_function import UnitFunction
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.unit_ref import UnitRef

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class GraphicTypeWhere:
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
