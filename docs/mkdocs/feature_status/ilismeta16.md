# Read Metamodel

This is about the necessary constructions to read an arbitrary INTERLIS Metamodel File (`*.imd`) in the
[ilismeta16](https://models.interlis.ch/core/IlisMeta16.ili) format. So about parsing the XML/XTF.

The following overview tries to reflect the order and structure how it is defined in the above linked
ILI file.

| ‼️  Currently, 67 of 126 ilismeta16 constructs are missing (~53%). |
|-------------------------------------------------------------------------------|

## MetaElements in general

| id    | Construct                | ili Kind       | Mandatory v1 | Implemented | Code                                                                                                                                         | Comment |
|-------|--------------------------|----------------|:------------:|:-----------:|----------------------------------------------------------------------------------------------------------------------------------------------|---------|
| 1 | ModelData.DocText           | STRUCTURE      |      ✅       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element.DocTextElement)                       |         |
| 2     | ModelData.MetaElement    | CLASS ABSTRACT |      ✅       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.meta_element.MetaElement)                              |         |
| 3     | ModelData.MetaAttribute  | CLASS          |      ✅       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element.MetaAttributeElement)                 |         |
| 4     | ModelData.MetaAttributes | ASSOCIATION    |      ✅       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element.MetaAttributeElement.MetaElement_ref) |         |
| 5     | ModelData.ExtendableME   | CLASS          |      ✅       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.ExtendableMe)              |         |
| 6     | ModelData.Inheritance    | ASSOCIATION    |      ✅       |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.ExtendableMe.Super_ref)    |         |

## Models

| id | Construct                  | ili Kind       | Mandatory v1 | Implemented | Code                                                                                                                                                   | Comment                                                        |
|----|----------------------------|----------------|:-----------:|:-----------:|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| 7  | ModelData.Package          | CLASS ABSTRACT |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.package.package.Package)                                         |                                                                |
| 8  | ModelData.Ili1Format       | STRUCTURE      |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.abstract_element.Ili1FormatElement)                              |                                                                |
| 9  | ModelData.Model            | CLASS          |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.package.package.Model)                                           |                                                                |
| 10 | ModelData.SubModel         | CLASS          |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.package.package.SubModel)                                        |                                                                |
| 11 | ModelData.PackageElements  | ASSOCIATION    |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.meta_element.MetaElement.ElementInPackage_ref)                   |                                                                |
| 12 | ModelData.Import           | ASSOCIATION    |      ❌      |      ❌      |                                                                                                                                                        | Not implemented yet.                                           |
| 13 | ModelData.Type             | CLASS          |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class.Type)                              |                                                                |
| 14 | ModelData.Expression       | STRUCTURE      |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.expression.Expression)             |                                                                |
| 15 | ModelData.Multiplicity     | STRUCTURE      |     (✅)     |     (✅)     | [Link](http://127.0.0.1:8000/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.serialization_elements.MultiplicityElement) | [Bug](https://github.com/rudert-geoinformatik/ili2py/issues/3) |
| 16 | ModelData.Constraint       | CLASS ABSTRACT |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.constraints.Constraint)                                          |                                                                |
| 17 | ModelData.DomainType       | CLASS ABSTRACT |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.DomainType)           |                                                                |
| 18 | ModelData.DomainConstraint | ASSOCIATION    |      ❌      |      ❌      |                                                                                                                                                        | Not implemented yet.                                           |

## Classes

| id | Construct                 | ili Kind    | Mandatory v1 | Implemented | Code                                                                                                                                           | Comment                                                         |
|----|---------------------------|-------------|:-----------:|:-----------:|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| 19 | ModelData.Class           | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class.Class)                     |                                                                 |
| 20 | ModelData.AttrOrParam     | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.AttrOrParam)                 |                                                                 |
| 21 | ModelData.ClassConstraint | ASSOCIATION |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.constraints.Constraint.ToClass_ref)                      |                                                                 |
| 22 | ModelData.LocalType       | ASSOCIATION |      ❌      |      ❌      |                                                                                                                                                | Not implemented yet. Tested models does not seem to contain it. |
| 23 | ModelData.AttrOrParamType | ASSOCIATION |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.AttrOrParam.Type_ref)        |                                                                 |
| 24 | ModelData.ClassAttr       | ASSOCIATION |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.AttrOrParam.AttrParent_ref)  |                                                                 |
| 25 | ModelData.ClassParam      | ASSOCIATION |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.AttrOrParam.ParamParent_ref) |                                                                 |

