"""Main `ili2py` CLI."""

import logging
import os
import sys

import click

from typing import Any
from ili2py import __version__
from ili2py.mappers.helpers import Index
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.uml import create_uml_diagram
from ili2py.writers.uml.interlis_23 import tool_settings, Diagram
from ili2py.writers.py import create_python_classes, Library

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


@cli.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__, "-V", "--version", message=version_msg())
@click.option("-v", "--verbose", is_flag=True, help="Print debug information", default=False)
@click.option("-i", "--imd", is_flag=False, help="full path to imd file")
@click.option("-m", "--models", is_flag=False, help="model names separated by comma")
@click.option(
    "-o",
    "--output",
    is_flag=False,
    default=list(tool_settings.keys())[0],
    help=f'the desired flavour (one of {", ".join(tool_settings.keys())})',
)
@click.option(
    "-f",
    "--folder_output",
    is_flag=False,
    help="Path to where the python package should be written",
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
def ili2py_uml(**kwargs: Any):
    """
    parse an arbitrary imd and creates a UML diagram of selected flavour
    """
    metamodel_path = kwargs.pop("imd")
    model_names = kwargs.pop("models")
    output_path = kwargs.pop("folder_output")
    direction = kwargs.pop("direction")
    linetype = kwargs.pop("linetype")
    if model_names:
        model_names = model_names.split(",")
    else:
        model_names = []
    flavour = kwargs.pop("output")
    if flavour not in tool_settings.keys():
        click.echo(
            f'The output {flavour} is not allowed. It has to be one of {" ,".join(tool_settings.keys())}'
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
            output_path=output_path,
            direction=direction,
            linetype=linetype,
        )
    except Exception as error:
        click.echo(error)
        sys.exit(1)


@cli.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__, "-V", "--version", message=version_msg())
@click.option("-v", "--verbose", is_flag=True, help="Print debug information", default=False)
@click.option("-i", "--imd", is_flag=False, help="full path to imd file")
@click.option(
    "-f",
    "--folder_output",
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
    """
    parse an arbitrary imd and creates a UML diagram of selected flavour
    """
    metamodel_path = kwargs.pop("imd")
    output_path = kwargs.pop("folder_output")
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
