from dataclasses import dataclass, field

from ili2py.interfaces.interlis import GeometryTags

# each model has its own name space below the base url (e.g. .../xtf/2.4/INTERLIS)
base_url = "http://www.interlis.ch/xtf/2.4"
namespace_map = {
    "ili": f"{base_url}/INTERLIS",
    "geom": "http://www.interlis.ch/geometry/1.0",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
}


class Ili24GeometryTags(GeometryTags):
    """
    The element names of the geometry in an INTERLIS 2.4 XTF. 2.4 moved the geometry into a
    namespace of its own (geom), writes it in lower case and learned MULTI geometries on the
    way.
    """

    transfer_namespace = namespace_map["ili"]
    namespace = namespace_map["geom"]
    coord_name = "coord"
    arc_name = "arc"
    polyline_name = "polyline"
    surface_name = "surface"
    boundary_names = ("exterior", "interior")
    axis_names = ("c1", "c2", "c3")
    arc_point_names = ("a1", "a2", "r")
    multipolyline_name = "multipolyline"
    multisurface_name = "multisurface"


@dataclass
class Model:
    model: str = field(metadata={"namespace": namespace_map["ili"]})


@dataclass
class Models:
    elements: list[Model] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": ({"name": "model", "type": Model, "namespace": namespace_map["ili"]},),
        },
    )


@dataclass
class HeaderSection:
    models: Models = field(metadata={"namespace": namespace_map["ili"]})
    sender: str | None = field(
        default=None,
        metadata={"namespace": namespace_map["ili"]},
    )


@dataclass
class Transfer:
    headersection: HeaderSection = field(metadata={"namespace": namespace_map["ili"]})
