import logging
from abc import ABC
from dataclasses import make_dataclass, field
from enum import Enum
from typing import Union, Any

from ili2py.interfaces.namepsaces import configuration
from ili2py.mappers.helpers import Index
from ili2py.writers.py.python_structure import (
    Library,
    Module,
    Enumeration,
    CoordType,
    MetaAttribute,
    Package,
    LineType,
    Class,
    Basket,
)


class PythonStructure:

    def __init__(self, index: Index, library: Library, version: str):
        self.imd_index = index
        self.imd_library = library
        self.xtf_index: dict = {}
        self.ili2py_index: dict = {}
        self.model_version = version
        self.configuration = configuration[version]
        self.construct_references()

    @property
    def namespace(self) -> str:
        return self.configuration["namespace_map"]["ili"]

    def decide_name(self, name: str):
        if self.model_version == "2.3":
            name = name.upper()
        return name

    def decide_attribute_namespace(self) -> dict:
        if self.model_version == "2.4":
            return {"namespace": self.namespace}
        return {}

    def construct_references(self):
        meta = type("Meta", (), {"name": self.decide_name("Ref"), "namespace": self.namespace})
        ref_field_metadata = {"type": "Attribute", "name": self.decide_name("ref")}
        ref_field_metadata.update(self.decide_attribute_namespace())
        ref_class = make_dataclass(
            "Ref",
            [("ref", str, field(default=None, metadata=ref_field_metadata))],
            namespace={"Meta": meta},
        )

        binblbox_type = type("BinBlBoxType", (bytes,), {})
        xmlblbox_type = type("XmlBlBoxType", (str,), {})

        self.ili2py_index["ref"] = ref_class
        self.ili2py_index["binblbox_type"] = binblbox_type
        self.ili2py_index["xmlblbox_type"] = xmlblbox_type

    def construct_class_domain_type(self, definition: dict, package_oid):
        if definition["oid"] not in self.xtf_index:
            type_match = {"str": str, "float": float, "int": int}
            referenced_type = type_match.get(definition["reference"])
            if not referenced_type:
                referenced_type = self.xtf_index.get(definition["reference_oid"])
                if not referenced_type:
                    logging.debug(
                        f"Creating type description first because it did not exist {definition["reference_oid"]} for type {definition["oid"]}"
                    )
                    self.construct_class_domain_type(
                        Module.create_type_definition(
                            definition["reference_oid"], self.imd_index, package_oid
                        ),
                        package_oid,
                    )
                    referenced_type = self.xtf_index[definition["reference_oid"]]

            @property
            def metadata(self) -> dict:
                return {
                    "interlis": {
                        "oid": definition["oid"],
                        "meta_attributes": {},
                        "type_restrictions": definition["restrictions"],
                    }
                }

            type_class = type(definition["name"], (referenced_type,), {"metadata": metadata})
            self.xtf_index[definition["oid"]] = type_class

    def construct_meta_attributes(self, meta_attributes: list[MetaAttribute]) -> dict:
        meta_attributes = {}
        for item in meta_attributes:
            meta_attributes[item.name] = item.value
        return meta_attributes

    def construct_class_enumeration(self, enumeration: Enumeration):
        if enumeration.identifier not in self.xtf_index:

            @property
            def metadata(self) -> dict:
                return {
                    "interlis": {
                        "oid": enumeration.identifier,
                        "meta_attributes": self.construct_meta_attributes(
                            enumeration.meta_attributes
                        ),
                        "kind": "Enumeration",
                    }
                }

            members = {"metadata": metadata}
            for value in enumeration.values:
                members[value.upper().replace(".", "_")] = value
            enumeration_class = Enum(enumeration.name, members, type=str)
            enumeration_class.metadata = metadata
            self.xtf_index[enumeration.identifier] = enumeration_class

    def coord_type_type_name(self, coord_type_name: str) -> str:
        return f"{coord_type_name}Type"

    def coord_type_arc_type_name(self, coord_type_name: str) -> str:
        return f"{coord_type_name}ARCType"

    def construct_dataclass_coord_type(self, coord_type: CoordType):
        coord_type_type_name = self.coord_type_type_name(coord_type.identifier)
        coord_type_type_fields = []
        for attribute in coord_type.attributes:
            attribute_metadata = {
                "type": "Element",
                "namespace": self.geom_namespace,
                "interlis": {
                    "meta_attributes": self.construct_meta_attributes(attribute.meta_attributes)
                },
            }
            if attribute.type_restrictions:
                attribute_metadata["type_restrictions"] = attribute.type_restrictions
            coord_type_type_fields.append(
                (
                    attribute.name.lower(),
                    attribute.type,
                    field(default=None, metadata=attribute_metadata),
                )
            )
        coord_type_type_class = make_dataclass(coord_type_type_name, coord_type_type_fields)
        self.xtf_index[coord_type_type_name] = coord_type_type_class

        coord_type_meta_attributes = {}
        for item in coord_type.meta_attributes:
            coord_type_meta_attributes[item.name] = item.value

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": coord_type.identifier,
                    "kind": "CoordType",
                    "meta_attributes": coord_type_meta_attributes,
                }
            }

        coord_type_fields = [
            (
                "coord",
                self.xtf_index[coord_type_type_name],
                field(
                    default=None,
                    metadata={"type": "Element", "namespace": self.geom_namespace, "interlis": {}},
                ),
            )
        ]

        coord_type_class = make_dataclass(coord_type.identifier, coord_type_fields)
        setattr(coord_type_class, "metadata", metadata)
        self.xtf_index[coord_type.identifier] = coord_type_class

        coord_type_arc_type_name = self.coord_type_arc_type_name(coord_type.identifier)
        coord_type_arc_type_fields = [
            (
                "a1",
                float,
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": self.geom_namespace,
                        "interlis": {"meta_attributes": {}, "type_restrictions": {}},
                    },
                ),
            ),
            (
                "a2",
                float,
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": self.geom_namespace,
                        "interlis": {"meta_attributes": {}, "type_restrictions": {}},
                    },
                ),
            ),
            (
                "r",
                float,
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": self.geom_namespace,
                        "interlis": {"meta_attributes": {}, "type_restrictions": {}},
                    },
                ),
            ),
        ]
        coord_type_arc_type_class = make_dataclass(
            coord_type_arc_type_name, coord_type_arc_type_fields
        )
        self.xtf_index[coord_type_arc_type_name] = coord_type_arc_type_class

    def line_type_reference(self, reference_targets: str) -> Any:
        if isinstance(reference_targets, str):
            return self.xtf_index[reference_targets]
        else:
            return reference_targets

    def construct_dataclass_line_type(self, line_type: LineType):
        if line_type.attribute.name in ["POLYLINE", "DIRECTEDPOLYLINE"]:
            reference = self.line_type_reference(line_type.attribute.reference_targets[0])
            line_type_fields = [
                (
                    line_type.attribute.name,
                    reference,
                    field(
                        default_factory=list,
                        metadata={
                            "type": "Elements",
                            "namespace": self.geom_namespace,
                            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
                        },
                    ),
                )
            ]

            line_type_line_class = make_dataclass(line_type.identifier, line_type_fields)
            self.xtf_index[line_type.identifier] = line_type_line_class
        elif line_type.attribute.name in ["SURFACE", "AREA"]:
            reference = self.line_type_reference(line_type.attribute.reference_targets[0])
            segment_fields = [
                (
                    "segments",
                    list[
                        self.xtf_index[self.coord_type_type_name(reference.__name__)]
                        | self.xtf_index[self.coord_type_arc_type_name(reference.__name__)]
                    ],
                    field(
                        default_factory=list,
                        metadata={
                            "type": "Elements",
                            "choices": (
                                {
                                    "name": "coord",
                                    "type": self.coord_type_type_name(reference),
                                    "namespace": self.geom_namespace,
                                },
                                {
                                    "name": "arc",
                                    "type": self.coord_type_arc_type_name(reference),
                                    "namespace": self.geom_namespace,
                                },
                            ),
                            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
                        },
                    ),
                )
            ]
            segment_dataclass = make_dataclass("Segment", segment_fields)
            polyline_fields = [
                (
                    "polyline",
                    segment_dataclass,
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": self.geom_namespace,
                            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
                        },
                    ),
                )
            ]
            polyline_dataclass = make_dataclass("Polyline", polyline_fields)

            polyline_interior_dataclass = make_dataclass(
                "PolylineInterior", [], bases=(polyline_dataclass,)
            )
            polyline_exterior_dataclass = make_dataclass(
                "PolylineExterior", [], bases=(polyline_dataclass,)
            )

            boundary_fields = [
                (
                    "boundaries",
                    list[polyline_exterior_dataclass | polyline_interior_dataclass],
                    field(
                        default_factory=list,
                        metadata={
                            "type": "Elements",
                            "choices": (
                                {
                                    "type": polyline_exterior_dataclass,
                                    "name": "exterior",
                                    "namespace": self.geom_namespace,
                                },
                                {
                                    "type": polyline_interior_dataclass,
                                    "name": "interior",
                                    "namespace": self.geom_namespace,
                                },
                            ),
                            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
                        },
                    ),
                )
            ]
            boundary_dataclass = make_dataclass("Boudary", boundary_fields)
            surface_fields = [
                (
                    "surface",
                    boundary_dataclass,
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": self.geom_namespace,
                            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
                        },
                    ),
                )
            ]
            surface_dataclass = make_dataclass(line_type.identifier, surface_fields)
            self.xtf_index[line_type.identifier] = surface_dataclass

    def construct_dataclass_class(self, class_definition: Class, package_identifier: str):
        class_attributes = []
        if class_definition.oid:
            class_attributes.append(
                (
                    class_definition.oid.name,
                    str,
                    field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": self.ili_namespace,
                            "name": class_definition.oid.name,
                            "interlis": {
                                "meta_attributes": {},
                                "type_restrictions": class_definition.oid.type_restrictions,
                            },
                        },
                    ),
                )
            )
        if class_definition.kind == "Class":
            class_attributes.append(
                (
                    "tid",
                    str,
                    field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": self.ili_namespace,
                            "name": "tid",
                            "interlis": {
                                "meta_attributes": {},
                                "type_restrictions": None,
                            },
                        },
                    ),
                )
            )
        for attribute in class_definition.attributes:
            meta_attributes = {}
            for item in attribute.meta_attributes:
                meta_attributes[item.name] = item.value
            interlis_metadata = {
                "oid": attribute.identifier,
                "meta_attributes": meta_attributes,
                "type_restrictions": attribute.type_restrictions,
            }
            if attribute.reference_targets:
                interlis_metadata["reference_targets"] = attribute.reference_targets
            metadata = {
                "type": "Element",
                "namespace": f"{self.configuration['base_url']}/{package_identifier}",
                "interlis": interlis_metadata,
            }
            if attribute.type_restrictions["type_related_type"]:
                metadata["name"] = attribute.name
            if attribute.enumeration:
                self.construct_class_enumeration(attribute.enumeration)
                class_attributes.append(
                    (
                        attribute.name,
                        self.xtf_index[attribute.enumeration.identifier],
                        field(
                            default=None,
                            metadata=metadata,
                        ),
                    )
                )
            elif attribute.line_type:
                self.construct_dataclass_line_type(attribute.line_type)
                class_attributes.append(
                    (
                        attribute.name,
                        self.xtf_index[attribute.line_type.identifier],
                        field(
                            default=None,
                            metadata=metadata,
                        ),
                    )
                )
            else:
                native_types = {
                    "str": str,
                    "float": float,
                    "int": int,
                    "bool": bool,
                    "Any": Any,
                    "XmlBlBoxType": self.ili2py_index["xmlblbox_type"],
                    "BinBlBoxType": self.ili2py_index["binblbox_type"],
                }
                if attribute.type in native_types:
                    attribute_type = native_types[attribute.type]
                else:
                    if attribute.list_type:
                        attribute_type = list[self.xtf_index[attribute.original_type]]
                    else:
                        if "ili2py" in attribute.original_type:
                            attribute_type = self.ili2py_index[
                                attribute.original_type.split(".")[-1]
                            ]
                        else:
                            attribute_type = self.xtf_index[attribute.original_type]
                class_attributes.append(
                    (
                        attribute.name,
                        attribute_type,
                        field(
                            default=None,
                            metadata=metadata,
                        ),
                    )
                )
        if class_definition.super_class:
            bases = (self.xtf_index[class_definition.super_class_identifier],)
        elif class_definition.abstract:
            bases = (ABC,)
        else:
            bases = ()
        class_dataclass = make_dataclass(class_definition.identifier, class_attributes, bases=bases)
        self.xtf_index[class_definition.identifier] = class_dataclass

    def construct_dataclass_basket(self, module: Module):
        if module.basket.choices:
            element_attribute_types = []
            choices_metadata = []
            for choice in module.basket.choices:
                element_attribute_types.append(self.xtf_index[choice.identifier])
                choices_metadata.append(
                    {
                        "name": choice.identifier,
                        "type": self.xtf_index[choice.identifier],
                        "namespace": self.basket_namespace,
                    }
                )
            dataclass_basket_attributes = [
                (
                    "elements",
                    list[Union[tuple(element_attribute_types)]],
                    field(
                        default_factory=list,
                        metadata={"type": "Elements", "choices": choices_metadata},
                    ),
                ),
                (
                    "bid",
                    str | None,
                    field(default=None, metadata={"type": "Attribute", "name": "BID"}),
                ),
                (
                    "kind",
                    str | None,
                    field(default=None, metadata={"type": "Attribute", "name": "KIND"}),
                ),
            ]
        basket_dataclass = make_dataclass(f"{module.identifier}TOPIC", dataclass_basket_attributes)
        self.xtf_index[f"{module.identifier}TOPIC"] = basket_dataclass

    @property
    def geom_namespace(self):
        return self.configuration["namespace_map"]["ili"]

    @property
    def ili_namespace(self):
        return self.configuration["namespace_map"]["ili"]

    @property
    def basket_namespace(self):
        return self.configuration["namespace_map"]["ili"]

    def construct_package(self, package: Package | Module):
        for definition in package.type_definitions:
            self.construct_class_domain_type(definition, package.identifier)
        for enumeration in package.enumerations:
            self.construct_class_enumeration(enumeration)
        for coord_type in package.coord_types:
            self.construct_dataclass_coord_type(coord_type)
        for line_type in package.line_types:
            self.construct_dataclass_line_type(line_type)
        for class_definition in package.classes:
            self.construct_dataclass_class(class_definition, package_identifier=package.identifier)

    def create_reader_structure(self):

        for package in self.imd_library.packages:
            self.construct_package(package)
            for module in package.modules:
                self.construct_package(module)
                self.construct_dataclass_basket(module)
