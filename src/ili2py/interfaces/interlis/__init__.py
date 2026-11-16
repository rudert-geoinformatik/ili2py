from abc import ABC
from typing import ClassVar


class GeometryTags(ABC):  # noqa: B024 - subclasses set the names of their transfer version
    """
    The element names of the geometry in an XTF. Each transfer version (`interlis_23`,
    `interlis_24`) subclasses it and only names its namespaces and the local names, the
    qualified names are put together here once, so the readers and writers can compare them
    directly with the tags of lxml.

    Attributes:
        transfer_namespace: The namespace of the transfer elements (TRANSFER, Transfer), it
            tells the transfer versions apart.
        namespace: The namespace of the geometry elements.
    """

    transfer_namespace: ClassVar[str]
    namespace: ClassVar[str]
    coord_name: ClassVar[str]
    arc_name: ClassVar[str]
    polyline_name: ClassVar[str]
    surface_name: ClassVar[str]
    boundary_names: ClassVar[tuple[str, ...]]
    axis_names: ClassVar[tuple[str, ...]]
    arc_point_names: ClassVar[tuple[str, ...]]
    multipolyline_name: ClassVar[str | None] = None
    multisurface_name: ClassVar[str | None] = None

    def __init__(self) -> None:
        self.coord = self.qualified(self.coord_name)
        self.arc = self.qualified(self.arc_name)
        self.polyline = self.qualified(self.polyline_name)
        self.surface = self.qualified(self.surface_name)
        self.boundaries = tuple(map(self.qualified, self.boundary_names))
        self.axes = tuple(map(self.qualified, self.axis_names))
        self.arc_points = tuple(map(self.qualified, self.arc_point_names))
        self.multipolyline = self.qualified_optional(self.multipolyline_name)
        self.multisurface = self.qualified_optional(self.multisurface_name)

    @classmethod
    def reads(cls, transfer_class: type) -> bool:
        """
        If the transfer class belongs to this transfer version, told by the namespace of its
        element.

        Args:
            transfer_class: The class of the root element of the XTF (`xtf_opening.Transfer`).

        Returns:
            True if the namespace is the one of this transfer version.
        """
        meta = getattr(transfer_class, "Meta", None)
        return getattr(meta, "namespace", None) == cls.transfer_namespace

    @staticmethod
    def local_name(tag: str) -> str:
        """The element name without its namespace."""
        return tag.rsplit("}", 1)[-1]

    def qualified(self, name: str) -> str:
        """The element name with the namespace of the geometry, as lxml writes it."""
        return f"{{{self.namespace}}}{name}"

    def qualified_optional(self, name: str | None) -> str | None:
        """As `qualified`, for the elements a transfer version does not know (None)."""
        return self.qualified(name) if name else None

    @property
    def geometries(self) -> frozenset[str]:
        """The element names of the geometries (COORD, POLYLINE, SURFACE, MULTI*)."""
        candidates = (
            self.coord,
            self.polyline,
            self.surface,
            self.multipolyline,
            self.multisurface,
        )
        return frozenset(tag for tag in candidates if tag)

    def boundary(self, index: int) -> str:
        """
        The element name of a boundary of a surface. 2.3 knows only BOUNDARY, 2.4 has the
        exterior first and interiors after it.

        Args:
            index: The index of the boundary in the surface.

        Returns:
            The element name.
        """
        return self.boundaries[min(index, len(self.boundaries) - 1)]
