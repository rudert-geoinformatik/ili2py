"""
The XTF backend based on xsdata and lxml (see `backend.XtfBackend`), with a fast path for the
geometry (`geometry`).

xsdata binds every XML element on its own (~11 µs per element), an XTF with surfaces consists
to ~97 % of COORD, C1 and C2 elements. So the geometry does not go through xsdata:

- Reading with `compact_geometry`: xsdata binds the objects, the geometric fields are left to
  a second pass which builds the compact geometry from the lxml elements (`geometry_parser`).
- Writing: `GeometrySerializer` hands a compact geometry as one value to
  `GeometryEventWriter`, which writes its elements as text, formatted as the xsdata writer
  would do it element by element. Geometry as dataclasses is written by xsdata.

The floats are written as xsdata writes them.
"""

import math
import sys
from array import array
from collections.abc import Iterator, Sequence
from dataclasses import dataclass, field, fields
from io import TextIOBase
from pathlib import Path
from typing import IO, Any, TypeVar

from lxml import etree  # type: ignore[import-untyped]
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.mixins import XmlWriterEvent
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
from xsdata.utils import namespaces

from ili2py.interfaces.interlis import GeometryTags
from ili2py.interfaces.interlis.interlis_23 import Ili23GeometryTags
from ili2py.interfaces.interlis.interlis_24 import Ili24GeometryTags
from ili2py.readers.xtf.backend import XtfBackend
from ili2py.readers.xtf.converters import registered_converters
from ili2py.readers.xtf.geometry import (
    Coord,
    CoordSpec,
    Geometry,
    MultiPolyline,
    MultiSurface,
    Polyline,
    Surface,
)
from ili2py.readers.xtf.geometry_parser import (
    GeometryBuilder,
    GeometryXmlParser,
    XtfLxmlEventHandler,
)

T = TypeVar("T")


class GeometryReader:
    """Converts the geometry elements of an lxml tree to compact geometries."""

    def __init__(self, tags: GeometryTags):
        """
        Args:
            tags: The element names of the transfer version.
        """
        self.tags = tags
        self.coord_values = etree.XPath(
            f"g:{tags.coord_name}/*/text()",
            namespaces={"g": tags.namespace},
            smart_strings=False,
        )
        self.axis_tags = set(tags.axes)

    def geometry(self, element: Any) -> Geometry:
        tags = self.tags
        tag = element.tag
        if tag == tags.coord:
            return Coord(tuple(float(axis.text) for axis in element))
        if tag == tags.polyline:
            return self.polyline(element)
        if tag == tags.surface:
            return self.surface(element)
        if tag == tags.multipolyline:
            return MultiPolyline([self.polyline(item) for item in element])
        if tag == tags.multisurface:
            return MultiSurface([self.surface(item) for item in element])
        raise ValueError(f"unknown geometry element {tag}")

    def surface(self, element: Any) -> Surface:
        # 2.3: BOUNDARY/POLYLINE, 2.4: exterior/polyline and interior/polyline
        return Surface([self.polyline(boundary[0]) for boundary in element])

    def polyline(self, element: Any) -> Polyline:
        if len(element) == 0:
            return Polyline(array("d"), 0, {})
        if element.find(self.tags.arc) is None:
            # straights only, the values are collected in C
            values = array("d", map(float, self.coord_values(element)))
            return Polyline(values, len(element[0]), {})
        coords = array("d")
        arcs: dict[int, tuple[float, ...]] = {}
        dimension = 0
        for index, vertex in enumerate(element):
            end_point = [float(item.text) for item in vertex if item.tag in self.axis_tags]
            dimension = dimension or len(end_point)
            coords.extend(end_point)
            if vertex.tag == self.tags.arc:
                arcs[index] = tuple(
                    float(item.text) for item in vertex if item.tag not in self.axis_tags
                )
        return Polyline(coords, dimension, arcs)


