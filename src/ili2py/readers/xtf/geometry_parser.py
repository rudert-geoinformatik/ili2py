"""
Reading of an XTF in two passes, the geometry apart from xsdata.

xsdata binds every XML element on its own (~11 µs per element, see `xsdata_backend`). Even
an element it is told to ignore still costs ~4.5 µs (`SkipNode`), and an XTF with surfaces
consists to ~97 % of COORD, C1 and C2 elements. So ignoring is not enough, the geometry is
kept from xsdata completely:

1. Bind: xsdata binds the objects as usual. The subtree of a geometric field is skipped in the
   lxml walk (`skip_subtree`), xsdata never sees it and the field keeps its default. The
   subtree is stored on the parser together with the bound object it belongs to.
2. Geometry: `bind_geometries` builds the geometry from the stored subtrees and sets it on the
   objects, free of xsdata.

The geometric fields are known from the classes: `metadata["geometric"]["is_geometric"]` of
the field, as rendered for every attribute.
"""

from collections.abc import Iterable
from dataclasses import dataclass, field, fields
from typing import Any, Protocol

from lxml import etree  # type: ignore[import-untyped]
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.parsers.handlers.lxml import EVENTS
from xsdata.formats.dataclass.parsers.nodes import ElementNode
from xsdata.models.enums import EventType


class GeometryBuilder(Protocol):
    """
    Builds the geometry of a geometric field in two steps.
    """

    def collapse(self, element: etree._Element) -> Any:
        """
        The geometry of the element of a field, without knowing the object it belongs to.

        Args:
            element: The element of the field, the geometry is its child.

        Returns:
            The geometry, None if the element is empty.
        """
        ...

    def finish(self, owner: type, name: str, geometry: Any) -> Any:
        """
        The value set on the field, from the geometry of `collapse`.

        Args:
            owner: The class of the object the field belongs to.
            name: The field name.
            geometry: The geometry of `collapse`.

        Returns:
            The value of the field.
        """
        ...


class XtfLxmlEventHandler(LxmlEventHandler):
    """
    Lxml event handler as `LxmlEventHandler`, without the limits of libxml2 on the depth and
    the size of text nodes (`huge_tree`), which a large XTF can reach.
    """

    @staticmethod
    def parser_options(config: ParserConfig) -> dict[str, Any]:
        """
        The options of libxml2, the same for parsing incrementally and into a tree. They live
        here once, so the two handlers can not drift apart on how forgiving they are.

        Args:
            config: The xsdata parser configuration.

        Returns:
            The keyword arguments of `etree.iterparse` and `etree.XMLParser`.
        """
        return {
            "recover": True,
            "remove_comments": True,
            "load_dtd": config.load_dtd,
            "resolve_entities": config.resolve_entities,
            "huge_tree": True,
        }

    def parse(self, source: Any, ns_map: dict[str | None, str]) -> Any:
        """
        Parses the source incrementally (`iterparse`), a tree or element is walked.

        Args:
            source: The path or file object of the XTF, or an lxml tree or element.
            ns_map: A namespace prefix-URI recorder map.

        Returns:
            An instance of the class type representing the parsed content.
        """
        config = self.parser.config
        if isinstance(source, (etree._ElementTree, etree._Element)) or config.process_xinclude:
            return super().parse(source, ns_map)
        context = etree.iterparse(source, EVENTS, **self.parser_options(config))
        return self.process_context(context, ns_map)


