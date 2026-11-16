"""
The access to the geometry of XTF data, the same whether it was read compact (`geometry`) or as
the rendered dataclasses. Tools reading geometry rely on these protocols and not on how the
geometry is stored, the rendered classes and the compact types fulfill them without importing
them.

The values of the axes come in the python types of the coord type of the model, the protocols
follow the geometry of INTERLIS (COORD, POLYLINE with straights and arcs, SURFACE and AREA by
their boundaries, MULTI* in INTERLIS 2.4), not the shape of the XML.
"""

from collections.abc import Iterator, Sequence
from typing import Protocol, runtime_checkable


@runtime_checkable
class CoordAccess(Protocol):
    """
    The access to a COORD, the same for the compact geometry (`geometry.Coord`) and the
    rendered coord dataclasses. Tools reading geometry rely on this and not on how it is
    stored.
    """

    @property
    def coordinates(self) -> tuple[float, ...]: ...


@runtime_checkable
class PolylineAccess(Protocol):
    """
    The access to a POLYLINE, the same for the compact geometry (`geometry.Polyline`) and
    the rendered line dataclasses. Iterating gives the values of the axes of each vertex.
    """

    def __len__(self) -> int: ...

    def __iter__(self) -> Iterator[tuple[float, ...]]: ...

    def vertex(self, index: int) -> tuple[float, ...]: ...

    def arc(self, index: int) -> tuple[float, ...] | None: ...


@runtime_checkable
class SurfaceAccess(Protocol):
    """
    The access to a SURFACE or AREA, the same for the compact geometry (`geometry.Surface`)
    and the rendered surface dataclasses. The first boundary is the exterior.
    """

    @property
    def boundaries(self) -> Sequence[PolylineAccess]: ...


@runtime_checkable
class MultiPolylineAccess(Protocol):
    """
    The access to a MULTIPOLYLINE (INTERLIS 2.4), see `PolylineAccess`.
    """

    @property
    def polylines(self) -> Sequence[PolylineAccess]: ...


@runtime_checkable
class MultiSurfaceAccess(Protocol):
    """
    The access to a MULTISURFACE or MULTIAREA (INTERLIS 2.4), see `SurfaceAccess`.
    """

    @property
    def surfaces(self) -> Sequence[SurfaceAccess]: ...
