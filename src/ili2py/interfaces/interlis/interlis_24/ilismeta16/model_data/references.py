import logging
from dataclasses import dataclass, field

from ili2py.interfaces.interlis.interlis_24.ilismeta16.shared import imd_namespace_map

log = logging.getLogger(__name__)

@dataclass
class Ref:

    ref: str = field(
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["ili"]
        }
    )


@dataclass
class OrderedRef(Ref):
    order_pos: str = field(
        metadata={
            "type": "Attribute",
            "namespace": imd_namespace_map["ili"]
        }
    )


class HasRef:
    """
    Abstract base class which is used to implement decent behaviour on desired subclasses.
    """
    def resolve_refs(self, index: dict):
        """
        References the actual object based on the unique identifier in the index. It is based currently
        on a naming pattern. The attribute to be referenced has to be of type `Ref` and its name has to
        end with *_ref*. Lets assume the attribute name is *Type_ref*. This method then installs a new
        runtime attribute *Type* at `self`. In addition it installs a new runtime attribute at the referenced
        object in our example that would be *Type_backref*. If this attribute does not exists already.
        This is currently always a list which is filled with the back referenced objects.

        TODO: handle multilevel references (currently we go only one level deep)
        TODO: handle multiplicity m:n, 1:1, 1:n, etc

        Args:
            index: The index containing all potential referencable objects.
        """
        for attribute_name in self.__dir__():
            if isinstance(getattr(self, attribute_name), Ref):
                reference = getattr(self, attribute_name).ref
                if not index.get(reference, False):
                    log.info(f'Element with tid <{reference}> was not found in index. It is highly possible that it is not implemented yet')
                else:
                    referenced_element = index[reference]
                    new_attribute_name = attribute_name.replace('_ref', '')
                    setattr(self, new_attribute_name, referenced_element)
                    backref_name = f'{new_attribute_name}_backref'
                    if not hasattr(referenced_element, backref_name):
                        setattr(referenced_element, backref_name, [])
                    getattr(referenced_element, backref_name).append(self)
