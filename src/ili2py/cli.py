"""Main `ili2py` CLI."""

import logging
import os
import sys
from typing import Any

import click
from rich.logging import RichHandler

from ili2py import version
from ili2py.mappers.helpers import Index
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.diagram import create_uml_diagram
from ili2py.writers.diagram.interlis import Diagram, tool_settings
from ili2py.writers.py.python_structure import Library
from ili2py.writers.py.render import create_python_classes, library_storage_name


def version_msg():
    """ili2py version, location and Python version.

    Get message about ili2py version, location
    and Python version.
    """
    python_version = sys.version[:6]
    message = f"ili2py {version} from {sys.argv[0]} (Python {python_version})"
    return message


@click.group()
@click.option("-v", "--verbose", is_flag=True, help="Print debug information", default=False)
@click.version_option(version, "-V", "--version", message=version_msg())
def cli(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    handlers = []
    # we recognize if we run in tty -> colorlogging is enabled with rich logging
    # else we use the default stream handler (this avoids awkward output when it's piped to a file).
    if sys.stdout.isatty():
        handlers.append(RichHandler())
    else:
        handlers.append(logging.StreamHandler(sys.stdout))
    logging.basicConfig(
        level=level, format="%(levelname)s: %(message)s", datefmt="[%X]", handlers=handlers
    )
    logging.info("Starting ili2py CLI")
    logging.info(version_msg())


@cli.command(
    help="""Parses an arbitrary IMD16 and creates a diagram of selected flavour
    representing the selected models.""",
    context_settings=dict(help_option_names=["-h", "--help"], show_default=True),
)
@click.option("-i", "--imd", is_flag=False, required=True, help="full path to IMD16 file")
@click.option(
    "-o",
    "--output_folder",
    is_flag=False,
    required=True,
    help="""Path to the folder where the diagram should be written to.
    The folder will be created if not existing.""",
)
@click.option(
    "-f",
    "--flavour",
    is_flag=False,
    default=list(tool_settings.keys())[0],
    help=f'the desired flavour (one of {", ".join(tool_settings.keys())})',
)
@click.option(
    "-d",
    "--direction",
    is_flag=False,
    default=None,
    help=f'the desired direction, depending on the selected flavour (one of {", ".join([f'{key}: {tool_settings[key]["settings"]["directions"]}' for key in tool_settings])})',
)
@click.option(
    "-l",
    "--linetype",
    is_flag=False,
    default=None,
    help=f'the desired linetype, depending on the selected flavour (one of {", ".join([f'{key}: {tool_settings[key]["settings"]["linetype"]}' for key in tool_settings])})',
)
@click.option(
    "-n",
    "--file_name",
    is_flag=False,
    default="diagram",
    help=f"The name of the output diagram. The postfix (md, puml, etc. is added automatically due to selected flavour).",
)
@click.option(
    "-m",
    "--models",
    is_flag=False,
    required=False,
    help="""Model names separated by comma. This is used to filter the content of the resulting diagram.
    If not provided, the full tree will be drawn.
    NOTE: This works in conjunction with the depth parameter
    """,
)
@click.option(
    "-s",
    "--spacing-line-length",
    is_flag=False,
    default=2,
    required=False,
    help="""The length of the drawn connectors between the diagram nodes.
    NOTE: Currently this only influences plantuml diagrams!
    """,
)
@click.option(
    "--depth",
    is_flag=False,
    default=None,
    type=int,
    required=False,
    help="""The depth how the diagram should be drawn in reference to the level of imports. 0 is the model itself,
    1 the model itself and all models its importing and so on.
    NOTE: This can be used in conjunction to the model names to add arbitrary models to the diagram.
    """,
)
@click.pass_context
def diagram(ctx: click.Context, **kwargs: Any):
    """
    parse an arbitrary imd and creates a UML diagram of selected flavour
    """
    logging.info("Creating diagram")
    metamodel_path = kwargs.pop("imd")
    model_names = kwargs.pop("models")
    output_path = kwargs.pop("output_folder")
    direction = kwargs.pop("direction")
    linetype = kwargs.pop("linetype")
    file_name = kwargs.pop("file_name")
    multiplier = kwargs.pop("spacing_line_length")
    depth = kwargs.pop("depth")
    if model_names:
        model_names = model_names.split(",")
    else:
        model_names = []
    flavour = kwargs.pop("flavour")
    if flavour not in tool_settings.keys():
        click.echo(
            f'The output {flavour} is not allowed. It has to be one of {", ".join(tool_settings.keys())}'
        )
        sys.exit(2)
    try:
        metamodel = Imd16Reader().read(metamodel_path)
        index = Index(metamodel.datasection)
        diagram = Diagram.from_imd(index)
        assembled_file_name = f"{file_name or flavour}.{tool_settings[flavour]['postfix']}"
        logging.info(
            f"""Diagram ({flavour}) is generated with:
            path:                   {os.path.join(output_path, assembled_file_name)}
            direction:              {direction if direction else 'DEFAULT'}
            linetype:               {linetype if linetype else 'DEFAULT'}
            spacing line length:    {multiplier}
            depth:                  {depth}
        """
        )
        create_uml_diagram(
            diagram,
            index,
            model_names,
            flavour,
            assembled_file_name,
            output_path=output_path,
            direction=direction,
            linetype=linetype,
            multiplier=multiplier,
            depth=depth,
        )
    except Exception as error:
        click.echo(error)
        sys.exit(1)


@cli.command(
    help="""Parses an arbitrary imd and creates a library of python classes which
    represents a typed interface to the complete construction.""",
    context_settings=dict(help_option_names=["-h", "--help"]),
)
@click.option("-i", "--imd", is_flag=False, required=True, help="full path to imd file")
@click.option(
    "-o",
    "--output_folder",
    is_flag=False,
    required=True,
    help="Path to where the python package should be written",
)
@click.option(
    "-l",
    "--library_name",
    is_flag=False,
    required=True,
    help="Library name which will be used to assemble all python structures in.",
)
def python_classes(**kwargs: Any):
    logging.info("Creating python-classes")
    metamodel_path = kwargs.pop("imd")
    output_path = kwargs.pop("output_folder")
    library_name = kwargs.pop("library_name")
    try:
        metamodel = Imd16Reader().read(metamodel_path)
        index = Index(metamodel.datasection)
        library = Library.from_imd(metamodel.datasection.ModelData, index, library_name)
        logging.info(
            f"""Classes are generated with:
            path:       {os.path.join(output_path, library_storage_name(library_name))}
        """
        )
        create_python_classes(library, index, output_path)
    except Exception as error:
        click.echo(error)
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    cli()
