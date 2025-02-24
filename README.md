# ili2py

Your pythonic gateway to INTERLIS

- [**Code**](https://github.com/rudert-geoinformatik/ili2py)
- [**Docs**](https://rudert-geoinformatik.github.io/ili2py)
- [**PyPI**](https://pypi.org/project/ili2py/)
- [**CI**](https://github.com/rudert-geoinformatik/ili2py/actions/)


## Features

**ili2py** `python package`

1. python bindings for interlis models
1. readers for IMD and XTF
1. writers: PythonSource Code, UML Charts

## Development

TBD

## Prerequisites

You need to have `Python` (>=3.11) installed.

## Quickstart

### Local Development
Creates a local virtual environment to develop and test the code:

```shell
make dev
```

The following command creates a python library corresponding to the passed imd in the folder `generated` in
project root. Content of `generated` will be overwritten by re issue of the command.

```shell
.venv/bin/python -m ili2py.cli ili2py-python-classes -i data/OeREBKRMtrsfr_V2_0.imd -f generated
```

### Running in Docker

First build the docker image:

```shell
docker build --network host -t ili2py:latest .
```

Then run the app like this (sample command with target ili2py-python-classes):

```shell
docker run --rm --network host ili2py:latest ili2py-python-classes -i data/OeREBKRMtrsfr_V2_0.imd -f generated
```
