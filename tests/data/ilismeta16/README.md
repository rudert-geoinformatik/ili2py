The `imd` and `xsd` from `ili` was created
with ili2c (as it is stated as sender in the `imd`).

The commands were:
```shell
java -jar <path-to-ili2c>/ili2c.jar -oIMD16 --out ./IlisMeta16.imd ./IlisMeta16.ili
java -jar <path-to-ili2c>/ili2c.jar -oXSD --out ./ ./IlisMeta16.ili
```
