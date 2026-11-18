"""
The access to the geometry of XTF data, the same whether it was read compact (`geometry`) or as
the rendered dataclasses. Tools reading geometry rely on these protocols and not on how the
geometry is stored. The compact types inherit them, so the type checker holds them to the
contract. The rendered classes fulfill them by their shape, the library must not depend on
ili2py.

The protocols have empty slots, otherwise every compact geometry inheriting them would get a
`__dict__` and lose what the slots save.

The values of the axes come in the python types of the coord type of the model, the protocols
follow the geometry of INTERLIS (COORD, POLYLINE with straights and arcs, SURFACE and AREA by
their boundaries, MULTI* in INTERLIS 2.4), not the shape of the XML. The XML would tell a tool
about BOUNDARY, POLYLINE and COORD elements, the tool only wants to know about a surface, its
boundaries and their vertices.

There is no MULTICOORD, the compact geometry does not know it either.
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

    __slots__ = ()

    @property
    def coordinates(self) -> tuple[float, ...]:
        """The values of the axes (C1, C2[, C3]), empty if the coord holds none."""


@runtime_checkable
class PolylineAccess(Protocol):
    """
    The access to a POLYLINE, the same for the compact geometry (`geometry.Polyline`) and
    the rendered line dataclasses. Iterating gives the values of the axes of each vertex.
    """

    __slots__ = ()

    def __len__(self) -> int:
        """The number of vertices, the start point included."""

    def __iter__(self) -> Iterator[tuple[float, ...]]:
        """
        Walks the vertices one after the other. Whoever wants to know if a vertex ends an arc
        asks `arc` with its index, most of the lines are straights only and don't want to pay
        for asking.

        Yields:
            The values of the axes of each vertex.
        """

    def vertex(self, index: int) -> tuple[float, ...]:
        """
        Args:
            index: The index of the vertex, negative counts from the end as in a list.

        Returns:
            The values of the axes of the vertex.

        Raises:
            IndexError: If the polyline has no such vertex.
        """

    def arc(self, index: int) -> tuple[float, ...] | None:
        """
        INTERLIS keeps an arc at its end point, the vertex carries the intermediate point
        and, if given, the radius. The arc starts at the vertex before.

        Args:
            index: The index of the vertex, negative counts from the end as in a list.

        Returns:
            The intermediate point and the radius if given (A1, A2[, R]), None if the vertex
            ends a straight.

        Raises:
            IndexError: If the polyline has no such vertex.
        """


@runtime_checkable
class SurfaceAccess(Protocol):
    """
    The access to a SURFACE or AREA, the same for the compact geometry (`geometry.Surface`)
    and the rendered surface dataclasses. The first boundary is the exterior.
    """

    __slots__ = ()

    @property
    def boundaries(self) -> Sequence[PolylineAccess]:
        """The boundaries, the exterior first and the holes after, empty if none."""


@runtime_checkable
class MultiPolylineAccess(Protocol):
    """
    The access to a MULTIPOLYLINE (INTERLIS 2.4), see `PolylineAccess`.
    """

    __slots__ = ()

    @property
    def polylines(self) -> Sequence[PolylineAccess]:
        """The polylines, each one answers on its own as `PolylineAccess`."""


@runtime_checkable
class MultiSurfaceAccess(Protocol):
    """
    The access to a MULTISURFACE or MULTIAREA (INTERLIS 2.4), see `SurfaceAccess`.
    """

    __slots__ = ()

    @property
    def surfaces(self) -> Sequence[SurfaceAccess]:
        """The surfaces, each one answers on its own as `SurfaceAccess`."""
