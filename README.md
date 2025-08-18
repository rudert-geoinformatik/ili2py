# ili2py

Your pythonic gateway to INTERLIS

- [**Code**](https://github.com/rudert-geoinformatik/ili2py)
- [**Docs**](https://rudert-geoinformatik.github.io/ili2py)
- [**PyPI**](https://pypi.org/project/ili2py/)
- [**CI**](https://github.com/rudert-geoinformatik/ili2py/actions/)


## Features

**ili2py** `python package`

1. python bindings for interlis models
1. reader for IMD16 meta models
1. reader for XTF corresponding to a given model
1. writers: PythonSource Code, UML Charts

## Docs

Find current version of Docs [here](https://ili2py-docs.rudert-geoinformatik.ch).

## Quickstart

The following sections will guide you to quickstart the project. Consult the [Doc](#Docs)
for further information!

If you are on windows, you need to change the direction of the slashes in the commands
you execute!

### Python

Assuming you have a working python and virtualenv installed on your system.

```shell
virtualenv .venv
.venv/bin/pip install --upgrade pip wheel setuptools
.venv/bin/python -m ili2py.cli ili2py-python-classes --help
.venv/bin/python -m ili2py.cli ili2py-uml --help
```

See [Doc](#Docs) for further information on usage.
