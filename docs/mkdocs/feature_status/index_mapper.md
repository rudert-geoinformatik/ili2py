This part is topped up on features used by subsequent tools. Main purpose of this is about resolving
Associations, easing the access between linked elements for later usage. For example, it gives easy access to
all the attributes of a class without any additional iteration as it is really helpful for UML and Python
Class generation.

In the current status as of 09/2025 we consider **21/51 ASSOCIATIONS in ilisMeta16 as helpful** candidates for
indexing.

## MetaElements in general

| Construct                | ili Kind    | Mandatory v1 |                Implemented                 |
|--------------------------|-------------|:------------:|:------------------------------------------:|
| ModelData.MetaAttributes | ASSOCIATION |      ✅       | ✅<br/>`Index().metaelement_metaattributes` |
| ModelData.Inheritance    | ASSOCIATION |      ✅       |          `0..1<br/>(not relevant)          |

## Models

| Construct                  | ili Kind    | Mandatory v1 |                     Implemented                      |
|----------------------------|-------------|:------------:|:----------------------------------------------------:|
| ModelData.PackageElements  | ASSOCIATION |      ✅       |              `0..1`<br/>(not relevant)               |
| ModelData.Import           | ASSOCIATION |      ❌       | ✅<br/>`Index().imported_p`<br/>`Index().importing_p` |
| ModelData.DomainConstraint | ASSOCIATION |      ❌       |          ❌<br/>no usecase in tested models           |

## Classes

| Construct                 | ili Kind    | Mandatory v1 |              Implemented              |
|---------------------------|-------------|:------------:|:-------------------------------------:|
| ModelData.ClassConstraint | ASSOCIATION |      ✅       |   ❌<br/>no usecase in tested models   |
| ModelData.LocalType       | ASSOCIATION |      ❌       |       `0..1`<br/>(not relevant)       |
| ModelData.AttrOrParamType | ASSOCIATION |      ✅       |        `1`<br/>(not relevant)         |
| ModelData.ClassAttr       | ASSOCIATION |      ✅       | ✅<br/>`Index().class_class_attribute` |
| ModelData.ClassParam      | ASSOCIATION |      ✅       | ✅<br/>`Index().class_class_parameter` |

## Types related to other types

| Construct                 | ili Kind    | Mandatory v1 |            Implemented            |
|---------------------------|-------------|:------------:|:---------------------------------:|
| ModelData.BaseType        | ASSOCIATION |      ✅       |      `1`<br/>(not relevant)       |
| ModelData.TypeRestriction | ASSOCIATION |      ❌       | ❌<br/>no usecase in tested models |

## Bag type

No Associations in this group.

## References and associations

| Construct                  | ili Kind    | Mandatory v1 |                         Implemented                         |
|----------------------------|-------------|:------------:|:-----------------------------------------------------------:|
| ModelData.BaseClass        | ASSOCIATION |      ✅       | ✅<br/>`Index().base_class`<br/>`Index().class_related_type` |
| ModelData.ClassRestriction | ASSOCIATION |      ❌       |                              ❌                              |
| ModelData.AssocRole        | ASSOCIATION |      ✅       |                   `1`<br/>(not relevant)                    |
| ModelData.ExplicitAssocAcc | ASSOCIATION |      ❌       |                              ❌                              |
| ModelData.AssocAccOrigin   | ASSOCIATION |      ❌       |                              ❌                              |
| ModelData.AssocAccTarget   | ASSOCIATION |      ❌       |                              ❌                              |
| ModelData.AssocAcc         | ASSOCIATION |      ✅       |                ❌<br/>(pending clarification)                |

## Information for easy transfer

| Construct                     | ili Kind    | Mandatory v1 |                          Implemented                          |
|-------------------------------|-------------|:------------:|:-------------------------------------------------------------:|
| ModelData.TransferElement     | ASSOCIATION |      ❌       | ✅<br/>`Index().transfer_element`<br/>`Index().transfer_class` |
| ModelData.Ili1TransferElement | ASSOCIATION |      ❌       |                        (not relevant)                         |

## DataUnits

| Construct                 | ili Kind    | Mandatory v1 |                                          Implemented                                           |
|---------------------------|-------------|:------------:|:----------------------------------------------------------------------------------------------:|
| ModelData.Dependency      | ASSOCIATION |      ❌       |             ✅<br/>`Index().dependency_depends_on`<br/>`Index().dependency_used_by`             |
| ModelData.AllowedInBasket | ASSOCIATION |      ❌       | ✅<br/>`Index().allowed_in_basket_class_in_basket`<br/>`Index().allowed_in_basket_of_data_unit` |

## Generics and Contexts (INTERLIS 2.4 only)

| Construct                    | ili Kind    | Mandatory v1 | Implemented |
|------------------------------|-------------|:------------:|:-----------:|
| ModelData.GenericDef         | ASSOCIATION |      ❌       |      ❌      |
| ModelData.ConcreteForGeneric | ASSOCIATION |      ❌       |      ❌      |

## Units

No Associations in this group.

## MetaObjects

| Construct                   | ili Kind    | Mandatory v1 |       Implemented        |
|-----------------------------|-------------|:------------:|:------------------------:|
| ModelData.MetaDataUnit      | ASSOCIATION |      ❌       |  `1`<br/>(not relevant)  |
| ModelData.MetaBasketMembers | ASSOCIATION |      ❌       | `<#>`<br/>(not relevant) |
| ModelData.MetaObjectClass   | ASSOCIATION |      ❌       |  `1`<br/>(not relevant)  |

