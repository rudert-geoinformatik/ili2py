
xsdata version: 25.7

```shell
xsdata generate -p ilismeta -r --unnest-classes -ss clusters --compound-fields ../../../../../../tests/data/ilismeta16/IlisMeta16.imd
```

xsdata created a file `class_ref_type_ref1.py` which was not correct. It inherited from nothing
and therefore missed alot of attributes which come from inheritance. It is still
unclear, why xsdata creates such construction because it also creates the almost
correct one. But this lacked the `ref` attribute. The solution was to add the
`ref` attribute from `class_ref_type_ref1.ClassRefTypeRef1` to the
`class_ref_type_ref.ClassRefTypeRef` and repoint all references too. After that, `class_ref_type_ref1.py`
was deleted.

while generating classes from xsd with xsdata another problem occurred in
[choice definition](ilismeta16_2022_10_10/actual_argument_type.py#L350). This was falsely
generated as a single object choice, but had to be a list of choices, actually. It had to be
corrected manually by making it an optional list of union... and in the field definition the
`default=None` had to be changed to `default_factory=list`. After that fix all expressions could
be parsed from IMD16 files in the tests.
