"""
Builds the python classes to read and write XTF at runtime, directly from the index of an IMD,
without rendering any code (see `writers.py.render` for the rendered classes).

The classes are kept flat in a registry. The key is the tid of the element a class is built for
(e.g. `Model.Topic.Class`), the class name is the slug of it (`Model_Topic_Class`). Classes
which are no element of the model (geometry, references, transfer) get a key with an `ili2py.`
prefix or a `:` suffix on the tid they belong to. All XML names come from the `Meta` of the
classes and the metadata of the fields, so the python names are free.

The classes do not have the structure of the rendered ones (no nesting, no modules, no
properties), but they read and write the same XTF: same element and attribute names, same
namespaces, same order and same value types.
"""

import keyword
import logging
import re
import sys
from collections.abc import Callable
from dataclasses import field, make_dataclass
from enum import Enum
from io import TextIOBase
from pathlib import Path
from types import ModuleType
from typing import IO, Any

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    AttrOrParam,
    BlackboxType,
    BooleanType,
    Class,
    CoordType,
    EnumTreeValueType,
    EnumType,
    FormattedType,
    LineType,
    MultiValueType,
    NumType,
    ReferenceType,
    Role,
    SubModel,
    TextType,
)
from ili2py.mappers.helpers import Index, mandatory, mandatory_ref
from ili2py.readers.interlis_24.ilismeta16.xsdata import Imd16Reader
from ili2py.readers.xtf.converters import registered_types
from ili2py.writers.helpers import handle_model_versions
from ili2py.writers.py.python_structure import Attribute, Basket, Enumeration
from ili2py.writers.py.render import render_configuration
from ili2py.writers.py.transfer_names import TransferNames

# a dataclass field as make_dataclass takes it: name, annotation, field
type FieldSpec = tuple[str, str, Any]

# a choice of an Elements field: element name, type, namespace
type ChoiceSpec = tuple[str, Any, str]

PREFIX = "ili2py"

SIMPLE_TYPES = (TextType, FormattedType, NumType, BooleanType, BlackboxType)


def slug(key: str) -> str:
    """
    Derives the class name of a registry key.

    Args:
        key: The key, e.g. 'Model.Topic.Class' or 'Model.Coord:Segment'.

    Returns:
        A valid python name, e.g. 'Model_Topic_Class' or 'Model_Coord_Segment'.
    """
    name = re.sub(r"\W", "_", key)
    return f"_{name}" if name[0].isdigit() else name


def python_name(name: str) -> str:
    """The python name of a field, keywords and invalid names get a trailing `_`."""
    if name.isidentifier() and not keyword.iskeyword(name):
        return name
    return f"{re.sub(r'\W', '_', name)}_"


def attribute_field(
    name: str, tag: str | None, namespace: str | None = None, annotation: str = "str | None"
) -> FieldSpec:
    metadata: dict[str, Any] = {"type": "Attribute"}
    if tag:
        metadata["name"] = tag
    if namespace:
        metadata["namespace"] = namespace
    return name, annotation, field(default=None, metadata=metadata)


def element_field(name: str, tag: str | None, annotation: str, namespace: str) -> FieldSpec:
    metadata: dict[str, Any] = {"type": "Element"}
    if tag:
        metadata["name"] = tag
    metadata["namespace"] = namespace
    return name, annotation, field(default=None, metadata=metadata)


def elements_field(name: str, annotation: str, choices: list[ChoiceSpec]) -> FieldSpec:
    metadata = {
        "type": "Elements",
        "choices": tuple(
            {"name": tag, "type": choice_type, "namespace": namespace}
            for tag, choice_type, namespace in choices
        ),
    }
    return name, annotation, field(default_factory=list, metadata=metadata)


def plain_field(name: str, annotation: str, metadata: dict, default: bool = True) -> FieldSpec:
    if default:
        return name, annotation, field(default=None, metadata=metadata)
    return name, annotation, field(metadata=metadata)


def type_names(choices: list[ChoiceSpec]) -> str:
    return " | ".join(choice_type.__name__ for _, choice_type, _ in choices) or "Any"