## Base types

| Construct                | ili Kind    | Mandatory v1 |                  Implemented                  |
|--------------------------|-------------|:------------:|:---------------------------------------------:|
| ModelData.NumUnit        | ASSOCIATION |      ✅       |            `1`<br/>(not relevant)             |
| ModelData.AxisSpec       | ASSOCIATION |      ✅       | ✅<br/>`Index().coord_type`<br/>`Index().axis` |
| ModelData.NumsRefSys     | ASSOCIATION |      ✅       |           `0..1`<br/>(not relevant)           |
| ModelData.StructOfFormat | ASSOCIATION |      ✅       |            `1`<br/>(not relevant)             |

## OID Definition

| Construct           | ili Kind    | Mandatory v1 |        Implemented        |
|---------------------|-------------|:------------:|:-------------------------:|
| ModelData.ObjectOID | ASSOCIATION |      ✅       | `0..1`<br/>(not relevant) |
| ModelData.BasketOID | ASSOCIATION |      ✅       | `0..1`<br/>(not relevant) |

## Functions

| Construct                | ili Kind    | Mandatory v1 |        Implemented        |
|--------------------------|-------------|:------------:|:-------------------------:|
| ModelData.LocalFType     | ASSOCIATION |      ❌       | `0..1`<br/>(not relevant) |
| ModelData.ResultType     | ASSOCIATION |      ❌       |  `1`<br/>(not relevant)   |
| ModelData.FormalArgument | ASSOCIATION |      ❌       | `<#>`<br/>(not relevant)  |
| ModelData.ArgumentType   | ASSOCIATION |      ❌       | `0..1`<br/>(not relevant) |

## Class and attribute reference types

| Construct                 | ili Kind    | Mandatory v1 |        Implemented        |
|---------------------------|-------------|:------------:|:-------------------------:|
| ModelData.ARefOf          | ASSOCIATION |      ❌       | `0..1`<br/>(not relevant) |
| ModelData.ARefRestriction | ASSOCIATION |      ❌       |             ❌             |

## Enumerations

| Construct                 | ili Kind    | Mandatory v1 |       Implemented        |
|---------------------------|-------------|:------------:|:------------------------:|
| ModelData.TopNode         | ASSOCIATION |      ✅       |  `1`<br/>(not relevant)  |
| ModelData.SubNode         | ASSOCIATION |      ✅       | `<#>`<br/>(not relevant) |
| ModelData.TreeValueTypeOf | ASSOCIATION |      ✅       |  `1`<br/>(not relevant)  |

## Line types

| Construct                   | ili Kind    | Mandatory v1 |                    Implemented                    |
|-----------------------------|-------------|:------------:|:-------------------------------------------------:|
| ModelData.LineFormStructure | ASSOCIATION |      ✅       |              `1`<br/>(not relevant)               |
| ModelData.LinesForm         | ASSOCIATION |      ✅       | ✅<br/>`Index().line_form`<br/>`Index().line_type` |
| ModelData.LineCoord         | ASSOCIATION |      ✅       |             `0..1`<br/>(not relevant)             |
| ModelData.LineAttr          | ASSOCIATION |      ❌       |             `0..1`<br/>(not relevant)             |

## Views

| Construct              | ili Kind    | Mandatory v1 |        Implemented        |
|------------------------|-------------|:------------:|:-------------------------:|
| ModelData.BaseViewDef  | ASSOCIATION |      ✅       | `<#>`<br/>(not relevant)  |
| ModelData.BaseViewRef  | ASSOCIATION |      ✅       |  `1`<br/>(not relevant)   |
| ModelData.DerivedAssoc | ASSOCIATION |      ✅       | `0..1`<br/>(not relevant) |

## Expressions, factors

No Associations in this group.

## Constraints

| Construct              | ili Kind    | Mandatory v1 |       Implemented        |
|------------------------|-------------|:------------:|:------------------------:|
| ModelData.ExistenceDef | ASSOCIATION |      ❌       | `<#>`<br/>(not relevant) |

## Graphic

| Construct             | ili Kind    | Mandatory v1 |        Implemented        |
|-----------------------|-------------|:------------:|:-------------------------:|
| ModelData.GraphicBase | ASSOCIATION |      ❌       | `0..1`<br/>(not relevant) |
| ModelData.GraphicRule | ASSOCIATION |      ❌       | `<#>`<br/>(not relevant)  |
| ModelData.SignClass   | ASSOCIATION |      ❌       | `0..1`<br/>(not relevant) |

## Translation

No Associations in this group.
