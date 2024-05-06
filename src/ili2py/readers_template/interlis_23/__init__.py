import re
import subprocess
import uuid
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from typing import List, Optional
from ili2py.interfaces.metamodel.ilismeta16 import ModelData, Class

from xsdata.codegen.exceptions import CodegenError

ns_map = {
    "ili": "http://www.interlis.ch/INTERLIS2.3"
}


def reader_classes(model_data: ModelData, all_model_data: List[ModelData]):
    tpl_dir = Path(__file__).parent.joinpath("templates")
    env = Environment(loader=FileSystemLoader(str(tpl_dir)), autoescape=False)
    output = env.get_template("frame.jinja2").render(model_data=model_data, all_model_data=all_model_data)
    file_path = Path(f"/tmp/{str(uuid.uuid4())}.py")
    with open(f'/tmp/debug.py', mode="w+") as f:
        f.write(output)
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
            "checks",
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
