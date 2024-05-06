from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ArefOfType:
    class Meta:
        name = "ARefOfType"


@dataclass
class AllowedInBasketType:
    of_data_unit: Optional["AllowedInBasketType.OfDataUnit"] = field(
        default=None,
        metadata={
            "name": "OfDataUnit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    class_in_basket: Optional["AllowedInBasketType.ClassInBasket"] = field(
        default=None,
        metadata={
            "name": "ClassInBasket",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class OfDataUnit:
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
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ArgumentTypeType:
    pass


@dataclass
class AssocAccOriginType:
    pass


@dataclass
class AssocAccTargetType:
    pass


@dataclass
class AssocRoleType:
    pass


@dataclass
class AttrOrParamTypeType:
    pass


@dataclass
class AxisSpecType:
    coord_type: Optional["AxisSpecType.CoordType"] = field(
        default=None,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    axis: Optional["AxisSpecType.Axis"] = field(
        default=None,
        metadata={
            "name": "Axis",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class CoordType:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class Axis:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class BaseClassType:
    crt: Optional["BaseClassType.Crt"] = field(
        default=None,
        metadata={
            "name": "CRT",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    base_class: Optional["BaseClassType.BaseClass"] = field(
        default=None,
        metadata={
            "name": "BaseClass",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class Crt:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class BaseClass:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class BaseTypeType:
    pass


@dataclass
class BaseViewDefType:
    pass


@dataclass
class BaseViewRefType:
    pass


@dataclass
class ClassAttrType:
    pass


@dataclass
class ClassConstraintType:
    pass


@dataclass
class ClassParamType:
    pass


@dataclass
class ClassRefType1:
    class Meta:
        name = "ClassRefType"

    ref: Optional["ClassRefType1.Ref"] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class Ref:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ClassRestrictionType:
    crtr: Optional["ClassRestrictionType.Crtr"] = field(
        default=None,
        metadata={
            "name": "CRTR",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    class_restriction: Optional["ClassRestrictionType.ClassRestriction"] = (
        field(
            default=None,
            metadata={
                "name": "ClassRestriction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )
    )

    @dataclass
    class Crtr:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class ClassRestriction:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ConcreteForGenericType:
    generic_def: Optional["ConcreteForGenericType.GenericDef"] = field(
        default=None,
        metadata={
            "name": "GenericDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    concrete_domain: Optional["ConcreteForGenericType.ConcreteDomain"] = field(
        default=None,
        metadata={
            "name": "ConcreteDomain",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class GenericDef:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class ConcreteDomain:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class DependencyType:
    using: Optional["DependencyType.Using"] = field(
        default=None,
        metadata={
            "name": "Using",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    dependent: Optional["DependencyType.Dependent"] = field(
        default=None,
        metadata={
            "name": "Dependent",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class Using:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class Dependent:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class DerivedAssocType:
    pass


@dataclass
class DocTextTranslationType:
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class DocTextType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class DomainConstraintType:
    pass


@dataclass
class ExistenceDefType:
    pass


@dataclass
class ExplicitAssocAccType:
    pass


@dataclass
class ExpressionType:
    pass


@dataclass
class FormalArgumentType:
    pass


@dataclass
class GenericDefType:
    pass


@dataclass
class GraphicBaseType:
    pass


@dataclass
class GraphicRuleType:
    pass


@dataclass
class Ili1FormatType:
    is_free: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isFree",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    line_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "LineSize",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 2147483647,
        },
    )
    tid_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "tidSize",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 2147483647,
        },
    )
    blank_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "blankCode",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )
    undefined_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "undefinedCode",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )
    continue_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "continueCode",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )
    font: Optional[str] = field(
        default=None,
        metadata={
            "name": "Font",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    tid_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "tidKind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    tid_explanation: Optional[str] = field(
        default=None,
        metadata={
            "name": "tidExplanation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )


@dataclass
class Ili1TransferElementType:
    ili1_transfer_class: Optional[
        "Ili1TransferElementType.Ili1TransferClass"
    ] = field(
        default=None,
        metadata={
            "name": "Ili1TransferClass",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    ili1_ref_attr: Optional["Ili1TransferElementType.Ili1RefAttr"] = field(
        default=None,
        metadata={
            "name": "Ili1RefAttr",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class Ili1TransferClass:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class Ili1RefAttr:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ImportType:
    importing_p: Optional["ImportType.ImportingP"] = field(
        default=None,
        metadata={
            "name": "ImportingP",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    imported_p: Optional["ImportType.ImportedP"] = field(
        default=None,
        metadata={
            "name": "ImportedP",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class ImportingP:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class ImportedP:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class InheritanceType:
    pass


@dataclass
class LineAttrType:
    pass


@dataclass
class LineCoordType:
    pass


@dataclass
class LineFormStructureType:
    pass


@dataclass
class LinesFormType:
    line_type: Optional["LinesFormType.LineType"] = field(
        default=None,
        metadata={
            "name": "LineType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    line_form: Optional["LinesFormType.LineForm"] = field(
        default=None,
        metadata={
            "name": "LineForm",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class LineType:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class LineForm:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class LocalFtypeType:
    class Meta:
        name = "LocalFTypeType"


@dataclass
class LocalTypeType:
    pass


@dataclass
class MetaAttributesType:
    pass


@dataclass
class MetaBasketMembersType:
    pass


@dataclass
class MetaDataUnitType:
    pass


@dataclass
class MetaObjectClassType:
    pass


@dataclass
class ModelDataBasketOidtype:
    class Meta:
        name = "ModelData.BasketOIDType"


@dataclass
class MultiplicityType:
    min: Optional[int] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )


@dataclass
class NumUnitType:
    pass


@dataclass
class NumsRefSysType:
    axis: Optional[int] = field(
        default=None,
        metadata={
            "name": "Axis",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 3,
        },
    )


@dataclass
class ObjectOidtype:
    class Meta:
        name = "ObjectOIDType"


@dataclass
class PackageElementsType:
    pass


@dataclass
class PathElType:
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ref: Optional["PathElType.Ref"] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    num_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumIndex",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )
    spec_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecIndex",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Ref:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ResultTypeType:
    pass


@dataclass
class SignClassType:
    pass


@dataclass
class StructOfFormatType:
    pass


@dataclass
class SubNodeType:
    pass


@dataclass
class TopNodeType:
    pass


@dataclass
class TransferElementType:
    transfer_class: Optional["TransferElementType.TransferClass"] = field(
        default=None,
        metadata={
            "name": "TransferClass",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    transfer_element: Optional["TransferElementType.TransferElement"] = field(
        default=None,
        metadata={
            "name": "TransferElement",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class TransferClass:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class TransferElement:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class TreeValueTypeOfType:
    pass


@dataclass
class TypeRestrictionType:
    trtr: Optional["TypeRestrictionType.Trtr"] = field(
        default=None,
        metadata={
            "name": "TRTR",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    type_restriction: Optional["TypeRestrictionType.TypeRestriction"] = field(
        default=None,
        metadata={
            "name": "TypeRestriction",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class Trtr:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class TypeRestriction:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ArefOf(ArefOfType):
    class Meta:
        name = "ARefOf"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AllowedInBasket(AllowedInBasketType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ArgumentType(ArgumentTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AssocAccOrigin(AssocAccOriginType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AssocAccTarget(AssocAccTargetType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AssocRole(AssocRoleType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AttrOrParamType(AttrOrParamTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AxisSpec(AxisSpecType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class BaseClass(BaseClassType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class BaseType(BaseTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class BaseViewDef(BaseViewDefType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class BaseViewRef(BaseViewRefType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassAttr(ClassAttrType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassConstraint(ClassConstraintType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassParam(ClassParamType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassRef(ClassRefType1):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassRestriction(ClassRestrictionType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ConcreteForGeneric(ConcreteForGenericType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Dependency(DependencyType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DerivedAssoc(DerivedAssocType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DocText(DocTextType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DocTextTranslation(DocTextTranslationType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DomainConstraint(DomainConstraintType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ExistenceDef(ExistenceDefType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ExplicitAssocAcc(ExplicitAssocAccType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Expression(ExpressionType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class FactorType(ExpressionType):
    pass


@dataclass
class FormalArgument(FormalArgumentType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class GenericDef(GenericDefType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class GraphicBase(GraphicBaseType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class GraphicRule(GraphicRuleType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Ili1Format(Ili1FormatType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Ili1TransferElement(Ili1TransferElementType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Import(ImportType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Inheritance(InheritanceType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LineAttr(LineAttrType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LineCoord(LineCoordType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LineFormStructure(LineFormStructureType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LinesForm(LinesFormType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LocalFtype(LocalFtypeType):
    class Meta:
        name = "LocalFType"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LocalType(LocalTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaAttributes(MetaAttributesType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaBasketMembers(MetaBasketMembersType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaDataUnit(MetaDataUnitType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaObjectClass(MetaObjectClassType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ModelDataBasketOid(ModelDataBasketOidtype):
    class Meta:
        name = "ModelData.BasketOID"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Multiplicity(MultiplicityType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class NumUnit(NumUnitType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class NumsRefSys(NumsRefSysType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ObjectOid(ObjectOidtype):
    class Meta:
        name = "ObjectOID"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class PackageElements(PackageElementsType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class PathEl(PathElType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ResultType(ResultTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class SignClass(SignClassType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class StructOfFormat(StructOfFormatType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class SubNode(SubNodeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TopNode(TopNodeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TransferElement(TransferElementType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TreeValueTypeOf(TreeValueTypeOfType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TypeRestriction(TypeRestrictionType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AttributeConstType(FactorType):
    attribute: Optional["AttributeConstType.Attribute"] = field(
        default=None,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Attribute:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ConstantType(FactorType):
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class Factor(FactorType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetranslationType:
    class Meta:
        name = "METranslationType"

    of: Optional["MetranslationType.Of"] = field(
        default=None,
        metadata={
            "name": "Of",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    translated_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TranslatedName",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    translated_doc: List["MetranslationType.TranslatedDoc"] = field(
        default_factory=list,
        metadata={
            "name": "TranslatedDoc",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Of:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class TranslatedDoc:
        doc_text_translation: Optional[DocTextTranslation] = field(
            default=None,
            metadata={
                "name": "DocTextTranslation",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )


@dataclass
class MetaElementType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    documentation: List["MetaElementType.Documentation"] = field(
        default_factory=list,
        metadata={
            "name": "Documentation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    element_in_package: Optional["MetaElementType.ElementInPackage"] = field(
        default=None,
        metadata={
            "name": "ElementInPackage",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )

    @dataclass
    class Documentation:
        doc_text: Optional[DocText] = field(
            default=None,
            metadata={
                "name": "DocText",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )

    @dataclass
    class ElementInPackage:
        package_elements: Optional[PackageElements] = field(
            default=None,
            metadata={
                "name": "PackageElements",
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


@dataclass
class PathOrInspFactorType(FactorType):
    path_els: List["PathOrInspFactorType.PathEls"] = field(
        default_factory=list,
        metadata={
            "name": "PathEls",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    inspection: Optional["PathOrInspFactorType.Inspection"] = field(
        default=None,
        metadata={
            "name": "Inspection",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class PathEls:
        path_el: Optional[PathEl] = field(
            default=None,
            metadata={
                "name": "PathEl",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )

    @dataclass
    class Inspection:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class RuntimeParamRefType(FactorType):
    runtime_param: Optional["RuntimeParamRefType.RuntimeParam"] = field(
        default=None,
        metadata={
            "name": "RuntimeParam",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class RuntimeParam:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class UnitFunctionType(FactorType):
    explanation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Explanation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class UnitRefType(FactorType):
    unit: Optional["UnitRefType.Unit"] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Unit:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class AttributeConst(AttributeConstType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Constant(ConstantType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ConstraintType(MetaElementType):
    to_class: Optional["ConstraintType.ToClass"] = field(
        default=None,
        metadata={
            "name": "ToClass",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    to_domain: Optional["ConstraintType.ToDomain"] = field(
        default=None,
        metadata={
            "name": "ToDomain",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class ToClass:
        class_constraint: Optional[ClassConstraint] = field(
            default=None,
            metadata={
                "name": "ClassConstraint",
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

    @dataclass
    class ToDomain:
        domain_constraint: Optional[DomainConstraint] = field(
            default=None,
            metadata={
                "name": "DomainConstraint",
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


@dataclass
class ContextType(MetaElementType):
    pass


@dataclass
class ExtendableMetype(MetaElementType):
    class Meta:
        name = "ExtendableMEType"

    abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Generic",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    super: Optional["ExtendableMetype.Super"] = field(
        default=None,
        metadata={
            "name": "Super",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Super:
        inheritance: Optional[Inheritance] = field(
            default=None,
            metadata={
                "name": "Inheritance",
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


@dataclass
class FunctionDefType(MetaElementType):
    explanation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Explanation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    result_type: Optional["FunctionDefType.ResultType"] = field(
        default=None,
        metadata={
            "name": "ResultType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class ResultType:
        result_type: Optional[ResultType] = field(
            default=None,
            metadata={
                "name": "ResultType",
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


@dataclass
class LineFormType(MetaElementType):
    structure: Optional["LineFormType.Structure"] = field(
        default=None,
        metadata={
            "name": "Structure",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class Structure:
        line_form_structure: Optional[LineFormStructure] = field(
            default=None,
            metadata={
                "name": "LineFormStructure",
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


@dataclass
class Metranslation(MetranslationType):
    class Meta:
        name = "METranslation"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaElement(MetaElementType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class PackageType(MetaElementType):
    pass


@dataclass
class PathOrInspFactor(PathOrInspFactorType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class RuntimeParamRef(RuntimeParamRefType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class UnitFunction(UnitFunctionType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class UnitRef(UnitRefType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Constraint(ConstraintType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Context(ContextType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DataUnitType(ExtendableMetype):
    view_unit: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ViewUnit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    data_unit_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataUnitName",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    oid: Optional["DataUnitType.Oid"] = field(
        default=None,
        metadata={
            "name": "Oid",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Oid:
        model_data_basket_oid: Optional[ModelDataBasketOid] = field(
            default=None,
            metadata={
                "name": "ModelData.BasketOID",
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


@dataclass
class EnumNodeType(ExtendableMetype):
    enum_type: Optional["EnumNodeType.EnumType"] = field(
        default=None,
        metadata={
            "name": "EnumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    parent_node: Optional["EnumNodeType.ParentNode"] = field(
        default=None,
        metadata={
            "name": "ParentNode",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class EnumType:
        top_node: Optional[TopNode] = field(
            default=None,
            metadata={
                "name": "TopNode",
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
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class ParentNode:
        sub_node: Optional[SubNode] = field(
            default=None,
            metadata={
                "name": "SubNode",
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
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ExistenceConstraintType(ConstraintType):
    attr: Optional["ExistenceConstraintType.Attr"] = field(
        default=None,
        metadata={
            "name": "Attr",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class Attr:
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )


@dataclass
class ExplicitAssocAccessType(ExtendableMetype):
    assoc_acc_of: Optional["ExplicitAssocAccessType.AssocAccOf"] = field(
        default=None,
        metadata={
            "name": "AssocAccOf",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    origin_role: Optional["ExplicitAssocAccessType.OriginRole"] = field(
        default=None,
        metadata={
            "name": "OriginRole",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    target_role: Optional["ExplicitAssocAccessType.TargetRole"] = field(
        default=None,
        metadata={
            "name": "TargetRole",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class AssocAccOf:
        explicit_assoc_acc: Optional[ExplicitAssocAcc] = field(
            default=None,
            metadata={
                "name": "ExplicitAssocAcc",
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
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class OriginRole:
        assoc_acc_origin: Optional[AssocAccOrigin] = field(
            default=None,
            metadata={
                "name": "AssocAccOrigin",
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

    @dataclass
    class TargetRole:
        assoc_acc_target: Optional[AssocAccTarget] = field(
            default=None,
            metadata={
                "name": "AssocAccTarget",
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


@dataclass
class ExtendableMe(ExtendableMetype):
    class Meta:
        name = "ExtendableME"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class FunctionDef(FunctionDefType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class LineForm(LineFormType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaBasketDefType(ExtendableMetype):
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    meta_data_topic: Optional["MetaBasketDefType.MetaDataTopic"] = field(
        default=None,
        metadata={
            "name": "MetaDataTopic",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class MetaDataTopic:
        meta_data_unit: Optional[MetaDataUnit] = field(
            default=None,
            metadata={
                "name": "MetaDataUnit",
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


@dataclass
class ModelType(PackageType):
    ili_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "iliVersion",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    contracted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Contracted",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
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
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "max_length": 5,
        },
    )
    at: Optional[str] = field(
        default=None,
        metadata={
            "name": "At",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    no_incremental_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoIncrementalTransfer",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    char_set_iananame: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSetIANAName",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    xmlns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ili1_transfername: Optional[str] = field(
        default=None,
        metadata={
            "name": "ili1Transfername",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ili1_format: Optional["ModelType.Ili1Format"] = field(
        default=None,
        metadata={
            "name": "ili1Format",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Ili1Format:
        ili1_format: Optional[Ili1Format] = field(
            default=None,
            metadata={
                "name": "Ili1Format",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )


@dataclass
class Package(PackageType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class RenamedBaseViewType(ExtendableMetype):
    or_null: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OrNull",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    base_view: Optional["RenamedBaseViewType.BaseView"] = field(
        default=None,
        metadata={
            "name": "BaseView",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    view: Optional["RenamedBaseViewType.View"] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class BaseView:
        base_view_ref: Optional[BaseViewRef] = field(
            default=None,
            metadata={
                "name": "BaseViewRef",
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

    @dataclass
    class View:
        base_view_def: Optional[BaseViewDef] = field(
            default=None,
            metadata={
                "name": "BaseViewDef",
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
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class SubModelType(PackageType):
    pass


@dataclass
class TranslationType:
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
            "max_length": 5,
        },
    )
    translations: List["TranslationType.Translations"] = field(
        default_factory=list,
        metadata={
            "name": "Translations",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )

    @dataclass
    class Translations:
        metranslation: Optional[Metranslation] = field(
            default=None,
            metadata={
                "name": "METranslation",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )


@dataclass
class TypeType(ExtendableMetype):
    lftparent: Optional["TypeType.Lftparent"] = field(
        default=None,
        metadata={
            "name": "LFTParent",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ltparent: Optional["TypeType.Ltparent"] = field(
        default=None,
        metadata={
            "name": "LTParent",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Lftparent:
        local_ftype: Optional[LocalFtype] = field(
            default=None,
            metadata={
                "name": "LocalFType",
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

    @dataclass
    class Ltparent:
        local_type: Optional[LocalType] = field(
            default=None,
            metadata={
                "name": "LocalType",
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


@dataclass
class ClassType(TypeType):
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    multiplicity: Optional["ClassType.Multiplicity"] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    embedded_role_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EmbeddedRoleTransfer",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    ili1_optional_table: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ili1OptionalTable",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    existence_constraint: Optional["ClassType.ExistenceConstraint"] = field(
        default=None,
        metadata={
            "name": "ExistenceConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    oid: Optional["ClassType.Oid"] = field(
        default=None,
        metadata={
            "name": "Oid",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    view: Optional["ClassType.View"] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Multiplicity:
        multiplicity: Optional[Multiplicity] = field(
            default=None,
            metadata={
                "name": "Multiplicity",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )

    @dataclass
    class ExistenceConstraint:
        existence_def: Optional[ExistenceDef] = field(
            default=None,
            metadata={
                "name": "ExistenceDef",
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

    @dataclass
    class Oid:
        object_oid: Optional[ObjectOid] = field(
            default=None,
            metadata={
                "name": "ObjectOID",
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

    @dataclass
    class View:
        derived_assoc: Optional[DerivedAssoc] = field(
            default=None,
            metadata={
                "name": "DerivedAssoc",
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


@dataclass
class DataUnit(DataUnitType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DomainTypeType(TypeType):
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    context: Optional["DomainTypeType.Context"] = field(
        default=None,
        metadata={
            "name": "Context",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Context:
        generic_def: Optional[GenericDef] = field(
            default=None,
            metadata={
                "name": "GenericDef",
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


@dataclass
class EnumNode(EnumNodeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ExistenceConstraint(ExistenceConstraintType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ExplicitAssocAccess(ExplicitAssocAccessType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaBasketDef(MetaBasketDefType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Model(ModelType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class RenamedBaseView(RenamedBaseViewType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class SubModel(SubModelType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Translation(TranslationType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TypeType(TypeType):
    class Meta:
        name = "Type"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AnyOidtypeType(DomainTypeType):
    class Meta:
        name = "AnyOIDTypeType"


@dataclass
class AttributeRefTypeType(DomainTypeType):
    of: Optional["AttributeRefTypeType.Of"] = field(
        default=None,
        metadata={
            "name": "Of",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Of:
        aref_of: Optional[ArefOf] = field(
            default=None,
            metadata={
                "name": "ARefOf",
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


@dataclass
class BlackboxTypeType(DomainTypeType):
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class BooleanTypeType(DomainTypeType):
    pass


@dataclass
class Class(ClassType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassRelatedTypeType(DomainTypeType):
    pass


@dataclass
class CoordTypeType(DomainTypeType):
    null_axis: Optional[int] = field(
        default=None,
        metadata={
            "name": "NullAxis",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 3,
        },
    )
    pi_half_axis: Optional[int] = field(
        default=None,
        metadata={
            "name": "PiHalfAxis",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 3,
        },
    )
    multi: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Multi",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )


@dataclass
class DomainType(DomainTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class EnumTreeValueTypeType(DomainTypeType):
    et: Optional["EnumTreeValueTypeType.Et"] = field(
        default=None,
        metadata={
            "name": "ET",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class Et:
        tree_value_type_of: Optional[TreeValueTypeOf] = field(
            default=None,
            metadata={
                "name": "TreeValueTypeOf",
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


@dataclass
class EnumTypeType(DomainTypeType):
    order: Optional[str] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class LineTypeType(DomainTypeType):
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    max_overlap: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxOverlap",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    multi: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Multi",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    coord_type: Optional["LineTypeType.CoordType"] = field(
        default=None,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    lastructure: Optional["LineTypeType.Lastructure"] = field(
        default=None,
        metadata={
            "name": "LAStructure",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class CoordType:
        line_coord: Optional[LineCoord] = field(
            default=None,
            metadata={
                "name": "LineCoord",
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

    @dataclass
    class Lastructure:
        line_attr: Optional[LineAttr] = field(
            default=None,
            metadata={
                "name": "LineAttr",
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


@dataclass
class ModelTranslationType:
    translation: List[Translation] = field(
        default_factory=list,
        metadata={
            "name": "Translation",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
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


@dataclass
class NumTypeType(DomainTypeType):
    min: Optional[str] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    max: Optional[str] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    circular: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Circular",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    clockwise: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Clockwise",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ref_sys: Optional["NumTypeType.RefSys"] = field(
        default=None,
        metadata={
            "name": "RefSys",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    unit: Optional["NumTypeType.Unit"] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class RefSys:
        nums_ref_sys: Optional[NumsRefSys] = field(
            default=None,
            metadata={
                "name": "NumsRefSys",
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

    @dataclass
    class Unit:
        num_unit: Optional[NumUnit] = field(
            default=None,
            metadata={
                "name": "NumUnit",
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


@dataclass
class TextTypeType(DomainTypeType):
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    max_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxLength",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": 1,
            "max_inclusive": 2147483647,
        },
    )


@dataclass
class TypeRelatedTypeType(DomainTypeType):
    base_type: Optional["TypeRelatedTypeType.BaseType"] = field(
        default=None,
        metadata={
            "name": "BaseType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class BaseType:
        base_type: Optional[BaseType] = field(
            default=None,
            metadata={
                "name": "BaseType",
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


@dataclass
class ViewType(ClassType):
    formation_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "FormationKind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    formation_parameter: List["ViewType.FormationParameter"] = field(
        default_factory=list,
        metadata={
            "name": "FormationParameter",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    where: Optional["ViewType.Where"] = field(
        default=None,
        metadata={
            "name": "Where",
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
            "required": True,
        },
    )

    @dataclass
    class FormationParameter:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional["ClassConst"] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional["FunctionCall"] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional["EnumMapping"] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional["CompoundExpr"] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional["UnaryExpr"] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )

    @dataclass
    class Where:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional["ClassConst"] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional["FunctionCall"] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional["EnumMapping"] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional["CompoundExpr"] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional["UnaryExpr"] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )


@dataclass
class AnyOidtype(AnyOidtypeType):
    class Meta:
        name = "AnyOIDType"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AttributeRefType(AttributeRefTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class BlackboxType(BlackboxTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class BooleanType(BooleanTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassRefTypeType(ClassRelatedTypeType):
    pass


@dataclass
class ClassRelatedType(ClassRelatedTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class CoordType(CoordTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class EnumTreeValueType(EnumTreeValueTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class EnumType(EnumTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class FormattedTypeType(NumTypeType):
    format: Optional[str] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    struct: Optional["FormattedTypeType.Struct"] = field(
        default=None,
        metadata={
            "name": "Struct",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class Struct:
        struct_of_format: Optional[StructOfFormat] = field(
            default=None,
            metadata={
                "name": "StructOfFormat",
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


@dataclass
class LineType(LineTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ModelTranslation(ModelTranslationType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MultiValueType(TypeRelatedTypeType):
    ordered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ordered",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    multiplicity: Optional["MultiValueType.Multiplicity"] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Multiplicity:
        multiplicity: Optional[Multiplicity] = field(
            default=None,
            metadata={
                "name": "Multiplicity",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )


@dataclass
class NumType(NumTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ObjectTypeType(ClassRelatedTypeType):
    multiple: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Multiple",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class ReferenceTypeType(ClassRelatedTypeType):
    external: Optional[bool] = field(
        default=None,
        metadata={
            "name": "External",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )


@dataclass
class TextType(TextTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class TypeRelatedType(TypeRelatedTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class View(ViewType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AssocAccType:
    view: Optional[View] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_value: Optional["AssocAccType.Class"] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    assoc_acc: Optional["AssocAccType.AssocAcc"] = field(
        default=None,
        metadata={
            "name": "AssocAcc",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )

    @dataclass
    class Class:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class AssocAcc:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ClassConstType(FactorType):
    view: Optional[View] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_value: Optional["ClassConstType.Class"] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Class:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ClassRefType(ClassRefTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class FormattedType(FormattedTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaObjectDefType(MetaElementType):
    is_ref_system: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRefSystem",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    view: Optional[View] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_value: Optional["MetaObjectDefType.Class"] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    meta_basket_def: Optional["MetaObjectDefType.MetaBasketDef"] = field(
        default=None,
        metadata={
            "name": "MetaBasketDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Class:
        meta_object_class: Optional[MetaObjectClass] = field(
            default=None,
            metadata={
                "name": "MetaObjectClass",
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

    @dataclass
    class MetaBasketDef:
        meta_basket_members: Optional[MetaBasketMembers] = field(
            default=None,
            metadata={
                "name": "MetaBasketMembers",
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


@dataclass
class MultiValue(MultiValueType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ObjectType(ObjectTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ReferenceType(ReferenceTypeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AssocAcc(AssocAccType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassConst(ClassConstType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaObjectDef(MetaObjectDefType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


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
    sub_expression: Optional["UnaryExprType.SubExpression"] = field(
        default=None,
        metadata={
            "name": "SubExpression",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class SubExpression:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional["FunctionCall"] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional["EnumMapping"] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional["CompoundExpr"] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional["UnaryExpr"] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )


@dataclass
class UnaryExpr(UnaryExprType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


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
    sub_expressions: List["CompoundExprType.SubExpressions"] = field(
        default_factory=list,
        metadata={
            "name": "SubExpressions",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class SubExpressions:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional["FunctionCall"] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional["EnumMapping"] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional["CompoundExpr"] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )


@dataclass
class CompoundExpr(CompoundExprType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class EnumAssignmentType:
    value_to_assign: Optional["EnumAssignmentType.ValueToAssign"] = field(
        default=None,
        metadata={
            "name": "ValueToAssign",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    min_enum_value: Optional["EnumAssignmentType.MinEnumValue"] = field(
        default=None,
        metadata={
            "name": "MinEnumValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    max_enum_value: Optional["EnumAssignmentType.MaxEnumValue"] = field(
        default=None,
        metadata={
            "name": "MaxEnumValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class ValueToAssign:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional["FunctionCall"] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional["EnumMapping"] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )

    @dataclass
    class MinEnumValue:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class MaxEnumValue:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class EnumAssignment(EnumAssignmentType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class EnumMappingType(FactorType):
    enum_value: Optional["EnumMappingType.EnumValue"] = field(
        default=None,
        metadata={
            "name": "EnumValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    cases: List["EnumMappingType.Cases"] = field(
        default_factory=list,
        metadata={
            "name": "Cases",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class EnumValue:
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )

    @dataclass
    class Cases:
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
class EnumMapping(EnumMappingType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ActualArgumentType:
    formal_argument: Optional["ActualArgumentType.FormalArgument"] = field(
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
    unit_function: Optional[UnitFunction] = field(
        default=None,
        metadata={
            "name": "UnitFunction",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    unit_ref: Optional[UnitRef] = field(
        default=None,
        metadata={
            "name": "UnitRef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    attribute_const: Optional[AttributeConst] = field(
        default=None,
        metadata={
            "name": "AttributeConst",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_const: Optional[ClassConst] = field(
        default=None,
        metadata={
            "name": "ClassConst",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    constant: Optional[Constant] = field(
        default=None,
        metadata={
            "name": "Constant",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    runtime_param_ref: Optional[RuntimeParamRef] = field(
        default=None,
        metadata={
            "name": "RuntimeParamRef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    function_call: Optional["FunctionCall"] = field(
        default=None,
        metadata={
            "name": "FunctionCall",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_mapping: Optional[EnumMapping] = field(
        default=None,
        metadata={
            "name": "EnumMapping",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    path_or_insp_factor: Optional[PathOrInspFactor] = field(
        default=None,
        metadata={
            "name": "PathOrInspFactor",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    factor: Optional[Factor] = field(
        default=None,
        metadata={
            "name": "Factor",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    compound_expr: Optional[CompoundExpr] = field(
        default=None,
        metadata={
            "name": "CompoundExpr",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    unary_expr: Optional[UnaryExpr] = field(
        default=None,
        metadata={
            "name": "UnaryExpr",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    expression: Optional["ActualArgumentType.Expression"] = field(
        default=None,
        metadata={
            "name": "Expression",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    object_classes: List["ActualArgumentType.ObjectClasses"] = field(
        default_factory=list,
        metadata={
            "name": "ObjectClasses",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class FormalArgument:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class Expression:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional["FunctionCall"] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )

    @dataclass
    class ObjectClasses:
        class_ref: Optional[ClassRef] = field(
            default=None,
            metadata={
                "name": "ClassRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )


@dataclass
class ActualArgument(ActualArgumentType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class FunctionCallType(FactorType):
    function: Optional["FunctionCallType.Function"] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    arguments: List["FunctionCallType.Arguments"] = field(
        default_factory=list,
        metadata={
            "name": "Arguments",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Function:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class Arguments:
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
class FunctionCall(FunctionCallType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class GraphicType(ExtendableMetype):
    where: Optional["GraphicType.Where"] = field(
        default=None,
        metadata={
            "name": "Where",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    base: Optional["GraphicType.Base"] = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Where:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional[FunctionCall] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )

    @dataclass
    class Base:
        graphic_base: Optional[GraphicBase] = field(
            default=None,
            metadata={
                "name": "GraphicBase",
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


@dataclass
class RoleType(ReferenceTypeType):
    strongness: Optional[str] = field(
        default=None,
        metadata={
            "name": "Strongness",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    ordered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ordered",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    multiplicity: Optional["RoleType.Multiplicity"] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    derivates: List["RoleType.Derivates"] = field(
        default_factory=list,
        metadata={
            "name": "Derivates",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    embedded_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EmbeddedTransfer",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    association: Optional["RoleType.Association"] = field(
        default=None,
        metadata={
            "name": "Association",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Multiplicity:
        multiplicity: Optional[Multiplicity] = field(
            default=None,
            metadata={
                "name": "Multiplicity",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )

    @dataclass
    class Derivates:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional[FunctionCall] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )

    @dataclass
    class Association:
        assoc_role: Optional[AssocRole] = field(
            default=None,
            metadata={
                "name": "AssocRole",
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
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class SignParamAssignmentType:
    param: Optional["SignParamAssignmentType.Param"] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    assignment: Optional["SignParamAssignmentType.Assignment"] = field(
        default=None,
        metadata={
            "name": "Assignment",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Param:
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class Assignment:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional[FunctionCall] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )


@dataclass
class SimpleConstraintType(ConstraintType):
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("100.00"),
        },
    )
    logical_expression: Optional["SimpleConstraintType.LogicalExpression"] = (
        field(
            default=None,
            metadata={
                "name": "LogicalExpression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
    )

    @dataclass
    class LogicalExpression:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional[FunctionCall] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )


@dataclass
class UniqueConstraintType(ConstraintType):
    where: Optional["UniqueConstraintType.Where"] = field(
        default=None,
        metadata={
            "name": "Where",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
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
    unique_def: List["UniqueConstraintType.UniqueDef"] = field(
        default_factory=list,
        metadata={
            "name": "UniqueDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Where:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional[FunctionCall] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )

    @dataclass
    class UniqueDef:
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )


@dataclass
class UnitType(ExtendableMetype):
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    definition: Optional["UnitType.Definition"] = field(
        default=None,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Definition:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional[FunctionCall] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )


@dataclass
class Graphic(GraphicType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Role(RoleType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class SignParamAssignment(SignParamAssignmentType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class SimpleConstraint(SimpleConstraintType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class UniqueConstraint(UniqueConstraintType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Unit(UnitType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ArefRestrictionType:
    class Meta:
        name = "ARefRestrictionType"

    aref: Optional["ArefRestrictionType.Aref"] = field(
        default=None,
        metadata={
            "name": "ARef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    view: Optional[View] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_value: Optional[Class] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    line_type: Optional[LineType] = field(
        default=None,
        metadata={
            "name": "LineType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_tree_value_type: Optional[EnumTreeValueType] = field(
        default=None,
        metadata={
            "name": "EnumTreeValueType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_type: Optional[EnumType] = field(
        default=None,
        metadata={
            "name": "EnumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    attribute_ref_type: Optional[AttributeRefType] = field(
        default=None,
        metadata={
            "name": "AttributeRefType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    any_oidtype: Optional[AnyOidtype] = field(
        default=None,
        metadata={
            "name": "AnyOIDType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    coord_type: Optional[CoordType] = field(
        default=None,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    formatted_type: Optional[FormattedType] = field(
        default=None,
        metadata={
            "name": "FormattedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    num_type: Optional[NumType] = field(
        default=None,
        metadata={
            "name": "NumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    blackbox_type: Optional[BlackboxType] = field(
        default=None,
        metadata={
            "name": "BlackboxType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    text_type: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "TextType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    boolean_type: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "BooleanType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    object_type: Optional[ObjectType] = field(
        default=None,
        metadata={
            "name": "ObjectType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    reference_type: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "ReferenceType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_ref_type: Optional[ClassRefType] = field(
        default=None,
        metadata={
            "name": "ClassRefType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_related_type: Optional[ClassRelatedType] = field(
        default=None,
        metadata={
            "name": "ClassRelatedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    multi_value: Optional[MultiValue] = field(
        default=None,
        metadata={
            "name": "MultiValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_related_type: Optional[TypeRelatedType] = field(
        default=None,
        metadata={
            "name": "TypeRelatedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    domain_type: Optional[DomainType] = field(
        default=None,
        metadata={
            "name": "DomainType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_value: Optional["ArefRestrictionType.TypeType"] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Aref:
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
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )


@dataclass
class ArgumentType1(MetaElementType):
    class Meta:
        name = "ArgumentType"

    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    function: Optional["ArgumentType1.Function"] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    view: Optional[View] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_value: Optional[Class] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    line_type: Optional[LineType] = field(
        default=None,
        metadata={
            "name": "LineType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_tree_value_type: Optional[EnumTreeValueType] = field(
        default=None,
        metadata={
            "name": "EnumTreeValueType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_type: Optional[EnumType] = field(
        default=None,
        metadata={
            "name": "EnumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    attribute_ref_type: Optional[AttributeRefType] = field(
        default=None,
        metadata={
            "name": "AttributeRefType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    any_oidtype: Optional[AnyOidtype] = field(
        default=None,
        metadata={
            "name": "AnyOIDType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    coord_type: Optional[CoordType] = field(
        default=None,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    formatted_type: Optional[FormattedType] = field(
        default=None,
        metadata={
            "name": "FormattedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    num_type: Optional[NumType] = field(
        default=None,
        metadata={
            "name": "NumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    blackbox_type: Optional[BlackboxType] = field(
        default=None,
        metadata={
            "name": "BlackboxType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    text_type: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "TextType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    boolean_type: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "BooleanType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    object_type: Optional[ObjectType] = field(
        default=None,
        metadata={
            "name": "ObjectType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    reference_type: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "ReferenceType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_ref_type: Optional[ClassRefType] = field(
        default=None,
        metadata={
            "name": "ClassRefType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_related_type: Optional[ClassRelatedType] = field(
        default=None,
        metadata={
            "name": "ClassRelatedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    multi_value: Optional[MultiValue] = field(
        default=None,
        metadata={
            "name": "MultiValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_related_type: Optional[TypeRelatedType] = field(
        default=None,
        metadata={
            "name": "TypeRelatedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    domain_type: Optional[DomainType] = field(
        default=None,
        metadata={
            "name": "DomainType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_value: Optional["ArgumentType1.TypeType"] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Function:
        formal_argument: Optional[FormalArgument] = field(
            default=None,
            metadata={
                "name": "FormalArgument",
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
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class TypeType:
        argument_type: Optional[ArgumentType] = field(
            default=None,
            metadata={
                "name": "ArgumentType",
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
    derivates: List["AttrOrParamType1.Derivates"] = field(
        default_factory=list,
        metadata={
            "name": "Derivates",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    attr_parent: Optional["AttrOrParamType1.AttrParent"] = field(
        default=None,
        metadata={
            "name": "AttrParent",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    param_parent: Optional["AttrOrParamType1.ParamParent"] = field(
        default=None,
        metadata={
            "name": "ParamParent",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    view: Optional[View] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_value: Optional[Class] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    line_type: Optional[LineType] = field(
        default=None,
        metadata={
            "name": "LineType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_tree_value_type: Optional[EnumTreeValueType] = field(
        default=None,
        metadata={
            "name": "EnumTreeValueType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_type: Optional[EnumType] = field(
        default=None,
        metadata={
            "name": "EnumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    attribute_ref_type: Optional[AttributeRefType] = field(
        default=None,
        metadata={
            "name": "AttributeRefType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    any_oidtype: Optional[AnyOidtype] = field(
        default=None,
        metadata={
            "name": "AnyOIDType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    coord_type: Optional[CoordType] = field(
        default=None,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    formatted_type: Optional[FormattedType] = field(
        default=None,
        metadata={
            "name": "FormattedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    num_type: Optional[NumType] = field(
        default=None,
        metadata={
            "name": "NumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    blackbox_type: Optional[BlackboxType] = field(
        default=None,
        metadata={
            "name": "BlackboxType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    text_type: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "TextType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    boolean_type: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "BooleanType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    object_type: Optional[ObjectType] = field(
        default=None,
        metadata={
            "name": "ObjectType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    reference_type: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "ReferenceType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_ref_type: Optional[ClassRefType] = field(
        default=None,
        metadata={
            "name": "ClassRefType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_related_type: Optional[ClassRelatedType] = field(
        default=None,
        metadata={
            "name": "ClassRelatedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    multi_value: Optional[MultiValue] = field(
        default=None,
        metadata={
            "name": "MultiValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_related_type: Optional[TypeRelatedType] = field(
        default=None,
        metadata={
            "name": "TypeRelatedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    domain_type: Optional[DomainType] = field(
        default=None,
        metadata={
            "name": "DomainType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_value: Optional["AttrOrParamType1.TypeType"] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Derivates:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional[FunctionCall] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )

    @dataclass
    class AttrParent:
        class_attr: Optional[ClassAttr] = field(
            default=None,
            metadata={
                "name": "ClassAttr",
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
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class ParamParent:
        class_param: Optional[ClassParam] = field(
            default=None,
            metadata={
                "name": "ClassParam",
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
        order_pos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "required": True,
            },
        )

    @dataclass
    class TypeType:
        attr_or_param_type: Optional[AttrOrParamType] = field(
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


@dataclass
class CondSignParamAssignmentType:
    where: Optional["CondSignParamAssignmentType.Where"] = field(
        default=None,
        metadata={
            "name": "Where",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    assignments: List["CondSignParamAssignmentType.Assignments"] = field(
        default_factory=list,
        metadata={
            "name": "Assignments",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Where:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional[FunctionCall] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )

    @dataclass
    class Assignments:
        sign_param_assignment: Optional[SignParamAssignment] = field(
            default=None,
            metadata={
                "name": "SignParamAssignment",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )


@dataclass
class SetConstraintType(ConstraintType):
    where: Optional["SetConstraintType.Where"] = field(
        default=None,
        metadata={
            "name": "Where",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    set_constraint: Optional["SetConstraint"] = field(
        default=None,
        metadata={
            "name": "SetConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    unique_constraint: Optional[UniqueConstraint] = field(
        default=None,
        metadata={
            "name": "UniqueConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    existence_constraint: Optional[ExistenceConstraint] = field(
        default=None,
        metadata={
            "name": "ExistenceConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    simple_constraint: Optional[SimpleConstraint] = field(
        default=None,
        metadata={
            "name": "SimpleConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    constraint: Optional["SetConstraintType.Constraint"] = field(
        default=None,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Where:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional[FunctionCall] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )

    @dataclass
    class Constraint:
        unit_function: Optional[UnitFunction] = field(
            default=None,
            metadata={
                "name": "UnitFunction",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unit_ref: Optional[UnitRef] = field(
            default=None,
            metadata={
                "name": "UnitRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        attribute_const: Optional[AttributeConst] = field(
            default=None,
            metadata={
                "name": "AttributeConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        class_const: Optional[ClassConst] = field(
            default=None,
            metadata={
                "name": "ClassConst",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        constant: Optional[Constant] = field(
            default=None,
            metadata={
                "name": "Constant",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        runtime_param_ref: Optional[RuntimeParamRef] = field(
            default=None,
            metadata={
                "name": "RuntimeParamRef",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        function_call: Optional[FunctionCall] = field(
            default=None,
            metadata={
                "name": "FunctionCall",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        enum_mapping: Optional[EnumMapping] = field(
            default=None,
            metadata={
                "name": "EnumMapping",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        path_or_insp_factor: Optional[PathOrInspFactor] = field(
            default=None,
            metadata={
                "name": "PathOrInspFactor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        factor: Optional[Factor] = field(
            default=None,
            metadata={
                "name": "Factor",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        compound_expr: Optional[CompoundExpr] = field(
            default=None,
            metadata={
                "name": "CompoundExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        unary_expr: Optional[UnaryExpr] = field(
            default=None,
            metadata={
                "name": "UnaryExpr",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )
        expression: Optional[Expression] = field(
            default=None,
            metadata={
                "name": "Expression",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            },
        )


@dataclass
class ArefRestriction(ArefRestrictionType):
    class Meta:
        name = "ARefRestriction"
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class Argument(ArgumentType1):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class AttrOrParam(AttrOrParamType1):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class CondSignParamAssignment(CondSignParamAssignmentType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class SetConstraint(SetConstraintType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class DrawingRuleType(ExtendableMetype):
    rule: List["DrawingRuleType.Rule"] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    view: Optional[View] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_value: Optional["DrawingRuleType.Class"] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    graphic: Optional["DrawingRuleType.Graphic"] = field(
        default=None,
        metadata={
            "name": "Graphic",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )

    @dataclass
    class Rule:
        cond_sign_param_assignment: Optional[CondSignParamAssignment] = field(
            default=None,
            metadata={
                "name": "CondSignParamAssignment",
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
                "required": True,
            },
        )

    @dataclass
    class Class:
        sign_class: Optional[SignClass] = field(
            default=None,
            metadata={
                "name": "SignClass",
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

    @dataclass
    class Graphic:
        graphic_rule: Optional[GraphicRule] = field(
            default=None,
            metadata={
                "name": "GraphicRule",
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


@dataclass
class DrawingRule(DrawingRuleType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class MetaAttributeType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
            "required": True,
        },
    )
    line_form: Optional[LineForm] = field(
        default=None,
        metadata={
            "name": "LineForm",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    argument: Optional[Argument] = field(
        default=None,
        metadata={
            "name": "Argument",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    function_def: Optional[FunctionDef] = field(
        default=None,
        metadata={
            "name": "FunctionDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    meta_object_def: Optional[MetaObjectDef] = field(
        default=None,
        metadata={
            "name": "MetaObjectDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    context: Optional[Context] = field(
        default=None,
        metadata={
            "name": "Context",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    set_constraint: Optional[SetConstraint] = field(
        default=None,
        metadata={
            "name": "SetConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    unique_constraint: Optional[UniqueConstraint] = field(
        default=None,
        metadata={
            "name": "UniqueConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    existence_constraint: Optional[ExistenceConstraint] = field(
        default=None,
        metadata={
            "name": "ExistenceConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    simple_constraint: Optional[SimpleConstraint] = field(
        default=None,
        metadata={
            "name": "SimpleConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    constraint: Optional[Constraint] = field(
        default=None,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    sub_model: Optional[SubModel] = field(
        default=None,
        metadata={
            "name": "SubModel",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    model: Optional[Model] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    package: Optional[Package] = field(
        default=None,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    drawing_rule: Optional[DrawingRule] = field(
        default=None,
        metadata={
            "name": "DrawingRule",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    graphic: Optional[Graphic] = field(
        default=None,
        metadata={
            "name": "Graphic",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    renamed_base_view: Optional[RenamedBaseView] = field(
        default=None,
        metadata={
            "name": "RenamedBaseView",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_node: Optional[EnumNode] = field(
        default=None,
        metadata={
            "name": "EnumNode",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    meta_basket_def: Optional[MetaBasketDef] = field(
        default=None,
        metadata={
            "name": "MetaBasketDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    unit: Optional[Unit] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    data_unit: Optional[DataUnit] = field(
        default=None,
        metadata={
            "name": "DataUnit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    explicit_assoc_access: Optional[ExplicitAssocAccess] = field(
        default=None,
        metadata={
            "name": "ExplicitAssocAccess",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    attr_or_param: Optional[AttrOrParam] = field(
        default=None,
        metadata={
            "name": "AttrOrParam",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    view: Optional[View] = field(
        default=None,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_value: Optional[Class] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    line_type: Optional[LineType] = field(
        default=None,
        metadata={
            "name": "LineType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_tree_value_type: Optional[EnumTreeValueType] = field(
        default=None,
        metadata={
            "name": "EnumTreeValueType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_type: Optional[EnumType] = field(
        default=None,
        metadata={
            "name": "EnumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    attribute_ref_type: Optional[AttributeRefType] = field(
        default=None,
        metadata={
            "name": "AttributeRefType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    any_oidtype: Optional[AnyOidtype] = field(
        default=None,
        metadata={
            "name": "AnyOIDType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    coord_type: Optional[CoordType] = field(
        default=None,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    formatted_type: Optional[FormattedType] = field(
        default=None,
        metadata={
            "name": "FormattedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    num_type: Optional[NumType] = field(
        default=None,
        metadata={
            "name": "NumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    blackbox_type: Optional[BlackboxType] = field(
        default=None,
        metadata={
            "name": "BlackboxType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    text_type: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "TextType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    boolean_type: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "BooleanType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    object_type: Optional[ObjectType] = field(
        default=None,
        metadata={
            "name": "ObjectType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    reference_type: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "ReferenceType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_ref_type: Optional[ClassRefType] = field(
        default=None,
        metadata={
            "name": "ClassRefType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_related_type: Optional[ClassRelatedType] = field(
        default=None,
        metadata={
            "name": "ClassRelatedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    multi_value: Optional[MultiValue] = field(
        default=None,
        metadata={
            "name": "MultiValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_related_type: Optional[TypeRelatedType] = field(
        default=None,
        metadata={
            "name": "TypeRelatedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    domain_type: Optional[DomainType] = field(
        default=None,
        metadata={
            "name": "DomainType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_value: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    extendable_me: Optional[ExtendableMe] = field(
        default=None,
        metadata={
            "name": "ExtendableME",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    meta_element: Optional["MetaAttributeType.MetaElement"] = field(
        default=None,
        metadata={
            "name": "MetaElement",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "required": True,
        },
    )

    @dataclass
    class MetaElement:
        meta_attributes: Optional[MetaAttributes] = field(
            default=None,
            metadata={
                "name": "MetaAttributes",
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


@dataclass
class MetaAttribute(MetaAttributeType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ModelDataType:
    line_form: List[LineForm] = field(
        default_factory=list,
        metadata={
            "name": "LineForm",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    argument: List[Argument] = field(
        default_factory=list,
        metadata={
            "name": "Argument",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    function_def: List[FunctionDef] = field(
        default_factory=list,
        metadata={
            "name": "FunctionDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    meta_object_def: List[MetaObjectDef] = field(
        default_factory=list,
        metadata={
            "name": "MetaObjectDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    context: List[Context] = field(
        default_factory=list,
        metadata={
            "name": "Context",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    set_constraint: List[SetConstraint] = field(
        default_factory=list,
        metadata={
            "name": "SetConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    unique_constraint: List[UniqueConstraint] = field(
        default_factory=list,
        metadata={
            "name": "UniqueConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    existence_constraint: List[ExistenceConstraint] = field(
        default_factory=list,
        metadata={
            "name": "ExistenceConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    simple_constraint: List[SimpleConstraint] = field(
        default_factory=list,
        metadata={
            "name": "SimpleConstraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    constraint: List[Constraint] = field(
        default_factory=list,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    sub_model: List[SubModel] = field(
        default_factory=list,
        metadata={
            "name": "SubModel",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    model: List[Model] = field(
        default_factory=list,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    package: List[Package] = field(
        default_factory=list,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    drawing_rule: List[DrawingRule] = field(
        default_factory=list,
        metadata={
            "name": "DrawingRule",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    graphic: List[Graphic] = field(
        default_factory=list,
        metadata={
            "name": "Graphic",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    renamed_base_view: List[RenamedBaseView] = field(
        default_factory=list,
        metadata={
            "name": "RenamedBaseView",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_node: List[EnumNode] = field(
        default_factory=list,
        metadata={
            "name": "EnumNode",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    meta_basket_def: List[MetaBasketDef] = field(
        default_factory=list,
        metadata={
            "name": "MetaBasketDef",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    unit: List[Unit] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    data_unit: List[DataUnit] = field(
        default_factory=list,
        metadata={
            "name": "DataUnit",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    explicit_assoc_access: List[ExplicitAssocAccess] = field(
        default_factory=list,
        metadata={
            "name": "ExplicitAssocAccess",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    attr_or_param: List[AttrOrParam] = field(
        default_factory=list,
        metadata={
            "name": "AttrOrParam",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    view: List[View] = field(
        default_factory=list,
        metadata={
            "name": "View",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_value: List[Class] = field(
        default_factory=list,
        metadata={
            "name": "Class",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    line_type: List[LineType] = field(
        default_factory=list,
        metadata={
            "name": "LineType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_tree_value_type: List[EnumTreeValueType] = field(
        default_factory=list,
        metadata={
            "name": "EnumTreeValueType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    enum_type: List[EnumType] = field(
        default_factory=list,
        metadata={
            "name": "EnumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    attribute_ref_type: List[AttributeRefType] = field(
        default_factory=list,
        metadata={
            "name": "AttributeRefType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    any_oidtype: List[AnyOidtype] = field(
        default_factory=list,
        metadata={
            "name": "AnyOIDType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    coord_type: List[CoordType] = field(
        default_factory=list,
        metadata={
            "name": "CoordType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    formatted_type: List[FormattedType] = field(
        default_factory=list,
        metadata={
            "name": "FormattedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    num_type: List[NumType] = field(
        default_factory=list,
        metadata={
            "name": "NumType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    blackbox_type: List[BlackboxType] = field(
        default_factory=list,
        metadata={
            "name": "BlackboxType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    text_type: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "TextType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    boolean_type: List[BooleanType] = field(
        default_factory=list,
        metadata={
            "name": "BooleanType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    object_type: List[ObjectType] = field(
        default_factory=list,
        metadata={
            "name": "ObjectType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    role: List[Role] = field(
        default_factory=list,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    reference_type: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_ref_type: List[ClassRefType] = field(
        default_factory=list,
        metadata={
            "name": "ClassRefType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_related_type: List[ClassRelatedType] = field(
        default_factory=list,
        metadata={
            "name": "ClassRelatedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    multi_value: List[MultiValue] = field(
        default_factory=list,
        metadata={
            "name": "MultiValue",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_related_type: List[TypeRelatedType] = field(
        default_factory=list,
        metadata={
            "name": "TypeRelatedType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    domain_type: List[DomainType] = field(
        default_factory=list,
        metadata={
            "name": "DomainType",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_value: List[TypeType] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    extendable_me: List[ExtendableMe] = field(
        default_factory=list,
        metadata={
            "name": "ExtendableME",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    meta_element: List[MetaElement] = field(
        default_factory=list,
        metadata={
            "name": "MetaElement",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    meta_attribute: List[MetaAttribute] = field(
        default_factory=list,
        metadata={
            "name": "MetaAttribute",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    import_value: List[Import] = field(
        default_factory=list,
        metadata={
            "name": "Import",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    type_restriction: List[TypeRestriction] = field(
        default_factory=list,
        metadata={
            "name": "TypeRestriction",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    base_class: List[BaseClass] = field(
        default_factory=list,
        metadata={
            "name": "BaseClass",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    class_restriction: List[ClassRestriction] = field(
        default_factory=list,
        metadata={
            "name": "ClassRestriction",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    assoc_acc: List[AssocAcc] = field(
        default_factory=list,
        metadata={
            "name": "AssocAcc",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    transfer_element: List[TransferElement] = field(
        default_factory=list,
        metadata={
            "name": "TransferElement",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    ili1_transfer_element: List[Ili1TransferElement] = field(
        default_factory=list,
        metadata={
            "name": "Ili1TransferElement",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    dependency: List[Dependency] = field(
        default_factory=list,
        metadata={
            "name": "Dependency",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    allowed_in_basket: List[AllowedInBasket] = field(
        default_factory=list,
        metadata={
            "name": "AllowedInBasket",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    concrete_for_generic: List[ConcreteForGeneric] = field(
        default_factory=list,
        metadata={
            "name": "ConcreteForGeneric",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    axis_spec: List[AxisSpec] = field(
        default_factory=list,
        metadata={
            "name": "AxisSpec",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    aref_restriction: List[ArefRestriction] = field(
        default_factory=list,
        metadata={
            "name": "ARefRestriction",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
        },
    )
    lines_form: List[LinesForm] = field(
        default_factory=list,
        metadata={
            "name": "LinesForm",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/IlisMeta16",
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


@dataclass
class ModelData(ModelDataType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"

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