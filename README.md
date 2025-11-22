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

Find current version of Docs [here](https://rudert-geoinformatik.github.io/ili2py/).

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
.venv/bin/pip install -e .
# show help about ili2py in general
.venv/bin/python -m ili2py.cli
# show version of ili2py
.venv/bin/python -m ili2py.cli -V
# show help about diagram tool
.venv/bin/python -m ili2py.cli diagram --help
# create plantuml diagram with one model selected
.venv/bin/python -m ili2py.cli diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o .generated -m OeREBKRMtrsfr_V2_0
# create plantuml diagram with all models which are related
.venv/bin/python -m ili2py.cli diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o .generated
# create plantuml diagram with 2 models selected
.venv/bin/python -m ili2py.cli diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o .generated -m OeREBKRMtrsfr_V2_0,OeREBKRM_V2_0
# create mermaid diagram with one model selected
.venv/bin/python -m ili2py.cli diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o .generated -m OeREBKRMtrsfr_V2_0
# create mermaid diagram with all models which are related
.venv/bin/python -m ili2py.cli diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o .generated
# create mermaid diagram with 2 models selected
.venv/bin/python -m ili2py.cli diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o .generated -m OeREBKRMtrsfr_V2_0,OeREBKRM_V2_0
# show debug output while generating diagram
.venv/bin/python -m ili2py.cli -v diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o .generated
# capture log into a log file
.venv/bin/python -m ili2py.cli -v diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o .generated > ili2py.log

# show help about python class generation tool
.venv/bin/python -m ili2py.cli python-classes --help
# generates complete set of python classes for a model
.venv/bin/python -m ili2py.cli python-classes -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o .generated -l interface
# if you have a python project which you want to include the interface directly you should name it regardingly (dotted python path).
# Of course you need to copy the output to the correct path then, or create it alread in the right place.
.venv/bin/python -m ili2py.cli python-classes -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o .generated -l ili2py.interfaces.interlis.OeREBKRMtrsfr_V2_0
# show debug output while generating python classes
.venv/bin/python -m ili2py.cli -v python-classes -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o .generated -l interface
# capture log into a log file
.venv/bin/python -m ili2py.cli -v python-classes -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o .generated -l interface > ili2py.log
```

### Docker

```shell
docker build -t ili2py:local-dev .

# show help about ili2py in general
docker run --rm -ti ili2py:local-dev
# show version of ili2py
docker run --rm -ti ili2py:local-dev -V
# show help about diagram tool
docker run --rm -ti ili2py:local-dev diagram --help
# create plantuml diagram with one model selected
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o /io/generated -m OeREBKRMtrsfr_V2_0
# create plantuml diagram with all models which are related
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o /io/generated
# create plantuml diagram with 2 models selected
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o /io/generated -m OeREBKRMtrsfr_V2_0,OeREBKRM_V2_0
# create mermaid diagram with one model selected
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o /io/generated -m OeREBKRMtrsfr_V2_0
# create mermaid diagram with all models which are related
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o /io/generated
# create mermaid diagram with 2 models selected
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o /io/generated -m OeREBKRMtrsfr_V2_0,OeREBKRM_V2_0

# show help about python class generation tool
docker run --rm -ti ili2py:local-dev python-classes --help
# generates complete set of python classes for a model
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev python-classes -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o /io/generated -l interface
# if you have a python project which you want to include the interface directly you should name it regardingly (dotted python path).
# Of course you need to copy the output to the correct path then, or create it alread in the right place.
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev python-classes -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o /io/generated -l ili2py.interfaces.interlis.OeREBKRMtrsfr_V2_0
```

See [Doc](#Docs) for further information on usage.
