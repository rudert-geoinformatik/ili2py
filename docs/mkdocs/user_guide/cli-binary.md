
# CLI (Binary version)

The binary version of ili2py cli can be downloaded from the [Releases Page on GitHub](https://github.com/rudert-geoinformatik/ili2py/releases)

As described above, the _Command Line Interface_ of ili2py offerse two sub commands besides the main command:

- `diagram`
- `python-classes`

Let's have a look how it is used.

## Main command

!!! tip
    Its possible that you need to execute `chmod +x ili2py-linux`/ `chmod +x ili2py-macos` for the first time.

```shell
# Linux (possibly chmod +x ili2py-linux)
./ili2py-linux

# Mac (possibly chmod +x ili2py-macos)
./ili2py-macos

# Windows
.\ili2py-windows.exe
```

!!! tip
    The same output you get with `--help`

```shell
# Linux
./ili2py-linux --help

# Mac
./ili2py-macos --help

# Windows
.\ili2py-windows.exe --help
```

With `-V`/`--version` you can output the used version.

```shell
# Linux
./ili2py-linux --V
./ili2py-linux --version

# Mac
./ili2py-macos --V
./ili2py-macos --version

# Windows
.\ili2py-windows.exe --V
.\ili2py-windows.exe --version
```

Output:
```
ili2py 0.0.1 from ./ili2py-linux (Python 3.13.7)
```

!!! Note
    The parameter `-v`/`--verbose` is used only in connection with the sub commands.

---

## Sub command `diagram`

Creates a diagram of your choice from an IlisMeta16 file input.

!!! info
    _**ili2py**_ does not render the final image. It creates the dedicated textual representation. You need to render the resulting
    image by yourself with the matching toolset.

```shell
# Linux
./ili2py-linux diagram --help

# Mac
./ili2py-macos diagram --help

# Windows
.\ili2py-windows.exe diagram --help
```

The mandatory parameters of the sub command `diagram` are:

- the path to the meta model `-i`/`--imd` (only IMD16 is allowed!)
- and the path where the result should be written to `-o`/`--output_folder`

!!! info
    A subfolder `output_folder` with the name of the flavor will be created.

All other parameters are optional:

- `-f`/`--flavour` => Which diagram type should be created. Currently `plantuml`, `plantuml_role_members`, `mermaid`, `dot` (experimental) are implemented. Default type is `mermaid`.
- `-d`/`--direction` => In which direction should the diagram be drawn. This depends on the selected `flavour`:
    - `mermaid` => `LR`, `RL`, `TD`, `DT` => default `LR`
    - `plantuml` => `'top to bottom'`, `'left to right'`  => default `'top to bottom'`
    - `plantuml_role_members` => `'top to bottom'`, `'left to right'`  => default `'top to bottom'`
    - `dot` => No setting available
- `-l`/`--linetype` => Of which kind should be the inter-class-connectors. This depends on the selected `flavour`:
    - `mermaid` => No setting available
    - `plantuml` => `polyline`, `ortho`, `spline`
    - `dot` => No setting available
- `-n`/`--file_name` => The name of the diagram file. Without file extension, this is defined by the `flavour` and is added automatically.
- `-m`/`--models` => A comma-separated list of ili model names. These are used as a filter on the content of the diagram. Only models contained in the list will be drawn on the diagram. If the list is empty (default), all models will be drawn.
- `--depth` => A filter based on the analysis of the import tree.

!!! info
    If command line parameters contain spaces, they must be wrapped into quotation marks `'a b c'` oder `"a b c"`!

The following command creates a mermaid diagram (markdown file) containing the elements of the model `OeREBKRMtrsfr_V2_0` (filter). The file is named `diagram.md` and is located in the newly created folder `mermaid`.

```shell
# Linux
./ili2py-linux diagram -i models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o ./ -m OeREBKRMtrsfr_V2_0

# Mac
./ili2py-macos diagram -i models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o ./ -m OeREBKRMtrsfr_V2_0

# Windows
.\ili2py-windows.exe diagram -i models\OeREBKRMtrsfr_V2_0\OeREBKRMtrsfr_V2_0.imd -o .\ -m OeREBKRMtrsfr_V2_0
```

The following command creates the same diagram but outputs a lot more logs. This is useful in cases you experience errors and need to investigate.

```shell
# Linux
./ili2py-linux -v diagram -i models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o ./ -m OeREBKRMtrsfr_V2_0

# Mac
./ili2py-macos -v diagram -i models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o ./ -m OeREBKRMtrsfr_V2_0

# Windows
.\ili2py-windows.exe -v diagram -i models\OeREBKRMtrsfr_V2_0\OeREBKRMtrsfr_V2_0.imd -o .\ -m OeREBKRMtrsfr_V2_0
```

## Sub command `python-classes`

Creates typed python class library out of an IlisMeta16 file input.

```shell
# Linux
./ili2py-linux python-classes --help

# Mac
./ili2py-macos python-classes --help

# Windows
.\ili2py-windows.exe python-classes --help
```
The mandatory parameters of the sub command python-classes` are:

- the path to the meta model `-i`/`--imd` (only IMD16 is allowed!)
- and the path where the result should be written to `-o`/`--output_folder`

!!! info
    A subfolder `output_folder` with the name of the flavor will be created.

Optional parameters are:

- `-l`/`--library_name` => The name of the resulting library.

!!! tip
    This can be a point separated name. The library is created to be in the scope of that path (internal imports are aligned). This way you can integrate the generated library easily in existing projects.

!!! info
    If the name is `ili2py.interfaces.interlis.OeREBKRMtrsfr_V2_0`, the library will be created still in the folder `OeREBKRMtrsfr_V2_0`. It has to be copied to the correct place manually then.

The following command creates a python library in the folder `OeREBKRMtrsfr_V2_0`:

```shell
# Linux
./ili2py-linux python-classes -i models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o ./ -l interface

# Mac
./ili2py-macos python-classes -i models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o ./ -l interface

# Windows
.\ili2py-windows.exe python-classes -i models\OeREBKRMtrsfr_V2_0\OeREBKRMtrsfr_V2_0.imd -o .\ -l interface
```


The following command creates the same library. But it puts out a lot more logs.

```shell
# Linux
./ili2py-linux python-classes -i models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o ./ -l interface

# Mac
./ili2py-macos python-classes -i models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd -o ./ -l interface

# Windows
.\ili2py-windows.exe python-classes -i models\OeREBKRMtrsfr_V2_0\OeREBKRMtrsfr_V2_0.imd -o .\ -l interface
```