class CompactGeometryBuilder(GeometryBuilder):
    """
    Builds the compact geometry of a geometric field of the dataclasses, the second pass of
    `GeometryXmlParser` (see `geometry_parser`). The spec of the axes is read from the classes
    of the field: the coord dataclass below it (`<coord type>Type`, element COORD) holds the
    axes with their type restrictions.

    `collapse` builds the geometry from the element, `finish` gives it the type carrying the
    spec (see `geometry_parser.GeometryBuilder`).
    """

    def __init__(self, tags: GeometryTags, context: XmlContext | None = None):
        """
        Args:
            tags: The element names of the transfer version.
            context: The xsdata context, the one of the parser if possible.
        """
        self.reader = GeometryReader(tags)
        # if possible we use the existing context of the parser so we squeeze another ms here
        self.context = XmlContext() if context is None else context
        self.specs: dict[tuple[type, str], CoordSpec | None] = {}
        self.types: dict[tuple[type[Geometry], CoordSpec | None], type[Geometry]] = {}

    def collapse(self, element: Any) -> Geometry | None:
        """
        The geometry of a field, without the spec of the axes=>this is collected in
        a separate step.

        Args:
            element: The element of the field, the geometry is its child.

        Returns:
            The geometry, None if the element is empty.
        """
        if len(element) == 0:
            return None
        return self.reader.geometry(element[0])

    def finish(self, owner: type, name: str, geometry: Geometry | None) -> Geometry | None:
        """
        The geometry of a field with the type carrying the spec of the axes.

        Args:
            owner: The class of the object the field belongs to.
            name: The field name.
            geometry: The geometry of `collapse`.

        Returns:
            The geometry, None if the element was empty.
        """
        if geometry is None:
            return None
        key = (owner, name)
        if key not in self.specs:
            self.specs[key] = self.spec(owner, name)
        spec = self.specs[key]
        if spec is None:
            return geometry
        base = type(geometry)
        typed = self.types.get((base, spec))
        if typed is None:
            typed = base.with_spec(spec)
            self.types[(base, spec)] = typed
        # same values, the type carries the spec
        return typed(*geometry.values())

    def spec(self, owner: type, name: str) -> CoordSpec | None:
        """
        The spec of the axes of a geometric field, searched in the classes below the field.

        Args:
            owner: The class of the object the field belongs to.
            name: The field name.

        Returns:
            The spec, None if the field has no coord dataclass (e.g. a line type of an
            abstract coord type).
        """
        var = next(
            var for var in self.context.build(owner).get_element_vars() if var.name == name
        )
        pending = list(var.types)
        seen: set[type] = set()
        while pending:
            clazz = pending.pop(0)
            if clazz in seen or not isinstance(clazz, type):
                continue
            seen.add(clazz)
            if not self.context.class_type.is_model(clazz):
                continue
            for item in self.context.build(clazz).get_element_vars():
                for sub_item in [item, *item.elements.values()]:
                    if sub_item.local_name.upper() == "COORD":
                        return self.axes_spec(sub_item.types[0])
                    pending.extend(sub_item.types)
        return None

    def axes_spec(self, axes: type) -> CoordSpec:
        """
        The spec of a coord dataclass holding the axes (`<coord type>Type`).

        Args:
            axes: The coord dataclass.

        Returns:
            The spec.
        """
        names: list[str] = []
        types: list[type] = []
        precisions: list[int | None] = []
        restrictions = {
            item.name: item.metadata.get("interlis", {}).get("type_restrictions") or {}
            for item in fields(axes)
        }
        for var in self.context.build(axes).get_element_vars():
            # the element names are lower case in 2.4, the axes of the model are C1, C2, C3
            names.append(var.local_name.upper())
            types.append(int if int in var.types else float)
            precisions.append(restrictions[var.name].get("precision"))
        return CoordSpec(
            tid=self.coord_type_tid(axes),
            axes=tuple(names),
            types=tuple(types),
            precisions=tuple(precisions),
        )

    @staticmethod
    def coord_type_tid(axes: type) -> str:
        """
        The tid of the coord type, from the metadata of its class next to the coord dataclass
        (`<coord type>` beside `<coord type>Type`). Empty if not found.
        """
        coord_type: Any = getattr(
            sys.modules.get(axes.__module__), axes.__name__.removesuffix("Type"), None
        )
        if not isinstance(getattr(coord_type, "metadata", None), property):
            return ""
        # the property does not use the instance, the classes are created with the defaults
        return coord_type().metadata.get("interlis", {}).get("oid", "")


