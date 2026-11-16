"""Helpers for the end-to-end tests IMD -> python classes -> XTF read/write -> ilivalidator."""

import importlib
import subprocess
import sys
import zipfile
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType
from typing import IO, cast
from xml.etree.ElementTree import iterparse

from ili2py.mappers.helpers import Index
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.writers.helpers import handle_model_versions
from ili2py.writers.py.python_structure import Library
from ili2py.writers.py.render import create_python_classes


@dataclass
class XtfHeader:
    """
    Represents the header section of an XTF, as far as it is needed before parsing the data.

    Attributes:
        models: The model names listed in the header section.
        namespaces: The namespaces declared in the document. The key is the prefix, "" is the
            default namespace.
    """

    models: set[str] = field(default_factory=set)
    namespaces: dict[str, str] = field(default_factory=dict)

    def ns_map(self) -> dict[str | None, str]:
        """The namespaces as the xsdata serializer takes them, the default "" becomes None."""
        return {(prefix or None): uri for prefix, uri in self.namespaces.items()}


@dataclass
class GeneratedLibrary:
    """
    Represents the python classes generated out of an IMD.

    Attributes:
        name: The library name, it is the name of the last model in the IMD.
        ili_version: The INTERLIS version of the models (2.3 or 2.4).
        path: The folder of the generated library package.
        models: All models of the IMD except INTERLIS. An IMD can hold several (e.g. LV03 and
            LV95).
    """

    name: str
    ili_version: str
    path: Path
    models: set[str] = field(default_factory=set)


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def xtf_header(source: str | Path | IO[bytes]) -> XtfHeader:
    """
    Reads the header section of an INTERLIS 2.3 or 2.4 XTF without parsing the data section.

    2.3: <HEADERSECTION><MODELS><MODEL NAME="..."/></MODELS>
    2.4: <ili:headersection><ili:models><ili:model>...</ili:model></ili:models>

    Args:
        source: The path or the file object (e.g. a member of a zip) to read the XTF from.

    Returns:
        The models and namespaces of the XTF.
    """
    header = XtfHeader()
    for event, item in iterparse(source, events=("start-ns", "start", "end")):
        if event == "start-ns":
            # typeshed types every item as Element, for start-ns it is (prefix, uri)
            prefix, uri = cast(tuple[str, str], item)
            header.namespaces.setdefault(prefix, uri)
            continue
        name = _local_name(item.tag)
        if event == "start" and name == "datasection":
            break
        if event == "end" and name == "model":
            model_name = item.get("NAME") or (item.text or "").strip()
            if model_name:
                header.models.add(model_name)
    return header


def _extract_member(archive: zipfile.ZipFile, member: str, target_dir: Path) -> Path:
    # flatten the member path, avoids writing outside target_dir
    target = target_dir / Path(member).name
    try:
        with archive.open(member) as src:
            target.write_bytes(src.read())
    except zipfile.BadZipFile as error:
        raise zipfile.BadZipFile(f"{archive.filename}: {error}") from error
    return target


def imd_models(index: Index) -> tuple[str, set[str]]:
    """
    The models of an IMD as the XTF of it lists them.

    Args:
        index: The index of the IMD.

    Returns:
        The main model (the last one, it is the library name) and all models except INTERLIS.
        An IMD can hold several (e.g. LV03 and LV95).
    """
    return index.types_bucket["Model"][-1].name, {
        model.name
        for model in index.types_bucket["Model"]
        if model.name != "INTERLIS" and "." not in model.name
    }


def find_xtf(main_model: str, models: set[str], model_folder: Path, target_dir: Path) -> Path:
    """
    Finds the XTF for the models of an IMD in its test data folder, see `imd_models`.

    The main model is searched first. Only if no XTF lists it, the other models of the IMD
    are accepted (e.g. LV95 variant in an IMD whose last model is LV03). Imported models are
    not preferred, otherwise data of an imported model in the same folder would win
    (LWB_Nutzungsflaechen_V2_0 imports LWB_Bewirtschaftungseinheiten_V2_0).

    Args:
        main_model: The main model of the IMD.
        models: All models of the IMD except INTERLIS.
        model_folder: The test data folder of the model.
        target_dir: The folder a zip member is extracted to.

    Returns:
        The path of the XTF.

    Raises:
        LookupError: If no XTF lists one of the models.
    """
    for model_names in ({main_model}, models):
        try:
            return _find_xtf(model_folder, model_names, target_dir)
        except LookupError:
            continue
    raise LookupError(f"no xtf for models {sorted(models)} found in {model_folder}")


