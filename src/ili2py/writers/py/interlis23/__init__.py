import re
import os
import subprocess
import uuid

from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer
from ili2py.interfaces.interlis.interlis_24.ilismeta16.helper import index_modeldata
from xsdata.codegen.exceptions import CodegenError

from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.extendable_me import \
    AttrOrParam
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.domain_type.domain_type import \
    TextType, NumType, BlackboxType
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class import Class


ns_map = {
    "ili": "http://www.interlis.ch/INTERLIS2.3"
}


def create_file(output_path: str, model_name: str, file_name:str):
    output_file = Path(os.path.join(output_path, model_name, file_name))
    output_file.parent.mkdir(exist_ok=True, parents=True)
    return output_file


def render_imports(imports: list[str]) -> list[str]:
    rendered_imports = []
    for import_path in imports:
        import_path_elements = import_path.split('.')
        import_target = import_path_elements.pop()
        rendered_imports.append(
            f"from ..{'.'.join(import_path_elements)} import {import_target}"
        )
    return rendered_imports


def render_type(attribute_item: AttrOrParam, imports: list[str], context: str, index: dict) -> str:
    if isinstance(attribute_item.Type, TextType):
        return 'str'
    elif isinstance(attribute_item.Type, NumType):
        return 'int'
    elif isinstance(attribute_item.Type, BlackboxType):
        return 'bytes'
    else:
        if hasattr(attribute_item.Type, 'base_type'):
            python_path = attribute_item.Type.base_type.ref
        else:
            python_path = attribute_item.Type.tid
        python_path = python_path.replace('.TYPE', '')
        if python_path.startswith(context):
            python_path = python_path.replace(f'{context}.', '')
        else:
            if python_path not in imports:
                imports.append(python_path)
            python_path = python_path.split('.')[-1]
        python_path = python_path.replace('.', '_')
        return python_path


def reader_classes(metamodel: ImdTransfer, output_path: str) -> str:
    index = index_modeldata(metamodel)
    tpl_dir = Path(__file__).parent.joinpath("templates")
    env = Environment(loader=FileSystemLoader(str(tpl_dir)), autoescape=False)
    output_classes = []
    for model_data in metamodel.datasection.ModelData:
        output_file = create_file(output_path, model_data.Model.Name, '__init__.py')
        model_doc_text = ['from dataclasses import dataclass', '', '"""']
        for item in model_data.Model.Documentation:
            model_doc_text = model_doc_text + [line.lstrip() for line in item.DocText.Text.split('\n')]
        model_doc_text.append('"""')
        model_doc_text = model_doc_text +['', '']
        imports = []
        for class_item in model_data.Class:
            output = env.get_template("class.jinja2").render(
                class_item=class_item,
                index=index,
                render_type=render_type,
                imports=imports,
                context=model_data.Model.Name
            )
            model_doc_text = model_doc_text + ["@dataclass"] + output.split('\n')
        model_doc_text = render_imports(imports) + model_doc_text
        output_file.write_text('\n'.join(model_doc_text))
        for submodel in model_data.SubModel:
            output_file = create_file(output_path, model_data.Model.Name, f'{submodel.Name}.py')
            model_doc_text = ['from dataclasses import dataclass', '', '"""']
            for item in submodel.Documentation:
                model_doc_text = model_doc_text + [line.lstrip() for line in item.DocText.Text.split('\n')]
            model_doc_text.append('"""')
            model_doc_text = model_doc_text + ['', '']
            imports = []
            # we access an attribute which is created at runtime
            for ElementInPackage_item in submodel.ElementInPackage_backref:
                if isinstance(ElementInPackage_item, Class):
                    output = env.get_template("class.jinja2").render(
                        class_item=ElementInPackage_item,
                        index=index,
                        render_type=render_type,
                        imports=imports,
                        context=f'{model_data.Model.Name}.{submodel.Name}'
                    )
                    model_doc_text = model_doc_text + ["@dataclass"] + output.split('\n')
            model_doc_text = render_imports(imports) + model_doc_text
            output_file.write_text('\n'.join(model_doc_text))
    file_path = Path(f"/tmp/{str(uuid.uuid4())}.py")
    with open(f'/tmp/debug.py', mode="w+") as f:
        f.write('\n'.join(output_classes))
    commands = [
        [
            "ruff",
            "format",
            "--stdin-filename",
            str(file_path),
            "--line-length",
            str(80),
        ],
        [
            "ruff",
            "check",
            "--stdin-filename",
            str(file_path),
            "--line-length",
            str(80),
            "--config",
            str(Path(__file__).parent / "ruff.toml"),
            "--fix",
            "--unsafe-fixes",
            "--exit-zero",
        ],
    ]
    try:
        src_code_encoded = output.encode()
        for command in commands:
            result = subprocess.run(
                command,
                input=src_code_encoded,
                capture_output=True,
                check=True,
            )
            src_code_encoded = result.stdout

        return src_code_encoded.decode()
    except subprocess.CalledProcessError as e:
        details = e.stderr.decode().replace("error: ", "").strip()
        print(f"Ruff command failed: {details}")
        source = code_excerpt(details, src_code_encoded.decode())
        raise CodegenError("Ruff failed", details=details, source=source)


def code_excerpt(details: str, src_code: str) -> str:
    """Extract source code excerpt from the error details message."""
    match = re.search(r"(\d+):(\d+)", details)
    if match:
        line_number = int(match.group(1)) - 1
        lines = src_code.split("\n")
        start = max(0, line_number - 4)
        end = min(len(lines), line_number + 4)

        excerpt = ["\n"]
        for index in range(start, end):
            prepend = "--->" if index == line_number else "   "
            excerpt.append(f"{prepend}{lines[index]}")

        return "\n".join(excerpt)

    return "NA"