class GeometryLxmlEventHandler(XtfLxmlEventHandler):
    """
    Lxml event handler which does not bind the geometric fields.

    The subtree of a geometric field is skipped, the field keeps its default and the subtree
    is handed to the parser together with the object it belongs to. Only `iterwalk` can skip
    a subtree, so the source is parsed into a tree first, which also keeps the stored
    subtrees for the second pass.
    """

    def parse(self, source: Any, ns_map: dict[str | None, str]) -> Any:
        """
        Parses the source into a tree and walks it (`iterwalk`).

        Args:
            source: The path or file object of the XTF, or an lxml tree or element.
            ns_map: A namespace prefix-URI recorder map.

        Returns:
            An instance of the class type representing the parsed content.
        """
        if not isinstance(source, (etree._ElementTree, etree._Element)):
            config = self.parser.config
            source = etree.parse(
                source,
                etree.XMLParser(**self.parser_options(config)),
                base_url=config.base_url,
            )
            if config.process_xinclude:
                source.xinclude()
        return self.process_context(etree.iterwalk(source, EVENTS), ns_map)

    def process_context(
        self,
        context: Iterable[tuple[str, Any]],
        ns_map: dict[str | None, str],
    ) -> Any:
        """
        Iterates the context and pushes the events to the parser, except the ones of
        geometric fields.

        Args:
            context: The lxml `iterwalk` context.
            ns_map: A namespace prefix-URI recorder map.

        Returns:
            An instance of the class type representing the parsed content.
        """
        parser = self.parser
        if not isinstance(parser, GeometryXmlParser):
            raise TypeError(f"{type(self).__name__} needs a GeometryXmlParser")
        if not isinstance(context, etree.iterwalk):
            raise TypeError(f"{type(self).__name__} needs an lxml iterwalk context")
        # id of the owner node -> [(field name, geometry element), ...]
        pending: dict[int, list[tuple[str, etree._Element]]] = {}
        skipped = None
        for event, element in context:
            if event == EventType.START:
                owner = self.queue[-1] if self.queue else None
                if isinstance(owner, ElementNode):
                    name = parser.geometric_fields(owner.meta).get(element.tag)
                    if name is not None and parser.holds_geometry(element):
                        pending.setdefault(id(owner), []).append((name, element))
                        context.skip_subtree()
                        skipped = element
                        continue
                parser.start(
                    self.clazz,
                    self.queue,
                    self.objects,
                    element.tag,
                    element.attrib,
                    element.nsmap,
                )
            elif event == EventType.END:
                if element is skipped:
                    # iterwalk delivers the end of a skipped element, no node was queued for it
                    skipped = None
                    continue
                owner = self.queue[-1]
                parser.end(self.queue, self.objects, element.tag, element.text, element.tail)
                geometries = pending.pop(id(owner), None)
                if geometries:
                    # the owner is bound now, it is the last intermediate object
                    obj = self.objects[-1][1]
                    parser.geometries.extend(
                        (obj, name, geometry) for name, geometry in geometries
                    )
                # no `element.clear()` as xsdata does: clearing an element with a referenced
                # geometry subtree below makes lxml move the subtree into an own document,
                # node by node (Hazard_Mapping: 107 s instead of 0.1 s). The tree is freed
                # with the end of the read.
            elif event == EventType.START_NS:
                prefix, uri = element
                parser.register_namespace(ns_map, prefix or None, uri)
            else:
                raise ValueError(f"Unhandled event: `{event}`.")

        return self.objects[-1][1] if self.objects else None


@dataclass
class GeometryXmlParser(XmlParser):
    """
    XmlParser which does things in 2 rounds.
    1. leaves the geometric fields and only parses the items not related to geometries
    2. `bind_geometries` which were collected in the first pass

    After `parse`, `geometries` holds `(object, field name, XML subtree)` for every geometric
    field found. The rendered dataclasses are not hashable (`eq=True`), so a list and not a
    dict.

    Attributes:
        geometry_tags: The qualified element names of the geometries (COORD, POLYLINE,
            SURFACE, MULTI*). A geometric field holding another element (e.g. a structure
            with a geometry inside) is bound by xsdata.
    """

    geometry_tags: frozenset[str] = frozenset()
    # we overwrite the original handler with our own geometry specific one
    handler: type[LxmlEventHandler] = field(default=GeometryLxmlEventHandler)
    geometries: list[tuple[Any, str, etree._Element]] = field(init=False, default_factory=list)
    _geometric_fields: dict[type, dict[str, str]] = field(
        init=False, default_factory=dict, repr=False
    )

    def holds_geometry(self, element: etree._Element) -> bool:
        """
        If the element of a geometric field holds a geometry, even if its an empty one.

        Args:
            element: The element of the field.

        Returns:
            True if the first child is a geometry or the element has no child.
        """
        return len(element) == 0 or element[0].tag in self.geometry_tags

    def geometric_fields(self, meta: XmlMeta) -> dict[str, str]:
        """
        Delivers the geometric fields of a bound class by element name, evaluated once per
        class. This is derived by the metainformation bound to classes and their attributes
        when the library was built.

        Args:
            meta: The xsdata meta of the bound class.

        Returns:
            Mapping of the qualified element name to the field name. Empty when the class has
            no geometric fields.
        """
        lookup = self._geometric_fields.get(meta.clazz)
        if lookup is None:
            names = {
                class_field.name
                for class_field in fields(meta.clazz)
                if class_field.metadata.get("geometric", {}).get("is_geometric")
            }
            lookup = {
                qname: var.name
                for qname, variables in meta.elements.items()
                for var in variables
                if var.name in names
            }
            self._geometric_fields[meta.clazz] = lookup
        return lookup

    def bind_geometries(self, builder: GeometryBuilder) -> None:
        """
        Second pass: builds the geometric objects from the stored subtrees and sets them on the
        objects they belong to. So here the "magic" happens, we put together what belongs
        together.

        Args:
            builder: Builds the geometry of a field.
        """
        for obj, name, element in self.geometries:
            setattr(obj, name, builder.finish(type(obj), name, builder.collapse(element)))
        self.geometries.clear()
