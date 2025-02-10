
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from typing import List

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer
from ili2py.interfaces.interlis.interlis_24.ilismeta16.helper import index_modeldata
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.extendable_me.type.type_class import \
    Class, BaseClass
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.serialization_elements import MultiplicityElement

flavours = ["mermaid", "plantuml"]

ns_map = {
    "ili": "http://www.interlis.ch/INTERLIS2.3"
}

direction = [
    'LR', 'RL', 'TD', 'DT'
]


def render_multiplicity(multiplicity: MultiplicityElement) -> str:
    if multiplicity.min == 1 and multiplicity.max == 1:
        return '1'
    elif multiplicity.min == 0 and multiplicity.max == 0:
        #Cardinality / Multiplicity '0' is not implemented in mermaid
        return '0'
    elif multiplicity.min == 0 and multiplicity.max == 1:
        return '0..1'
    elif multiplicity.min == 1 and multiplicity.max is None:
        return '1..*'
    elif multiplicity.min == 0 and multiplicity.max is None:
        # Cardinality / Multiplicity '0..*' is not implemented in mermaid directly we deliver empty string
        return "0..*"
    elif multiplicity.min is None and multiplicity.max is None:
        return '*'
    else:
        return f'{multiplicity.min}..{multiplicity.max}'


def uml_diagram(metamodel: ImdTransfer, model_names: List[str], flavour: str):
    index = index_modeldata(metamodel)
    tpl_dir = Path(__file__).parent.joinpath("templates")
    env = Environment(loader=FileSystemLoader(str(tpl_dir)), autoescape=False)
    if flavour not in flavours:
        raise NotImplementedError
    output = env.get_template(f"{flavour}.jinja2").render(
        metamodel=metamodel,
        index=index,
        model_names=model_names,
        class_type=Class,
        base_class_instance=BaseClass,
        isinstance=isinstance,
        render_multiplicity=render_multiplicity,
        direction=direction[1],
        len=len
    )
    src_code_encoded = output.encode()
    return src_code_encoded.decode()
