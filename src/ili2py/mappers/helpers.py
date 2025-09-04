import logging
from dataclasses import dataclass
from typing import Any

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    AllowedInBasket,
    AttrOrParam,
    AxisSpec,
    BaseClass,
    Class,
    ClassRefType,
    CoordType,
    DataUnit,
    ExplicitAssocAccess,
    Ili1TransferElement,
    Import,
    LineForm,
    LinesForm,
    LineType,
    Model,
    NumType,
    ObjectType,
    Role,
    TransferElement,
    View,
    MetaAttribute,
    SubModel,
)
from ili2py.interfaces.interlis.interlis_24.ilismeta16 import DataSection


@dataclass
class Reference:
    model: str
    type: type[Any]
    instance: Any


class Index:
    """
    Attributes:
        index: The index of all elements which have a TID. The TID is the key.
        imported_p: Which Package is imported by what packages. The key of the dict is the package tid
            which has a list of tid's of packages which are importing it. IMPORTANT: Explicit imports only!
        importing_p: The other direction as imported_p. Key is the package tid which has a list of package
            tid's it is exporting. IMPORTANT: Explicit imports only!
        class_in_basket: Key is the class tid, and it has a list of basket tid's which is in.
        of_data_unit: TODO
        transfer_class: A representation of the Class construct out of the imd which is specifically for
            parsing transfer data more easily. The key is the class tid and it has a list of tuple containing
            the order number of the attribute and the tid to the linked attribute.
        transfer_element: The other direction as transfer_class. The key is the attribute and the value is the
            element it is referenced to AttrOrParam OR ExplicitAssocAccess OR Role
        ili1_transfer_class: TODO
        ili1_ref_attr: TODO
        base_class: TODO
        class_related_type: TODO
        coord_type: Key is the tid of the CoordType, value is a list of tid's to the linked coordinates
            (NumType).
        axis: The opposite direction of coord_type. The key is the tid of the axis related NumType and the
            value is the CoordType the element belongs to.
        line_type: The key is the tid of the LineType value is a list of tid's to the LineForm elements.
        line_form: The opposite direction of line_type. Key is the tid of the LineForm and value is the list
            of tid's of LineTypes which are of this LineForm.
        class_class_attribute: The key is the tid of Class of Kind Class and value is a list of tid's to the
            AttrOrParam which has attr_parent defined.
        class_class_parameter: The key is the tid of Class of Kind Class and value is a list of tid's to the
            AttrOrParam which has param_parent defined.
        class_association_attribute: The key is the tid of Class of Kind Association and value is a list of
            tid's to the AttrOrParam which has attr_parent defined.
        class_association_parameter: The key is the tid of Class of Kind Association and value is a list of
            tid's to the AttrOrParam which has param_parent defined.
        association_role: Key is the tid of the Role and value is a list of tid's to the Class of kind
            Association belonging to the Role.
        association_to_class_ref_attributes: Key is the tid of Class of kind Class and value is a list of
            tuple which contain the tid to the Role and the tid to the related Class kind Class. This is the
            the embedded reference, where the actual class might get additional attributes by the association
            definition. It explicitly is only used when association is one or zero on the side of the class in
            question.
        element_in_package: Key is the tid of the package (Model, Submodel) and value is a list of tid's of
            elements which are in the package.
    """

    def __init__(self, data_section: DataSection):
        self.index: dict = {}

        self.imported_p: dict = {}
        self.importing_p: dict = {}

        self.class_in_basket: dict = {}
        self.of_data_unit: dict = {}

        self.transfer_class: dict = {}
        self.transfer_element: dict = {}

        self.ili1_transfer_class: dict = {}
        self.ili1_ref_attr: dict = {}

        self.base_class: dict = {}
        self.class_related_type: dict = {}

        self.coord_type: dict = {}
        self.axis: dict = {}

        self.line_type: dict = {}
        self.line_form: dict = {}

        self.class_class_attribute: dict = {}
        self.class_class_parameter: dict = {}
        self.class_association_attribute: dict = {}
        self.class_association_parameter: dict = {}

        self.association_role: dict = {}
        self.association_to_class_ref_attributes: dict = {}
        self.association_as_class_ref_attributes: dict = {}
        self.association_bucket: dict = {}
        self.associated_classes: dict = {}

        self.types_bucket = {}

        self.types_specialized_bucket = {}

        self.metaelement_metaattributes: dict = {}

        self.class_in_package: dict = {}
        self.submodel_in_package: dict = {}
        self.association_in_package: dict = {}

        for basket in data_section.ModelData:
            for element in basket.choice:
                self.unwrap_tree(element)
        for basket in data_section.ModelData:
            for element in basket.choice:
                self.prepare_tree(element)

        if self.types_specialized_bucket.get("Class.Association"):
            for association_class in self.types_specialized_bucket["Class.Association"]:
                self.prepare_association(association_class)

    def prepare_tree(self, element: Any):
        self.resolve_references(element)
        self.handle_types(element)

    def handle_types(self, element: Any):
        if element.__class__.__name__ not in self.types_bucket:
            self.types_bucket[element.__class__.__name__] = []
        self.types_bucket[element.__class__.__name__].append(element)
        if hasattr(element, "kind"):
            key = f"{element.__class__.__name__}.{element.kind}"
            if key not in self.types_specialized_bucket:
                self.types_specialized_bucket[key] = []
            self.types_specialized_bucket[key].append(element)

    def resolve_references(self, element: Any):
        """
        Helper method to resolve references between elements.

        IMPORTANT: the order in which the handle_... methods are called is important!!!

        Args:
            element: the element which is looked up and which references will be deconstructed.
        """
        if isinstance(element, Import):
            self.handle_import(element)
        elif isinstance(element, AllowedInBasket):
            self.handle_allowed_in_basket(element)
        elif isinstance(element, TransferElement):
            self.handle_transfer_element(element)
        elif isinstance(element, Ili1TransferElement):
            self.handle_ili1_transfer_element(element)
        elif isinstance(element, BaseClass):
            self.handle_base_class(element)
        elif isinstance(element, AxisSpec):
            self.handle_axis_spec(element)
        elif isinstance(element, LinesForm):
            self.handle_lines_form(element)
        elif isinstance(element, Role):
            self.handle_role(element)
        elif isinstance(element, AttrOrParam):
            self.handle_attr_or_param(element)
        elif isinstance(element, MetaAttribute):
            self.handle_metaattribute(element)

    def handle_import(self, element: Import):
        """
        Resolves the Import references between Models.
        Args:
            element: The import reference which will be handled.
        """
        imported_p_bucket = self.imported_p[element.imported_p.ref]
        if element.imported_p.ref not in imported_p_bucket:
            imported_p_bucket.append(element.importing_p.ref)
        importing_p_bucket = self.importing_p[element.importing_p.ref]
        if element.importing_p.ref not in importing_p_bucket:
            importing_p_bucket.append(element.imported_p.ref)

    def handle_allowed_in_basket(self, element: AllowedInBasket):
        """

        Args:
            element: The allowed-in-basket reference which will be handled.
        """
        of_data_unit_bucket = self.class_in_basket[element.class_in_basket.ref]
        if element.of_data_unit.ref not in of_data_unit_bucket:
            of_data_unit_bucket.append(element.of_data_unit.ref)
        class_in_basket_bucket = self.of_data_unit[element.of_data_unit.ref]
        if element.class_in_basket.ref not in class_in_basket_bucket:
            class_in_basket_bucket.append(element.class_in_basket.ref)

    def handle_transfer_element(self, element: TransferElement):
        transfer_class_bucket = self.transfer_class[element.transfer_class.ref]
        self.transfer_element[element.transfer_element.ref] = element.transfer_class.ref
        if element.transfer_element.ref not in transfer_class_bucket:
            transfer_class_bucket.append(
                (element.transfer_element.order_pos, element.transfer_element.ref)
            )

    def handle_ili1_transfer_element(self, element: Ili1TransferElement):
        ili1_transfer_class_bucket = self.ili1_transfer_class[element.ili1_transfer_class.ref]
        ili1_ref_bucket = self.ili1_ref_attr[element.ili1_ref_attr.ref]
        if element.ili1_transfer_class.ref not in ili1_ref_bucket:
            ili1_ref_bucket.append(element.ili1_transfer_class.ref)
        if element.ili1_ref_attr.ref not in ili1_transfer_class_bucket:
            ili1_transfer_class_bucket.append(element.ili1_ref_attr.ref)

    def handle_base_class(self, element: BaseClass):
        base_class_bucket = self.base_class[element.base_class.ref]
        self.class_related_type[element.crt.ref] = element.base_class.ref
        if element.crt.ref not in base_class_bucket:
            base_class_bucket.append(element.crt.ref)

        # handle association unwrapping
        base_class = self.index[element.base_class.ref]
        class_related_type = self.index[element.crt.ref]
        if isinstance(base_class, Class) and isinstance(class_related_type, Role):
            # this is an association part
            association = self.index[class_related_type.association.ref]
            if association.tid not in self.association_bucket:
                self.association_bucket[association.tid] = []
            self.association_bucket[association.tid].append(
                (class_related_type.tid, base_class.tid)
            )
            if base_class.tid not in self.associated_classes:
                self.associated_classes[base_class.tid] = []
            self.associated_classes[base_class.tid].append(association.tid)

    def handle_axis_spec(self, element: AxisSpec):
        coord_type_bucket = self.coord_type[element.coord_type.ref]
        self.axis[element.axis.ref] = element.coord_type.ref
        if element.axis.ref not in coord_type_bucket:
            coord_type_bucket.append(element.axis.ref)

    def handle_lines_form(self, element: LinesForm):
        line_form_bucket = self.line_form[element.line_form.ref]
        line_type_bucket = self.line_type[element.line_type.ref]
        if element.line_form.ref not in line_type_bucket:
            line_type_bucket.append(element.line_form.ref)
        if element.line_type.ref not in line_form_bucket:
            line_form_bucket.append(element.line_type.ref)

    def handle_role(self, element: Role):
        if element.association.ref not in self.association_role:
            self.association_role[element.association.ref] = []
        self.association_role[element.association.ref].append(element.tid)

    def handle_metaattribute(self, element: MetaAttribute):
        if element.meta_element.ref not in self.metaelement_metaattributes:
            self.metaelement_metaattributes[element.meta_element.ref] = []
        self.metaelement_metaattributes[element.meta_element.ref].append(element.tid)
        logging.debug(
            f"Element type is {type(self.index[element.meta_element.ref])} and has a MetaAttribute"
        )

    def unwrap_tree(self, element: Any):
        """
        Helper method to assemble a one dimensional index with the elements unique
        identifiers *tid* as the key.

        Args:
            element: The object to inspect for flattening.
        """
        if hasattr(element, "tid"):
            if element.tid is None:
                # element had no tid
                logging.debug(f"Element {element} had no tid and is not added to the index.")
            else:
                # tid is not None
                # the element has already a unique identifier. we can use this in the index
                if element.tid in self.index:
                    raise LookupError(
                        f"Element {element.tid} was already in tree. "
                        f"Thats not allowed! {element} {self.index[element.tid]}"
                    )
                else:
                    self.index[element.tid] = element
                if isinstance(element, Model):
                    if element.tid not in self.imported_p:
                        self.imported_p[element.tid] = []
                    if element.tid not in self.importing_p:
                        self.importing_p[element.tid] = []
                elif isinstance(element, SubModel):
                    if element.element_in_package.ref not in self.submodel_in_package:
                        self.submodel_in_package[element.element_in_package.ref] = []
                    self.submodel_in_package[element.element_in_package.ref].append(element.tid)

                elif isinstance(element, DataUnit):
                    if element.tid not in self.of_data_unit:
                        self.of_data_unit[element.tid] = []

                elif isinstance(element, Class):
                    if element.tid not in self.class_in_basket:
                        self.class_in_basket[element.tid] = []
                    if element.tid not in self.transfer_class:
                        self.transfer_class[element.tid] = []
                    if element.tid not in self.ili1_transfer_class:
                        self.ili1_transfer_class[element.tid] = []
                    if element.tid not in self.base_class:
                        self.base_class[element.tid] = []
                    if element.kind == "Class":
                        if element.element_in_package.ref not in self.class_in_package:
                            self.class_in_package[element.element_in_package.ref] = []
                        self.class_in_package[element.element_in_package.ref].append(element.tid)
                    if element.kind == "Association":
                        if element.element_in_package.ref not in self.association_in_package:
                            self.association_in_package[element.element_in_package.ref] = []
                        self.association_in_package[element.element_in_package.ref].append(
                            element.tid
                        )

                elif isinstance(element, View):
                    if element.tid not in self.class_in_basket:
                        self.class_in_basket[element.tid] = []
                    if element.tid not in self.transfer_class:
                        self.transfer_class[element.tid] = []

                elif isinstance(element, AttrOrParam):
                    if element.tid not in self.transfer_element:
                        self.transfer_element[element.tid] = None
                    if element.tid not in self.ili1_ref_attr:
                        self.ili1_ref_attr[element.tid] = []

                elif isinstance(element, ExplicitAssocAccess):
                    if element.tid not in self.transfer_element:
                        self.transfer_element[element.tid] = None

                elif isinstance(element, Role):
                    if element.tid not in self.transfer_element:
                        self.transfer_element[element.tid] = None
                    if element.tid not in self.ili1_ref_attr:
                        self.ili1_ref_attr[element.tid] = []
                    if element.tid not in self.class_related_type:
                        self.class_related_type[element.tid] = None

                elif isinstance(element, ClassRefType):
                    if element.tid not in self.class_related_type:
                        self.class_related_type[element.tid] = None

                elif isinstance(element, ObjectType):
                    if element.tid not in self.class_related_type:
                        self.class_related_type[element.tid] = None

                elif isinstance(element, CoordType):
                    if element.tid not in self.coord_type:
                        self.coord_type[element.tid] = []

                elif isinstance(element, LineType):
                    if element.tid not in self.line_type:
                        self.line_type[element.tid] = []

                elif isinstance(element, LineForm):
                    if element.tid not in self.line_form:
                        self.line_form[element.tid] = []

    def prepare_association(self, association_class: Class):
        """
        The following preassumptions were made:
            - 1:n is installed as class attribute to the referenced class with the 1 side, a backref attribute
              is installed at the referenced class as a list, if the association itself has no attributes itself
            - m:n is created as extra class with the attributes and references to the tid's of the
              corresponding objects, same approach is implemented for any associaton which has additional
              attributes itself
            - QUESTION: what happens, if association has super class?
        Args:
            association_class ():

        Returns:

        """

        if self.association_role.get(association_class.tid):
            # we have associated classes in this association
            association_members = self.association_role[association_class.tid]
        else:
            # association does not have associated classes
            # this is the case when association is just a subclass of another one
            # TODO: currently we step only one level deep here, this has to be recursively deep!
            if association_class.super:
                association_members = self.association_role[association_class.super.ref]
            else:
                association_members = []
        from_class = None
        attributes = []
        for member_ref in association_members:
            # handling of embedded associations
            role: Role = self.index[member_ref]
            for linked_class in self.class_related_type[member_ref]:
                # multiple classes can be linked with additional logical operator
                # (currently OR is what is implemented according to ref manual)
                if (
                    role.multiplicity.multiplicity.min in [0, 1]
                    and role.multiplicity.multiplicity.max == 1
                ):
                    # regarding ref manual direct embedded class attributes are only existing
                    # on exactly 1 or 0 related association targets - all others are modeled as
                    # own class like entities in the transfer data
                    attributes.append((role.tid, linked_class))
                else:
                    from_class = linked_class
        if from_class not in self.association_to_class_ref_attributes:
            self.association_to_class_ref_attributes[from_class] = attributes
        else:
            self.association_to_class_ref_attributes[from_class] = (
                self.association_to_class_ref_attributes[from_class] + attributes
            )

    def handle_attr_or_param(self, element: AttrOrParam):
        if element.attr_parent:
            referenced_class = self.index[element.attr_parent.ref]
            if referenced_class.kind == "Class":
                if element.attr_parent.ref not in self.class_class_attribute:
                    self.class_class_attribute[element.attr_parent.ref] = []
                self.class_class_attribute[element.attr_parent.ref].append(element.tid)
            elif referenced_class.kind == "Association":
                if element.attr_parent.ref not in self.class_association_attribute:
                    self.class_association_attribute[element.attr_parent.ref] = []
                self.class_association_attribute[element.attr_parent.ref].append(element.tid)
        elif element.param_parent:
            referenced_class = self.index[element.param_parent.ref]
            if referenced_class.kind == "Class":
                if element.param_parent.ref not in self.class_class_attribute:
                    self.class_class_attribute[element.param_parent.ref] = []
                self.class_class_attribute[element.param_parent.ref].append(element.tid)
            elif referenced_class.kind == "Association":
                if element.param_parent.ref not in self.class_association_attribute:
                    self.class_association_attribute[element.param_parent.ref] = []
                self.class_association_attribute[element.param_parent.ref].append(element.tid)
