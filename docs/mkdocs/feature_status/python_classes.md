!!! info
This part is a demonstrator to show a possible usage of the python bindings.

Its aim is to generate a pure python library reflecting the understanding of the underlying Interlis model.
Meaning a low level network of
interdependent classes which may be used to read XTF-data of the model in question, but also access the
specifics of the model like constraints, types, restrictions etc.

It should not be understood as a standalone library serving already a purpose but as a basic compilation
artifact which then can be used in domain specific python applications to handle the desired data. This way
the application can be written with a mapping layer to the compiled interface. In case the underling Interlis
model changes, only that layer has to be adapted to the newly compiled version of the interface.

Why to compile the model to source coda anyway? This is a performance question and a matter of explicit
formulation. This enables usage of known development toolchains like gitops, packaging. In addition, it
enables developer convenience type-completion while coding, typing, in editor docs, prevention of errors.

As a part of the initial project we defined
[requirements](https://github.com/rudert-geoinformatik/ili2py/discussions/16)

| Description                                                                                                                                                                                                                                                                                                               | Mandatory | Implemented |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------:|:-----------:|
| one python package per INTERLIS model                                                                                                                                                                                                                                                                                     |     ✅     |      ✅      |
| everything within a model without TOPIC goes to `__init__.py`                                                                                                                                                                                                                                                             |     ✅     |      ✅      |
| one python file per topic in the regarding model package                                                                                                                                                                                                                                                                  |     ✅     |      ✅      |
| Classes will be Python classes                                                                                                                                                                                                                                                                                            |     ✅     |      ✅      |
| attributes will be Python class attributes                                                                                                                                                                                                                                                                                |     ✅     |      ✅      |
| attribute types will be defined in the pythonic way  (library has to be self containing)                                                                                                                                                                                                                                  |     ✅     |      ✅      |
| Domain-Definitions are stored in `__init__.py`                                                                                                                                                                                                                                                                            |     ✅     |      ✅      |
| Type constraints are read and stored so that other tools can use them later. ili2py does not validate those.                                                                                                                                                                                                              |     ✅     |      ✅      |
| Constraints are read and stored so that other tools can use them later. ili2py does not validate those.                                                                                                                                                                                                                   |     ✅     |      ✅      |
| Inline documentation from model files (ili) is stored as Docstrings for each corresponding element. The style of the python doc strings is the [Google notation](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) since it is well readable in the source code and widely supported by tools. |     ✅     |      ✅      |
| Associations are stored as references. This is done to be agnostic to later usage in tools. With this construction associations can always be determined cleanly.                                                                                                                                                         |     ✅     |      ✅      |
| Information about association constraints (e.g. 1:n, etc.) are read and stored for later use by other tools. ili2py does not validate those.                                                                                                                                                                              |     ✅     |      ✅      |
| Inheritance is implemented with Python class inheritance 1:1 as defined in the INTERLIS model.                                                                                                                                                                                                                            |     ✅     |      ✅      |