"""
The interface to read and write XTF with the rendered classes (see `writers.py.render`).

The classes themselves do not depend on a library to parse or serialize XML. A backend binds
them to an XTF, it reads the field metadata of the dataclasses (element names, namespaces) and
may read the geometry compact (`geometry`). `xsdata_backend.XsdataBackend` is the one of
ili2py.
"""

from io import TextIOBase
from pathlib import Path
from typing import IO, Any, Protocol, TypeVar, runtime_checkable

T = TypeVar("T")


@runtime_checkable
class XtfBackend(Protocol):
    """Reads and writes an XTF with the classes of a rendered library."""

    def read(self, source: str | Path | IO[bytes], transfer_class: type[T]) -> T:
        """
        Parses an XTF into the objects of the classes.

        Args:
            source: The path or file object of the XTF.
            transfer_class: The class of the root element of the XTF (`xtf_opening.Transfer`).

        Returns:
            The transfer object tree.
        """
        ...

    def write(
        self, transfer: Any, out: TextIOBase, ns_map: dict[str | None, str] | None = None
    ) -> None:
        """
        Serializes a transfer object tree to an XTF.

        Args:
            transfer: The transfer object tree.
            out: The text stream to write to.
            ns_map: The namespace prefixes, key None is the default namespace.
        """
        ...
