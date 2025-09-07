import os
import shutil
import subprocess
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from ili2py.writers import create_file
from ili2py.writers.py.interlis23.python import Library

ns_map = {"ili": "http://www.interlis.ch/INTERLIS2.3"}


def reader_classes(library: Library, output_path: str):
    tpl_dir = Path(__file__).parent.joinpath("templates")
    env = Environment(loader=FileSystemLoader(str(tpl_dir)), autoescape=False)
    library_content = env.get_template("library_init.jinja2").render(library=library)
    target_path = os.path.join(output_path, library.name)
    if os.path.isdir(target_path):
        shutil.rmtree(target_path)
    library_file = create_file(output_path, library.name, "__init__.py")
    library_file.write_text(library_content)
    output_path = os.path.join(output_path, library.name)
    for package in library.packages:
        package_file = create_file(output_path, package.name, "__init__.py")
        package_content = env.get_template("package_init.jinja2").render(package=package)
        package_file.write_text(package_content)
        for module in package.modules:
            module_file = create_file(output_path, package.name, f"{module.name}.py")
            module_content = env.get_template("module.jinja2").render(module=module)
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
