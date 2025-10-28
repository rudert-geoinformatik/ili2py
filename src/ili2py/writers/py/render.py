import inspect
import os
import shutil
from pathlib import Path

import autoflake
import black
import isort
from jinja2 import Environment, FileSystemLoader

from ili2py.mappers.helpers import Index
from ili2py.writers.helpers import create_file, handle_model_versions
from ili2py.writers.py import constraints
from ili2py.writers.py.python_structure import Library

base_url_23 = "http://www.interlis.ch/INTERLIS2.3"
base_url_24 = "http://www.interlis.ch/xtf/2.4"

render_configuration = {
    "2.3": {"selector": 23, "base_url": base_url_23, "namespace_map": {"ili": base_url_23}},
    "2.4": {
        "selector": 24,
        "base_url": base_url_24,
        "namespace_map": {
            "ili": f"{base_url_24}/INTERLIS",
            "geom": "http://www.interlis.ch/geometry/1.0",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        },
    },
}


def create_python_classes(library: Library, index: Index, output_path: str, beautify: bool = True):
    ili_version = handle_model_versions(index)
    if ili_version == "2.3":
        reader_classes(
            library, output_path, render_config=render_configuration[ili_version], beautify=beautify
        )
    elif ili_version == "2.4":
        reader_classes(
            library, output_path, render_config=render_configuration[ili_version], beautify=beautify
        )
    else:
        raise NotImplementedError(f"ili version '{ili_version}' not supported")


def library_storage_name(library_name: str) -> str:
    return library_name.split(".")[-1]


def reader_classes(library: Library, output_path: str, render_config: dict, beautify: bool = True):
    tpl_dir = Path(__file__).parent.joinpath(f"interlis{render_config['selector']}", "templates")
    env = Environment(loader=FileSystemLoader(str(tpl_dir)), autoescape=False)
    library_content = env.get_template("library_init.jinja2").render(
        library=library, render_config=render_config
    )
    # we expect the name to contain dots (as python dotted path) this can be used to create the interface in
    # the correct way for a library where it should be included to. As we always want the folder of the
    # library package to be named after the library we expect the last element the right match in any case.
    library_name = library_storage_name(library.name)
    target_path = os.path.join(output_path, library_name)
    if os.path.isdir(target_path):
        shutil.rmtree(target_path)

    library_file = create_file(output_path, library_name, "__init__.py")
    library_file.write_text(library_content)
    references_content = env.get_template("references.jinja2").render(render_config=render_config)
    references_file = create_file(output_path, library_name, "references.py")
    references_file.write_text(references_content)
    # this way we can use the code and also deliver it to the built package
    constraints_file = create_file(output_path, library_name, "constraints.py")
    constraints_file.write_text(inspect.getsource(constraints))
    convertable_types_content = env.get_template("convertable_types.jinja2").render(
        library=library, render_config=render_config
    )
    convertable_types_file = create_file(output_path, library_name, "convertable_types.py")
    convertable_types_file.write_text(convertable_types_content)
    xtf_opening_content = env.get_template("xtf_opening.jinja2").render(
        library=library, render_config=render_config
    )
    xtf_opening_file = create_file(output_path, library_name, "xtf_opening.py")
    xtf_opening_file.write_text(xtf_opening_content)
    output_path = os.path.join(output_path, library_name)
    for package in library.packages:
        package_file = create_file(output_path, package.name, "__init__.py")
        package_content = env.get_template("package_init.jinja2").render(
            package=package, render_config=render_config
        )
        package_file.write_text(package_content)
        for module in package.modules:
            module_file = create_file(output_path, package.name, f"{module.name}.py")
            module_content = env.get_template("module.jinja2").render(
                module=module, render_config=render_config, package=package
            )
            module_file.write_text(module_content)
    if beautify:

        output_path_pathlib = Path(output_path)
        py_files = (
            output_path_pathlib.rglob("*.py")
            if output_path_pathlib.is_dir()
            else [output_path_pathlib]
        )

        # run autoflake
        for file_path in py_files:
            code = file_path.read_text()
            fixed_code = autoflake.fix_code(
                code,
                remove_all_unused_imports=True,
                remove_unused_variables=True,
            )
            file_path.write_text(fixed_code)

        # run isort
        for file_path in py_files:
            isort.file(file_path, profile="black", float_to_top=True)

        # run black
        mode = black.FileMode(line_length=79)
        for file_path in py_files:
            black.format_file_in_place(
                file_path, fast=False, mode=mode, write_back=black.WriteBack.YES
            )
