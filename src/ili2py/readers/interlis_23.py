from dataclasses import dataclass, field, make_dataclass
from typing import List, Optional
from ili2py.interfaces.metamodel.ilismeta16 import ModelData, Class

ns_map = {
    "ili": "http://www.interlis.ch/INTERLIS2.3"
}


def reader_classes(model_data: ModelData, all_model_data: List[ModelData]):

    class ILI_META_BASE:
        namespace = ns_map["ili"]

    topic_fields = []
    for topic_item in model_data.sub_model:
        class_fields = [("bid", str, field(metadata={"name": "BID", "type": "Attribute"}))]
        # find all classes inside sub_model[ili:TOPIC]
        for class_item in model_data.classes:
            if class_item.element_in_package.ref == topic_item.tid and class_item.kind == "Class":
                attr_or_param_fields = [("tid", Optional[str], field(default=None, metadata={"name": "TID", "type": "Attribute"}))]
                # find all attributes related to class
                for attr_or_param_item in model_data.attr_or_param:
                    if attr_or_param_item.attr_parent.ref == class_item.tid:
                        # find type definition for attribute (currently we have implemented [ili:TextType]
                        for type_item in model_data.text_types:
                            if type_item.tid == attr_or_param_item.type.ref:
                                attr_or_param_field = (
                                    attr_or_param_item.name.lower(),
                                    str if type_item.mandatory else Optional[str],
                                    field(
                                        metadata={
                                            "name": attr_or_param_item.name,
                                            "type": "Element",
                                            "required": type_item.mandatory
                                        }
                                    ) if type_item.mandatory else field(
                                        default=None,
                                        metadata={
                                            "name": attr_or_param_item.name,
                                            "type": "Element",
                                            "required": type_item.mandatory
                                        }
                                    )
                                )
                                # dataclasses have kwargs and args. We need to ensure, that the stay in correct
                                # order (args first)
                                if type_item.mandatory:
                                    attr_or_param_fields.insert(0, attr_or_param_field)
                                else:
                                   attr_or_param_fields.append(attr_or_param_field)
                        # find type definition for attribute (currently we have implemented [ili:TextType]
                        for type_item in model_data.num_types:
                           if type_item.tid == attr_or_param_item.type.ref:
                               attr_or_param_field = (
                                   attr_or_param_item.name.lower(),
                                   int if type_item.mandatory else Optional[int],
                                   field(
                                       metadata={
                                           "name": attr_or_param_item.name,
                                           "type": "Element",
                                           "required": type_item.mandatory
                                       }
                                   ) if type_item.mandatory else field(
                                       default=None,
                                       metadata={
                                           "name": attr_or_param_item.name,
                                           "type": "Element",
                                           "required": type_item.mandatory
                                       }
                                   )
                               )
                               # dataclasses have kwargs and args. We need to ensure, that the stay in correct
                               # order (args first)
                               if type_item.mandatory:
                                   attr_or_param_fields.insert(0, attr_or_param_field)
                               else:
                                   attr_or_param_fields.append(attr_or_param_field)


                class_fields.append(
                    (
                        class_item.name.lower(),
                        List[make_dataclass(class_item.name, attr_or_param_fields)],
                        field(
                            default=None,
                            metadata={
                                "name": class_item.tid,
                                "type": "Element",
                                "default": None
                            }
                        )
                    )
                )
        topic_fields.append(
            (
                topic_item.name.lower(),
                make_dataclass(topic_item.name, class_fields),
                field(
                    metadata={
                        "name": topic_item.tid,
                        "type":"Element",
                        "default":None
                    }
                )
            )
        )

    Datasection = make_dataclass("DATASECTION", fields=topic_fields)

    @dataclass(kw_only=True)
    class Model:
        class Meta(ILI_META_BASE):
            name = "MODEL"

        name: str = field(
            metadata={
                "name": "NAME",
                "type": "Attribute",
                "required": False,
            },
        )
        version: str = field(
            metadata={
                "name": "VERSION",
                "type": "Attribute",
                "required": False,
            },
        )
        uri: str = field(
            metadata={
                "name": "URI",
                "type": "Attribute",
                "required": False,
            },
        )

    @dataclass
    class ModelItem:
        class Meta(ILI_META_BASE):
            name = "MODEL"

        model: Model = field(
            metadata={
                "name": "MODEL",
                "type": "Element",
                "required": True,
            },
        )

    @dataclass
    class Headersection:
        class Meta(ILI_META_BASE):
            name = "HEADERSECTION"

        models: List[ModelItem] = field(
            metadata={
                "name": "MODELS",
                "type": "Element",
                "required": True,
            },
        )
        sender: str = field(
            default=None,
            metadata={
                "name": "SENDER",
                "type": "Attribute",
                "required": True,
            },
        )
        version: str = field(
            default=None,
            metadata={
                "name": "VERSION",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Transfer:
        class Meta(ILI_META_BASE):
            name = "TRANSFER"

        headersection: Headersection = field(
            metadata={
                "name": "HEADERSECTION",
                "type": "Element",
                "required": True,
            },
        )
        datasection: Datasection = field(
            metadata={
                "name": "DATASECTION",
                "type": "Element",
                "required": True,
            },
        )
    return Transfer
