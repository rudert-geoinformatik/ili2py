from ili2py.mappers.helpers import Index
from ili2py.writers.diagram.interlis import Diagram, uml_diagram
from ili2py.writers.helpers import handle_model_versions


def create_uml_diagram(
    diagram: Diagram,
    index: Index,
    model_names: list[str],
    flavour: str,
    file_name: str,
    output_path: str,
    direction: str | None = None,
    linetype: str | None = None,
    multiplier: int = 2,
    depth: int | None = None,
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
            multiplier=multiplier,
            depth=depth,
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
            multiplier=multiplier,
            depth=depth,
        )
    else:
        raise NotImplementedError(f"ili version '{ili_version}' not supported")
