Handling of IMD16 is split into 3 levels of processing:

```mermaid
flowchart TD
reading["Reading/Parsing IMD16 XML"]
mapping["Mapping/Indexing into internal knowledge"]
rendering["Rendering into desired format"]
rendering-->mapping-->reading
```

The following table gives an overview about current status of the implementation:

|             Name              |                 Features implemented                 | Coverage |                                                                          Comment                                                                          |
|:-----------------------------:|:----------------------------------------------------:|:--------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------:|
|         Reading IMD16         |                   ⏳<br/>(125/126)                    |   ~99%   | All constructs out of<br/>`ilisMeta16.ili` (version 2022-04-28)<br/>exported by ili2c 5.6.9 can be read into Python<br/>see [Reading IlisMeta16](ilismeta16.md) |
|         Index Mapper          |                    ⏳<br/>(12/21)                     |   ~57%   |                                                  Ongoing DEV process see [Index Mapper](index_mapper.md)                                                  |
| Python Classes<br/>(renderer) | ✅<br/>(13/13 mandatory)<br/>(17/18 incl. nice to have) |   100%   |                    Coverage of the mandatory requirements.<br/>Reads and writes XTF 2.3 and 2.4, see [Python Classes](python_classes.md)                    |
|  UML Diagrams<br/>(renderer)  |  ✅<br/>(6/6 mandatory)<br/>(9/11 incl. nice to have)  |   100%   |                          Coverage of the mandatory requirements.<br/>Demonstrator tool, see [UML Diagrams](diagrams.md)                           |
