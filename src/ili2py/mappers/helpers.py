import logging
from dataclasses import dataclass
from typing import Any

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import DataSection
from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10 import (
    AllowedInBasket,
    AttrOrParam,
    AxisSpec,
    BaseClass,
    Class,
    ClassRefType,
    ClassType,
    ConstraintType,
    CoordType,
    CoordTypeType,
    DataUnit,
    DataUnitType,
    Dependency,
    DomainTypeType,
    ExistenceConstraintType,
    ExplicitAssocAccess,
    ExtendableMetype,
    Ili1TransferElement,
    Import,
    LineForm,
    LinesForm,
    LineType,
    LineTypeType,
    MetaAttribute,
    MetaElementType,
    Model,
    MultiValueType,
    ObjectType,
    Role,
    SetConstraintType,
    SimpleConstraintType,
    SubModel,
    TransferElement,
    UniqueConstraintType,
    View,
)


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
        allowed_in_basket_class_in_basket: Key is the class tid, and it has a list of basket tid's which is in.
        allowed_in_basket_of_data_unit: TODO
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
        elements_in_package: Key is the tid of the package (Model, Submodel) and value is a list of tid's of
            elements which are in the package.
        topic_basket: Key is the tid of the package (SubModel) and value is the tid of the corresponding
            basket.
        dependency_using: Key is the
    """

    def __init__(self, data_section: DataSection):
        self.aa_not_touched: list = []
        self.index: dict = {}
        self.imported_p: dict = {}
        self.importing_p: dict = {}
        self.models: list = []

        self.allowed_in_basket_class_in_basket: dict = {}
        self.allowed_in_basket_of_data_unit: dict = {}

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

        self.types_used_by_attributes: dict = {}

        self.class_class_attribute: dict = {}
        self.class_class_parameter: dict = {}
        self.class_association_attribute: dict = {}
        self.class_association_parameter: dict = {}

        self.geometric_attributes: list = []
        self.geometric_attributes_multi: list = []
        self.geometric_attributes_line_form: dict = {}
        self.geometric_attributes_point_like: list = []
        self.geometric_attributes_line_like: list = []
        self.geometric_attributes_polygon_like: list = []

        self.geometric_classes: dict = {}

        self.association_role: dict = {}
        self.association_to_class_ref_attributes: dict = {}
        self.association_as_class_ref_attributes: dict = {}
        self.association_bucket: dict = {}
        self.associated_classes: dict = {}

        self.types_bucket = {}
        self.types_kind_bucket = {}
        self.type_super_classes = {}
        self.type_sub_classes = {}

        self.metaelement_metaattributes: dict = {}

        self.class_in_package: dict = {}
        self.submodel_in_package: dict = {}
        self.association_in_package: dict = {}
        self.elements_in_package: dict = {}
        self.elements_in_package_class_class: dict = {}
        self.elements_in_package_class_structure: dict = {}
        self.elements_in_package_class_association: dict = {}
        self.topic_basket: dict = {}
        self.class_subclassed_by: dict = {}

        self.dependency_depends_on: dict = {}
        self.dependency_used_by: dict = {}

        self.object_oid_in_submodel: dict = {}
        self.object_oid_in_model: dict = {}

        self.basket_oid_in_submodel: dict = {}
        self.basket_oid_in_model: dict = {}

        self.class_with_simple_constraints: dict = {}
        self.class_with_existence_constraints: dict = {}
        self.class_with_unique_constraints: dict = {}
        self.class_with_set_constraints: dict = {}
        self.domain_with_simple_constraints: dict = {}
        self.domain_with_existence_constraints: dict = {}
        self.domain_with_unique_constraints: dict = {}
        self.domain_with_set_constraints: dict = {}

        self.types_in_domain: dict = {}

        self.depth_tree: list = []

        for basket in data_section.ModelData:
            for element in basket.choice:
                self.unwrap_tree(element)
        for basket in data_section.ModelData:
            for element in basket.choice:
                self.prepare_tree(element)

        if self.types_kind_bucket.get("Class.Association"):
            for association_class in self.types_kind_bucket["Class.Association"]:
                self.prepare_association(association_class)

        self.root_model: str = self.models[-1]
        self.depth_tree.append([self.root_model])
        self.assemble_depth_tree(self.root_model, [self.root_model])
        self.associations_embedded

    def assemble_depth_tree(self, model_name: str, visited_models: list):
        selected_models = []
        for importing in self.importing_p[model_name]:
            if importing not in visited_models:
                visited_models.append(importing)
                selected_models.append(importing)
        if len(selected_models) > 0:
            self.depth_tree.append(self.depth_tree[-1] + selected_models)
        for importing in self.importing_p[model_name]:
            self.assemble_depth_tree(importing, visited_models)

    def prepare_tree(self, element: Any):
        self.resolve_references(element)
        self.handle_types(element)

    def _follow_super_ref(self, element: ExtendableMetype, super_references_list: list):
        if element.super is not None:
            reference = element.super.ref
            if reference not in self.type_sub_classes:
                self.type_sub_classes[reference] = []
            self.type_sub_classes[reference].append(element.tid)
            if reference not in super_references_list:
                super_references_list.append(reference)
            self._follow_super_ref(self.index[reference], super_references_list)

    def handle_types(self, element: Any):
        if element.__class__.__name__ not in self.types_bucket:
            self.types_bucket[element.__class__.__name__] = []
        self.types_bucket[element.__class__.__name__].append(element)
        if hasattr(element, "kind"):
            key = f"{element.__class__.__name__}.{element.kind}"
            if key not in self.types_kind_bucket:
                self.types_kind_bucket[key] = []
            self.types_kind_bucket[key].append(element)
        if hasattr(element, "super"):
            if element.super is not None:
                super_references_list = []
                self._follow_super_ref(element, super_references_list)
                if element.tid not in self.type_super_classes:
                    self.type_super_classes[element.tid] = []
                self.type_super_classes[element.tid] += super_references_list

    def resolve_references(self, element: Any):
        """
        Helper method to resolve references between elements.

        IMPORTANT: the order in which the handle_... methods are called is important!!!

        Args:
            element: the element which is looked up and which references will be deconstructed.
        """
        if isinstance(element, MetaElementType):
            # we want to track all basic meta elements
            self.handle_element_in_package(element)
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
            self.handle_geometric(element)
            self.handle_multivalue_type(element)
        elif isinstance(element, MetaAttribute):
            self.handle_metaattribute(element)
        elif isinstance(element, Dependency):
            self.handle_dependency(element)
        elif isinstance(element, Class):
            self.handle_class(element)
        elif isinstance(element, ConstraintType):
            self.handle_constraint(element)
        if isinstance(element, DomainTypeType):
            self.handle_domain_type(element)

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
        of_data_unit_bucket = self.allowed_in_basket_class_in_basket[element.class_in_basket.ref]
        if element.of_data_unit.ref not in of_data_unit_bucket:
            of_data_unit_bucket.append(element.of_data_unit.ref)
        class_in_basket_bucket = self.allowed_in_basket_of_data_unit[element.of_data_unit.ref]
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
                (
                    class_related_type.tid,
                    base_class.tid,
                    class_related_type.strongness,
                    class_related_type.multiplicity.multiplicity.min,
                    class_related_type.multiplicity.multiplicity.max,
                )
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

    def handle_element_in_package(self, element: MetaElementType):
        if element.element_in_package:
            if element.element_in_package.ref not in self.elements_in_package:
                self.elements_in_package[element.element_in_package.ref] = []
            self.elements_in_package[element.element_in_package.ref].append(element.tid)
        if isinstance(element, DataUnitType):
            self.topic_basket[element.element_in_package.ref] = element.tid
            if element.oid:
                package = self.index[element.element_in_package.ref]
                if isinstance(package, SubModel):
                    self.basket_oid_in_submodel[package.tid] = element.tid
                    package = self.index[package.element_in_package.ref]
                self.basket_oid_in_model[package.tid] = element.tid
        if isinstance(element, ClassType):
            if element.kind == "Class":
                if element.element_in_package.ref not in self.elements_in_package_class_class:
                    self.elements_in_package_class_class[element.element_in_package.ref] = []
                self.elements_in_package_class_class[element.element_in_package.ref].append(
                    element.tid
                )
            elif element.kind == "Structure":
                if element.element_in_package.ref not in self.elements_in_package_class_structure:
                    self.elements_in_package_class_structure[element.element_in_package.ref] = []
                self.elements_in_package_class_structure[element.element_in_package.ref].append(
                    element.tid
                )
            elif element.kind == "Association":
                if element.element_in_package.ref not in self.elements_in_package_class_association:
                    self.elements_in_package_class_association[element.element_in_package.ref] = []
                self.elements_in_package_class_association[element.element_in_package.ref].append(
                    element.tid
                )
            else:
                logging.debug(f"Element kind of Class type was not handled correctly: {element}")

    def handle_dependency(self, element: Dependency):
        if element.using.ref not in self.dependency_used_by:
            self.dependency_used_by[element.using.ref] = []
        self.dependency_used_by[element.using.ref].append(element.dependent.ref)
        if element.dependent.ref not in self.dependency_depends_on:
            self.dependency_depends_on[element.dependent.ref] = []
        self.dependency_depends_on[element.dependent.ref].append(element.using.ref)

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
                    self.models.append(element.tid)
                elif isinstance(element, SubModel):
                    if element.element_in_package.ref not in self.submodel_in_package:
                        self.submodel_in_package[element.element_in_package.ref] = []
                    self.submodel_in_package[element.element_in_package.ref].append(element.tid)

                elif isinstance(element, DataUnit):
                    if element.tid not in self.allowed_in_basket_of_data_unit:
                        self.allowed_in_basket_of_data_unit[element.tid] = []

                elif isinstance(element, Class):
                    if element.tid not in self.allowed_in_basket_class_in_basket:
                        self.allowed_in_basket_class_in_basket[element.tid] = []
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
                    if element.tid not in self.allowed_in_basket_class_in_basket:
                        self.allowed_in_basket_class_in_basket[element.tid] = []
                    if element.tid not in self.transfer_class:
                        self.transfer_class[element.tid] = []

                elif isinstance(element, AttrOrParam):
                    if element.type_value:
                        type_definition = self.index[element.type_value.ref]
                        type_ref = type_definition.tid
                        if (
                            isinstance(type_definition, MultiValueType)
                            and type_definition.name == "TYPE"
                        ):
                            type_ref = type_definition.base_type.ref
                        if type_ref not in self.types_used_by_attributes:
                            self.types_used_by_attributes[type_ref] = []
                        self.types_used_by_attributes[type_ref].append(element.tid)
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
            linked = self.class_related_type[member_ref]
            if not isinstance(linked, list):
                linked = [linked]
            for linked_class in linked:
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
            if referenced_class.kind in ["Class", "Structure"]:
                if element.attr_parent.ref not in self.class_class_attribute:
                    self.class_class_attribute[element.attr_parent.ref] = []
                self.class_class_attribute[element.attr_parent.ref].append(element.tid)
            elif referenced_class.kind == "Association":
                if element.attr_parent.ref not in self.class_association_attribute:
                    self.class_association_attribute[element.attr_parent.ref] = []
                self.class_association_attribute[element.attr_parent.ref].append(element.tid)
        elif element.param_parent:
            referenced_class = self.index[element.param_parent.ref]
            if referenced_class.kind in ["Class", "Structure"]:
                if element.param_parent.ref not in self.class_class_attribute:
                    self.class_class_attribute[element.param_parent.ref] = []
                self.class_class_attribute[element.param_parent.ref].append(element.tid)
            elif referenced_class.kind == "Association":
                if element.param_parent.ref not in self.class_association_attribute:
                    self.class_association_attribute[element.param_parent.ref] = []
                self.class_association_attribute[element.param_parent.ref].append(element.tid)

    def handle_class(self, element: Class):
        if element.oid:
            if element.element_in_package:
                package = self.index[element.element_in_package.ref]
                if isinstance(package, SubModel):
                    self.object_oid_in_submodel[package.tid] = element.oid.ref
                    package = self.index[package.element_in_package.ref]
                self.object_oid_in_model[package.tid] = element.oid.ref
        if element.super:
            if element.super.ref not in self.class_subclassed_by:
                self.class_subclassed_by[element.super.ref] = []
            self.class_subclassed_by[element.super.ref].append(element.tid)

    def handle_constraint(self, element: ConstraintType):
        if isinstance(element, SimpleConstraintType):
            if element.to_class:
                if element.to_class.ref not in self.class_with_simple_constraints:
                    self.class_with_simple_constraints[element.to_class.ref] = []
                self.class_with_simple_constraints[element.to_class.ref].append(element.tid)
            if element.to_domain:
                if element.to_domain.ref not in self.domain_with_simple_constraints:
                    self.domain_with_simple_constraints[element.to_domain.ref] = []
                self.domain_with_simple_constraints[element.to_domain.ref].append(element.tid)
        elif isinstance(element, ExistenceConstraintType):
            if element.to_class:
                if element.to_class.ref not in self.class_with_existence_constraints:
                    self.class_with_existence_constraints[element.to_class.ref] = []
                self.class_with_existence_constraints[element.to_class.ref].append(element.tid)
            if element.to_domain:
                if element.to_domain.ref not in self.domain_with_existence_constraints:
                    self.domain_with_existence_constraints[element.to_domain.ref] = []
                self.domain_with_existence_constraints[element.to_domain.ref].append(element.tid)
        elif isinstance(element, UniqueConstraintType):
            if element.to_class:
                if element.to_class.ref not in self.class_with_unique_constraints:
                    self.class_with_unique_constraints[element.to_class.ref] = []
                self.class_with_unique_constraints[element.to_class.ref].append(element.tid)
            if element.to_domain:
                if element.to_domain.ref not in self.domain_with_unique_constraints:
                    self.domain_with_unique_constraints[element.to_domain.ref] = []
                self.domain_with_unique_constraints[element.to_domain.ref].append(element.tid)
        elif isinstance(element, SetConstraintType):
            if element.to_class:
                if element.to_class.ref not in self.class_with_set_constraints:
                    self.class_with_set_constraints[element.to_class.ref] = []
                self.class_with_set_constraints[element.to_class.ref].append(element.tid)
            if element.to_domain:
                if element.to_domain.ref not in self.domain_with_set_constraints:
                    self.domain_with_set_constraints[element.to_domain.ref] = []
                self.domain_with_set_constraints[element.to_domain.ref].append(element.tid)
        else:
            logging.warning(f"Constraint was not handled as expected: {element}")

    def handle_domain_type(self, element: DomainTypeType):
        if element.name not in ["TYPE", "C1", "C2", "C3"]:
            if element.element_in_package:
                if element.element_in_package.ref not in self.types_in_domain:
                    self.types_in_domain[element.element_in_package.ref] = []
                self.types_in_domain[element.element_in_package.ref].append(element)

    def handle_geometric(
        self,
        element: AttrOrParam,
        origin_type: CoordType | LineType | None = None,
        multi: bool = False,
    ):
        if origin_type:
            type_definition = origin_type
        else:
            type_definition = self.index[element.type_value.ref]
        if isinstance(type_definition, CoordType) or isinstance(type_definition, LineType):
            if origin_type:
                inner_multi = multi
            else:
                inner_multi = type_definition.multi
            if element.tid not in self.geometric_attributes:
                self.geometric_attributes.append(element.tid)
            if inner_multi and element.tid not in self.geometric_attributes_multi:
                self.geometric_attributes_multi.append(element.tid)
            if isinstance(type_definition, CoordTypeType):
                if element.tid not in self.geometric_attributes_point_like:
                    self.geometric_attributes_point_like.append(element.tid)
            elif isinstance(type_definition, LineTypeType) and type_definition.kind in [
                "Polyline",
                "DirectedPolyline",
            ]:
                if element.tid not in self.geometric_attributes_line_like:
                    self.geometric_attributes_line_like.append(element.tid)
            elif isinstance(type_definition, LineTypeType) and type_definition.kind in [
                "Surface",
                "Area",
            ]:
                if element.tid not in self.geometric_attributes_polygon_like:
                    self.geometric_attributes_polygon_like.append(element.tid)
            else:
                logging.debug(f"Unexpected geometric type {type_definition}")
            class_definition: Class = self.index[element.attr_parent.ref]
            if class_definition.tid not in self.geometric_classes:
                self.geometric_classes[class_definition.tid] = []
            self.geometric_classes[class_definition.tid].append(element.tid)
            # adding attribute info level to index
            if isinstance(type_definition, LineType):
                if element.tid not in self.geometric_attributes_line_form:
                    self.geometric_attributes_line_form[element.tid] = self.line_type[
                        type_definition.tid
                    ]
            for attribute_oid in self.types_used_by_attributes.get(class_definition.tid, []):
                # the geometric class was used as a type for another class attribute
                structure_attribute = self.index[attribute_oid]
                structure_attribute_type = self.index[structure_attribute.type_value.ref]
                multi = inner_multi
                if structure_attribute_type.multiplicity:
                    if (
                        structure_attribute_type.multiplicity.multiplicity.max is None
                        or structure_attribute_type.multiplicity.multiplicity.max > 1
                    ):
                        multi = True
                self.handle_geometric(structure_attribute, type_definition, multi)

    def handle_multivalue_type(self, element: AttrOrParam):
        pass

    @property
    def association_classes(self) -> dict:
        """
        Delivers all associations which represent own classes as defined in the reference manual of INTERLIS.

        Returns:
            A dictionary where the key is the association oid and the value is a list of tuples
            defining the attributes of the association and its roles.
        """
        association_classes: dict = {}
        for association_oid in self.association_bucket:
            association_object = self.index[association_oid]
            role_definitions = self.association_bucket[association_oid]
            maxes = []
            logging.debug(f"Deciding if association is own class {association_object}")
            for role_oid, referenced_class_oid, strongness, min, max in role_definitions:
                if max is None or max > 1:
                    maxes.append(referenced_class_oid)
            if len(role_definitions) > 2:
                association_classes[association_oid] = role_definitions
                logging.debug("    Association has > 2 roles => own class")
            elif len(maxes) == len(role_definitions):
                association_classes[association_oid] = role_definitions
                logging.debug("    Multiplicities are > 1 for all roles => own class")
            elif len(maxes) == 1:
                class_object = self.index[maxes[0]]
                if class_object.element_in_package.ref != association_object.element_in_package.ref:
                    association_classes[association_oid] = role_definitions
                    logging.debug(
                        f"    One roles multiplicity is > 1 but cant be embedded because target class {class_object} is in an other topic than the base association {association_object} => own class"
                    )
            elif len(maxes) == 0:
                logging.debug("    Multiplicities are <= 1 for all roles")
                class_object2 = self.index[role_definitions[1][1]]
                class_object1 = self.index[role_definitions[0][1]]
                if (
                    class_object2.element_in_package.ref
                    != association_object.element_in_package.ref
                    != class_object1.element_in_package.ref
                ):
                    logging.debug(
                        f"        Both target classes {class_object2} {class_object1} are in different topic than base association {association_object} => own class"
                    )
            elif hasattr(association_object, "oid") and association_object.oid is not None:
                association_classes[association_oid] = role_definitions
                logging.debug("    Association has OID => own class")
            elif len(self.class_subclassed_by.get(association_object.tid, [])) > 0:
                association_classes[association_oid] = role_definitions
                logging.debug(
                    f"    Associaction has Subclasses, we construct a class for validity reason "
                    f"(Dataclasses) {association_object} => own class"
                )
        return association_classes

    @property
    def associations_embedded(self):
        associations_embedded: dict = {}
        association_classes = self.association_classes
        for association_oid in self.association_bucket:
            association_object = self.index[association_oid]
            logging.debug(f"Deciding if association gets embedded {association_object}")
            role_definitions = self.association_bucket[association_oid]
            if association_oid not in association_classes:
                if len(role_definitions) == 2:
                    # we check only the associations which are not already clearly own classes
                    # and regarding reference manual only associations with 2 members are candidates
                    # to be embedded.
                    logging.debug(
                        "   Association has 2 Role definitions, checking how to embedd..."
                    )
                    maxes = []
                    roles = {}
                    for role_definition in role_definitions:
                        multiplicity_max = role_definition[-1]
                        if multiplicity_max is None or multiplicity_max > 1:
                            maxes.append(role_definition)
                        roles[role_definition[0]] = role_definition
                    if len(maxes) == 1:
                        if maxes[0][1] not in associations_embedded:
                            associations_embedded[maxes[0][1]] = []
                        associations_embedded[maxes[0][1]].append(self.switch(roles, maxes[0][0]))
                        logging.debug(
                            "   Embedding at target class vice versa the multiplicity > 1"
                        )
                    elif len(maxes) == 0:
                        class_object2 = self.index[role_definitions[1][1]]
                        class_object1 = self.index[role_definitions[0][1]]
                        if (
                            class_object2.element_in_package.ref
                            == association_object.element_in_package.ref
                        ):
                            if class_object2.tid not in associations_embedded:
                                associations_embedded[class_object2.tid] = []
                            associations_embedded[class_object2.tid].append(role_definitions[0])
                            logging.debug(
                                "   Embedding at target class 2 vice versa the multiplicity <= 1"
                            )
                        elif (
                            class_object1.element_in_package.ref
                            == association_object.element_in_package.ref
                        ):
                            if class_object1.tid not in associations_embedded:
                                associations_embedded[class_object1.tid] = []
                            associations_embedded[class_object1.tid].append(role_definitions[1])
                            logging.debug(
                                "   Embedding at target class 1 vice versa the multiplicity <= 1"
                            )
                else:
                    self.aa_not_touched.append(association_oid)

        return associations_embedded

    def switch(self, d, key):
        # Dict hat genau 2 Keys
        k1, k2 = d.keys()
        return d[k2] if key == k1 else d[k1]
