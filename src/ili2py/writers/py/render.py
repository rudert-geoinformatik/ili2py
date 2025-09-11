import os
import shutil
import subprocess
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from ili2py.mappers.helpers import Index
from ili2py.writers.helpers import handle_model_versions, create_file
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


def create_python_classes(library: Library, index: Index, output_path: str):
    ili_version = handle_model_versions(index)
    if ili_version == "2.3":
        reader_classes(library, output_path, render_config=render_configuration[ili_version])
    elif ili_version == "2.4":
        reader_classes(library, output_path, render_config=render_configuration[ili_version])
    else:
        raise NotImplementedError(f"ili version '{ili_version}' not supported")


def reader_classes(library: Library, output_path: str, render_config: dict):
    tpl_dir = Path(__file__).parent.joinpath(f"interlis{render_config['selector']}", "templates")
    env = Environment(loader=FileSystemLoader(str(tpl_dir)), autoescape=False)
    library_content = env.get_template("library_init.jinja2").render(
        library=library, render_config=render_config
    )
    target_path = os.path.join(output_path, library.name)
    if os.path.isdir(target_path):
        shutil.rmtree(target_path)
    library_file = create_file(output_path, library.name, "__init__.py")
    library_file.write_text(library_content)
    references_content = env.get_template("references.jinja2").render(render_config=render_config)
    references_file = create_file(output_path, library.name, "references.py")
    references_file.write_text(references_content)
    convertable_types_content = env.get_template("convertable_types.jinja2").render(
        library=library, render_config=render_config
    )
    convertable_types_file = create_file(output_path, library.name, "convertable_types.py")
    convertable_types_file.write_text(convertable_types_content)
    xtf_opening_content = env.get_template("xtf_opening.jinja2").render(
        library=library, render_config=render_config
    )
    xtf_opening_file = create_file(output_path, library.name, "xtf_opening.py")
    xtf_opening_file.write_text(xtf_opening_content)
    output_path = os.path.join(output_path, library.name)
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
    commands = [
        ["isort", output_path, "--profile black", "--float-to-top"],
        [
            "ruff",
            "format",
            "--line-length",
            "88",
            output_path,
        ],
        [
            "ruff",
            "check",
            "--extend-select",
            "I",
            "--extend-select",
            "E401",
            "--fix",
            "--unsafe-fixes",
            "--exit-zero",
            output_path,
        ],
        ["autoflake", "--in-place", "--remove-all-unused-imports", "--recursive", output_path],
    ]
    executable_path = os.path.dirname(sys.executable)
    env = os.environ.copy()
    if env.get("PATH"):
        env["PATH"] = executable_path + os.pathsep + env["PATH"]
    for command in commands:
        subprocess.run(
            command,
            capture_output=True,
            check=True,
            env=env,
        )