class GeometryWriter:
    """Generates the xsdata writer events of the geometry elements."""

    def __init__(self, tags: GeometryTags):
        """
        Args:
            tags: The element names of the transfer version.
        """
        self.tags = tags
        self.axis_tags = list(tags.axes)
        self.arc_tags = list(tags.arc_points)

    @staticmethod
    def format_float(value: float) -> str:
        """As xsdata writes floats (FloatConverter)."""
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "INF" if value > 0 else "-INF"
        return repr(value).upper().replace("E+", "E")

    def events(self, geometry: Geometry) -> Iterator[tuple]:
        """The events of a geometry, its axes as its spec defines them."""
        yield from self.geometry(geometry, geometry.spec)

    def geometry(self, geometry: Geometry, spec: CoordSpec | None) -> Iterator[tuple]:
        if isinstance(geometry, Coord):
            yield from self.coord(geometry.values_, spec)
        elif isinstance(geometry, Polyline):
            yield from self.polyline(geometry, spec)
        elif isinstance(geometry, Surface):
            yield from self.surface(geometry, spec)
        elif isinstance(geometry, MultiPolyline):
            yield from self.multi(self.tags.multipolyline, geometry.polylines, spec)
        elif isinstance(geometry, MultiSurface):
            yield from self.multi(self.tags.multisurface, geometry.surfaces, spec)
        else:
            raise TypeError(f"unknown geometry {geometry}")

    def values(self, tags: list[str], values: Any, spec: CoordSpec | None) -> Iterator[tuple]:
        start, data, end = XmlWriterEvent.START, XmlWriterEvent.DATA, XmlWriterEvent.END
        types = spec.types if spec else ()
        for index, value in enumerate(values):
            tag = tags[index]
            yield start, tag
            if index < len(types) and types[index] is int:
                yield data, str(int(value))
            else:
                yield data, self.format_float(value)
            yield end, tag

    def coord(self, values: Any, spec: CoordSpec | None) -> Iterator[tuple]:
        yield XmlWriterEvent.START, self.tags.coord
        yield from self.values(self.axis_tags, values, spec)
        yield XmlWriterEvent.END, self.tags.coord

    def polyline(self, polyline: Polyline, spec: CoordSpec | None) -> Iterator[tuple]:
        tags = self.tags
        yield XmlWriterEvent.START, tags.polyline
        dimension = polyline.dimension
        coords = polyline.coords
        arcs = polyline.arcs
        for index in range(len(polyline)):
            values = coords[index * dimension : (index + 1) * dimension]
            if index in arcs:
                yield XmlWriterEvent.START, tags.arc
                yield from self.values(self.axis_tags, values, spec)
                # A1, A2 and R are no axes, they are written as floats
                yield from self.values(self.arc_tags, arcs[index], None)
                yield XmlWriterEvent.END, tags.arc
            else:
                yield from self.coord(values, spec)
        yield XmlWriterEvent.END, tags.polyline

    def surface(self, surface: Surface, spec: CoordSpec | None) -> Iterator[tuple]:
        tags = self.tags
        yield XmlWriterEvent.START, tags.surface
        for index, boundary in enumerate(surface.boundaries):
            boundary_tag = tags.boundary(index)
            yield XmlWriterEvent.START, boundary_tag
            yield from self.polyline(boundary, spec)
            yield XmlWriterEvent.END, boundary_tag
        yield XmlWriterEvent.END, tags.surface

    def multi(
        self, tag: str | None, items: Sequence[Geometry], spec: CoordSpec | None
    ) -> Iterator[tuple]:
        if tag is None:
            raise TypeError("the transfer version has no multi geometries")
        yield XmlWriterEvent.START, tag
        for item in items:
            yield from self.geometry(item, spec)
        yield XmlWriterEvent.END, tag