## Types related to other types

| id | Construct                 | ili Kind       | Mandatory v1 | Implemented | Code                                                                                                                                                           | Comment              |
|----|---------------------------|----------------|:-----------:|:-----------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| 26 | ModelData.TypeRelatedType | CLASS ABSTRACT |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.TypeRelatedType)              |                      |
| 27 | ModelData.BaseType        | ASSOCIATION    |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.TypeRelatedType.BaseType_ref) |                      |
| 28 | ModelData.TypeRestriction | ASSOCIATION    |      ❌      |      ❌      |                                                                                                                                                                | Not implemented yet. |

## Bag type

| id | Construct            | ili Kind | Mandatory v1 | Implemented | Code                                                                                                                                         | Comment |
|----|----------------------|----------|:-----------:|:-----------:|----------------------------------------------------------------------------------------------------------------------------------------------|---------|
| 29 | ModelData.MultiValue | CLASS    |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.MultiValue) |         |

## References and associations

| id | Construct                     | ili Kind       | Mandatory v1 | Implemented | Code                                                                                                                                                                         | Comment                                                         |
|----|-------------------------------|----------------|:-----------:|:-----------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| 30 | ModelData.ClassRelatedType    | CLASS ABSTRACT |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type.ClassRelatedType) |                                                                 |
| 31 | ModelData.BaseClass           | ASSOCIATION    |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class.BaseClass)                                               |                                                                 |
| 32 | ModelData.ClassRestriction    | ASSOCIATION    |      ❌      |      ❌      |                                                                                                                                                                              | Not implemented yet.                                            || 4   | ModelData.ReferenceType       | CLASS          |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type.ReferenceType)    |                                                                 |
| 33 | ModelData.Role                | CLASS          |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.role.Role)                           |                                                                 |
| 34 | ModelData.AssocRole           | ASSOCIATION    |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.role.Role.Association_ref)           |                                                                 |
| 35 | ModelData.ExplicitAssocAccess | CLASS          |      ❌      |      ❌      |                                                                                                                                                                              | Not implemented yet. Tested models does not seem to contain it. |
| 37 | ModelData.ExplicitAssocAcc    | ASSOCIATION    |      ❌      |      ❌      |                                                                                                                                                                              | Not implemented yet. Tested models does not seem to contain it. |
| 38 | ModelData.AssocAccOrigin      | ASSOCIATION    |      ❌      |      ❌      |                                                                                                                                                                              | Not implemented yet. Tested models does not seem to contain it. |
| 39 | ModelData.AssocAccTarget      | ASSOCIATION    |      ❌      |      ❌      |                                                                                                                                                                              | Not implemented yet. Tested models does not seem to contain it. |
| 40 | ModelData.AssocAcc            | ASSOCIATION    |      ✅      |      ❌      |                                                                                                                                                                              | Not implemented yet. Tested models does not seem to contain it. |

## Information for easy transfer

| id | Construct                     | ili Kind    | Mandatory v1 | Implemented | Code | Comment              |
|----|-------------------------------|-------------|:-----------:|:-----------:|------|----------------------|
| 41 | ModelData.TransferElement     | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |
| 42 | ModelData.Ili1TransferElement | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |

## DataUnits

