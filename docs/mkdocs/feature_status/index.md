Handling of IMD16 is split into 3 levels of processing:

```mermaid
flowchart TD
reading["Reading/Parsing IMD16 XML"]
mapping["Mapping/Indexing into internal knowledge"]
rendering["Rendering into desired format"]
rendering-->mapping-->reading
```

The following table gives an overview about current status of the implementation:

|             Name              | Features implemented | Coverage |                                                                Comment                                                                 |
|:-----------------------------:|:--------------------:|:--------:|:--------------------------------------------------------------------------------------------------------------------------------------:|
|         Reading IMD16         |   ⏳<br/>(123/126)    |   ~97%   | All constucts out of<br/>`ilisMeta16.ili` (version 2022-04-28)<br/>can be read into Python<br/>see [Reading IlisMeta16](ilismeta16.md) |
|         Index Mapper          |    ⏳<br/>(10/21)     |   ~48%   |                                        Ongoing DEV process see [Index Mapper](index_mapper.md)                                         |
| Python Classes<br/>(renderer) |                      |    ⏳     |                                       Demonstrator tool, see [Python Classes](python_classes.md)                                       |
|  UML Diagrams<br/>(renderer)  |     ✅<br/>(7/7)      |   100%   |                                         Demonstrator tool, see [UML Diagrams](uml_diagrams.md)                                         |
