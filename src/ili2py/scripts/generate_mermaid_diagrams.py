"""This script assumes plantuml and mmdc (mermaid cli) is installed and available on the system!"""

import logging
import os.path
import shutil
import subprocess
from pathlib import Path

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
    # png_data = cairosvg.svg2png(url=input_path, background_color="white")
    img = Image.open(input_path)

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
output_path = "build/mermaid_showcase_diagrams"
dirpath = Path(output_path)
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)
print(os.getcwd())
data = [
    {
        "imd": "tests/data/models/OeREBKRMtrsfr_V2_0/OeREBKRMtrsfr_V2_0.imd",
        "model_names": [
            ["OeREBKRMtrsfr_V2_0"],
            ["OeREBKRMtrsfr_V2_0", "OeREBKRM_V2_0"],
            ["OeREBKRMtrsfr_V2_0", "OeREBKRM_V2_0", "INTERLIS"],
        ],
        "xtf": [
            "tests/data/models/OeREBKRMtrsfr_V2_0/ch.bazl.kataster-belasteter-standorte-zivilflugplaetze_v2_0.oereb.xtf"
        ],
    },
]

diagram_config = [
    {"flavour": "mermaid", "direction": "LR", "linetype": None, "postfix": "md"},
    {"flavour": "mermaid", "direction": "RL", "linetype": None, "postfix": "md"},
    {"flavour": "mermaid", "direction": "TB", "linetype": None, "postfix": "md"},
    {"flavour": "mermaid", "direction": "BT", "linetype": None, "postfix": "md"},
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
            subprocess.call(["mmdc", "-i", written_path, "-o", written_path.replace(".md", ".png")])
            resize_image(
                written_path.replace(".md", "-1.png"),
                written_path.replace(".md", ".resized.png"),
                (3840, 2160),
            )


"""
run in bash afterwards:
find build/ili2py_output_test/mermaid/ -type f -name "*.md" | parallel -j 14 'mmdc -i {} -o {.}.png'
plantuml -tpng build/ili2py_output_test/plantuml/*.puml
"""
