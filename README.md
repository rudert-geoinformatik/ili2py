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
.venv/bin/pip install -e .
# show help about uml tool
.venv/bin/python -m ili2py.cli ili2py-diagram --help
# create plantuml uml diagram with one model selected
.venv/bin/python -m ili2py.cli ili2py-diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o .generated -m OeREBKRMtrsfr_V2_0
# create plantuml uml diagram with all models which are related
.venv/bin/python -m ili2py.cli ili2py-diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o .generated
# create plantuml uml diagram with 2 models selected
.venv/bin/python -m ili2py.cli ili2py-diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o .generated -m OeREBKRMtrsfr_V2_0,OeREBKRM_V2_0
# create mermaid uml diagram with one model selected
.venv/bin/python -m ili2py.cli ili2py-diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o .generated -m OeREBKRMtrsfr_V2_0
# create mermaid uml diagram with all models which are related
.venv/bin/python -m ili2py.cli ili2py-diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o .generated
# create mermaid uml diagram with 2 models selected
.venv/bin/python -m ili2py.cli ili2py-diagram -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o .generated -m OeREBKRMtrsfr_V2_0,OeREBKRM_V2_0

# show help about python class generation tool
.venv/bin/python -m ili2py.cli ili2py-python-classes --help
# generates complete set of python classes for a model
.venv/bin/python -m ili2py.cli ili2py-python-classes -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o .generated -l interface
# if you have a python project which you want to include the interface directly you should name it regardingly (dotted python path).
# Of course you need to copy the output to the correct path then, or create it alread in the right place.
.venv/bin/python -m ili2py.cli ili2py-python-classes -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o .generated -l ili2py.interfaces.interlis.OeREBKRMtrsfr_V2_0
```

### Docker

```shell
docker build -t ili2py:local-dev .

# show help about uml tool
docker run --rm -ti ili2py:local-dev ili2py-diagram --help
# create plantuml uml diagram with one model selected
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev ili2py-diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o /io/generated -m OeREBKRMtrsfr_V2_0
# create plantuml uml diagram with all models which are related
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev ili2py-diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o /io/generated
# create plantuml uml diagram with 2 models selected
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev ili2py-diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f plantuml -o /io/generated -m OeREBKRMtrsfr_V2_0,OeREBKRM_V2_0
# create mermaid uml diagram with one model selected
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev ili2py-diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o /io/generated -m OeREBKRMtrsfr_V2_0
# create mermaid uml diagram with all models which are related
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev ili2py-diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o /io/generated
# create mermaid uml diagram with 2 models selected
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev ili2py-diagram -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f mermaid -o /io/generated -m OeREBKRMtrsfr_V2_0,OeREBKRM_V2_0

# show help about python class generation tool
docker run --rm -ti ili2py:local-dev ili2py-python-classes --help
# generates complete set of python classes for a model
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev ili2py-python-classes -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o /io/generated -l interface
# if you have a python project which you want to include the interface directly you should name it regardingly (dotted python path).
# Of course you need to copy the output to the correct path then, or create it alread in the right place.
docker run --rm -ti -v ./tests/data/models:/io/data -v ./.generated:/io/generated ili2py:local-dev ili2py-python-classes -i /io/data/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o /io/generated -l ili2py.interfaces.interlis.OeREBKRMtrsfr_V2_0
```

See [Doc](#Docs) for further information on usage.
