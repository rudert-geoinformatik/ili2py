import os
from random import randint

from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from typing import List

from ili2py.mappers.helpers import Index
from ili2py.writers.helpers import create_file
from ili2py.writers.uml.interlis_23.uml import Diagram

ns_map = {"ili": "http://www.interlis.ch/INTERLIS2.3"}

tool_settings = {
    "mermaid": {
        "settings": {
            "directions": ["LR", "RL", "TD", "DT"],
            # currently not supported on class diagrams
            "linetype": [],
        },
    },
    "plantuml": {
        "settings": {
            "directions": ["top to bottom", "left to right"],
            "linetype": ["polyline", "ortho", "spline"],
        },
    },
    "dot": {
        "settings": {
            "directions": [],
            # currently not supported on class diagrams
            "linetype": [],
        },
    },
}


def uml_diagram(
    diagram: Diagram,
    index: Index,
    model_names: List[str],
    flavour: str,
    file_name: str,
    output_path: str,
    direction: str | None = None,
    linetype: str | None = None,
):
    if flavour == "mermaid":
        selected_direction = tool_settings[flavour]["settings"]["directions"][0]
        selected_linetype = None
    elif flavour == "plantuml":
        selected_direction = tool_settings[flavour]["settings"]["directions"][0]
        selected_linetype = tool_settings[flavour]["settings"]["linetype"][0]
    elif flavour == "dot":
        selected_direction = None
        selected_linetype = None
    else:
        raise NotImplementedError
    if direction is not None:
        if direction not in tool_settings[flavour]["settings"]["directions"]:
            raise NotImplementedError
        else:
            selected_direction = direction
    if linetype is not None:
        if linetype not in tool_settings[flavour]["settings"]["linetype"]:
            raise NotImplementedError
        else:
            selected_linetype = linetype

    tpl_dir = os.path.join(Path(__file__).parent.joinpath("templates"), flavour)
    env = Environment(loader=FileSystemLoader(str(tpl_dir)), autoescape=False)
    if len(model_names) == 0:
        model_names = [model.name for model in diagram.model_groups]
    output = env.get_template(f"{flavour}.jinja2").render(
        diagram=diagram,
        index=index,
        len=len,
        randint=randint,
        model_names=model_names,
        direction=selected_direction,
        linetype=selected_linetype,
    )
    src_code_encoded = output.encode()

    diagram_file = create_file(output_path, flavour, file_name)
    diagram_file.write_text(src_code_encoded.decode())
