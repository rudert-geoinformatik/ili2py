# Quickstart

## Locally

### Prepare virtual environment

Creates a local virtual environment to develop and test the code:

```shell
make dev
```

### Usage

The following command creates a python library corresponding to the passed imd in the folder `generated` in
project root. Content of `generated` will be overwritten by re issue of the command.

#### Generate Python classes

```shell
.venv/bin/python -m ili2py.cli ili2py-python-classes -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f generated
```

#### UML Diagram generation

First you need to create a folder called `uml` in the root of the project.

Linux:
```shell
mkdir uml
```

The following command creates a UML Diagram (PlantUML).

```shell
.venv/bin/python -m ili2py.cli ili2py-uml -i tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o plantuml > uml/test.puml
```

The resulting File contains the UML description as it can be used with plantuml. To save it as an image (e.g. svg or png) we can run
the following command:

```shell
docker run --rm -v $(pwd)/uml:/io plantuml/plantuml -tsvg -o /io /io/test.puml
```

## Docker

### Prepare Image

First build the docker image:

```shell
docker build -t ili2py:latest .
```

### Usage

Then run the app like this (sample command with target ili2py-python-classes):

```shell
docker run --rm -v $(pwd)/tests/data/models:/io/models ili2py:latest ili2py-python-classes -i /io/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -f /io/generated
```