| id | Construct                 | ili Kind    | Mandatory v1 | Implemented | Code                                                                                                                        | Comment                                                         |
|----|---------------------------|-------------|:-----------:|:-----------:|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| 43 | ModelData.DataUnit        | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.DataUnit) |                                                                 |
| 44 | ModelData.Dependency      | ASSOCIATION |      ❌      |      ❌      |                                                                                                                             | [TODO](https://github.com/rudert-geoinformatik/ili2py/issues/5) |
| 45  | ModelData.AllowedInBasket | ASSOCIATION |      ❌      |      ❌      |                                                                                                                             | [TODO](https://github.com/rudert-geoinformatik/ili2py/issues/6) |

## Generics and Contexts (INTERLIS 2.4 only)

| id | Construct                    | ili Kind    | Mandatory v1 | Implemented | Code | Comment                                                         |
|----|------------------------------|-------------|:-----------:|:-----------:|------|-----------------------------------------------------------------|
| 46 | ModelData.Context            | CLASS       |      ❌      |      ❌      |      | Not implemented yet. Tested models does not seem to contain it. |
| 47 | ModelData.GenericDef         | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. Tested models does not seem to contain it. |
| 48 | ModelData.ConcreteForGeneric | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. Tested models does not seem to contain it. |

## Units

| id | Construct      | ili Kind | Mandatory v1 | Implemented | Code                                                                                                                    | Comment                                                         |
|----|----------------|----------|:-----------:|:-----------:|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| 49 | ModelData.Unit | CLASS    |     (✅)     |     (✅)     | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.Unit) | [TODO](https://github.com/rudert-geoinformatik/ili2py/issues/4) |
 
## MetaObjects

| id | Construct                   | ili Kind    | Mandatory v1 | Implemented | Code | Comment              |
|----|-----------------------------|-------------|:-----------:|:-----------:|------|----------------------|
| 50 | ModelData.MetaBasketDef     | CLASS       |      ❌      |      ❌      |      | Not implemented yet. |
| 51 | ModelData.MetaDataUnit      | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |
| 52 | ModelData.MetaObjectDef     | CLASS       |      ❌      |      ❌      |      | Not implemented yet. |
| 53 | ModelData.MetaBasketMembers | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |
| 54 | ModelData.MetaObjectClass   | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |

## Base types

| id | Construct                | ili Kind    | Mandatory v1 | Implemented | Code                                                                                                                                                       | Comment              |
|----|--------------------------|-------------|:-----------:|:-----------:|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| 55 | ModelData.BooleanType    | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.BooleanType)              |                      |
| 56 | ModelData.TextType       | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.TextType)                 |                      |
| 57 | ModelData.BlackboxType   | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.BlackboxType)             |                      |
| 58 | ModelData.NumType        | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.NumType)                  |                      |
| 59 | ModelData.NumUnit        | ASSOCIATION |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.NumType.Unit_ref)         |                      |
| 60 | ModelData.CoordType      | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.CoordType)                |                      |
| 61 | ModelData.AxisSpec       | ASSOCIATION |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.AxisSpec)                 |                      |
| 62 | ModelData.NumsRefSys     | ASSOCIATION |      ✅      |      ❌      |                                                                                                                                                            | Not implemented yet. |
| 63 | ModelData.FormattedType  | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.FormattedType)            |                      |
| 64 | ModelData.StructOfFormat | ASSOCIATION |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.FormattedType.Struct_ref) |                      |

 ## OID Definition

| id | Construct            | ili Kind    | Mandatory v1 | Implemented | Code | Comment              |
|----|----------------------|-------------|:-----------:|:-----------:|------|----------------------|
| 65 | ModelData.AnyOIDType | CLASS       |      ✅      |      ❌      |      | Not implemented yet. |
| 66 | ModelData.ObjectOID  | ASSOCIATION |      ✅      |      ❌      |      | Not implemented yet. |
| 67 | ModelData.BasketOID  | ASSOCIATION |      ✅      |      ❌      |      | Not implemented yet. |
 
## Functions

| id | Construct                | ili Kind    | Mandatory v1 | Implemented | Code | Comment              |
|----|--------------------------|-------------|:-----------:|:-----------:|------|----------------------|
| 68 | ModelData.FunctionDef    | CLASS       |      ❌      |      ❌      |      | Not implemented yet. |
| 69 | ModelData.LocalFType     | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |
| 70 | ModelData.ResultType     | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |
| 71 | ModelData.Argument       | CLASS       |      ❌      |      ❌      |      | Not implemented yet. |
| 72 | ModelData.FormalArgument | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |
| 73 | ModelData.ArgumentType   | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |

