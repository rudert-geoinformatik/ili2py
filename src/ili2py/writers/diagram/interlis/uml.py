import logging
from abc import ABC
from dataclasses import InitVar, dataclass, field
from typing import Any

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    AttrOrParam as ImdAttrOrParam,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    BlackboxType as ImdBlackboxType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    BooleanType as ImdBooleanType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    Class as ImdClass,
)
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
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    Model as ImdModel,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    MultiValue as ImdMultiValue,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    NumType as ImdNumType,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    Role as ImdRole,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    SubModel as ImdSubmodel,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    TextType as ImdTextType,
)
from ili2py.mappers.helpers import Index, mandatory, mandatory_ref

# (class tid, multiplicity, strongness, role tid) of one end of an association
type AssociationEnd = tuple[str, str | None, str, str]
# all ends of an association, followed by the name of the association
type Association = list[AssociationEnd | str]


@dataclass
class Base(ABC):
    oid: str
    name: str
    index: InitVar[Index]
    language: InitVar[str | None]

    def __post_init__(self, index: Index, language: str | None = None):
        if language is not None:
            translated_name = index.model_translations.get(self.oid, {}).get(language)
            if translated_name is None:
                logging.info(
                    f"No Translation was found for {self.oid} "
                    f"in language {language} => using original model."
                )
            else:
                self.name = translated_name

    def get_translated_name(self, index: Index, language: str | None) -> str:
        if language is not None:
            translated_name = index.model_translations.get(self.oid, {}).get(language)
            if translated_name is None:
                logging.info(f"No Translation was found for {self.oid} in language {language}")
            else:
                translated_name = self.name
        return translated_name

    @property
    def save_oid(self) -> str:
        return self.oid.replace(".", "_")


@dataclass
class Attribute(Base):
    type_definition: str
    mandatory: str

    @classmethod
    def from_imd(cls, attribute: ImdAttrOrParam, index: Index, language: str | None):
        type_name, is_mandatory = Attribute.handle_type(attribute, index)
        return cls(
            index=index,
            name=mandatory(attribute.name),
            oid=mandatory(attribute.tid),
            type_definition=type_name,
            mandatory="[1]" if is_mandatory else "[0..1]",
            language=language,
        )

    @staticmethod
    def handle_type(attribute: ImdAttrOrParam, index: Index) -> tuple[str, bool]:
        type_definition = index.index[mandatory_ref(attribute.type_value)]
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
                return Attribute.handle_type_trail(
                    index.index[type_definition.super.ref], index
                )
            else:
                return mandatory(type_definition.name)
        elif isinstance(type_definition, ImdBlackboxType):
            return "BlackBox"
        elif isinstance(type_definition, ImdNumType):
            return "Number"
        elif isinstance(type_definition, ImdBooleanType):
            return "Boolean"
        elif isinstance(type_definition, ImdMultiValue):
            return index.index[mandatory_ref(type_definition.base_type)].name
        elif isinstance(type_definition, (ImdEnumType, ImdEnumTreeValueType)):
            return "Enumeration"
        elif isinstance(type_definition, (ImdCoordType, ImdLineType)):
            if type_definition.super and type_definition.name == "TYPE":
                return Attribute.handle_type_trail(
                    index.index[type_definition.super.ref], index
                )
            else:
                return mandatory(type_definition.name)
        elif isinstance(type_definition, ImdClassRefType):
            return index.index[index.class_related_type[type_definition.tid]].name
        else:
            logging.debug(
                f"Type was not handled correctly for UML preparation: {type_definition}"
            )
            return "UNKNOWN"


@dataclass
class Class(Base):
    attributes: list[Attribute]
    inherits_from: str | None
    association_attributes: list[Attribute] = field(default_factory=list)

    @classmethod
    def from_imd(cls, class_definition: ImdClass, index: Index, language: str | None):
        attributes = []
        if index.class_class_attribute.get(class_definition.tid):
            for attribute_tid in index.class_class_attribute[class_definition.tid]:
                attribute = index.index[attribute_tid]
                attributes.append(Attribute.from_imd(attribute, index, language))
        association_attributes = []
        association_oids = index.associated_classes.get(class_definition.tid, [])
        for association_oid in association_oids:
            for (
                role_oid,
                related_class_oid,
                _strongness,
                _min,
                _max,
            ) in index.association_bucket[association_oid]:
                if related_class_oid != class_definition.tid:
                    role_object: ImdRole = index.index[role_oid]
                    multiplicity = Index.role_multiplicity(role_object)
                    minimum = multiplicity.min or 0
                    maximum = "*" if multiplicity.max is None else multiplicity.max
                    association_attributes.append(
                        Attribute(
                            index=index,
                            oid=role_oid,
                            name=mandatory(role_object.name),
                            type_definition="Ref",
                            mandatory=f"{minimum}...{maximum}"
                            if minimum != maximum
                            else f"{minimum}",
                            language=language,
                        )
                    )

        return cls(
            index=index,
            name=mandatory(class_definition.name),
            oid=mandatory(class_definition.tid),
            inherits_from=class_definition.super.ref if class_definition.super else None,
            attributes=attributes,
            association_attributes=association_attributes,
            language=language,
        )


