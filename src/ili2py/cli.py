"""Main `ili2py` CLI."""
import logging
import os
import sys
from dataclasses import asdict
import json
from ili2py import version

import click

from typing import Any
from ili2py import __version__
from ili2py.readers.interlis_24.ilismeta16.xsdata import Reader as Imd16Reader
from ili2py.readers.interlis_23.xtf.xsdata import Reader as Xtf23Reader
from ili2py.writers.uml import create_uml_diagram
from ili2py.writers.uml.interlis_23 import flavours
from ili2py.writers.py import create_python_classes

this_file_location = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)

def version_msg():
    """ili2py version, location and Python version.

    Get message about ili2py version, location
    and Python version.
    """
    python_version = sys.version[:6]
    location = os.path.dirname(this_file_location)
    message = f"ili2py {version} from {location} (Python {python_version})"
    click.echo(message)

@click.group()
def cli():
    logging.Formatter(fmt='%(levelname)-8s :: %(message)s')
    logging.basicConfig(level=logging.INFO)
    logger.info('Starting ili2py CLI')
    version_msg()


@cli.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version', message=version_msg())
@click.option('-v', '--verbose', is_flag=True, help='Print debug information', default=False)
@click.option('-i', '--imd', is_flag=False, help='full path to imd file')
def imd_json(**kwargs: Any):
    """
    parse an arbitrary imd to python and promote understood structure as json format
    """
    path = kwargs.pop("imd")
    try:
        click.echo(json.dumps(asdict(Imd16Reader().read(path)), indent=2))
    except Exception as error:
        click.echo(error)
        sys.exit(1)


@cli.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version', message=version_msg())
@click.option('-v', '--verbose', is_flag=True, help='Print debug information', default=False)
@click.option('-i', '--imd', is_flag=False, help='full path to imd file')
@click.option('-x', '--xtf', is_flag=False, help='full path to xtf file')
def xtf_json(**kwargs: Any):
    """
    parse an arbitrary imd create an XTF Reader from it and promote data structure as json format
    """
    metamodel_path = kwargs.pop("imd")
    xtf_data_path = kwargs.pop("xtf")
    try:
        # create a useable python object representation of metamodel
        metamodel = Imd16Reader().read(metamodel_path)
        # create a reader for XTF based on the metamodel
        xtf_reader = Xtf23Reader(metamodel)
        # read the xtf with the generated reader
        xtf_data = xtf_reader.read(xtf_data_path)
        xtf_dict = {}
        for key in xtf_data:
            xtf_dict[key] = asdict(xtf_data[key])
        click.echo(json.dumps(xtf_dict, indent=2))
    except Exception as error:
        click.echo(error)
        sys.exit(1)


@cli.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version', message=version_msg())
@click.option('-v', '--verbose', is_flag=True, help='Print debug information', default=False)
@click.option('-i', '--imd', is_flag=False, help='full path to imd file')
@click.option('-m', '--models', is_flag=False, help='model names separated by comma')
@click.option('-o', '--output', is_flag=False, default=flavours[0], help=f'the desired flavour (one of {", ".join(flavours)})')
def ili2py_uml(**kwargs: Any):
    """
    parse an arbitrary imd and creates a UML diagram of selected flavour
    """
    metamodel_path = kwargs.pop("imd")
    model_names = kwargs.pop("models")
    if model_names:
        model_names = model_names.split(',')
    flavour = kwargs.pop("output")
    if flavour not in flavours:
        click.echo(f'The output {flavour} is not allowed. It has to be one of {" ,".join(flavours)}')
        sys.exit(2)
    try:
        metamodel = Imd16Reader().read(metamodel_path)
        xtf_classes = create_uml_diagram(model_names, metamodel, flavour)
        click.echo(xtf_classes)
    except Exception as error:
        click.echo(error)
        sys.exit(1)


@cli.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version', message=version_msg())
@click.option('-v', '--verbose', is_flag=True, help='Print debug information', default=False)
@click.option('-i', '--imd', is_flag=False, help='full path to imd file')
@click.option('-f', '--folder_output', is_flag=False, help='Path to where the python package should be written')
def ili2py_python_classes(**kwargs: Any):
    """
    parse an arbitrary imd and creates a UML diagram of selected flavour
    """
    metamodel_path = kwargs.pop("imd")
    output_path = kwargs.pop("folder_output")
    try:
        metamodel = Imd16Reader().read(metamodel_path)
        output = create_python_classes(metamodel, output_path)
        click.echo(output)
    except Exception as error:
        click.echo(error)
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    cli()