class RuntimeLibrary:
    """
    The classes to read and write the XTF of the models of an IMD, built at runtime.

    Usage:
        with RuntimeLibrary.from_imd("Model.imd") as library:
            transfer = library.read("data.xtf")
            library.classes["Model.Topic.Class"]

    The classes are registered in a module (`sys.modules`) while the library is built, so the
    annotations can be resolved and the objects can be pickled.

    Attributes:
        index: The index of the IMD.
        ili_version: The INTERLIS version of the models (2.3 or 2.4).
        name: The name of the module the classes are registered in.
        classes: The registry, key is the tid of the element a class is built for.
        module: The module the classes are registered in.
    """

    def __init__(self, index: Index, name: str | None = None):
        self.index = index
        self.ili_version = handle_model_versions(index)
        if self.ili_version not in render_configuration:
            raise NotImplementedError(f"ili version '{self.ili_version}' not supported")
        self.render_config: dict[str, Any] = render_configuration[self.ili_version]
        self.name = name or f"{PREFIX}_runtime_{slug(index.root_model)}"
        self.classes: dict[str, type] = {}
        self.module = ModuleType(self.name)
        self.module.Any = Any  # type: ignore[attr-defined]
        # the tags of translated models are in the translated language in INTERLIS 2.3 only
        self.transfer_names = TransferNames(index) if self.is_23 else None
        self._building: set[str] = set()

    @classmethod
    def from_imd(cls, imd_path: str | Path, name: str | None = None) -> "RuntimeLibrary":
        """
        Reads the IMD and prepares the runtime library, call `build` (or use it as context
        manager) to create the classes.

        Args:
            imd_path: The path of the IMD.
            name: The name of the module the classes are registered in.

        Returns:
            The runtime library.
        """
        metamodel = Imd16Reader().read(str(imd_path))
        return cls(Index(metamodel.datasection), name)

    @property
    def is_23(self) -> bool:
        return self.ili_version == "2.3"

    @property
    def base_url(self) -> str:
        return self.render_config["base_url"]

    @property
    def ili_namespace(self) -> str:
        return self.render_config["namespace_map"]["ili"]

    @property
    def geom_namespace(self) -> str:
        # INTERLIS 2.3 has no own geometry namespace
        return self.render_config["namespace_map"].get("geom", self.ili_namespace)

    @property
    def is_built(self) -> bool:
        return f"{PREFIX}.Transfer" in self.classes

    @property
    def transfer(self) -> type:
        """The class of the root element of the XTF, the library is built if needed."""
        self.build()
        return self.classes[f"{PREFIX}.Transfer"]

    @property
    def bin_bl_box(self) -> type:
        """The bytes type of BLACKBOX BINARY, it needs a converter."""
        self.build()
        return self.classes[f"{PREFIX}.BinBlBox" if self.is_23 else f"{PREFIX}.BinBlBoxType"]

    def __enter__(self) -> "RuntimeLibrary":
        return self.build()

    def __exit__(self, *args: Any) -> None:
        self.unload()

    def build(self) -> "RuntimeLibrary":
        """
        Builds the classes of all classes, structures and associations of the IMD and of the
        transfer, and registers the module of the classes in `sys.modules`. Nothing happens if
        the library is built and registered already, a library which was unloaded is registered
        again.

        Returns:
            The library itself.

        Raises:
            ImportError: If a module with the name is imported already.
        """
        if sys.modules.get(self.name) is self.module:
            return self
        if self.name in sys.modules:
            raise ImportError(f"a module named '{self.name}' is imported already")
        sys.modules[self.name] = self.module
        if self.is_built:
            return self
        try:
            self.build_references()
            for imd_class in self.index.types_bucket.get("Class", []):
                self.class_name(mandatory(imd_class.tid))
            self.build_transfer()
        except Exception:
            self.unload()
            self.classes = {}
            self.module = ModuleType(self.name)
            self.module.Any = Any  # type: ignore[attr-defined]
            raise
        return self

    def unload(self) -> None:
        """Removes the module of the classes from `sys.modules`."""
        if sys.modules.get(self.name) is self.module:
            del sys.modules[self.name]

    def read(self, source: str | Path | IO[bytes], config: ParserConfig | None = None) -> Any:
        """
        Parses an XTF into objects of the runtime classes, the library is built if needed.

        Args:
            source: The path or file object of the XTF.
            config: The xsdata parser configuration.

        Returns:
            The transfer object tree.
        """
        with registered_types(self.bin_bl_box, []):
            parser = XmlParser(config=config or ParserConfig())
            return parser.parse(
                str(source) if isinstance(source, Path) else source, self.transfer
            )

    def write(
        self,
        transfer: Any,
        out: TextIOBase,
        ns_map: dict[str | None, str] | None = None,
        config: SerializerConfig | None = None,
    ) -> None:
        """
        Serializes a transfer object tree of the runtime classes to an XTF.

        Args:
            transfer: The transfer object tree.
            out: The text stream to write to.
            ns_map: The namespace prefixes, key None is the default namespace.
            config: The xsdata serializer configuration.
        """
        with registered_types(self.bin_bl_box, []):
            serializer = XmlSerializer(
                config=config
                or SerializerConfig(indent="  ", xml_declaration=True, encoding="UTF-8")
            )
            serializer.write(out, transfer, ns_map=ns_map)

    # registry

    def register(self, key: str, created: type) -> type:
        name = created.__name__
        if hasattr(self.module, name):
            raise LookupError(f"the class name {name} of {key} is used already")
        created.__module__ = self.name
        setattr(self.module, name, created)
        self.classes[key] = created
        return created

    def make_class(
        self,
        key: str,
        fields: list[FieldSpec],
        meta: dict[str, str] | None = None,
        bases: tuple[type, ...] = (),
    ) -> type:
        name = slug(key)
        namespace: dict[str, Any] = {"__module__": self.name, "__qualname__": name}
        if meta is not None:
            namespace["Meta"] = type(
                "Meta", (), {"__module__": self.name, "__qualname__": f"{name}.Meta"} | meta
            )
        # a name defined twice keeps its position and gets the last definition, as in a class
        # body (e.g. an attribute named like the TID field)
        unique_fields: dict[str, FieldSpec] = {}
        for spec in fields:
            unique_fields[spec[0]] = spec
        created = make_dataclass(
            name,
            list(unique_fields.values()),
            bases=bases,
            namespace=namespace,
            module=self.name,
        )
        return self.register(key, created)

    def ensure(self, key: str, build: Callable[[], Any]) -> str:
        """
        Builds the class of the key if it does not exist yet. The fields reference classes by
        name only, so a class which is built currently (recursive structures) is not built
        again.

        Args:
            key: The key of the class.
            build: Builds the class and registers it under the key.

        Returns:
            The class name, to be used in annotations.
        """
        if key not in self.classes and key not in self._building:
            self._building.add(key)
            try:
                build()
            finally:
                self._building.discard(key)
        return slug(key)

    # names

    def tag(self, tid: str) -> str:
        """The INTERLIS 2.3 tag of an element: its qualified name, translated."""
        assert self.transfer_names is not None
        return self.transfer_names.path(tid) or tid

    def attribute_tag(self, tid: str, name: str) -> str:
        """The INTERLIS 2.3 tag of an attribute or role: its name, translated."""
        assert self.transfer_names is not None
        return self.transfer_names.name(tid) or name

    def model_namespace(self, model_name: str) -> str:
        return f"{self.base_url}/{model_name}"

    def model_of(self, tid: str) -> str:
        """The name (= tid) of the model an element (class, topic, domain) is defined in."""
        package = self.index.index[mandatory_ref(self.index.index[tid].element_in_package)]
        if isinstance(package, SubModel):
            package = self.index.index[mandatory_ref(package.element_in_package)]
        return mandatory(package.name)

    # references.jinja2

    def build_references(self) -> None:
        ili_namespace = self.ili_namespace
        if self.is_23:
            self.make_class(
                f"{PREFIX}.Ref",
                [plain_field("ref", "str | None", {"type": "Attribute", "name": "REF"})],
                {"namespace": ili_namespace, "name": "REF"},
            )
            # value of an attribute of an OID type, 2.3 encodes it as <attr OID="..."/>
            self.make_class(
                f"{PREFIX}.Oid",
                [plain_field("oid", "str | None", {"type": "Attribute", "name": "OID"})],
                {"namespace": ili_namespace},
            )
            bin_bl_box = self.register(
                f"{PREFIX}.BinBlBox", type(slug(f"{PREFIX}.BinBlBox"), (bytes,), {})
            )
            box_metadata = {"type": "Element", "namespace": ili_namespace}
            self.make_class(
                f"{PREFIX}.BinBlBoxType",
                [plain_field("BINBLBOX", bin_bl_box.__name__, box_metadata, default=False)],
                {"namespace": ili_namespace},
            )
        else:
            ref_metadata = {"type": "Attribute", "namespace": ili_namespace}
            self.make_class(
                f"{PREFIX}.Ref",
                [plain_field("ref", "str | None", ref_metadata)],
                {"namespace": ili_namespace},
            )
            self.register(
                f"{PREFIX}.BinBlBoxType", type(slug(f"{PREFIX}.BinBlBoxType"), (bytes,), {})
            )

    # definitions/classes.jinja2

    def class_name(self, tid: str) -> str:
        """The class name of a class, structure or association, it is built if needed."""
        return self.ensure(tid, lambda: self.build_class(tid))

    def is_built_class(self, tid: str) -> bool:
        """
        Tells if a class is built for an element: classes and structures always, associations
        only if they are an own class in the transfer or extend another association.
        """
        element = self.index.index[tid]
        if not isinstance(element, Class):
            return False
        if element.kind != "Association":
            return True
        return element.super is not None or self.index.is_association_class(tid)

    def build_class(self, tid: str) -> None:
        imd_class: Class = self.index.index[tid]
        if not self.is_built_class(tid):
            return
        bases: tuple[type, ...] = ()
        if imd_class.super:
            super_tid = mandatory_ref(imd_class.super)
            self.class_name(super_tid)
            bases = (self.classes[super_tid],)
        model_name = self.model_of(tid)
        if self.is_23:
            meta = {"name": self.tag(tid), "namespace": self.ili_namespace}
        else:
            meta = {
                "name": mandatory(imd_class.name),
                "namespace": self.model_namespace(model_name),
            }
        fields = self.object_fields(imd_class)
        if imd_class.kind == "Association":
            if self.index.is_association_class(tid):
                roles = self.index.association_bucket.get(tid, [])
                fields += self.role_fields(
                    [(role_tid, class_tid) for role_tid, class_tid, *_ in roles], model_name
                )
        else:
            for attribute_tid in self.index.class_class_attribute.get(tid, []):
                fields.append(self.attribute_field(self.index.index[attribute_tid], imd_class))
            fields += self.role_fields(
                self.index.association_to_class_ref_attributes.get(tid, []), model_name
            )
        self.make_class(tid, fields, meta, bases)

    def object_fields(self, imd_class: Class) -> list[FieldSpec]:
        """The TID and (2.3) the object attributes of incremental transfers, as in ili2c."""
        fields = []
        oid_type = (
            self.oid_python_type(mandatory_ref(imd_class.oid)) if imd_class.oid else None
        )
        if oid_type or imd_class.kind == "Class":
            annotation = f"{oid_type or 'str'} | None"
            if self.is_23:
                fields.append(attribute_field("tid", "TID", annotation=annotation))
            else:
                fields.append(attribute_field("tid", "tid", self.ili_namespace, annotation))
        if self.is_23 and imd_class.kind in ["Class", "Association", "View"]:
            for tag in ["BID", "OPERATION", "CONSISTENCY"]:
                fields.append(attribute_field(tag.lower(), tag))
        return fields

    def oid_python_type(self, oid_tid: str) -> str:
        oid_type = self.index.index[oid_tid]
        if isinstance(oid_type, SIMPLE_TYPES):
            return self.simple_type(oid_type)
        return "str"

    def role_fields(self, roles: list[tuple[str, str]], model_name: str) -> list[FieldSpec]:
        """
        The fields of the roles, either embedded in a class or of an association class. A
        role with more than one associated class (OR) is one field.
        """
        targets: dict[str, list[str]] = {}
        for role_tid, class_tid in roles:
            targets.setdefault(role_tid, []).append(class_tid)
        fields = []
        names: set[str] = set()
        for role_tid, class_tids in targets.items():
            role: Role = self.index.index[role_tid]
            name = mandatory(role.name)
            if name in names:
                continue
            names.add(name)
            fields.append(
                self.value_field(
                    role_tid,
                    name,
                    slug(f"{PREFIX}.Ref"),
                    False,
                    model_name,
                    reference_targets=class_tids,
                    type_restrictions=Attribute.construct_type_restrictions(role),
                )
            )
        return fields

    def value_field(
        self,
        tid: str,
        name: str,
        type_name: str,
        is_list: bool,
        model_name: str,
        tag: str | None = None,
        xml_type: str = "Element",
        **interlis: Any,
    ) -> FieldSpec:
        """
        A field of an attribute or a role.

        Args:
            tid: The tid of the attribute or role.
            name: The name of the attribute or role.
            type_name: The python type of a value.
            is_list: If the field holds a list of values.
            model_name: The model of the element name (INTERLIS 2.4).
            tag: The element name if it is not the (translated) name.
            xml_type: The xsdata type of the field.
            interlis: The interlis metadata of the field.

        Returns:
            The field.
        """
        field_name = python_name(name)
        metadata: dict[str, Any] = {"type": xml_type}
        if self.is_23:
            metadata["namespace"] = self.ili_namespace
            tag = tag or self.attribute_tag(tid, name)
            if tag != field_name:
                metadata["name"] = tag
        else:
            metadata["namespace"] = self.model_namespace(model_name)
            metadata["name"] = tag or name
        metadata["interlis"] = {"oid": tid} | interlis
        if is_list:
            return (
                field_name,
                f"list[{type_name}]",
                field(default_factory=list, metadata=metadata),
            )
        return field_name, f"{type_name} | None", field(default=None, metadata=metadata)

    def attribute_field(self, attribute: AttrOrParam, owner: Class) -> FieldSpec:
        tid = mandatory(attribute.tid)
        type_object = self.index.index[mandatory_ref(attribute.type_value)]
        if isinstance(type_object, MultiValueType):
            type_name = self.multi_value_class_name(attribute, type_object, owner)
            is_list = Attribute.decide_list_type(type_object)
        else:
            type_name = self.value_type(type_object)
            is_list = False
            if self.is_23 and self.index.is_oid_type(mandatory(type_object.tid)):
                type_name = slug(f"{PREFIX}.Oid")
        origin = attribute
        if tid in self.index.type_super_classes:
            # an extended attribute is in the namespace of the model which defines it first
            origin = self.index.index[self.index.type_super_classes[tid][-1]]
        return self.value_field(
            tid,
            mandatory(attribute.name),
            type_name,
            is_list,
            Attribute.get_model_name_from_attribute(origin, self.index),
            type_restrictions=Attribute.construct_type_restrictions(type_object),
        )

    def simple_type(self, type_object: Any) -> str:
        type_name, _ = Attribute.handle_type_trail(type_object, self.index)
        if type_name == "BinBlBoxType":
            return slug(f"{PREFIX}.BinBlBoxType")
        if type_name == "XmlBlBoxType":
            return "str"
        return type_name

    def value_type(self, type_object: Any) -> str:
        """
        The python type of the values of a type, the class is built if needed.

        Args:
            type_object: The type of the metamodel.

        Returns:
            The name of the type, either a builtin or a class of the registry.
        """
        if isinstance(type_object, SIMPLE_TYPES):
            return self.simple_type(type_object)
        if isinstance(type_object, ReferenceType):
            return slug(f"{PREFIX}.Ref")
        if isinstance(type_object, EnumTreeValueType):
            return self.enumeration_name(self.index.index[mandatory_ref(type_object.et)])
        if isinstance(type_object, EnumType):
            return self.enumeration_name(type_object)
        if isinstance(type_object, CoordType):
            return self.coord_type_name(self.domain(type_object))
        if isinstance(type_object, LineType):
            return self.line_type_name(self.domain(type_object))
        if isinstance(type_object, Class):
            return self.class_name(mandatory(type_object.tid))
        logging.debug(f"type is read as text: {type_object}")
        return "str"

    def domain(self, type_object: Any) -> Any:
        """A local type (TYPE) which extends a domain is the domain, as for the rendered."""
        if type_object.name == "TYPE" and type_object.super:
            return self.index.index[mandatory_ref(type_object.super)]
        return type_object

    # BAG/LIST OF, see Attribute.handle_local_types

    def multi_value_class_name(
        self, attribute: AttrOrParam, multi_value: MultiValueType, owner: Class
    ) -> str:
        """
        The class between the attribute and its values. For BAG/LIST OF structures it holds
        the structure elements, for BAG/LIST OF other types (INTERLIS 2.4) the text.
        """
        key = f"{attribute.tid}:Struct"

        def build() -> None:
            base_type = self.index.index[mandatory_ref(multi_value.base_type)]
            base_tid = mandatory(base_type.tid)
            if multi_value.name == "MVT":
                content = self.value_field(
                    f"{PREFIX}.{base_tid}",
                    "struct_content",
                    self.value_type(base_type),
                    Attribute.decide_list_type(base_type),
                    Attribute.get_model_name_from_type(multi_value, self.index),
                    tag="struct_content",
                    xml_type="Element" if self.is_23 else "Text",
                )
            else:
                content = self.value_field(
                    f"{PREFIX}.{base_tid}",
                    "struct_content",
                    self.value_type(base_type),
                    Attribute.decide_list_type(multi_value),
                    Attribute.get_model_name_from_type(base_type, self.index),
                    tag=self.tag(base_tid) if self.is_23 else mandatory(base_type.name),
                )
            if self.is_23:
                meta = {
                    "name": self.tag(mandatory(multi_value.tid)),
                    "namespace": self.ili_namespace,
                }
            else:
                meta = {
                    "name": f"{owner.name}{attribute.name}Struct",
                    "namespace": self.model_namespace(self.model_of(mandatory(owner.tid))),
                }
            self.make_class(key, [content], meta)

        return self.ensure(key, build)

    # definitions/enumerations.jinja2

    def enumeration_name(self, enum_type: EnumType) -> str:
        key = mandatory(enum_type.tid)

        def build() -> None:
            enumeration = Enumeration.from_imd(enum_type, self.index)
            if self.transfer_names is not None:
                self.transfer_names.enumeration(enumeration)
            members = [
                (value.upper().replace(".", "_"), enumeration.value_tags.get(value, value))
                for value in enumeration.values
            ]
            name = slug(key)
            created = Enum(name, members, type=str, module=self.name, qualname=name)  # type: ignore[misc]
            self.register(key, created)

        return self.ensure(key, build)

    # definitions/coord_types.jinja2

    def coord_type_name(self, coord_type: CoordType) -> str:
        """The class of a coord attribute, it holds the coord element."""
        key = mandatory(coord_type.tid)

        def build() -> None:
            namespace = self.geom_namespace
            coord = element_field(
                "coord",
                "COORD" if self.is_23 else None,
                f"{self.coord_value_name(coord_type)} | None",
                namespace,
            )
            self.make_class(key, [coord], {"namespace": namespace})

        return self.ensure(key, build)

    def coord_value_name(self, coord_type: CoordType | None) -> str:
        """The class of the values of a coord (C1, C2, C3), 'Any' without coord type."""
        if coord_type is None:
            return "Any"
        key = f"{coord_type.tid}:Value"

        def build() -> None:
            namespace = self.geom_namespace
            fields = []
            for axis_tid in self.index.coord_type.get(coord_type.tid, []):
                axis = self.index.index[axis_tid]
                axis_name = mandatory(axis.name)
                fields.append(
                    element_field(
                        axis_name.lower(),
                        axis_name if self.is_23 else None,
                        f"{self.simple_type(axis)} | None",
                        namespace,
                    )
                )
            self.make_class(key, fields)

        return self.ensure(key, build)

    def coord_arc_name(self, coord_type: CoordType | None) -> str:
        """The class of an arc point, the coord of the end point with A1, A2 and R."""
        if coord_type is None:
            return "Any"
        key = f"{coord_type.tid}:Arc"
        value_name = self.coord_value_name(coord_type)

        def build() -> None:
            namespace = self.geom_namespace
            fields = [
                element_field(
                    tag.lower(), tag if self.is_23 else None, "float | None", namespace
                )
                for tag in ["A1", "A2", "R"]
            ]
            bases = (getattr(self.module, value_name),)
            self.make_class(key, fields, {"namespace": namespace}, bases)

        return self.ensure(key, build)

    # definitions/line_types*.jinja2, the classes are shared by all line types of a coord type

    def line_type_name(self, line_type: LineType) -> str:
        """The class of a line attribute (polyline, surface, multi polyline, multi surface)."""
        coord_type = (
            self.index.index[mandatory_ref(line_type.coord_type)]
            if line_type.coord_type
            else None
        )
        kind = mandatory(line_type.kind)
        multi = bool(line_type.multi) and not self.is_23
        if kind in ["Polyline", "DirectedPolyline"]:
            if multi:
                return self.multi_polyline_name(coord_type)
            return self.polyline_name(coord_type)
        if kind in ["Surface", "Area"]:
            if multi:
                return self.multi_surface_name(coord_type)
            return self.surface_name(coord_type)
        logging.debug(f"line type is read as text: {line_type}")
        return "str"

    def coord_key(self, coord_type: CoordType | None, suffix: str) -> str:
        return f"{coord_type.tid if coord_type else PREFIX}:{suffix}"

    def class_of(self, name: str) -> Any:
        return Any if name == "Any" else getattr(self.module, name)

    def segment_name(self, coord_type: CoordType | None) -> str:
        key = self.coord_key(coord_type, "Segment")

        def build() -> None:
            namespace = self.geom_namespace
            value_name = self.coord_value_name(coord_type)
            arc_name = self.coord_arc_name(coord_type)
            vertex_types = "Any" if value_name == "Any" else f"{value_name} | {arc_name}"
            choices = [
                ("COORD" if self.is_23 else "coord", self.class_of(value_name), namespace),
                ("ARC" if self.is_23 else "arc", self.class_of(arc_name), namespace),
            ]
            vertices = elements_field("vertices", f"list[{vertex_types}]", choices)
            self.make_class(key, [vertices], {"namespace": namespace})

        return self.ensure(key, build)

    def polyline_name(self, coord_type: CoordType | None) -> str:
        key = self.coord_key(coord_type, "Polyline")

        def build() -> None:
            namespace = self.geom_namespace
            polyline = element_field(
                "polyline",
                "POLYLINE" if self.is_23 else None,
                f"{self.segment_name(coord_type)} | None",
                namespace,
            )
            self.make_class(key, [polyline], {"namespace": namespace})

        return self.ensure(key, build)

    def multi_polyline_name(self, coord_type: CoordType | None) -> str:
        key = self.coord_key(coord_type, "MultiPolyline")

        def build() -> None:
            namespace = self.geom_namespace
            segment_name = self.segment_name(coord_type)
            parts = elements_field(
                "parts",
                f"list[{segment_name}]",
                [("polyline", self.class_of(segment_name), namespace)],
            )
            polylines = self.make_class(
                self.coord_key(coord_type, "Polylines"), [parts], {"namespace": namespace}
            )
            multipolyline = element_field("multipolyline", None, polylines.__name__, namespace)
            self.make_class(key, [multipolyline], {"namespace": namespace})

        return self.ensure(key, build)

    def boundary_name(self, coord_type: CoordType | None) -> str:
        key = self.coord_key(coord_type, "Boundary")

        def build() -> None:
            namespace = self.geom_namespace
            polyline = self.class_of(self.polyline_name(coord_type))
            choices: list[ChoiceSpec]
            if self.is_23:
                choices = [("BOUNDARY", polyline, namespace)]
                meta = {"namespace": namespace, "name": "SURFACE"}
            else:
                # own classes per choice, xsdata picks the element name by the type
                exterior = self.make_class(
                    self.coord_key(coord_type, "PolylineExterior"), [], bases=(polyline,)
                )
                interior = self.make_class(
                    self.coord_key(coord_type, "PolylineInterior"), [], bases=(polyline,)
                )
                choices = [
                    ("exterior", exterior, namespace),
                    ("interior", interior, namespace),
                ]
                meta = {"namespace": namespace}
            boundaries = elements_field("boundaries", f"list[{polyline.__name__}]", choices)
            self.make_class(key, [boundaries], meta)

        return self.ensure(key, build)

    def surface_name(self, coord_type: CoordType | None) -> str:
        key = self.coord_key(coord_type, "Surface")

        def build() -> None:
            namespace = self.geom_namespace
            surface = element_field(
                "surface",
                "SURFACE" if self.is_23 else None,
                f"{self.boundary_name(coord_type)} | None",
                namespace,
            )
            self.make_class(key, [surface], {"namespace": namespace})

        return self.ensure(key, build)

    def multi_surface_name(self, coord_type: CoordType | None) -> str:
        key = self.coord_key(coord_type, "MultiSurface")

        def build() -> None:
            namespace = self.geom_namespace
            boundary_name = self.boundary_name(coord_type)
            parts = elements_field(
                "parts",
                f"list[{boundary_name}]",
                [("surface", self.class_of(boundary_name), namespace)],
            )
            surfaces = self.make_class(
                self.coord_key(coord_type, "Surfaces"), [parts], {"namespace": namespace}
            )
            multisurface = element_field("multisurface", None, surfaces.__name__, namespace)
            self.make_class(key, [multisurface], {"namespace": namespace})

        return self.ensure(key, build)

    # module.jinja2 (basket), xtf_opening.jinja2

    def build_topic(self, topic: SubModel) -> type | None:
        """The basket class of a topic, None if no element is allowed in its basket."""
        topic_tid = mandatory(topic.tid)
        basket_tid = self.index.topic_basket.get(topic_tid)
        if basket_tid is None:
            return None
        choices: list[ChoiceSpec] = []
        element_names: dict[str, dict[str, str]] = {}
        for element_tid in self.index.allowed_in_basket_of_data_unit.get(basket_tid, []):
            if not self.is_built_class(element_tid):
                # embedded associations have no objects, views are not transferred
                continue
            element_class = self.class_of(self.class_name(element_tid))
            model_tid = self.model_of(element_tid)
            if self.is_23:
                choices.append((self.tag(element_tid), element_class, self.ili_namespace))
                continue
            if model_tid not in element_names:
                element_names[model_tid] = Basket.xtf24_element_names(model_tid, self.index)
            name = element_names[model_tid].get(
                element_tid, mandatory(self.index.index[element_tid].name)
            )
            choices.append((name, element_class, self.model_namespace(model_tid)))
        if not choices:
            return None
        fields = [elements_field("elements", f"list[{type_names(choices)}]", choices)]
        if self.is_23:
            # basket attributes as in ili2c (XSDGenerator)
            fields += [
                attribute_field(name, tag)
                for name, tag in [
                    ("bid", "BID"),
                    ("topics", "TOPICS"),
                    ("kind", "KIND"),
                    ("start_state", "STARTSTATE"),
                    ("end_state", "ENDSTATE"),
                    ("consistency", "CONSISTENCY"),
                ]
            ]
            meta = {"name": self.tag(topic_tid)}
        else:
            fields += [
                attribute_field(name, None, self.ili_namespace) for name in ["bid", "kind"]
            ]
            meta = {"name": mandatory(topic.name)}
        return self.make_class(topic_tid, fields, meta)

    def build_transfer(self) -> None:
        ili_namespace = self.ili_namespace
        meta = {"namespace": ili_namespace}

        def tag(name: str) -> str:
            return name.upper() if self.is_23 else name

        def key(name: str) -> str:
            return f"{PREFIX}.{name}"

        # DataSection
        choices: list[ChoiceSpec] = []
        for topic in self.index.types_bucket.get("SubModel", []):
            basket_class = self.build_topic(topic)
            if basket_class is None:
                continue
            if self.is_23:
                choices.append((self.tag(topic.tid), basket_class, ili_namespace))
            else:
                namespace = self.model_namespace(self.model_of(topic.tid))
                choices.append((mandatory(topic.name), basket_class, namespace))
        baskets = elements_field("baskets", f"list[{type_names(choices)}]", choices)
        data_section = self.make_class(key("DataSection"), [baskets], meta)

        # Model
        if self.is_23:
            model_fields = [
                plain_field(name, "str | None", {"name": name.upper(), "type": "Attribute"})
                for name in ["name", "version", "uri"]
            ]
        else:
            model_fields = [plain_field("name", "str | None", {"type": "Text"})]
        model = self.make_class(key("Model"), model_fields, meta)
        model_choices = [(tag("model"), model, ili_namespace)]
        models = self.make_class(
            key("ModelsType"),
            [elements_field("choice", f"list[{model.__name__}]", model_choices)],
        )

        # HeaderSection
        models_metadata = {
            "name": tag("models"),
            "type": "Element",
            "namespace": ili_namespace,
        }
        header_fields = [
            plain_field("models", models.__name__, models_metadata, default=False)
        ]
        if self.is_23:
            alias, oid_spaces = self.build_23_header_types()
            header_fields += [
                element_field(name, element_tag, f"{annotation} | None", ili_namespace)
                for name, annotation, element_tag in [
                    ("alias", alias.__name__, "ALIAS"),
                    ("oid_spaces", oid_spaces.__name__, "OIDSPACES"),
                    ("comment", "str", "COMMENT"),
                ]
            ]
            header_fields += [
                plain_field(name, "str | None", {"name": name.upper(), "type": "Attribute"})
                for name in ["sender", "version"]
            ]
        else:
            header_fields += [
                element_field(name, None, "str | None", ili_namespace)
                for name in ["sender", "version", "comment"]
            ]
        header = self.make_class(key("HeaderSection"), header_fields, meta)

        # Transfer
        transfer_fields = []
        for name, section in [("headersection", header), ("datasection", data_section)]:
            metadata = {"type": "Element", "namespace": ili_namespace}
            if self.is_23:
                metadata = {"name": name.upper()} | metadata
            transfer_fields.append(
                plain_field(name, section.__name__, metadata, default=False)
            )
        self.make_class(key("Transfer"), transfer_fields, meta | {"name": tag("transfer")})

    def build_23_header_types(self) -> tuple[type, type]:
        """The ALIAS and OIDSPACES of the INTERLIS 2.3 HEADERSECTION, as in ili2c."""
        ili_namespace = self.ili_namespace

        def key(name: str) -> str:
            return f"{PREFIX}.{name}"

        def attribute(name: str, xml_name: str) -> FieldSpec:
            return plain_field(name, "str | None", {"name": xml_name, "type": "Attribute"})

        def elements(name: str, annotation: str, xml_name: str) -> FieldSpec:
            metadata = {"name": xml_name, "type": "Element", "namespace": ili_namespace}
            return name, annotation, field(default_factory=list, metadata=metadata)

        entries = {
            "TagEntry": [attribute("from_value", "FROM"), attribute("to_value", "TO")],
            "ValEntry": [
                attribute("tag", "TAG"),
                attribute("attr", "ATTR"),
                attribute("from_value", "FROM"),
                attribute("to_value", "TO"),
            ],
            "DelEntry": [attribute("tag", "TAG"), attribute("attr", "ATTR")],
        }
        choices: list[ChoiceSpec] = [
            (name.upper(), self.make_class(key(name), fields), ili_namespace)
            for name, fields in entries.items()
        ]
        entries_type = self.make_class(
            key("EntriesType"),
            [
                elements_field("choice", f"list[{type_names(choices)}]", choices),
                attribute("for_value", "FOR"),
            ],
        )
        alias = self.make_class(
            key("AliasType"),
            [elements("entries", f"list[{entries_type.__name__}]", "ENTRIES")],
        )
        oid_space = self.make_class(
            key("OidSpace"), [attribute("name", "NAME"), attribute("oid_domain", "OIDDOMAIN")]
        )
        oid_spaces = self.make_class(
            key("OidSpacesType"),
            [elements("oid_spaces", f"list[{oid_space.__name__}]", "OIDSPACE")],
        )
        return alias, oid_spaces