def _find_xtf(model_folder: Path, model_names: set[str], target_dir: Path) -> Path:
    """
    Searches the XTF for one of the models, see `find_xtf`. A plain .xtf in the folder wins,
    otherwise the zips are searched. Zips and members are searched in sorted order, the first
    .xtf whose header lists one of the models is used.

    Catalogue .xml in the zips are not used: validating them together with the data fails
    when a zip ships translated catalogues with the same OIDs (Richtplan_erneuerbare_Energien).

    Args:
        model_folder: The test data folder of the model.
        model_names: The models of which one has to be listed in the header section.
        target_dir: The folder a zip member is extracted to.

    Returns:
        The path of the XTF.

    Raises:
        LookupError: If no XTF lists one of the models.
    """
    for xtf in sorted(model_folder.glob("*.xtf")):
        if model_names & xtf_header(xtf).models:
            return xtf
    for zip_path in sorted(model_folder.glob("*.zip")):
        with zipfile.ZipFile(zip_path) as archive:
            for member in sorted(archive.namelist()):
                if not member.lower().endswith(".xtf"):
                    continue
                with archive.open(member) as stream:
                    models = xtf_header(stream).models
                if not model_names & models:
                    continue
                target_dir.mkdir(parents=True, exist_ok=True)
                return _extract_member(archive, member, target_dir)
    raise LookupError(f"no xtf for models {sorted(model_names)} found in {model_folder}")


def generate_library(imd_path: Path, output_path: Path) -> GeneratedLibrary:
    """
    Reads the IMD and renders the python classes, as test_write_python.py does.

    Args:
        imd_path: The path of the IMD.
        output_path: The folder the library package is created in.

    Returns:
        The generated library.
    """
    metamodel = Imd16Reader().read(str(imd_path))
    index = Index(metamodel.datasection)
    library_name, models = imd_models(index)
    library = Library.from_imd(metamodel.datasection.ModelData, index, library_name)
    create_python_classes(library, index, str(output_path))
    return GeneratedLibrary(
        name=library_name,
        ili_version=handle_model_versions(index),
        path=output_path / library_name,
        models=models,
    )


@contextmanager
def imported_library(library: GeneratedLibrary) -> Iterator[ModuleType]:
    """
    Imports `<library>.xtf_opening` and removes the library from sys.path and sys.modules on
    exit. Parametrized runs generate libraries into different folders, without cleanup a
    library imported earlier would shadow the next one.

    Args:
        library: The generated library to import.

    Yields:
        The imported xtf_opening module, it holds the Transfer class.
    """
    search_path = str(library.path.parent)
    sys.path.insert(0, search_path)
    try:
        yield importlib.import_module(f"{library.name}.xtf_opening")
    finally:
        sys.path.remove(search_path)
        for module_name in list(sys.modules):
            if module_name == library.name or module_name.startswith(f"{library.name}."):
                del sys.modules[module_name]
        importlib.invalidate_caches()


def run_ilivalidator(
    jar: Path,
    files: list[Path],
    modeldirs: list[str],
    log_path: Path,
    timeout: int = 900,
) -> subprocess.CompletedProcess[str]:
    """
    Validates XTF files with ilivalidator.

    Args:
        jar: The path of the ilivalidator jar.
        files: The XTF files to validate.
        modeldirs: The folders and repositories where ilivalidator looks up the models.
        log_path: The path of the ilivalidator log file.
        timeout: The maximum run time in seconds.

    Returns:
        The finished process, the return code is 0 if the validation passed.
    """
    command = [
        "java",
        "-jar",
        str(jar),
        "--modeldir",
        ";".join(modeldirs),
        "--log",
        str(log_path),
        *(str(file) for file in files),
    ]
    return subprocess.run(  # noqa: S603 - fixed command, paths from the test data
        command, capture_output=True, text=True, timeout=timeout, check=False
    )
