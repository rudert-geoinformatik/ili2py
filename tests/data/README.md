# Test models

This folder contains the metamodels which is ili2py tested against.

With the following commands the imd's can be updated.

Build image:
```shell
docker build --build-arg ILI2C_VERSION=5.6.3 -t ili2c:latest .
```

Create IMD16 from Models:
```shell
docker run -v $(pwd)/models:/io/models --rm ili2c:latest
```