class GeometryText:
    """
    Writes the geometry elements as text at a depth of the document, indented as
    `XmlEventWriter` does it.
    """

    def __init__(self, writer: GeometryWriter, prefix: str | None, depth: int, indent: str):
        self.writer = writer
        self.prefix = prefix
        self.depth = depth
        self.indent = indent
        self.templates: dict[tuple[int, int, tuple[type, ...]], str] = {}

    def name(self, tag: str) -> str:
        local = GeometryTags.local_name(tag)
        return f"{self.prefix}:{local}" if self.prefix else local

    def newline(self, depth: int) -> str:
        return f"\n{self.indent * depth}" if self.indent else ""

    def text(self, geometry: Geometry) -> str:
        parts: list[str] = []
        self.geometry(parts, geometry, self.depth, geometry.spec)
        return "".join(parts)

    def geometry(
        self, parts: list[str], geometry: Geometry, depth: int, spec: CoordSpec | None
    ) -> None:
        tags = self.writer.tags
        if isinstance(geometry, Coord):
            dimension = len(geometry.values_)
            parts.append(
                self.coord_template(depth, dimension, spec).format(
                    *self.strings(geometry.values_, dimension, spec)
                )
            )
        elif isinstance(geometry, Polyline):
            self.polyline(parts, geometry, depth, spec)
        elif isinstance(geometry, Surface):
            self.surface(parts, geometry, depth, spec)
        elif isinstance(geometry, MultiPolyline):
            self.multi(parts, tags.multipolyline, geometry.polylines, depth, spec)
        elif isinstance(geometry, MultiSurface):
            self.multi(parts, tags.multisurface, geometry.surfaces, depth, spec)
        else:
            raise TypeError(f"unknown geometry {geometry}")

    def strings(self, values: Any, dimension: int, spec: CoordSpec | None) -> list[str]:
        """The values of the vertices (flat) as xsdata writes them, int axes as int."""
        strings = list(map(repr, values))
        # repr is what xsdata writes, except exponents, nan and inf
        if any("e" in item or "n" in item for item in strings):
            strings = list(map(GeometryWriter.format_float, values))
        types = spec.types if spec else ()
        for axis, axis_type in enumerate(types[:dimension]):
            if axis_type is int:
                strings[axis::dimension] = [
                    str(int(value)) for value in values[axis::dimension]
                ]
        return strings

    def coord_template(self, depth: int, dimension: int, spec: CoordSpec | None) -> str:
        key = (depth, dimension, spec.types if spec else ())
        if key not in self.templates:
            axes = "".join(
                f"{self.newline(depth + 1)}<{name}>{{}}</{name}>"
                for name in map(self.name, self.writer.axis_tags[:dimension])
            )
            coord = self.name(self.writer.tags.coord)
            self.templates[key] = (
                f"{self.newline(depth)}<{coord}>{axes}{self.newline(depth)}</{coord}>"
            )
        return self.templates[key]

    def polyline(
        self, parts: list[str], polyline: Polyline, depth: int, spec: CoordSpec | None
    ) -> None:
        name = self.name(self.writer.tags.polyline)
        count = len(polyline)
        if not count:
            parts.append(f"{self.newline(depth)}<{name}/>")
            return
        parts.append(f"{self.newline(depth)}<{name}>")
        dimension = polyline.dimension
        strings = self.strings(polyline.coords, dimension, spec)
        coord = self.coord_template(depth + 1, dimension, spec)
        if not polyline.arcs:
            # straights only, one format call for all vertices
            parts.append((coord * count).format(*strings))
        else:
            arc = self.name(self.writer.tags.arc)
            axes = [self.name(tag) for tag in self.writer.axis_tags]
            arc_points = [self.name(tag) for tag in self.writer.arc_tags]
            for index in range(count):
                values = strings[index * dimension : (index + 1) * dimension]
                if index not in polyline.arcs:
                    parts.append(coord.format(*values))
                    continue
                parts.append(f"{self.newline(depth + 1)}<{arc}>")
                inner = self.newline(depth + 2)
                for axis, value in zip(axes, values, strict=False):
                    parts.append(f"{inner}<{axis}>{value}</{axis}>")
                # A1, A2 and R are no axes, they are written as floats
                for point, arc_value in zip(arc_points, polyline.arcs[index], strict=False):
                    parts.append(
                        f"{inner}<{point}>{GeometryWriter.format_float(arc_value)}</{point}>"
                    )
                parts.append(f"{self.newline(depth + 1)}</{arc}>")
        parts.append(f"{self.newline(depth)}</{name}>")

    def surface(
        self, parts: list[str], surface: Surface, depth: int, spec: CoordSpec | None
    ) -> None:
        tags = self.writer.tags
        name = self.name(tags.surface)
        if not surface.boundaries:
            parts.append(f"{self.newline(depth)}<{name}/>")
            return
        parts.append(f"{self.newline(depth)}<{name}>")
        for index, boundary in enumerate(surface.boundaries):
            boundary_name = self.name(tags.boundary(index))
            parts.append(f"{self.newline(depth + 1)}<{boundary_name}>")
            self.polyline(parts, boundary, depth + 2, spec)
            parts.append(f"{self.newline(depth + 1)}</{boundary_name}>")
        parts.append(f"{self.newline(depth)}</{name}>")

    def multi(
        self,
        parts: list[str],
        tag: str | None,
        items: Sequence[Geometry],
        depth: int,
        spec: CoordSpec | None,
    ) -> None:
        if tag is None:
            raise TypeError("the transfer version has no multi geometries")
        name = self.name(tag)
        if not items:
            parts.append(f"{self.newline(depth)}<{name}/>")
            return
        parts.append(f"{self.newline(depth)}<{name}>")
        for item in items:
            self.geometry(parts, item, depth + 1, spec)
        parts.append(f"{self.newline(depth)}</{name}>")


