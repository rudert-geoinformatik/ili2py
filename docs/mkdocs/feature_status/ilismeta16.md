# Read Metamodel

This is about the necessary constructions to read an arbitrary INTERLIS Metamodel File (`*.imd`) in the
[ilismeta16](https://models.interlis.ch/core/IlisMeta16.ili) format. So about parsing the XML/XTF.

The following overview tries to reflect the order and structure how it is defined in the above linked
ILI file.

| ‼️  Currently, 67 of 126 ilismeta16 constructs are missing (~53%). |
|-------------------------------------------------------------------------------|

## MetaElements in general

| Construct                | ili Kind       | Implemented | Code                                                                                                                                         | Comment |
|--------------------------|----------------|:-----------:|----------------------------------------------------------------------------------------------------------------------------------------------|---------|
| ModelData.DocText        | STRUCTURE      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element.DocTextElement)                       |         |
| ModelData.MetaElement    | CLASS ABSTRACT |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.meta_element.MetaElement)                              |         |
| ModelData.MetaAttribute  | CLASS          |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element.MetaAttributeElement)                 |         |
| ModelData.MetaAttributes | ASSOCIATION    |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element.MetaAttributeElement.MetaElement_ref) |         |
| ModelData.ExtendableME   | CLASS          |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.ExtendableMe)              |         |
| ModelData.Inheritance    | ASSOCIATION    |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.ExtendableMe.Super_ref)    |         |

## Models

| Construct                  | ili Kind       | Implemented | Code                                                                                                                                                   | Comment                                                        |
|----------------------------|----------------|:-----------:|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| ModelData.Package          | CLASS ABSTRACT |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.package.package.Package)                                         |                                                                |
| ModelData.Ili1Format       | STRUCTURE      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element.Ili1FormatElement)                              |                                                                |
| ModelData.Model            | CLASS          |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.package.package.Model)                                           |                                                                |
| ModelData.SubModel         | CLASS          |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.package.package.SubModel)                                        |                                                                |
| ModelData.PackageElements  | ASSOCIATION    |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.meta_element.MetaElement.ElementInPackage_ref)                   |                                                                |
| ModelData.Import           | ASSOCIATION    |      ❌      |                                                                                                                                                        | Not implemented yet.                                           |
| ModelData.Type             | CLASS          |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class.Type)                              |                                                                |
| ModelData.Expression       | STRUCTURE      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.expression.Expression)             |                                                                |
| ModelData.Multiplicity     | STRUCTURE      |     (✅)     | [Link](http://127.0.0.1:8000/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.serialization_elements.MultiplicityElement) | [Bug](https://github.com/rudert-geoinformatik/ili2py/issues/3) |
| ModelData.Constraint       | CLASS ABSTRACT |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.constraints.Constraint)                                          |                                                                |
| ModelData.DomainType       | CLASS ABSTRACT |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.DomainType)           |                                                                |
| ModelData.DomainConstraint | ASSOCIATION    |      ❌      |                                                                                                                                                        | Not implemented yet.                                           |

## Classes

| Construct                 | ili Kind    | Implemented | Code                                                                                                                                           | Comment                                                         |
|---------------------------|-------------|:-----------:|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| ModelData.Class           | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class.Class)                     |                                                                 |
| ModelData.AttrOrParam     | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.AttrOrParam)                 |                                                                 |
| ModelData.ClassConstraint | ASSOCIATION |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.constraints.Constraint.ToClass_ref)                      |                                                                 |
| ModelData.LocalType       | ASSOCIATION |      ❌      |                                                                                                                                                | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.AttrOrParamType | ASSOCIATION |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.AttrOrParam.Type_ref)        |                                                                 |
| ModelData.ClassAttr       | ASSOCIATION |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.AttrOrParam.AttrParent_ref)  |                                                                 |
| ModelData.ClassParam      | ASSOCIATION |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.AttrOrParam.ParamParent_ref) |                                                                 |

## Types related to other types

