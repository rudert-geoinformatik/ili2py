"""
Compact geometry of XTF data, the values of the geometric fields of the rendered classes when
read with compact geometry (`xsdata_backend.XsdataBackend`).

Each geometry (COORD, POLYLINE, SURFACE, MULTI*) is one value instead of one object per XML
element. The module is plain python, it does not know how an XTF is read or written. That is
the task of a backend (see `backend.XtfBackend`), e.g. `xsdata_backend`.

The values are kept as `float`, `float(text)` keeps the value of the transfer exactly (shortest
repr). The precision of the axes is in `CoordSpec`.

Tools don't need to know any of this. The geometries inherit the protocols of `access`, which
the rendered dataclasses fulfill as well, so a tool reads a surface the same way whether it
was read compact or not. Only the values the protocols hand out are converted into the types
of the axes, what is stored stays float.
"""

from array import array
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Any, ClassVar, Self

from ili2py.readers.xtf.access import (
    CoordAccess,
    MultiPolylineAccess,
    MultiSurfaceAccess,
    PolylineAccess,
    SurfaceAccess,
)


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
        # the protocol bases bring their metaclass, without the module it would claim to be abc
        namespace = {"__slots__": (), "spec": spec, "__module__": cls.__module__}
        return type(cls.__name__, (cls,), namespace)

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


class Coord(Geometry, CoordAccess):
    """
    Attributes:
        values_: The values of the axes (C1, C2[, C3]). The trailing underscore keeps it apart
            from the method `values`.
    """

    __slots__ = ("values_",)

    values_: tuple[float, ...]

    @property
    def coordinates(self) -> tuple[float, ...]:
        """The values of the axes in the python types of the coord type, see `access`."""
        return self.axis_values(self.values_)


class Polyline(Geometry, PolylineAccess):
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
        """
        Walks the vertices, see `access.PolylineAccess`. This is the hot path of a tool
        reading all the geometry, so the vertices are sliced straight out of `coords`
        instead of asking `vertex` and its bounds check each time.

        Yields:
            The values of the axes of each vertex in the python types of the coord type.
        """
        coords, dimension = self.coords, self.dimension
        if not dimension:
            # an empty polyline does not know its dimension, there is nothing to slice
            return
        for start in range(0, len(self) * dimension, dimension):
            yield self.axis_values(coords[start : start + dimension])

    def vertex(self, index: int) -> tuple[float, ...]:
        """
        Args:
            index: The index of the vertex, negative counts from the end as in a list.

        Returns:
            The values of the axes of the vertex in the python types of the coord type.

        Raises:
            IndexError: If the polyline has no such vertex.
        """
        start = self.position(index) * self.dimension
        return self.axis_values(self.coords[start : start + self.dimension])

    def arc(self, index: int) -> tuple[float, ...] | None:
        """
        Args:
            index: The index of the vertex, negative counts from the end as in a list.

        Returns:
            The intermediate point and the radius if given (A1, A2[, R]) if the vertex ends an
            arc, None if it ends a straight.

        Raises:
            IndexError: If the polyline has no such vertex.
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


class Surface(Geometry, SurfaceAccess):
    """
    Attributes:
        boundaries: The boundaries, the first one is the exterior.
    """

    __slots__ = ("boundaries",)

    boundaries: list[Polyline]


class MultiPolyline(Geometry, MultiPolylineAccess):
    """
    Attributes:
        polylines: The polylines, INTERLIS 2.4 only.
    """

    __slots__ = ("polylines",)

    polylines: list[Polyline]


class MultiSurface(Geometry, MultiSurfaceAccess):
    """
    Attributes:
        surfaces: The surfaces, INTERLIS 2.4 only.
    """

    __slots__ = ("surfaces",)

    surfaces: list[Surface]
