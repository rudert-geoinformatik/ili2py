"""This script assumes plantuml and mmdc (mermaid cli) is installed and available on the system!"""

import io
import logging
import os.path
import shutil
import subprocess
from pathlib import Path

import cairosvg
from PIL import Image

from ili2py.mappers.helpers import Index
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.diagram.interlis import uml_diagram
from ili2py.writers.diagram.interlis.uml import Diagram
from ili2py.writers.py.python_structure import Library
from ili2py.writers.py.render import create_python_classes

logging.getLogger().setLevel(logging.DEBUG)


def resize_image(input_path, output_path, target_size=(1920, 1080)):
    # Bild laden
    png_data = cairosvg.svg2png(url=input_path, background_color="white")
    img = Image.open(io.BytesIO(png_data))

    # Thumbnail erstellen (verhältnismäßig)
    img.thumbnail(target_size, Image.Resampling.LANCZOS)

    # Neues Bild mit schwarzem Hintergrund (oder beliebiger Farbe)
    new_img = Image.new("RGB", target_size, (255, 255, 255))

    # Berechne Position zum Zentrieren
    left = (target_size[0] - img.width) // 2
    top = (target_size[1] - img.height) // 2

    # Thumbnail einfügen
    new_img.paste(img, (left, top))

    # Speichern
    new_img.save(output_path)


reader = Imd16Reader()

# output_path = tempfile.mkdtemp(prefix="ili2py")
output_path = "build/ili2py_doc_diagrams"
dirpath = Path(output_path)
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)
print(os.getcwd())
data = [
    {
        "imd": "tests/data/models/LWB_Bewirtschaftungseinheiten_V3_0/LWB_Bewirtschaftungseinheiten_V3_0.imd",
        "model_names": [
            ["LWB_Bewirtschaftungseinheiten_V3_0"],
            [
                "LWB_Bewirtschaftungseinheiten_V3_0",
                "LWB_Landwirtschaftliche_Zonengrenzen_Kataloge_V2_0",
            ],
            [
                "LWB_Bewirtschaftungseinheiten_V3_0",
                "LWB_Landwirtschaftliche_Zonengrenzen_Kataloge_V2_0",
                "LWB_Landwirtschaftliche_Zonengrenzen_Kataloge_V2_0",
            ],
        ],
        "xtf": [],
    },
    {
        "imd": "tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd",
        "model_names": [["OeREBKRMtrsfr_V2_0"], ["OeREBKRMtrsfr_V2_0", "OeREBKRM_V2_0"]],
        "xtf": [
            "tests/data/models/OeREBKRMtrsfr_V2_0/ch.bazl.kataster-belasteter-standorte-zivilflugplaetze_v2_0.oereb.xtf"
        ],
    },
    {
        "imd": "tests/data/models/SIA405_Wasser_2015_2_d-20181005/SIA405_Wasser_2015_2_d-20181005.imd",
        "model_names": [
            ["SIA405_WASSER_2015_LV95"],
            ["SIA405_WASSER_2015_LV95", "SIA405_Base_LV95"],
            ["SIA405_WASSER_2015_LV95", "SIA405_Base_LV95", "Base_LV95"],
        ],
        "xtf": [],
    },
]

diagram_config = [
    {
        "flavour": "plantuml",
        "direction": "top to bottom",
        "linetype": "spline",
        "postfix": "puml",
        "multiplier": 2,
    },
    {
        "flavour": "plantuml",
        "direction": "top to bottom",
        "linetype": "spline",
        "postfix": "puml",
        "multiplier": 5,
    },
    {
        "flavour": "plantuml",
        "direction": "top to bottom",
        "linetype": "spline",
        "postfix": "puml",
        "multiplier": 8,
    },
    {
        "flavour": "plantuml",
        "direction": "top to bottom",
        "linetype": "ortho",
        "postfix": "puml",
        "multiplier": 2,
    },
    {
        "flavour": "plantuml",
        "direction": "top to bottom",
        "linetype": "ortho",
        "postfix": "puml",
        "multiplier": 5,
    },
    {
        "flavour": "plantuml",
        "direction": "top to bottom",
        "linetype": "ortho",
        "postfix": "puml",
        "multiplier": 8,
    },
]

for test_set in data:
    metamodel = reader.read(test_set["imd"])
    index = Index(metamodel.datasection)
    library_name = f'{index.types_bucket["Model"][-1].name}'
    library = Library.from_imd(metamodel.datasection.ModelData, index, library_name)
    create_python_classes(library, index, output_path)
    diagram = Diagram.from_imd(index)
    for configuration in diagram_config:
        for model_names in test_set["model_names"]:
            written_path = uml_diagram(
                diagram,
                index,
                model_names,
                configuration["flavour"],
                ".".join(
                    [
                        library_name,
                        "_".join(model_names),
                        configuration["flavour"],
                        configuration["direction"],
                        configuration["linetype"] if configuration["linetype"] else "_",
                        str(configuration.get("multiplier", 2)),
                        configuration["postfix"],
                    ]
                ),
                output_path,
                linetype=configuration["linetype"],
                direction=configuration["direction"],
                multiplier=configuration.get("multiplier", 2),
            )
            subprocess.call(["plantuml", "-tsvg", written_path])
            resize_image(
                written_path.replace(".puml", ".svg"),
                written_path.replace(".puml", ".resized.png"),
                (3840, 2160),
            )


"""
run in bash afterwards:
find build/ili2py_output_test/mermaid/ -type f -name "*.md" | parallel -j 14 'mmdc -i {} -o {.}.png'
plantuml -tpng build/ili2py_output_test/plantuml/*.puml
"""