## Class and attribute reference types

| id | Construct                  | ili Kind    | Mandatory v1 | Implemented | Code                                                                                                                                                                     | Comment              |
|----|----------------------------|-------------|:-----------:|:-----------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| 74 | ModelData.ClassRefType     | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type.ClassRefType) |                      |
| 75 | ModelData.ObjectType       | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.class_related_type.class_related_type.ObjectType)   |                      |
| 76 | ModelData.AttributeRefType | CLASS       |      ❌      |      ❌      |                                                                                                                                                                          | Not implemented yet. |
| 77 | ModelData.ARefOf           | ASSOCIATION |      ❌      |      ❌      |                                                                                                                                                                          | Not implemented yet. |
| 78 | ModelData.ARefRestriction  | ASSOCIATION |      ❌      |      ❌      |                                                                                                                                                                          | Not implemented yet. |

## Enumerations

| id | Construct                   | ili Kind    | Mandatory v1 | Implemented | Code                                                                                                                                       | Comment              |
|----|-----------------------------|-------------|:-----------:|:-----------:|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| 79 | ModelData.EnumType          | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.EnumType) |                      |
| 80 | ModelData.EnumNode          | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me.EnumNode)                |                      |
| 81 | ModelData.TopNode           | ASSOCIATION |      ✅      |      ❌      |                                                                                                                                            | Not implemented yet. |
| 82 | ModelData.SubNode           | ASSOCIATION |      ✅      |      ❌      |                                                                                                                                            | Not implemented yet. |
| 83 | ModelData.EnumTreeValueType | CLASS       |      ✅      |      ❌      |                                                                                                                                            | Not implemented yet. |
| 84 | ModelData.TreeValueTypeOf   | ASSOCIATION |      ✅      |      ❌      |                                                                                                                                            | Not implemented yet. |

## Line types

| id | Construct                   | ili Kind    | Mandatory v1 | Implemented | Code                                                                                                                                                     | Comment              |
|----|-----------------------------|-------------|:-----------:|:-----------:|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| 85 | ModelData.LineForm          | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.line_form.LineForm)                                                |                      |
| 86 | ModelData.LineFormStructure | ASSOCIATION |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.line_form.LineForm.Structure_ref)                                  |                      |
| 87 | ModelData.LineType          | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.LineType)               |                      |
| 88 | ModelData.LinesForm         | ASSOCIATION |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.line_form.LinesForm)                                               |                      |
| 89 | ModelData.LineCoord         | ASSOCIATION |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type.LineType.CoordType_ref) |                      |
| 90 |  ModelData.LineAttr         | ASSOCIATION |      ❌      |      ❌      |                                                                                                                                                          | Not implemented yet. |

## Views

| id | Construct                 | ili Kind    | Mandatory v1 | Implemented | Code | Comment              |
|----|---------------------------|-------------|:-----------:|:-----------:|------|----------------------|
| 91 | ModelData.View            | CLASS       |      ✅      |      ❌      |      | Not implemented yet. |
| 92 | ModelData.RenamedBaseView | CLASS       |      ✅      |      ❌      |      | Not implemented yet. |
| 93 | ModelData.BaseViewDef     | ASSOCIATION |      ✅      |      ❌      |      | Not implemented yet. |
| 94 | ModelData.BaseViewRef     | ASSOCIATION |      ✅      |      ❌      |      | Not implemented yet. |
| 95 | ModelData.DerivedAssoc    | ASSOCIATION |      ✅      |      ❌      |      | Not implemented yet. |

## Expressions, factors

