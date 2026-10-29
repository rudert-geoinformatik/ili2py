import logging

from ili2py.mappers.helpers import Index, TranslatedModel
from ili2py.writers.py.python_structure import (
    Attribute,
    Base,
    Choice,
    Class,
    Enumeration,
    Library,
    Module,
    Package,
)

HOP_PREFIX = "ili2py."


class TransferNames:
    """
    Changes the transfer names of the elements of translated models in a library which was
    built from the original model (see `Library.from_imd`). This is only needed for
    INTERLIS 2.3, where the tags of a translated model are in the translated language
    (ili2-refman_2006-04-13_d.pdf, 3.3.3). In INTERLIS 2.4 they stay in the original language.

    What basically happens here is a overhaul of the complete python class structure
    applying the translated names on the base names and taking the basenames as translations.
    Might be no correct interlis wise, but we need parser classes and it works this wy well.

    Per element it changes:
        - the tag (classes, topics, basket choices, attributes)
        - the enumeration values
        - the translations, the original name goes in under the language of the original
          model and the translated language goes out

    Python names, identifiers (oid), reference targets and constraint paths stay the ones of
    the original model, they are ili2py internal.

    Attributes:
        index: The index of the IMD.
        models: Key is the tid of the original model, value is the translation which is used
            for the transfer names.
    """

    def __init__(self, index: Index):
        self.index = index
        self.models: dict[str, TranslatedModel] = {}
        for original, translations in index.translated_models.items():
            if len(translations) == 1:
                self.models[original] = translations[0]
            else:
                # the IMD does not tell which one is used in the transfer
                logging.warning(
                    f"{original} has translations in "
                    f"{', '.join(translation.language for translation in translations)}, "
                    "the transfer names stay the original ones"
                )

    def translation(self, tid: str) -> TranslatedModel | None:
        """
        Looks up the translation of the model an element belongs to.

        Args:
            tid: The tid of the element (its qualified name in the original model).

        Returns:
            The translated model or None if the model of the element is not translated.
        """
        return self.models.get(tid.split(Base.OID_SEPARATOR)[0])

    def path(self, tid: str) -> str | None:
        """
        Translates the qualified name of an element, that is its tag.

        Args:
            tid: The tid of the element.

        Returns:
            The translated qualified name or None if the model is not translated.
        """
        translated_model = self.translation(tid)
        if translated_model is None:
            return None
        return self.index.translated_path(tid, translated_model.language)

    def name(self, tid: str) -> str | None:
        """
        Translates the name of an element.

        Args:
            tid: The tid of the element.

        Returns:
            The translated name or None if there is no translation.
        """
        translated_model = self.translation(tid)
        if translated_model is None:
            return None
        return self.index.translated_name(tid, translated_model.language)

    def switch(self, translations: dict[str, str], tid: str, name: str) -> dict[str, str]:
        """
        Switches the translations of an element to the view of the translated model.

        Args:
            translations: The translations of the element in the original model.
            tid: The tid of the element.
            name: The name of the element in the original model.

        Returns:
            The translations, e.g. {'de': 'Ausgangslage'} instead of
            {'fr': 'Donnees_de_base'}. Unchanged if the model is not translated.
        """
        translated_model = self.translation(tid)
        if translated_model is None:
            return translations
        switched = {
            language: translated_name
            for language, translated_name in translations.items()
            if language != translated_model.language
        }
        if translated_model.original_language:
            switched[translated_model.original_language] = name
        else:
            logging.warning(
                f"{translated_model.original} has no language, the original name of {tid} "
                "is not added to the translations"
            )
        return switched

    def element(self, element: Base):
        element.tag = self.path(element.identifier) or element.tag
        element.translations = self.switch(
            element.translations,
            element.identifier,
            element.identifier.split(Base.OID_SEPARATOR)[-1],
        )

    def choice(self, choice: Choice):
        choice.tag = self.path(choice.identifier) or choice.tag
        choice.translations = self.switch(
            choice.translations,
            choice.identifier,
            choice.identifier.split(Base.OID_SEPARATOR)[-1],
        )

    def constraints(self, constraints: list[dict]):
        for constraint in constraints:
            constraint["translations"] = self.switch(
                constraint.get("translations", {}), constraint["id"], constraint["name"]
            )

    def enumeration(self, enumeration: Enumeration):
        self.element(enumeration)
        translated_model = self.translation(enumeration.identifier)
        if translated_model is None:
            return
        for value in enumeration.values:
            value_translations = enumeration.value_translations.get(value, {})
            if translated_model.language in value_translations:
                enumeration.value_tags[value] = value_translations[translated_model.language]
            enumeration.value_translations[value] = self.switch(
                value_translations, enumeration.identifier, value
            )

    def attribute(self, attribute: Attribute):
        if attribute.identifier.startswith(HOP_PREFIX):
            # attributes inserted by ili2py, only the one of a structure is tagged with the
            # qualified name of the structure (Attribute.default_tag)
            if attribute.type_restrictions.get("type_related_type"):
                attribute.tag = (
                    self.path(attribute.identifier.removeprefix(HOP_PREFIX)) or attribute.tag
                )
        else:
            attribute.tag = self.name(attribute.identifier) or attribute.tag
            attribute.translations = self.switch(
                attribute.translations, attribute.identifier, attribute.name
            )
        if attribute.enumeration:
            self.enumeration(attribute.enumeration)
        if attribute.line_type:
            self.element(attribute.line_type)
        if attribute.type_related_type_class:
            self.class_definition(attribute.type_related_type_class)

    def class_definition(self, class_definition: Class):
        self.element(class_definition)
        for attribute in class_definition.attributes:
            self.attribute(attribute)
        for enumeration in class_definition.enumerations:
            self.enumeration(enumeration)
        self.constraints(class_definition.existence_constraints)
        self.constraints(class_definition.set_constraints)
        self.constraints(class_definition.simple_constraints)
        self.constraints(class_definition.unique_constraints)

    def module(self, module: Module):
        self.element(module)
        for class_definition in module.classes:
            self.class_definition(class_definition)
        for enumeration in module.enumerations:
            self.enumeration(enumeration)
        for coord_type in module.coord_types:
            self.element(coord_type)
        for line_type in module.line_types:
            self.element(line_type)
        for definition in module.type_definitions:
            definition["translations"] = self.switch(
                definition["translations"], definition["oid"], definition["name"]
            )
            for kind in (
                "existence_constraints",
                "set_constraints",
                "simple_constraints",
                "unique_constraints",
            ):
                self.constraints(definition.get(kind, []))
        if module.basket:
            for choice in module.basket.choices:
                self.choice(choice)

    def package(self, package: Package):
        self.module(package)
        for module in package.modules:
            self.module(module)

    def library(self, library: Library):
        for package in library.packages:
            self.package(package)
        for choice in library.topic_choices:
            self.choice(choice)


def translate_transfer_names(library: Library, index: Index):
    """
    Changes the transfer names of the translated models in the library to the ones of the
    INTERLIS 2.3 transfer, see `TransferNames`. The library is changed in place.

    Args:
        library: The library built from the original models.
        index: The index of the IMD.
    """
    TransferNames(index).library(library)
