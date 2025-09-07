
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


