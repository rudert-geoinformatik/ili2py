"""
Compact geometry of XTF data, the values of the geometric fields of the rendered classes when
read with compact geometry (`xsdata_backend.XsdataBackend`).

Each geometry (COORD, POLYLINE, SURFACE, MULTI*) is one value instead of one object per XML
element. The module is plain python, it does not know how an XTF is read or written. That is
the task of a backend (see `backend.XtfBackend`), e.g. `xsdata_backend`.

The values are kept as `float`, `float(text)` keeps the value of the transfer exactly (shortest
repr). The precision of the axes is in `CoordSpec`.
"""

from array import array
from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass
from typing import Any, ClassVar, Protocol, Self, runtime_checkable


@dataclass(frozen=True, slots=True)
class CoordSpec:
    """
    The axes of a coord type.

    Attributes:
        tid: The tid of the coord type.
        axes: The axis names (C1, C2, C3).
        types: The python type of each axis (int or float).
        precisions: The number of decimals of each axis, None if not defined.
    """

    tid: str
    axes: tuple[str, ...]
    types: tuple[type, ...]
    precisions: tuple[int | None, ...]


class Geometry:
    """
    Base of the geometries. A subclass per coord type carries the spec of its axes
    (`with_spec`). They are no dataclasses, a backend binding dataclasses as XML elements
    would treat them as such instead of as one value.
    """

    __slots__: tuple[str, ...] = ()
    spec: ClassVar[CoordSpec | None] = None

    def __init__(self, *args: Any) -> None:
        """
        Args:
            args: The values in the order of `fields`.
        """
        for name, value in zip(self.__slots__ or self.fields(), args, strict=True):
            setattr(self, name, value)

    @classmethod
    def fields(cls) -> tuple[str, ...]:
        """The names of the values, the slots of the base geometry type."""
        for base in cls.__mro__:
            if base.__dict__.get("__slots__"):
                return base.__dict__["__slots__"]
        return ()

    @classmethod
    def with_spec(cls, spec: CoordSpec | None) -> type[Self]:
        """
        A subclass of the geometry type which carries the spec of the axes. It keeps the name
        of its base, so a printed geometry does not tell about the trick.

        Args:
            spec: The spec of the axes of a coord type.

        Returns:
            The subclass, the backend keeps one per geometry type and spec.
        """
        return type(cls.__name__, (cls,), {"__slots__": (), "spec": spec})

    def values(self) -> tuple[Any, ...]:
        """The values in the order of `fields`, enough to build the geometry again."""
        return tuple(getattr(self, name) for name in self.fields())

    def axis_values(self, values: Iterable[float]) -> tuple[Any, ...]:
        """
        The values of the axes of a vertex in the python types of the coord type. The compact
        geometry stores every axis as float, the rendered coord dataclasses carry the type of
        the model (e.g. int for `INTERLIS.LineCoord`).

        Args:
            values: The values of the axes as stored.

        Returns:
            The values as the model defines them, as float if the spec is unknown.
        """
        spec = self.spec
        if spec is None or int not in spec.types:
            return tuple(values)
        return tuple(
            axis_type(value) for axis_type, value in zip(spec.types, values, strict=True)
        )

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Geometry)
            and self.fields() == other.fields()
            and self.values() == other.values()
        )

    def __repr__(self) -> str:
        values = ", ".join(f"{name}={getattr(self, name)!r}" for name in self.fields())
        return f"{type(self).__name__}({values})"

    def __reduce__(self) -> tuple:
        return type(self), self.values()


class Coord(Geometry):
    """
    Attributes:
        values_: The values of the axes (C1, C2[, C3]). The trailing underscore keeps it apart
            from the method `values`.
    """

    __slots__ = ("values_",)

    values_: tuple[float, ...]

    @property
    def coordinates(self) -> tuple[float, ...]:
        """The values of the axes in the python types of the coord type (`CoordAccess`)."""
        return self.axis_values(self.values_)


class Polyline(Geometry):
    """
    Attributes:
        coords: The coordinates of all vertices, flat (x1, y1, x2, y2, ...).
        dimension: The number of axes of a vertex.
        arcs: Key is the index of a vertex which is the end point of an arc, value is the
            intermediate point and the radius if given (A1, A2[, R]).
    """

    __slots__ = ("coords", "dimension", "arcs")

    coords: array
    dimension: int
    arcs: dict[int, tuple[float, ...]]

    def __len__(self) -> int:
        return len(self.coords) // self.dimension if self.dimension else 0

    def __iter__(self) -> Iterator[tuple[float, ...]]:
        for index in range(len(self)):
            yield self.vertex(index)

    def vertex(self, index: int) -> tuple[float, ...]:
        """
        Args:
            index: The index of the vertex, negative counts from the end as in a list.

        Returns:
            The values of the axes of the vertex in the python types of the coord type.
        """
        start = self.position(index) * self.dimension
        return self.axis_values(self.coords[start : start + self.dimension])

    def arc(self, index: int) -> tuple[float, ...] | None:
        """
        Args:
            index: The index of the vertex.

        Returns:
            The intermediate point and the radius if given (A1, A2[, R]) if the vertex ends an
            arc, None if it ends a straight.
        """
        return self.arcs.get(self.position(index))

    def position(self, index: int) -> int:
        """
        The position of a vertex, negative indices count from the end as they do in a list.

        Args:
            index: The index of the vertex.

        Returns:
            The position, between 0 and the number of vertices.

        Raises:
            IndexError: If the polyline has no such vertex.
        """
        count = len(self)
        if not -count <= index < count:
            raise IndexError(f"vertex {index} out of {count}")
        return index % count


class Surface(Geometry):
    """
    Attributes:
        boundaries: The boundaries, the first one is the exterior.
    """

    __slots__ = ("boundaries",)

    boundaries: list[Polyline]


class MultiPolyline(Geometry):
    """
    Attributes:
        polylines: The polylines, INTERLIS 2.4 only.
    """

    __slots__ = ("polylines",)

    polylines: list[Polyline]


class MultiSurface(Geometry):
    """
    Attributes:
        surfaces: The surfaces, INTERLIS 2.4 only.
    """

    __slots__ = ("surfaces",)

    surfaces: list[Surface]


@runtime_checkable
class CoordAccess(Protocol):
    """
    The access to a COORD, the same for the compact geometry (`Coord`) and the rendered coord
    dataclasses. Tools reading geometry rely on this and not on how it is stored.
    """

    @property
    def coordinates(self) -> tuple[float, ...]: ...


@runtime_checkable
class PolylineAccess(Protocol):
    """
    The access to a POLYLINE, the same for the compact geometry (`Polyline`) and the rendered
    line dataclasses. Iterating gives the values of the axes of each vertex.
    """

    def __len__(self) -> int: ...

    def __iter__(self) -> Iterator[tuple[float, ...]]: ...

    def vertex(self, index: int) -> tuple[float, ...]: ...

    def arc(self, index: int) -> tuple[float, ...] | None: ...


@runtime_checkable
class SurfaceAccess(Protocol):
    """
    The access to a SURFACE or AREA, the same for the compact geometry (`Surface`) and the
    rendered surface dataclasses. The first boundary is the exterior.
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
