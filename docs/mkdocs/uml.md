# UML-Diagram generation

One of the demonstrator programms is the generation of UML-Diagrams from imd16. The following section gives
an overview about what formats are supported and the limitations.

!!! info
    Be aware, this project is not meant to be used to create UML-Diagrams you can edit later. It trys to
    produce the best automatic diagram with the different solutions instead. The approach is positioned more
    towards automation and forced regeneration of diagrams in a developer friendly way. Change the source
    (ili file) and regenerate. Never beautify by hand.

## Mermaid

[Mermaid](https://mermaid.js.org/syntax/classDiagram.html) is well known and widely used. Its strength is the 
wide support in many development tools (Ide's, github, gitlab, ...).

The format is a markdown code snippet. See mermaid documentation for details.

!!! danger
    The mermaid class diagram capabilities are limited. In addition, they depend heavily on the renderer you
    use to generate the diagram out of the markdown. That may be the plugin of your Ide, your browser or
    something else.

### Limitations

Currently, known limitations are:

- Nesting of [namespaces](https://mermaid.js.org/syntax/classDiagram.html#define-namespace) is not supported
  by mermaid.
- Potentially broken self references (awkward rendering of Cardinalities, strange positioning of connectors).
- routing of connectors between classes is a bit flaky especially when it comes to larger diagrams

![](assets/img/mermaid_example.png)

## PlantUML

[PlantUML](https://plantuml.com/en/class-diagram) is a non-interactive tool which renders a specific syntax
text file into the desired output. The aim is to automation here too. We want to transform the understanding
of imd16 into an uml diagram without any further tuning. This is, what PlantUML is good for. It renders
quickly and produces nice outputs even on larger diagrams with a lot of content. Especially the routing of the
connectors is looking better than with mermaid.

![](assets/img/plantuml_example.png)
