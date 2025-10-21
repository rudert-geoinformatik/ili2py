"""Main `ili2py` CLI."""

import logging
import os
import sys
from typing import Any

import click

from ili2py import __version__
from ili2py.mappers.helpers import Index
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.py.python_structure import Library
from ili2py.writers.py.render import create_python_classes
from ili2py.writers.uml import create_uml_diagram
from ili2py.writers.uml.interlis_23 import Diagram, tool_settings

this_file_location = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))

logging.basicConfig(level="DEBUG")


def version_msg():
    """ili2py version, location and Python version.

    Get message about ili2py version, location
    and Python version.
    """
    python_version = sys.version[:6]
    location = os.path.dirname(this_file_location)
    message = f"ili2py from {location} (Python {python_version})"
    return message


@click.group()
def cli():
    logging.info("Starting ili2py CLI")
    logging.info(version_msg())


@cli.command(
    help="""Parses an arbitrary imd and creates and creates a diagram of selected flavour
    representing the selected models.""",
    context_settings=dict(help_option_names=["-h", "--help"]),
)
@click.version_option(__version__, "-V", "--version", message=version_msg())
@click.option("-v", "--verbose", is_flag=True, help="Print debug information", default=False)
@click.option("-i", "--imd", is_flag=False, help="full path to imd file")
@click.option(
    "-m",
    "--models",
    is_flag=False,
    help="""Model names separated by comma. This is used to filter the content of the resulting diagram.
    If not provided, the full tree will be drawn.""",
)
@click.option(
    "-f",
    "--flavour",
    is_flag=False,
    default=list(tool_settings.keys())[0],
    help=f'the desired flavour (one of {", ".join(tool_settings.keys())})',
)
@click.option(
    "-o",
    "--output_folder",
    is_flag=False,
    help="""Path to the folder where the python package should be written to.
    The folder will be created if not existing.""",
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
def ili2py_diagram(**kwargs: Any):
    """
    parse an arbitrary imd and creates a UML diagram of selected flavour
    """
    metamodel_path = kwargs.pop("imd")
    model_names = kwargs.pop("models")
    output_path = kwargs.pop("output_folder")
    direction = kwargs.pop("direction")
    linetype = kwargs.pop("linetype")
    file_name = kwargs.pop("file_name")
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
        create_uml_diagram(
            diagram,
            index,
            model_names,
            flavour,
            f"{file_name or flavour}.{tool_settings[flavour]['postfix']}",
            output_path=output_path,
            direction=direction,
            linetype=linetype,
        )
    except Exception as error:
        click.echo(error)
        sys.exit(1)


@cli.command(
    help="""Parses an arbitrary imd and creates a library of python classes which
    represents a typed interface to the complete construction.""",
    context_settings=dict(help_option_names=["-h", "--help"]),
)
@click.version_option(__version__, "-V", "--version", message=version_msg())
@click.option("-v", "--verbose", is_flag=True, help="Print debug information", default=False)
@click.option("-i", "--imd", is_flag=False, help="full path to imd file")
@click.option(
    "-o",
    "--output_folder",
    is_flag=False,
    help="Path to where the python package should be written",
)
@click.option(
    "-l",
    "--library_name",
    is_flag=False,
    help="Library name which will be used to assemble all python structures in.",
)
def ili2py_python_classes(**kwargs: Any):
    metamodel_path = kwargs.pop("imd")
    output_path = kwargs.pop("output_folder")
    try:
        metamodel = Imd16Reader().read(metamodel_path)
        index = Index(metamodel.datasection)
        library = Library.from_imd(
            metamodel.datasection.ModelData, index, kwargs.pop("library_name")
        )
        create_python_classes(library, index, output_path)
    except Exception as error:
        click.echo(error)
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    cli()