| Construct                 | ili Kind       | Implemented | Code                                                                                                                                                           | Comment              |
|---------------------------|----------------|:-----------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| ModelData.TypeRelatedType | CLASS ABSTRACT |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.TypeRelatedType)              |                      |
| ModelData.BaseType        | ASSOCIATION    |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.TypeRelatedType.BaseType_ref) |                      |
| ModelData.TypeRestriction | ASSOCIATION    |      ❌      |                                                                                                                                                                | Not implemented yet. |

## Bag type

| Construct            | ili Kind | Implemented | Code                                                                                                                                         | Comment |
|----------------------|----------|:-----------:|----------------------------------------------------------------------------------------------------------------------------------------------|---------|
| ModelData.MultiValue | CLASS    |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.MultiValue) |         |

## References and associations

| Construct                     | ili Kind       | Implemented | Code                                                                                                                                                                         | Comment                                                         |
|-------------------------------|----------------|:-----------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| ModelData.ClassRelatedType    | CLASS ABSTRACT |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type.ClassRelatedType) |                                                                 |
| ModelData.BaseClass           | ASSOCIATION    |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class.BaseClass)                                               |                                                                 |
| ModelData.ClassRestriction    | ASSOCIATION    |      ❌      |                                                                                                                                                                              | Not implemented yet.                                            |
| ModelData.ReferenceType       | CLASS          |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type.ReferenceType)    |                                                                 |
| ModelData.Role                | CLASS          |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.role.Role)                           |                                                                 |
| ModelData.AssocRole           | ASSOCIATION    |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.role.Role.Association_ref)           |                                                                 |
| ModelData.ExplicitAssocAccess | CLASS          |      ❌      |                                                                                                                                                                              | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.ExplicitAssocAcc    | ASSOCIATION    |      ❌      |                                                                                                                                                                              | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.AssocAccOrigin      | ASSOCIATION    |      ❌      |                                                                                                                                                                              | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.AssocAccTarget      | ASSOCIATION    |      ❌      |                                                                                                                                                                              | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.AssocAcc            | ASSOCIATION    |      ❌      |                                                                                                                                                                              | Not implemented yet. Tested models does not seem to contain it. |

## Information for easy transfer

| Construct                     | ili Kind    | Implemented | Code | Comment              |
|-------------------------------|-------------|:-----------:|------|----------------------|
| ModelData.TransferElement     | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.Ili1TransferElement | ASSOCIATION |      ❌      |      | Not implemented yet. |

## DataUnits

| Construct                 | ili Kind    | Implemented | Code                                                                                                                        | Comment                                                         |
|---------------------------|-------------|:-----------:|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| ModelData.DataUnit        | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.DataUnit) |                                                                 |
| ModelData.Dependency      | ASSOCIATION |      ❌      |                                                                                                                             | [TODO](https://github.com/rudert-geoinformatik/ili2py/issues/5) |
| ModelData.AllowedInBasket | ASSOCIATION |      ❌      |                                                                                                                             | [TODO](https://github.com/rudert-geoinformatik/ili2py/issues/6) |

## Generics and Contexts (INTERLIS 2.4 only)

| Construct                    | ili Kind    | Implemented | Code | Comment                                                         |
|------------------------------|-------------|:-----------:|------|-----------------------------------------------------------------|
| ModelData.Context            | CLASS       |      ❌      |      | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.GenericDef         | ASSOCIATION |      ❌      |      | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.ConcreteForGeneric | ASSOCIATION |      ❌      |      | Not implemented yet. Tested models does not seem to contain it. |

## Units

| Construct      | ili Kind | Implemented | Code                                                                                                                    | Comment                                                         |
|----------------|----------|:-----------:|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| ModelData.Unit | CLASS    |     (✅)     | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.Unit) | [TODO](https://github.com/rudert-geoinformatik/ili2py/issues/4) |

## MetaObjects

| Construct                   | ili Kind    | Implemented | Code | Comment              |
|-----------------------------|-------------|:-----------:|------|----------------------|
| ModelData.MetaBasketDef     | CLASS       |      ❌      |      | Not implemented yet. |
| ModelData.MetaDataUnit      | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.MetaObjectDef     | CLASS       |      ❌      |      | Not implemented yet. |
| ModelData.MetaBasketMembers | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.MetaObjectClass   | ASSOCIATION |      ❌      |      | Not implemented yet. |

## Base types

| Construct                | ili Kind    | Implemented | Code                                                                                                                                                       | Comment              |
|--------------------------|-------------|:-----------:|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| ModelData.BooleanType    | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.BooleanType)              |                      |
| ModelData.TextType       | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.TextType)                 |                      |
| ModelData.BlackboxType   | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.BlackboxType)             |                      |
| ModelData.NumType        | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.NumType)                  |                      |
| ModelData.NumUnit        | ASSOCIATION |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.NumType.Unit_ref)         |                      |
| ModelData.CoordType      | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.CoordType)                |                      |
| ModelData.AxisSpec       | ASSOCIATION |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.AxisSpec)                 |                      |
| ModelData.NumsRefSys     | ASSOCIATION |      ❌      |                                                                                                                                                            | Not implemented yet. |
| ModelData.FormattedType  | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.FormattedType)            |                      |
| ModelData.StructOfFormat | ASSOCIATION |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.FormattedType.Struct_ref) |                      |

