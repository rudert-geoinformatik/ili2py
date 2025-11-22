import logging
from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Tuple

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    AttrOrParam as ImdAttrOrParam,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    BlackboxType as ImdBlackboxType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    BooleanType as ImdBooleanType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import Class as ImdClass
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    ClassRefType as ImdClassRefType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    CoordType as ImdCoordType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    EnumTreeValueType as ImdEnumTreeValueType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    EnumType as ImdEnumType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    FormattedType as ImdFormattedType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    LineType as ImdLineType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import Model as ImdModel
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    MultiValue as ImdMultiValue,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    NumType as ImdNumType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    RoleType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    SubModel as ImdSubmodel,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    TextType as ImdTextType,
)
from ili2py.mappers.helpers import Index


@dataclass
class Base(ABC):
    oid: str
    name: str

    @property
    def save_oid(self) -> str:
        return self.oid.replace(".", "_")


@dataclass
class Attribute(Base):
    type_definition: str
    mandatory: str

    @classmethod
    def from_imd(cls, attribute: ImdAttrOrParam, index: Index):
        type_name, mandatory = Attribute.handle_type(attribute, index)
        return cls(
            name=attribute.name,
            oid=attribute.tid,
            type_definition=type_name,
            mandatory="[1]" if mandatory else "[0..1]",
        )

    @staticmethod
    def handle_type(attribute: ImdAttrOrParam, index: Index) -> Tuple[str, bool]:
        type_definition = index.index[attribute.type_value.ref]
        name = Attribute.handle_type_trail(type_definition, index)
        return name, type_definition.mandatory

    @staticmethod
    def handle_type_trail(
        type_definition: (
            ImdTextType
            | ImdFormattedType
            | ImdBlackboxType
            | ImdNumType
            | ImdBooleanType
            | ImdMultiValue
            | ImdEnumType
            | ImdCoordType
            | ImdLineType
            | ImdEnumTreeValueType
            | ImdClassRefType
        ),
        index: Index,
    ) -> str:
        if isinstance(type_definition, ImdTextType):
            return "String"
        elif isinstance(type_definition, ImdFormattedType):
            if type_definition.super and type_definition.name == "TYPE":
                return Attribute.handle_type_trail(index.index[type_definition.super.ref], index)
            else:
                return type_definition.name
        elif isinstance(type_definition, ImdBlackboxType):
            return "BlackBox"
        elif isinstance(type_definition, ImdNumType):
            return "Number"
        elif isinstance(type_definition, ImdBooleanType):
            return "Boolean"
        elif isinstance(type_definition, ImdMultiValue):
            return index.index[type_definition.base_type.ref].name
        elif isinstance(type_definition, ImdEnumType):
            return "Enumeration"
        elif isinstance(type_definition, ImdEnumTreeValueType):
            return "Enumeration"
        elif isinstance(type_definition, ImdCoordType):
            if type_definition.super and type_definition.name == "TYPE":
                return Attribute.handle_type_trail(index.index[type_definition.super.ref], index)
            else:
                return type_definition.name
        elif isinstance(type_definition, ImdLineType):
            if type_definition.super and type_definition.name == "TYPE":
                return Attribute.handle_type_trail(index.index[type_definition.super.ref], index)
            else:
                return type_definition.name
        elif isinstance(type_definition, ImdClassRefType):
            return index.index[index.class_related_type[type_definition.tid]].name
        else:
            logging.debug(f"Type was not handled correctly for UML preparation: {type_definition}")
            return "UNKNOWN"


@dataclass
class Class(Base):
    attributes: list[Attribute]
    inherits_from: str | None
    association_attributes: list[Attribute] = field(default_factory=list)

    @classmethod
    def from_imd(cls, class_definition: ImdClass, index: Index):
        attributes = []
        if index.class_class_attribute.get(class_definition.tid):
            for attribute_tid in index.class_class_attribute[class_definition.tid]:
                attribute = index.index[attribute_tid]
                attributes.append(Attribute.from_imd(attribute, index))
        association_attributes = []
        association_oids = index.associated_classes.get(class_definition.tid, [])
        for association_oid in association_oids:
            for role_oid, related_class_oid, strongness, min, max in index.association_bucket[
                association_oid
            ]:
                if related_class_oid != class_definition.tid:
                    role_object: RoleType = index.index[role_oid]
                    min = role_object.multiplicity.multiplicity.min
                    if min is None:
                        min = 0
                    max = role_object.multiplicity.multiplicity.max
                    if max is None:
                        max = "*"
                    association_attributes.append(
                        Attribute(
                            oid=role_object.tid,
                            name=role_object.name,
                            type_definition="Ref",
                            mandatory=f"{min}...{max}" if min != max else f"{min}",
                        )
                    )

        return cls(
            name=class_definition.name,
            oid=class_definition.tid,
            inherits_from=class_definition.super.ref if class_definition.super else None,
            attributes=attributes,
            association_attributes=association_attributes,
        )


