import logging
import os
from pathlib import Path
from random import randint
from typing import List

from jinja2 import Environment, FileSystemLoader

from ili2py.mappers.helpers import Index
from ili2py.writers.diagram.interlis.uml import Diagram, TopicGroup
from ili2py.writers.helpers import create_file

ns_map = {"ili": "http://www.interlis.ch/INTERLIS2.3"}

tool_settings = {
    "mermaid": {
        "postfix": "md",
        "settings": {
            "directions": ["LR", "RL", "TB", "BT"],
            # currently not supported on class diagrams
            "linetype": [],
        },
    },
    "plantuml": {
        "postfix": "puml",
        "settings": {
            "directions": ["top to bottom", "left to right"],
            "linetype": ["polyline", "ortho", "spline"],
        },
    },
    "plantuml_role_members": {
        "postfix": "puml",
        "settings": {
            "directions": ["top to bottom", "left to right"],
            "linetype": ["polyline", "ortho", "spline"],
        },
    },
    "dot": {
        "postfix": "dot",
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
    multiplier: int = 2,
    depth: int | None = None,
):
    if flavour == "mermaid":
        selected_direction = tool_settings[flavour]["settings"]["directions"][0]
        selected_linetype = None
    elif flavour == "plantuml":
        selected_direction = tool_settings[flavour]["settings"]["directions"][0]
        selected_linetype = tool_settings[flavour]["settings"]["linetype"][0]
    elif flavour == "plantuml_role_members":
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
    if depth is None:
        # all relevant models
        inner_model_names = index.depth_tree[-1]
    else:
        try:
            inner_model_names = index.depth_tree[depth]
        except IndexError:
            inner_model_names = index.depth_tree[-1]

    if len(model_names) > 0:
        if depth is not None:
            inner_model_names = list(set(model_names) | set(inner_model_names))
        else:
            inner_model_names = model_names
    logging.info(f"Drawing diagram for models: {inner_model_names}")
    output = env.get_template(f"{flavour}.jinja2").render(
        diagram=diagram,
        index=index,
        len=len,
        randint=randint,
        render_multiplicity=TopicGroup.render_multiplicity,
        model_names=inner_model_names,
        direction=selected_direction,
        linetype=selected_linetype,
        multiplier=multiplier,
    )
    src_code_encoded = output.encode()

    diagram_file = create_file(output_path, flavour, file_name)
    diagram_file.write_text(src_code_encoded.decode(), encoding="utf-8")
    return str(diagram_file)