## OID Definition

| Construct            | ili Kind    | Implemented | Code | Comment              |
|----------------------|-------------|:-----------:|------|----------------------|
| ModelData.AnyOIDType | CLASS       |      ❌      |      | Not implemented yet. |
| ModelData.ObjectOID  | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.BasketOID  | ASSOCIATION |      ❌      |      | Not implemented yet. |

## Functions

| Construct                | ili Kind    | Implemented | Code | Comment              |
|--------------------------|-------------|:-----------:|------|----------------------|
| ModelData.FunctionDef    | CLASS       |      ❌      |      | Not implemented yet. |
| ModelData.LocalFType     | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.ResultType     | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.Argument       | CLASS       |      ❌      |      | Not implemented yet. |
| ModelData.FormalArgument | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.ArgumentType   | ASSOCIATION |      ❌      |      | Not implemented yet. |

## Class and attribute reference types

| Construct                  | ili Kind    | Implemented | Code                                                                                                                                                                     | Comment              |
|----------------------------|-------------|:-----------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| ModelData.ClassRefType     | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type.ClassRefType) |                      |
| ModelData.ObjectType       | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type.ObjectType)   |                      |
| ModelData.AttributeRefType | CLASS       |      ❌      |                                                                                                                                                                          | Not implemented yet. |
| ModelData.ARefOf           | ASSOCIATION |      ❌      |                                                                                                                                                                          | Not implemented yet. |
| ModelData.ARefRestriction  | ASSOCIATION |      ❌      |                                                                                                                                                                          | Not implemented yet. |

## Enumerations

| Construct                   | ili Kind    | Implemented | Code                                                                                                                                       | Comment              |
|-----------------------------|-------------|:-----------:|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| ModelData.EnumType          | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.EnumType) |                      |
| ModelData.EnumNode          | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.EnumNode)                |                      |
| ModelData.TopNode           | ASSOCIATION |      ❌      |                                                                                                                                            | Not implemented yet. |
| ModelData.SubNode           | ASSOCIATION |      ❌      |                                                                                                                                            | Not implemented yet. |
| ModelData.EnumTreeValueType | CLASS       |      ❌      |                                                                                                                                            | Not implemented yet. |
| ModelData.TreeValueTypeOf   | ASSOCIATION |      ❌      |                                                                                                                                            | Not implemented yet. |

## Line types

| Construct                   | ili Kind    | Implemented | Code                                                                                                                                                     | Comment              |
|-----------------------------|-------------|:-----------:|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| ModelData.LineForm          | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.line_form.LineForm)                                                |                      |
| ModelData.LineFormStructure | ASSOCIATION |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.line_form.LineForm.Structure_ref)                                  |                      |
| ModelData.LineType          | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.LineType)               |                      |
| ModelData.LinesForm         | ASSOCIATION |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.line_form.LinesForm)                                               |                      |
| ModelData.LineCoord         | ASSOCIATION |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.LineType.CoordType_ref) |                      |
| ModelData.LineAttr          | ASSOCIATION |      ❌      |                                                                                                                                                          | Not implemented yet. |

