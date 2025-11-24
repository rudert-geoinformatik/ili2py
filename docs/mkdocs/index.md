
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

## What's next

There are already ideas and follow-up projects around. Feel free to reach out if you are interested in those, or you
have an idea you want to discuss.

### QGIS XTF Object browser

<figure class="video_container">
  <video controls="true" allowfullscreen="true">
    <source src="assets/video/qgis_xtf_browser.mp4" type="video/mp4">
  </video>
</figure>

This quick draft to show how we could navigate through the objects loaded from an XTF via the python classes generated
by **_ili2py_**. Only feature we use here is the layers which contains the geometry and a field for the OID. All the rest
happens in memory in the object world. No ORM in place!
Since we are able to read/write valid XTF with the python classes, the next steps are obvious: Instead of only showing
the information we can make it editable. This would enable quick inspection of Interlis data, to fix typos or other stuff
including geometries.

### Interlis Object Flow

<figure class="video_container">
  <video controls="true" allowfullscreen="true">
    <source src="assets/video/interlis_object_flow.mp4" type="video/mp4">
  </video>
</figure>

This quick draft based on **_ili2py_** and the generated classes shows a QT (PyQT) canvas with nodes and ports to create data
flows to ETL XTF's directly. Because its QT it natively integrates with Python and QGIS.
The infinite canvas allows positioning of nodes all around. Patching ports of nodes with connectors to other nodes.
All elements including their position can bei serialized and therefore be stored. A styling inteface already allows
customization.

First usecases coming into my mind are:

- inter-model-transformer like MGDM2OEREB (but with a nice GUI and without XSLT)
- XTF merger (when you have xtfs handled municipality wise)

Besides that, it would be a good foundation to a modern and easy to use UML editor.