class GeometryEventWriter(XmlEventWriter):
    """
    The streaming xsdata writer, a geometry (see `GeometrySerializer`) is written as text by
    `GeometryText`. If the namespace of the geometry has no prefix in the document yet, its
    events are written one by one, so xsdata declares it.
    """

    __slots__ = ("geometry_writer", "texts")

    def __init__(
        self,
        config: SerializerConfig,
        output: TextIOBase,
        ns_map: dict,
        geometry_writer: GeometryWriter,
    ):
        super().__init__(config, output, ns_map)
        self.geometry_writer = geometry_writer
        self.texts: dict[tuple[str | None, int], GeometryText] = {}

    def set_data(self, data: Any) -> None:
        if not isinstance(data, Geometry):
            super().set_data(data)
            return
        namespace = self.geometry_writer.tags.namespace
        prefixes = [prefix for prefix, uri in self.ns_map.items() if uri == namespace]
        if not prefixes:
            self.write_events(data)
            return
        self.flush_start(False)
        key = (prefixes[0], self.current_level)
        if key not in self.texts:
            self.texts[key] = GeometryText(
                self.geometry_writer, prefixes[0], self.current_level, self.config.indent or ""
            )
        # unescaped, the values are numbers
        self.handler.ignorableWhitespace(self.texts[key].text(data))
        self.pending_end_element = True
        self.in_tail = True

    def write_events(self, geometry: Geometry) -> None:
        for name, *args in self.geometry_writer.events(geometry):
            if name == XmlWriterEvent.START:
                self.start_tag(*args)
            elif name == XmlWriterEvent.END:
                self.end_tag(*args)
            else:
                super().set_data(*args)


@dataclass
class GeometrySerializer(XmlSerializer):
    """
    The xsdata serializer, a geometry is handed as one value to `GeometryEventWriter`. The
    writer is always `GeometryEventWriter`, it writes as `LxmlEventWriter` (the default of
    xsdata) does.
    """

    geometry_writer: GeometryWriter | None = None

    def convert_element(self, value: Any, var: XmlVar, namespace: str | None) -> Any:
        if isinstance(value, Geometry) and self.geometry_writer is not None:
            yield XmlWriterEvent.START, var.qname
            yield XmlWriterEvent.DATA, value
            yield XmlWriterEvent.END, var.qname
        else:
            yield from super().convert_element(value, var, namespace)

    def write(self, out: TextIOBase, obj: Any, ns_map: dict | None = None) -> None:
        if self.geometry_writer is None:
            super().write(out, obj, ns_map)
            return
        handler = GeometryEventWriter(
            config=self.config,
            output=out,
            ns_map=namespaces.clean_prefixes(ns_map) if ns_map else {},
            geometry_writer=self.geometry_writer,
        )
        handler.write(self.generate(obj))