@dataclass
class Group(Base, ABC):
    """
    Common base of ili:Model and ili:Topic
    """

    classes: list[Class]
    associations: list[Association]

    @staticmethod
    def handle_class(classes: list[Class], element: Any, index: Index, language: str | None):
        classes.append(Class.from_imd(element, index, language))

    @classmethod
    def handle_association(
        cls,
        associations: list[Association],
        association: ImdClass,
        index: Index,
        language: str | None,
    ):
        if index.association_bucket.get(association.tid):
            association_string: Association = []
            for role_tid, class_tid, _strongness, _min, _max in index.association_bucket[
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
            association_string.append(mandatory(association.name))
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
            # Cardinality / Multiplicity '0..*' is not implemented in mermaid directly we
            # deliver empty string
            return "0..*"
        elif minimum is None and maximum is None:
            return "*"
        else:
            return f"{minimum}..{maximum}"

    @staticmethod
    def render_strongness(strongness: str):
        if strongness == "Assoc":
            # TODO: decide if we want to show direction of association with arrows at the end
            # of the connector
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
class TopicGroup(Group):
    """
    Represents an ili:Topic
    """

    @classmethod
    def from_imd(cls, sub_model: ImdSubmodel, index: Index, language: str | None):
        classes: list[Class] = []
        associations: list[Association] = []

        if index.class_in_package.get(sub_model.tid):
            for element_tid in index.class_in_package[sub_model.tid]:
                element = index.index[element_tid]
                cls.handle_class(classes, element, index, language)
        if index.association_in_package.get(sub_model.tid):
            for element_tid in index.association_in_package[sub_model.tid]:
                element = index.index[element_tid]
                cls.handle_association(associations, element, index, language)

        return cls(
            index=index,
            name=mandatory(sub_model.name),
            oid=mandatory(sub_model.tid),
            classes=classes,
            associations=associations,
            language=language,
        )


@dataclass
class ModelGroup(Group):
    """
    Represents an ili:Model
    """

    topic_groups: list[TopicGroup]

    @classmethod
    def from_imd(cls, model: ImdModel, index: Index, language: str | None):
        topics: list[TopicGroup] = []
        classes: list[Class] = []
        associations: list[Association] = []
        if index.submodel_in_package.get(model.tid):
            for element_tid in index.submodel_in_package[model.tid]:
                element = index.index[element_tid]
                cls.handle_topic(topics, element, index, language)
        if index.class_in_package.get(model.tid):
            for element_tid in index.class_in_package[model.tid]:
                element = index.index[element_tid]
                cls.handle_class(classes, element, index, language)
        if index.association_in_package.get(model.tid):
            for element_tid in index.association_in_package[model.tid]:
                element = index.index[element_tid]
                cls.handle_association(associations, element, index, language)
        return cls(
            index=index,
            language=language,
            name=mandatory(model.name),
            oid=mandatory(model.tid),
            topic_groups=topics,
            classes=classes,
            associations=associations,
        )

    @staticmethod
    def handle_topic(
        topics: list[TopicGroup], element: Any, index: Index, language: str | None
    ):
        if isinstance(element, ImdSubmodel):
            topics.append(TopicGroup.from_imd(element, index, language=language))


@dataclass
class Diagram(Base):
    """
    Represents the whole diagram with all nested items
    """

    model_groups: list[ModelGroup]

    def __post_init__(self, index: Index, language: str | None):
        pass

    @classmethod
    def from_imd(cls, index: Index, language: str | None = None):
        models = []
        for model in index.types_bucket["Model"]:
            models.append(ModelGroup.from_imd(model, index, language))
        return cls(
            index=index,
            language=language,
            name=", ".join([model.name for model in models]),
            oid="diagram",
            model_groups=models,
        )
