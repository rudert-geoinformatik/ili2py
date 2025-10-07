base_url_23 = "http://www.interlis.ch/INTERLIS2.3"
base_url_24 = "http://www.interlis.ch/xtf/2.4"
configuration = {
    "2.3": {"selector": 23, "base_url": base_url_23, "namespace_map": {"ili": base_url_23}},
    "2.4": {
        "selector": 24,
        "base_url": base_url_24,
        "namespace_map": {
            "ili": f"{base_url_24}/INTERLIS",
            "geom": "http://www.interlis.ch/geometry/1.0",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        },
    },
}
