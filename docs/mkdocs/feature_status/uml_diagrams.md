!!! info
    This part is a demonstrator to show a possible usage of the python bindings.

Its aim is to put the knowledge about the IMD16 into an automatically generated UML diagram which is never
touched afterward. Usecase is the developer or data model designer who always writes Interlis models directly
as text and wants an easy documentation through GitOps based workflows.

Since the approach is purely automatic, it has its limitations. Namely, it always will lose against a manually
designed and placed UML diagram in terms of readability. However, for rapid development and changes in the
early project phases this is a valuable help. In addition, we can utilize different placement, connector style
and filter policies to reduce the downsides to a tolerable minimum.

As a part of the initial project we defined
[requirements](https://github.com/rudert-geoinformatik/ili2py/discussions/14) which were refined with this
[comment](https://github.com/rudert-geoinformatik/ili2py/discussions/14#discussioncomment-13206839).

|                                                                                  Description | Mandatory |                    Implemented                    |
|---------------------------------------------------------------------------------------------|:---------:|:-------------------------------------------------:|
|                                                                                      Classes |     ✅     |                         ✅                         |
|                                                                                   Attributes |     ✅     |                         ✅                         |
|                                                                                 Associations |     ✅     |                         ✅                         |
|                                                                                  Cardinality |     ✅     |                         ✅                         |
|                                                                                  Inheritance |     ✅     |                         ✅                         |
|                                                                                   Data types |     ✅     |                         ✅                         |
|                                                         Association role names on connectors |    💡     |                         ❌                         |
|                                                              Association names on connectors |    💡     |                         ✅                         |
|                                                      Filter of drawn models by CLI parameter |    💡     |                         ✅                         |
| Optimization of connector placement (Association/Inheritance) - less overlapping as possible |    ⚠️     | (✅)<br/>through `linetype` parameter for plantuml |

!!! info
    💡 = `Nice To Have`

    ⚠️ = `Should-have`

When ever relevant, this implementation follows Interlis
[umleditor](https://www.interlis.ch/en/downloads/umleditor) style as reference.
