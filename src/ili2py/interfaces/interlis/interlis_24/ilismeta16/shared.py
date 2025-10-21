from ili2py.interfaces.interlis.interlis_24 import namespace_map

# we make a local copy of the map to add the imd namespace.
imd_namespace_map = dict(namespace_map)
imd_namespace_map["IlisMeta16"] = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
