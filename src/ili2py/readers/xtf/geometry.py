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
from dataclasses import dataclass
from typing import Any, ClassVar, Self


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
        """The values of the axes, for those who prefer to read a name without underscore."""
        return self.values_


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

    def vertex(self, index: int) -> tuple[float, ...]:
        """
        Args:
            index: The index of the vertex.

        Returns:
            The values of the axes of the vertex.
        """
        start = index * self.dimension
        return tuple(self.coords[start : start + self.dimension])


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
