"""Main `ili2py` CLI."""

import os
import sys
from dataclasses import asdict
import json
from pathlib import Path

import click

from typing import Any
from ili2py import __version__
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.models.config import GeneratorConfig, GeneratorOutput
from xsdata.codegen.transformer import ResourceTransformer
from xsdata.codegen.writer import CodeWriter
from ili2py.interfaces.metamodel.ili import Transfer
from xsdata.utils.click import model_options
from xsdata.models.mixins import array_element, attribute, element
from xsdata.formats.dataclass.parsers.config import ParserConfig
from ili2py.interfaces.xsdata.generator import IMDGenerator

from ili2py.readers import create_reader_classes
from ili2py.readers_template import create_reader_classes as template_create_reader_classes

this_file_location = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))


def version_msg():
    """ili2py version, location and Python version.

    Get message about ili2py version, location
    and Python version.
    """
    python_version = sys.version[:3]
    message = u"ili2py %(version)s from {} (Python {})"
    location = os.path.dirname(this_file_location)
    return message.format(location, python_version)


def imd(input_meta_model: str) -> Transfer:
    ns_map = {}
    parser = XmlParser()
    parser.config = ParserConfig()
    parser.config.fail_on_unknown_properties = False
    metamodel = parser.parse(input_meta_model, Transfer, ns_map=ns_map)
    return metamodel


def xtf(input_data: str, model_name: str, metamodel: Transfer):
    parser = XmlParser()
    parser.config = ParserConfig()
    parser.config.fail_on_unknown_properties = False
    reader_classes = create_reader_classes(model_name, metamodel)
    interlis_transfer = parser.parse(input_data, reader_classes)
    return interlis_transfer


def xsdata_hooked(input_meta_model: str):
    config_file = Path(".xsdata.xml").resolve()
    config = GeneratorConfig.read(config_file)
    CodeWriter.generators.update({"imd": IMDGenerator})
    config.output.format.value = "imd"
    transformer = ResourceTransformer(config=config, print=True)
    transformer.process([input_meta_model], cache=False)


def xtf_reader_classes(model_name: str, metamodel: Transfer):
    parser = XmlParser()
    parser.config = ParserConfig()
    parser.config.fail_on_unknown_properties = False
    reader_classes = template_create_reader_classes(model_name, metamodel)
    return reader_classes


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version', message=version_msg())
@click.option('-v', '--verbose', is_flag=True, help='Print debug information', default=False)
@click.option('-i', '--imd', is_flag=False, help='full path to imd file')
def imd_json(**kwargs: Any):
    """
    parse an arbitrary metamodel to python and promote understood structure as json format
    """
    path = kwargs.pop("imd")
    try:
        click.echo(json.dumps(asdict(imd(path)), indent=2))
    except Exception as error:
        click.echo(error)
        sys.exit(1)


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version', message=version_msg())
@click.option('-v', '--verbose', is_flag=True, help='Print debug information', default=False)
@click.option('-i', '--imd', is_flag=False, help='full path to imd file')
@click.option('-x', '--xtf', is_flag=False, help='full path to xtf file')
@click.option('-m', '--model', is_flag=False, help='model name')
def xtf_json(**kwargs: Any):
    """
    parse an arbitrary metamodel create an XTF Reader from it and promote data structure as json format
    """
    metamodel_path = kwargs.pop("imd")
    xtf_data_path = kwargs.pop("xtf")
    model_name = kwargs.pop("model")
    try:
        metamodel = imd(metamodel_path)
        xtf_data = xtf(xtf_data_path, model_name, metamodel)
        click.echo(json.dumps(asdict(xtf_data), indent=2))
    except Exception as error:
        click.echo(error)
        sys.exit(1)


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version', message=version_msg())
@click.option('-v', '--verbose', is_flag=True, help='Print debug information', default=False)
@click.option('-i', '--imd', is_flag=False, help='full path to imd file')
@click.option('-m', '--model', is_flag=False, help='model name')
def xtf_reader_classes_cli(**kwargs: Any):
    """
    parse an arbitrary metamodel create an XTF Reader from it and promote data structure as json format
    """
    metamodel_path = kwargs.pop("imd")
    model_name = kwargs.pop("model")
    try:
        metamodel = imd(metamodel_path)
        xtf_classes = xtf_reader_classes(model_name, metamodel)
        click.echo(xtf_classes)
    except Exception as error:
        click.echo(error)
        sys.exit(1)


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version', message=version_msg())
@click.option('-v', '--verbose', is_flag=True, help='Print debug information', default=False)
@click.option('-i', '--imd', is_flag=False, help='full path to imd file')
def imd_xsdata(**kwargs: Any):
    """
    parse an arbitrary metamodel to python and promote understood structure as json format
    """
    path = kwargs.pop("imd")
    try:
        xsdata_hooked(path)
    except Exception as error:
        click.echo(error)
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    xsdata_hooked("file:///home/kalle/projects/rudert-geoinformatik/ili2py/data/Planungszonen_V1_1.imd")
    # pass