
This is about the necessary constructions to read an arbitrary INTERLIS Metamodel File (`*.imd`) in the
[IMD16](https://models.interlis.ch/core/IlisMeta16.ili) format. So about parsing the XML/XTF.

The following overview tries to reflect the order and structure how it is defined in the above linked
ILI file.

## MetaElements in general

| Construct                | ili Kind       | Mandatory v1 | Implemented |
|--------------------------|----------------|:------------:|:-----------:|
| ModelData.DocText        | STRUCTURE      |      ✅       |      ✅      |
| ModelData.MetaElement    | CLASS ABSTRACT |      ✅       |      ✅      |
| ModelData.MetaAttribute  | CLASS          |      ✅       |      ✅      |
| ModelData.MetaAttributes | ASSOCIATION    |      ✅       |      ✅      |
| ModelData.ExtendableME   | CLASS          |      ✅       |      ✅      |
| ModelData.Inheritance    | ASSOCIATION    |      ✅       |      ✅      |

## Models

| Construct                  | ili Kind       | Mandatory v1 | Implemented |
|----------------------------|----------------|:------------:|:-----------:|
| ModelData.Package          | CLASS ABSTRACT |      ✅       |      ✅      |
| ModelData.Ili1Format       | STRUCTURE      |      ✅       |      ✅      |
| ModelData.Model            | CLASS          |      ✅       |      ✅      |
| ModelData.SubModel         | CLASS          |      ✅       |      ✅      |
| ModelData.PackageElements  | ASSOCIATION    |      ✅       |      ✅      |
| ModelData.Import           | ASSOCIATION    |      ❌       |      ✅      |
| ModelData.Type             | CLASS          |      ✅       |      ✅      |
| ModelData.Expression       | STRUCTURE      |      ✅       |      ✅      |
| ModelData.Multiplicity     | STRUCTURE      |      ✅       |      ✅      |
| ModelData.Constraint       | CLASS ABSTRACT |      ✅       |      ✅      |
| ModelData.DomainType       | CLASS ABSTRACT |      ✅       |      ✅      |
| ModelData.DomainConstraint | ASSOCIATION    |      ❌       |      ✅      |

## Classes

| Construct                 | ili Kind    | Mandatory v1 | Implemented |
|---------------------------|-------------|:------------:|:-----------:|
| ModelData.Class           | CLASS       |      ✅       |      ✅      |
| ModelData.AttrOrParam     | CLASS       |      ✅       |      ✅      |
| ModelData.ClassConstraint | ASSOCIATION |      ✅       |      ✅      |
| ModelData.LocalType       | ASSOCIATION |      ❌       |      ✅      |
| ModelData.AttrOrParamType | ASSOCIATION |      ✅       |      ✅      |
| ModelData.ClassAttr       | ASSOCIATION |      ✅       |      ✅      |
| ModelData.ClassParam      | ASSOCIATION |      ✅       |      ✅      |

## Types related to other types

| Construct                 | ili Kind       | Mandatory v1 | Implemented |
|---------------------------|----------------|:------------:|:-----------:|
| ModelData.TypeRelatedType | CLASS ABSTRACT |      ✅       |      ✅      |
| ModelData.BaseType        | ASSOCIATION    |      ✅       |      ✅      |
| ModelData.TypeRestriction | ASSOCIATION    |      ❌       |      ✅      |

## Bag type

| Construct            | ili Kind | Mandatory v1 | Implemented |
|----------------------|----------|:------------:|:-----------:|
| ModelData.MultiValue | CLASS    |      ✅       |      ✅      |

## References and associations

| Construct                     | ili Kind       | Mandatory v1 | Implemented |
|-------------------------------|----------------|:------------:|:-----------:|
| ModelData.ClassRelatedType    | CLASS ABSTRACT |      ✅       |      ✅      |
| ModelData.BaseClass           | ASSOCIATION    |      ✅       |      ✅      |
| ModelData.ClassRestriction    | ASSOCIATION    |      ❌       |      ✅      |
| ModelData.ReferenceType       | CLASS          |      ✅       |      ✅      |
| ModelData.Role                | CLASS          |      ✅       |      ✅      |
| ModelData.AssocRole           | ASSOCIATION    |      ✅       |      ✅      |
| ModelData.ExplicitAssocAccess | CLASS          |      ❌       |      ✅      |
| ModelData.ExplicitAssocAcc    | ASSOCIATION    |      ❌       |      ✅      |
| ModelData.AssocAccOrigin      | ASSOCIATION    |      ❌       |      ✅      |
| ModelData.AssocAccTarget      | ASSOCIATION    |      ❌       |      ✅      |
| ModelData.AssocAcc            | ASSOCIATION    |      ✅       |      ✅      |

## Information for easy transfer

| Construct                     | ili Kind    | Mandatory v1 | Implemented |
|-------------------------------|-------------|:------------:|:-----------:|
| ModelData.TransferElement     | ASSOCIATION |      ❌       |      ✅      |
| ModelData.Ili1TransferElement | ASSOCIATION |      ❌       |      ✅      |

## DataUnits

| Construct                 | ili Kind    | Mandatory v1 | Implemented |
|---------------------------|-------------|:------------:|:-----------:|
| ModelData.DataUnit        | CLASS       |      ✅       |      ✅      |
| ModelData.Dependency      | ASSOCIATION |      ❌       |      ✅      |
| ModelData.AllowedInBasket | ASSOCIATION |      ❌       |      ✅      |

## Generics and Contexts (INTERLIS 2.4 only)

| Construct                    | ili Kind    | Mandatory v1 | Implemented |
|------------------------------|-------------|:------------:|:-----------:|
| ModelData.Context            | CLASS       |      ❌       |      ✅      |
| ModelData.GenericDef         | ASSOCIATION |      ❌       |      ✅      |
| ModelData.ConcreteForGeneric | ASSOCIATION |      ❌       |      ✅      |

## Units

| Construct      | ili Kind | Mandatory v1 | Implemented |
|----------------|----------|:------------:|:-----------:|
| ModelData.Unit | CLASS    |     (✅)      |      ✅      |

## MetaObjects

| Construct                   | ili Kind    | Mandatory v1 | Implemented |
|-----------------------------|-------------|:------------:|:-----------:|
| ModelData.MetaBasketDef     | CLASS       |      ❌       |      ✅      |
| ModelData.MetaDataUnit      | ASSOCIATION |      ❌       |      ✅      |
| ModelData.MetaObjectDef     | CLASS       |      ❌       |      ✅      |
| ModelData.MetaBasketMembers | ASSOCIATION |      ❌       |      ✅      |
| ModelData.MetaObjectClass   | ASSOCIATION |      ❌       |      ✅      |

## Base types

| Construct                | ili Kind    | Mandatory v1 | Implemented |
|--------------------------|-------------|:------------:|:-----------:|
| ModelData.BooleanType    | CLASS       |      ✅       |      ✅      |
| ModelData.TextType       | CLASS       |      ✅       |      ✅      |
| ModelData.BlackboxType   | CLASS       |      ✅       |      ✅      |
| ModelData.NumType        | CLASS       |      ✅       |      ✅      |
| ModelData.NumUnit        | ASSOCIATION |      ✅       |      ✅      |
| ModelData.CoordType      | CLASS       |      ✅       |      ✅      |
| ModelData.AxisSpec       | ASSOCIATION |      ✅       |      ✅      |
| ModelData.NumsRefSys     | ASSOCIATION |      ✅       |      ✅      |
| ModelData.FormattedType  | CLASS       |      ✅       |      ✅      |
| ModelData.StructOfFormat | ASSOCIATION |      ✅       |      ✅      |

## OID Definition

| Construct            | ili Kind    | Mandatory v1 | Implemented |
|----------------------|-------------|:------------:|:-----------:|
| ModelData.AnyOIDType | CLASS       |      ✅       |      ✅      |
| ModelData.ObjectOID  | ASSOCIATION |      ✅       |      ✅      |
| ModelData.BasketOID  | ASSOCIATION |      ✅       |      ✅      |

## Functions

| Construct                | ili Kind    | Mandatory v1 | Implemented |
|--------------------------|-------------|:------------:|:-----------:|
| ModelData.FunctionDef    | CLASS       |      ❌       |      ✅      |
| ModelData.LocalFType     | ASSOCIATION |      ❌       |      ✅      |
| ModelData.ResultType     | ASSOCIATION |      ❌       |      ✅      |
| ModelData.Argument       | CLASS       |      ❌       |      ✅      |
| ModelData.FormalArgument | ASSOCIATION |      ❌       |      ✅      |
| ModelData.ArgumentType   | ASSOCIATION |      ❌       |      ✅      |

## Class and attribute reference types

| Construct                  | ili Kind    | Mandatory v1 | Implemented |
|----------------------------|-------------|:------------:|:-----------:|
| ModelData.ClassRefType     | CLASS       |      ✅       |      ✅      |
| ModelData.ObjectType       | CLASS       |      ✅       |      ✅      |
| ModelData.AttributeRefType | CLASS       |      ❌       |      ✅      |
| ModelData.ARefOf           | ASSOCIATION |      ❌       |      ✅      |
| ModelData.ARefRestriction  | ASSOCIATION |      ❌       |      ✅      |

## Enumerations

| Construct                   | ili Kind    | Mandatory v1 | Implemented |
|-----------------------------|-------------|:------------:|:-----------:|
| ModelData.EnumType          | CLASS       |      ✅       |      ✅      |
| ModelData.EnumNode          | CLASS       |      ✅       |      ✅      |
| ModelData.TopNode           | ASSOCIATION |      ✅       |      ✅      |
| ModelData.SubNode           | ASSOCIATION |      ✅       |      ✅      |
| ModelData.EnumTreeValueType | CLASS       |      ✅       |      ✅      |
| ModelData.TreeValueTypeOf   | ASSOCIATION |      ✅       |      ✅      |

## Line types

| Construct                   | ili Kind    | Mandatory v1 | Implemented |
|-----------------------------|-------------|:------------:|:-----------:|
| ModelData.LineForm          | CLASS       |      ✅       |      ✅      |
| ModelData.LineFormStructure | ASSOCIATION |      ✅       |      ✅      |
| ModelData.LineType          | CLASS       |      ✅       |      ✅      |
| ModelData.LinesForm         | ASSOCIATION |      ✅       |      ✅      |
| ModelData.LineCoord         | ASSOCIATION |      ✅       |      ✅      |
| ModelData.LineAttr          | ASSOCIATION |      ❌       |      ✅      |

## Views

| Construct                 | ili Kind    | Mandatory v1 | Implemented |
|---------------------------|-------------|:------------:|:-----------:|
| ModelData.View            | CLASS       |      ✅       |      ✅      |
| ModelData.RenamedBaseView | CLASS       |      ✅       |      ✅      |
| ModelData.BaseViewDef     | ASSOCIATION |      ✅       |      ✅      |
| ModelData.BaseViewRef     | ASSOCIATION |      ✅       |      ✅      |
| ModelData.DerivedAssoc    | ASSOCIATION |      ✅       |      ✅      |

## Expressions, factors

| Construct                  | ili Kind  | Mandatory v1 | Implemented |
|----------------------------|-----------|:------------:|:-----------:|
| ModelData.UnaryExpr        | STRUCTURE |      ✅       |      ✅      |
| ModelData.CompoundExpr     | STRUCTURE |      ✅       |      ✅      |
| ModelData.Factor           | STRUCTURE |      ✅       |      ✅      |
| ModelData.PathEl           | STRUCTURE |      ✅       |      ✅      |
| ModelData.PathOrInspFactor | STRUCTURE |      ✅       |      ✅      |
| ModelData.EnumAssignment   | STRUCTURE |      ❌       |      ✅      |
| ModelData.EnumMapping      | STRUCTURE |      ❌       |      ✅      |
| ModelData.ClassRef         | STRUCTURE |      ❌       |      ✅      |
| ModelData.ActualArgument   | STRUCTURE |      ❌       |      ✅      |
| ModelData.FunctionCall     | STRUCTURE |      ❌       |      ✅      |
| ModelData.RuntimeParamRef  | STRUCTURE |      ❌       |      ✅      |
| ModelData.Constant         | STRUCTURE |      ✅       |      ✅      |
| ModelData.ClassConst       | STRUCTURE |      ❌       |      ✅      |
| ModelData.AttributeConst   | STRUCTURE |      ❌       |      ✅      |
| ModelData.UnitRef          | STRUCTURE |      ✅       |      ✅      |
| ModelData.UnitFunction     | STRUCTURE |      ✅       |      ✅      |

## Constraints

| Construct                     | ili Kind    | Mandatory v1 | Implemented |
|-------------------------------|-------------|:------------:|:-----------:|
| ModelData.SimpleConstraint    | CLASS       |      ✅       |      ✅      |
| ModelData.ExistenceConstraint | CLASS       |      ❌       |      ✅      |
| ModelData.ExistenceDef        | ASSOCIATION |      ❌       |      ✅      |
| ModelData.UniqueConstraint    | CLASS       |      ✅       |      ✅      |
| ModelData.SetConstraint       | CLASS       |      ✅       |      ✅      |

## Graphic

| Construct                         | ili Kind    | Mandatory v1 | Implemented |
|-----------------------------------|-------------|:------------:|:-----------:|
| ModelData.Graphic                 | CLASS       |      ❌       |      ✅      |
| ModelData.GraphicBase             | ASSOCIATION |      ❌       |      ✅      |
| ModelData.SignParamAssignment     | STRUCTURE   |      ❌       |      ✅      |
| ModelData.CondSignParamAssignment | STRUCTURE   |      ❌       |      ✅      |
| ModelData.DrawingRule             | CLASS       |      ❌       |      ✅      |
| ModelData.GraphicRule             | ASSOCIATION |      ❌       |      ✅      |
| ModelData.SignClass               | ASSOCIATION |      ❌       |      ✅      |

## Translation

| Construct                           | ili Kind  | Mandatory v1 | Implemented |
|-------------------------------------|-----------|:------------:|:-----------:|
| ModelTranslation.DocTextTranslation | STRUCTURE |      ✅       |      ❌      |
| ModelTranslation.METranslation      | STRUCTURE |      ✅       |      ❌      |
| ModelTranslation.Translation        | CLASS     |      ✅       |      ❌      |

