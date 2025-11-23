
**_ili2py_ is the [IlisMeta16](https://www.interlis.ch/modelle/metamodell) model (IMD16) in python.** Its aim is to natively
implement the understanding of the IMD16 representation of any ili model in python. It is a bridge library which can be used to
build python applications on top.

In its core **_ili2py_** offers handy mappers and indexed access to **all** constructs of the IMD16. This includes:

- classes and their attributes
- constraints
- geometries (incl. multi)
- structures
- associations
- and many many more...

On top **_ili2py_** offers already some built in applications to demonstrate its potential. These can be used directly
out of python or with an easy-to-use CLI.

## Diagrams

![](assets/img/diagrams/showcase.gif)

This program generates UML diagrams of different flavourss. Its advanced features are:

- **multiple TOPICS and MODELS in one diagram** to vizualize the broader context
- fine-grained settings for direction, distance and connector types
- filter to select which models should be drawn
- import based depth filter to easily filter diagram content
- and more...

Consult the [Userguide](user_guide/diagram.md) for more info.

## Python Classes

![](assets/img/python_classes/showcase.gif)

This program generates Python Classes representing 1:1 the classes defined in the Interlis model. Its advanced features are:

- **complete standalone python package structure** reflecting the desired interlis model
- based on python native dataclasses (**100% no 3rd party dependencies**)
- utilizes:
    - associations
    - constraints
    - meta attributes
    - enumerations
    - geometries
    - documentation
- delivers a well-structured and ready to use python package
- enables comfortable coding (autocompletion, jump-to-definition, documentation, ...)
- and many many more...

Consult the [Userguide](user_guide/python_classes.md) for more info.
