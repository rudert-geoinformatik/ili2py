
The following section will guide you through some general usage of the python library by example.

It is based on the example given in the [start section](../user_guide/start.md) - the `OeREBKRMtrsfr_V2_0` model. If not
already done, you should head over and first create the python classes for that model as described.

!!! info
    The following examples preassume you have called you library ili2py_interface and you have a python script next to
    that resulting folder like:

    ![](../assets/img/python_classes_example_expected_structure.png)

!!! tip
    All following examples assume you are in a command line session in the root of the project as shown above.
    After each change in the script you need to execute the script with `python demo.py`

## Enumerations

As described in the [user guide](../user_guide/python_classes.md) enumeration are stored as native python enums. But
how you access them?

Add that to your python script.
```python
from ili2py_interface.OeREBKRM_V2_0 import RechtsStatus
print(list(RechtsStatus))
```

The output should look like:
`[<RechtsStatus.INKRAFT: 'inKraft'>, <RechtsStatus.AENDERUNGMITVORWIRKUNG: 'AenderungMitVorwirkung'>, <RechtsStatus.AENDERUNGOHNEVORWIRKUNG: 'AenderungOhneVorwirkung'>]`

So you can see that the information of the value list is there.

How to access the content?

Alter your script to.
```python
from ili2py_interface.OeREBKRM_V2_0 import RechtsStatus
print(list(RechtsStatus.INKRAFT.value))
```

The output should look like:
`ìnKraft`

This is how you access the value lists defined originally in the interlis model. You find them by following the linked
types in the IDE of your choice using go-to-definition features.

## Access metainformation

Each class and each field in the created library has meta information stored.

How can we access it?

```python
from ili2py_interface.OeREBKRMtrsfr_V2_0.Transferstruktur import Eigentumsbeschraenkung
from dataclasses import fields
print(fields(Eigentumsbeschraenkung)[2])
```

The output should look like:
```
Field(name='publiziertAb',type='str | None',default=None,default_factory=<dataclasses._MISSING_TYPE object at 0x7f0439902f90>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({'type': 'Element', 'namespace': 'http://www.interlis.ch/INTERLIS2.3', 'interlis': {'oid': 'OeREBKRMtrsfr_V2_0.Transferstruktur.Eigentumsbeschraenkung.publiziertAb', 'meta_attributes': {}, 'type_restrictions': {'mandatory': True, 'kind': None, 'format': '"Year"-"Month"-"Day"', 'unit': None, 'ref_sys': None, 'clockwise': None, 'circular': None, 'abstract': False, 'final': False, 'generic': False, 'super': 'OeREBKRM_V2_0.Datum', 'type_related_type': False, 'multiplicity': {'min': 1, 'max': 1}, 'struct': 'INTERLIS.GregorianDate', 'min': '1848-1-1', 'max': '2100-12-31'}}, 'geometric': {'is_geometric': False, 'multi': False, 'point_like': False, 'line_like': False, 'polygon_like': False}}),kw_only=False,_field_type=_FIELD)
```

Fields of dataclasses can be accessed from a class or also from an instance. This is really handy since we also can
access this information at runtime on instantiated objects. We use the [fields](https://docs.python.org/3/library/dataclasses.html#dataclasses.fields)
method from the `dataclasses` library for that.

In the example above we access the 3rd field of the class `Eigentumsbeschraenkung` which is the `publiziertAb` attribute.

On that we now can access the dataclass native `metadata` attribute and in that the interlis specific information.

Alter your script:

```python
from ili2py_interface.OeREBKRMtrsfr_V2_0.Transferstruktur import Eigentumsbeschraenkung
from dataclasses import fields
print(fields(Eigentumsbeschraenkung)[2].metadata['interlis']['type_restrictions'])
```

This gives:

```python
{'mandatory': True, 'kind': None, 'format': '"Year"-"Month"-"Day"', 'unit': None, 'ref_sys': None, 'clockwise': None, 'circular': None, 'abstract': False, 'final': False, 'generic': False, 'super': 'OeREBKRM_V2_0.Datum', 'type_related_type': False, 'multiplicity': {'min': 1, 'max': 1}, 'struct': 'INTERLIS.GregorianDate', 'min': '1848-1-1', 'max': '2100-12-31'}
```

To access the metadata of the object instance itself:

```python
print(Eigentumsbeschraenkung().metadata)
```
