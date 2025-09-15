from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer
from typing import List

from ili2py.mappers.helpers import Index
from ili2py.writers.helpers import handle_model_versions
from ili2py.writers.uml.interlis_23 import uml_diagram, Diagram


def create_uml_diagram(
    diagram: Diagram,
    index: Index,
    model_names: list[str],
    flavour: str,
    file_name: str,
    output_path: str,
    direction: str | None = None,
    linetype: str | None = None,
):
    ili_version = handle_model_versions(index)
    if ili_version == "2.3":
        uml_diagram(
            diagram,
            index,
            model_names,
            flavour,
            file_name,
            output_path,
            direction=direction,
            linetype=linetype,
        )
    elif ili_version == "2.4":
        uml_diagram(
            diagram,
            index,
            model_names,
            flavour,
            file_name,
            output_path,
            direction=direction,
            linetype=linetype,
        )
    else:
        raise NotImplementedError(f"ili version '{ili_version}' not supported")
