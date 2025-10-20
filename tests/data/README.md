# Test models

This folder contains the metamodels which is ili2py tested against.

With the following commands the imd's can be updated.

ili2c versions available can be found here: https://downloads.interlis.ch/ili2c/

Build image:
```shell
docker build --build-arg ILI2C_VERSION=<desired-verion-of-ili2c> -t ili2c:latest .
```

Create IMD16 from Models:
```shell
docker run -v $(pwd)/models:/io/models --rm ili2c:latest
```

Or directly without docker:
```shell
ILI2C_EXECUTABLE="java -jar <ABSOLUTE-PATH-TO-ILI2C-JAR>" make recreate-imd
```