@dataclass
class XsdataBackend(XtfBackend):
    """
    Reads and writes an XTF with xsdata, see `backend.XtfBackend`. The special types of the
    library are registered as xsdata converters for the time of a call, types registered
    already are left as they are.

    The converter registry of xsdata is global per process, it is not thread safe.

    Attributes:
        parser_config: The xsdata parser configuration.
        serializer_config: The xsdata serializer configuration.
        compact_geometry: If the geometric fields are read as compact geometry (see
            `geometry_parser`).
    """

    parser_config: ParserConfig = field(default_factory=ParserConfig)
    serializer_config: SerializerConfig = field(
        default_factory=lambda: SerializerConfig(
            indent="  ", xml_declaration=True, encoding="UTF-8"
        )
    )
    compact_geometry: bool = False

    @staticmethod
    def geometry_tags(transfer_class: type) -> GeometryTags:
        """
        The element names of the geometry in the transfer version the transfer class reads.

        Args:
            transfer_class: The class of the root element of the XTF (`xtf_opening.Transfer`).

        Returns:
            The element names of INTERLIS 2.3 or 2.4.
        """
        for tags_class in (Ili23GeometryTags, Ili24GeometryTags):
            if tags_class.reads(transfer_class):
                return tags_class()
        raise ValueError(f"{transfer_class} is no transfer of INTERLIS 2.3 or 2.4")

    @staticmethod
    def library_name(transfer_class: type) -> str:
        """The name of the rendered library of the transfer class (`<library>.xtf_opening`)."""
        return transfer_class.__module__.rsplit(".", 1)[0]

    def read(self, source: str | Path | IO[bytes], transfer_class: type[T]) -> T:
        with registered_converters(self.library_name(transfer_class)):
            return self.parse(source, transfer_class)

    def write(
        self, transfer: Any, out: TextIOBase, ns_map: dict[str | None, str] | None = None
    ) -> None:
        with registered_converters(self.library_name(type(transfer))):
            self.serialize(transfer, out, ns_map)

    def parse(self, source: str | Path | IO[bytes], transfer_class: type[T]) -> T:
        """
        Parses an XTF into the objects of the classes, the geometric fields compact if
        configured. Has to be called while the converters of the special types are registered
        (`converters.registered_converters`), `read` does it on its own.

        Args:
            source: The path or file object of the XTF.
            transfer_class: The class of the root element of the XTF from the library
                dataclasses, this is the `Transfer` class always.

        Returns:
            The transfer object tree.
        """
        if isinstance(source, Path):
            source = str(source)
        if not self.compact_geometry:
            parser = XmlParser(config=self.parser_config, handler=XtfLxmlEventHandler)
            return parser.parse(source, transfer_class)
        tags = self.geometry_tags(transfer_class)
        geometry_parser = GeometryXmlParser(
            config=self.parser_config, geometry_tags=tags.geometries
        )
        transfer = geometry_parser.parse(source, transfer_class)
        geometry_parser.bind_geometries(CompactGeometryBuilder(tags))
        return transfer

    def serialize(
        self, transfer: Any, out: TextIOBase, ns_map: dict[str | None, str] | None = None
    ) -> None:
        """
        Serializes a transfer object tree to an XTF, the geometry compact or as dataclasses.
        Has to be called while the converters of the special types are registered, `write`
        does it on its own.

        Args:
            transfer: The transfer object tree.
            out: The text stream to write to.
            ns_map: The namespace prefixes, key None is the default namespace.
        """
        serializer = GeometrySerializer(
            config=self.serializer_config,
            geometry_writer=GeometryWriter(self.geometry_tags(type(transfer))),
        )
        serializer.write(out, transfer, ns_map=ns_map)
