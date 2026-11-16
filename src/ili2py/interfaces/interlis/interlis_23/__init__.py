from dataclasses import dataclass

from ili2py.interfaces.interlis import GeometryTags

# the common name space used in an INTERLIS 2.3 XTF, the models share it
base_url = "http://www.interlis.ch/INTERLIS2.3"
namespace_map = {"ili": base_url}


class ILI_META_BASE:
    namespace = namespace_map["ili"]


class Ili23GeometryTags(GeometryTags):
    """
    The element names of the geometry in an INTERLIS 2.3 XTF. 2.3 keeps everything in its one
    namespace, writes the elements in capitals and does not know MULTI geometries yet
    (see the encoding of the geometry in ili2-refman_2006-04-13_d.pdf).
    """

    transfer_namespace = namespace_map["ili"]
    namespace = namespace_map["ili"]
    coord_name = "COORD"
    arc_name = "ARC"
    polyline_name = "POLYLINE"
    surface_name = "SURFACE"
    boundary_names = ("BOUNDARY",)
    axis_names = ("C1", "C2", "C3")
    arc_point_names = ("A1", "A2", "R")


@dataclass(kw_only=True)
class MODEL:
    class Meta(ILI_META_BASE):
        pass

    NAME: str
    VERSION: str
    URI: str


@dataclass
class HeaderSection:
    class Meta(ILI_META_BASE):
        pass

    MODELS: list[MODEL]
    SENDER: str
    VERSION: str


@dataclass
class TRANSFER:
    class Meta(ILI_META_BASE):
        pass

    HEADERSECTION: HeaderSection