@dataclass
class TopicGroup(Base):
    """
    Represents an ili:Topic
    """

    classes: list[Class]
    associations: list[str]

    @classmethod
    def from_imd(cls, sub_model: ImdSubmodel, index: Index):
        classes = []
        associations = []

        if index.class_in_package.get(sub_model.tid):
            for element_tid in index.class_in_package[sub_model.tid]:
                element = index.index[element_tid]
                cls.handle_class(classes, element, index)
        if index.association_in_package.get(sub_model.tid):
            for element_tid in index.association_in_package[sub_model.tid]:
                element = index.index[element_tid]
                cls.handle_association(associations, element, index)

        return cls(
            name=sub_model.name, oid=sub_model.tid, classes=classes, associations=associations
        )

    @staticmethod
    def handle_class(classes: list[Class], element: Any, index: Index):
        classes.append(Class.from_imd(element, index))

    @classmethod
    def handle_association(
        cls,
        associations: list[list[Tuple[str, str, str]]],
        association: ImdClass,
        index: Index,
    ):
        if index.association_bucket.get(association.tid):
            association_string = []
            for role_tid, class_tid, strongness, min, max in index.association_bucket[
                association.tid
            ]:
                role = index.index[role_tid]
                related_class = index.index[class_tid]
                if role.multiplicity.multiplicity is None:
                    multiplicity_string = None
                else:
                    multiplicity_string = TopicGroup.render_multiplicity(
                        role.multiplicity.multiplicity.min, role.multiplicity.multiplicity.max
                    )
                strongness_string = TopicGroup.render_strongness(role.strongness)
                association_string.append(
                    (related_class.tid, multiplicity_string, strongness_string, role_tid)
                )
            association_string.append(association.name)
            associations.append(association_string)

    @staticmethod
    def render_multiplicity(minimum, maximum) -> str:
        if minimum == 1 and maximum == 1:
            return "1"
        elif minimum == 0 and maximum == 0:
            # Cardinality / Multiplicity '0' is not implemented in mermaid
            return "0"
        elif minimum == 0 and maximum == 1:
            return "0..1"
        elif minimum == 1 and maximum is None:
            return "1..*"
        elif minimum == 0 and maximum is None:
            # Cardinality / Multiplicity '0..*' is not implemented in mermaid directly we deliver empty string
            return "0..*"
        elif minimum is None and maximum is None:
            return "*"
        else:
            return f"{minimum}..{maximum}"

    @staticmethod
    def render_strongness(strongness: str):
        if strongness == "Assoc":
            # TODO: decide if we want to show direction of association with arrows at the end of the connector
            logging.debug("Association is drawn without arrows currently!")
            return ""
        elif strongness == "Aggr":
            return "o"
        elif strongness == "Comp":
            return "*"
        else:
            logging.error(f"Unknown strongness: {strongness}")
            return ""


@dataclass
class ModelGroup(TopicGroup):
    """
    Represents an ili:Model
    """

    topic_groups: list[TopicGroup]
    associations: list[str]

    @classmethod
    def from_imd(cls, model: ImdModel, index: Index):
        topics = []
        classes = []
        associations = []
        if index.submodel_in_package.get(model.tid):
            for element_tid in index.submodel_in_package[model.tid]:
                element = index.index[element_tid]
                cls.handle_topic(topics, element, index)
        if index.class_in_package.get(model.tid):
            for element_tid in index.class_in_package[model.tid]:
                element = index.index[element_tid]
                cls.handle_class(classes, element, index)
        if index.association_in_package.get(model.tid):
            for element_tid in index.association_in_package[model.tid]:
                element = index.index[element_tid]
                cls.handle_association(associations, element, index)
        return cls(
            name=model.name,
            oid=model.tid,
            topic_groups=topics,
            classes=classes,
            associations=associations,
        )

    @staticmethod
    def handle_topic(topics: list[TopicGroup], element: Any, index: Index):
        if isinstance(element, ImdSubmodel):
            topics.append(TopicGroup.from_imd(element, index))


@dataclass
class Diagram(Base):
    """
    Represents the whole diagram with all nested items
    """

    model_groups: list[ModelGroup]

    @classmethod
    def from_imd(cls, index: Index):
        models = []
        for model in index.types_bucket["Model"]:
            models.append(ModelGroup.from_imd(model, index))
        return cls(
            name=", ".join([model.name for model in models]), oid="diagram", model_groups=models
        )