## Views

| Construct                 | ili Kind    | Implemented | Code | Comment              |
|---------------------------|-------------|:-----------:|------|----------------------|
| ModelData.View            | CLASS       |      ❌      |      | Not implemented yet. |
| ModelData.RenamedBaseView | CLASS       |      ❌      |      | Not implemented yet. |
| ModelData.BaseViewDef     | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.BaseViewRef     | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.DerivedAssoc    | ASSOCIATION |      ❌      |      | Not implemented yet. |

## Expressions, factors

| Construct                  | ili Kind  | Implemented | Code                                                                                                                                                | Comment                                                         |
|----------------------------|-----------|:-----------:|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| ModelData.UnaryExpr        | STRUCTURE |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.expression.UnaryExpr)           |                                                                 |
| ModelData.CompoundExpr     | STRUCTURE |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.expression.CompoundExpr)        |                                                                 |
| ModelData.Factor           | STRUCTURE |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor.Factor)           |                                                                 |
| ModelData.PathEl           | STRUCTURE |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.path_elements.PathElElement)                                  |                                                                 |
| ModelData.PathOrInspFactor | STRUCTURE |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor.PathOrInspFactor) |                                                                 |
| ModelData.EnumAssignment   | STRUCTURE |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.EnumMapping      | STRUCTURE |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.ClassRef         | STRUCTURE |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.ActualArgument   | STRUCTURE |      ❌      |                                                                                                                                                     | Not implemented yet.                                            |
| ModelData.FunctionCall     | STRUCTURE |      ❌      |                                                                                                                                                     | Not implemented yet.                                            |
| ModelData.RuntimeParamRef  | STRUCTURE |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.Constant         | STRUCTURE |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor.Constant)         |                                                                 |
| ModelData.ClassConst       | STRUCTURE |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.AttributeConst   | STRUCTURE |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| ModelData.UnitRef          | STRUCTURE |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor.UnitRef)          |                                                                 |
| ModelData.UnitFunction     | STRUCTURE |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor.UnitFunction)     |                                                                 |

## Constraints

| Construct                     | ili Kind    | Implemented | Code                                                                                                                | Comment              |
|-------------------------------|-------------|:-----------:|---------------------------------------------------------------------------------------------------------------------|----------------------|
| ModelData.SimpleConstraint    | CLASS       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.constraints.SimpleConstraint) |                      |
| ModelData.ExistenceConstraint | CLASS       |      ❌      |                                                                                                                     | Not implemented yet. |
| ModelData.ExistenceDef        | ASSOCIATION |      ❌      |                                                                                                                     | Not implemented yet. |
| ModelData.UniqueConstraint    | CLASS       |      ❌      |                                                                                                                     | Not implemented yet. |
| ModelData.SetConstraint       | CLASS       |      ❌      |                                                                                                                     | Not implemented yet. |

## Graphic

| Construct                         | ili Kind    | Implemented | Code | Comment              |
|-----------------------------------|-------------|:-----------:|------|----------------------|
| ModelData.Graphic                 | CLASS       |      ❌      |      | Not implemented yet. |
| ModelData.GraphicBase             | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.SignParamAssignment     | STRUCTURE   |      ❌      |      | Not implemented yet. |
| ModelData.CondSignParamAssignment | STRUCTURE   |      ❌      |      | Not implemented yet. |
| ModelData.DrawingRule             | CLASS       |      ❌      |      | Not implemented yet. |
| ModelData.GraphicRule             | ASSOCIATION |      ❌      |      | Not implemented yet. |
| ModelData.SignClass               | ASSOCIATION |      ❌      |      | Not implemented yet. |

## Translation

| Construct                           | ili Kind  | Implemented | Code | Comment              |
|-------------------------------------|-----------|:-----------:|------|----------------------|
| ModelTranslation.DocTextTranslation | STRUCTURE |      ❌      |      | Not implemented yet. |
| ModelTranslation.METranslation      | STRUCTURE |      ❌      |      | Not implemented yet. |
| ModelTranslation.Translation        | CLASS     |      ❌      |      | Not implemented yet. |

