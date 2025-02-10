from dataclasses import make_dataclass, field
from typing import List, Optional

from ili2py.interfaces.interlis.interlis_23 import TRANSFER
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.model_data import ModelData
from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer


class DataClassGenerator:

    def __init__(self, meta_model: ImdTransfer):
        self.meta_model = meta_model

    def find_model_by_name(self, model_name: str) -> ModelData:
        for model_data in self.meta_model.datasection.ModelData:
            if model_name == model_data.Model.Name:
                return model_data
        raise LookupError(f"No model with name {model_name} could be found.")

    def generate(self, model_name: str):
        """
        This is a factory method which produces dataclasses at runtime `make_dataclass`. The
        construction plan of the dataclasses is derived from the tree of dataclass objects
        which has to be created to be first.

        TODO: currently this makes no big sense since we usually want to read all models which can be
            in an XTF.

        Args:
            model_name: The name of the desired model name which the XTF is constructed from.

        Returns: The tree of dataclasses representing the structure of the XTF. This can be used to generate
            readers out of it.
        """
        model_data = self.find_model_by_name(model_name)
        topic_fields = []
        for topic_item in model_data.SubModel:
            class_fields = [("bid", str, field(metadata={"name": "BID", "type": "Attribute"}))]
            # find all classes inside sub_model[ili:TOPIC]
            for class_item in model_data.Class:
                if class_item.element_in_package.ref == topic_item.tid and class_item.kind == "Class":
                    attr_or_param_fields = [("tid", Optional[str], field(default=None,
                                                                         metadata={"name": "TID",
                                                                                   "type": "Attribute"}))]
                    # find all attributes related to class
                    for attr_or_param_item in model_data.AttrOrParam:
                        if attr_or_param_item.AttrParent_ref.ref == class_item.tid:
                            # find type definition for attribute (currently we have implemented [ili:TextType]
                            for type_item in model_data.TextType:
                                if type_item.tid == attr_or_param_item.Type_ref.ref:
                                    attr_or_param_field = (
                                        attr_or_param_item.Name.lower(),
                                        str if type_item.mandatory else Optional[str],
                                        field(
                                            metadata={
                                                "name": attr_or_param_item.Name,
                                                "type": "Element",
                                                "required": type_item.mandatory
                                            }
                                        ) if type_item.mandatory else field(
                                            default=None,
                                            metadata={
                                                "name": attr_or_param_item.Name,
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
                            # find type definition for attribute (currently we have implemented [ili:NumType]
                            for type_item in model_data.NumType:
                                if type_item.tid == attr_or_param_item.Type_ref.ref:
                                    attr_or_param_field = (
                                        attr_or_param_item.Name.lower(),
                                        int if type_item.mandatory else Optional[int],
                                        field(
                                            metadata={
                                                "name": attr_or_param_item.Name,
                                                "type": "Element",
                                                "required": type_item.mandatory
                                            }
                                        ) if type_item.mandatory else field(
                                            default=None,
                                            metadata={
                                                "name": attr_or_param_item.Name,
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
                    topic_item.Name.lower(),
                    make_dataclass(topic_item.Name, class_fields),
                    field(
                        metadata={
                            "name": topic_item.tid,
                            "type": "Element",
                            "default": None
                        }
                    )
                )
            )

        class XtfTransfer(TRANSFER):
            DATASECTION: make_dataclass("DATASECTION", fields=topic_fields)

        return XtfTransfer