| id  | Construct                  | ili Kind  | Mandatory v1 | Implemented | Code                                                                                                                                                | Comment                                                         |
|-----|----------------------------|-----------|:-----------:|:-----------:|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| 96  | ModelData.UnaryExpr        | STRUCTURE |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.expression.UnaryExpr)           |                                                                 |
| 97  | ModelData.CompoundExpr     | STRUCTURE |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.expression.CompoundExpr)        |                                                                 |
| 98  | ModelData.Factor           | STRUCTURE |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor.Factor)           |                                                                 |
| 99  | ModelData.PathEl           | STRUCTURE |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.path_elements.PathElElement)                                  |                                                                 |
| 100 | ModelData.PathOrInspFactor | STRUCTURE |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor.PathOrInspFactor) |                                                                 |
| 101 | ModelData.EnumAssignment   | STRUCTURE |      ❌      |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| 102 | ModelData.EnumMapping      | STRUCTURE |      ❌      |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| 103 | ModelData.ClassRef         | STRUCTURE |      ❌      |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| 104 | ModelData.ActualArgument   | STRUCTURE |      ❌      |      ❌      |                                                                                                                                                     | Not implemented yet.                                            |
| 105 | ModelData.FunctionCall     | STRUCTURE |      ❌      |      ❌      |                                                                                                                                                     | Not implemented yet.                                            |
| 106 | ModelData.RuntimeParamRef  | STRUCTURE |      ❌      |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| 107 | ModelData.Constant         | STRUCTURE |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor.Constant)         |                                                                 |
| 108 | ModelData.ClassConst       | STRUCTURE |      ❌      |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| 109 | ModelData.AttributeConst   | STRUCTURE |      ❌      |      ❌      |                                                                                                                                                     | Not implemented yet. Tested models does not seem to contain it. |
| 110 | ModelData.UnitRef          | STRUCTURE |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor.UnitRef)          |                                                                 |
| 111 | ModelData.UnitFunction     | STRUCTURE |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.expression.factor.factor.UnitFunction)     |                                                                 |

## Constraints

| id  | Construct                     | ili Kind    | Mandatory v1 | Implemented | Code                                                                                                                | Comment              |
|-----|-------------------------------|-------------|:-----------:|:-----------:|---------------------------------------------------------------------------------------------------------------------|----------------------|
| 112 | ModelData.SimpleConstraint    | CLASS       |      ✅      |      ✅      | [Link](/code/ilismeta16/#ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.constraints.SimpleConstraint) |                      |
| 113 | ModelData.ExistenceConstraint | CLASS       |      ❌      |      ❌      |                                                                                                                     | Not implemented yet. |
| 114 | ModelData.ExistenceDef        | ASSOCIATION |      ❌      |      ❌      |                                                                                                                     | Not implemented yet. |
| 115 | ModelData.UniqueConstraint    | CLASS       |      ❌      |      ❌      |                                                                                                                     | Not implemented yet. |
| 116 | ModelData.SetConstraint       | CLASS       |      ❌      |      ❌      |                                                                                                                     | Not implemented yet. |

## Graphic

| id  | Construct                         | ili Kind    | Mandatory v1 | Implemented | Code | Comment              |
|-----|-----------------------------------|-------------|:-----------:|:-----------:|------|----------------------|
| 117 | ModelData.Graphic                 | CLASS       |      ❌      |      ❌      |      | Not implemented yet. |
| 118 | ModelData.GraphicBase             | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |
| 119 | ModelData.SignParamAssignment     | STRUCTURE   |      ❌      |      ❌      |      | Not implemented yet. |
| 120 | ModelData.CondSignParamAssignment | STRUCTURE   |      ❌      |      ❌      |      | Not implemented yet. |
| 121 | ModelData.DrawingRule             | CLASS       |      ❌      |      ❌      |      | Not implemented yet. |
| 122 | ModelData.GraphicRule             | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |
| 123 | ModelData.SignClass               | ASSOCIATION |      ❌      |      ❌      |      | Not implemented yet. |

## Translation

| id  | Construct                           | ili Kind  | Mandatory v1 | Implemented | Code | Comment              |
|-----|-------------------------------------|-----------|:-----------:|:-----------:|------|----------------------|
| 124 | ModelTranslation.DocTextTranslation | STRUCTURE |      ❌      |      ❌      |      | Not implemented yet. |
| 125 | ModelTranslation.METranslation      | STRUCTURE |      ❌      |      ❌      |      | Not implemented yet. |
| 126 | ModelTranslation.Translation        | CLASS     |      ❌      |      ❌      |      | Not implemented yet. |

