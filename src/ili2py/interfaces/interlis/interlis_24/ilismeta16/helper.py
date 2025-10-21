from uuid import uuid4

from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer
from ili2py.interfaces.interlis.interlis_24.ilismeta16.model_data.references import HasRef


def unwrap_tree(element: object, index: dict):
    """
    A little helper method to assemble a one dimensional index with the elements unique
    identifiers *tid* as the key.

    Args:
        index: the dictionary which should be filled with the elements.
    """
    if hasattr(element, "__annotations__"):
        if hasattr(element, "tid"):
            # the element has already a unique identifier. we can use this in the index
            if element.tid in index:
                raise LookupError(f"Element {element.tid} was already in tree. Thats not allowed!")
        else:
            # the element does not have a unique idendtifier (usually relations) we will set up a runtime
            # one to make linking possible
            setattr(element, "tid", f"{element.__class__.__name__}.{str(uuid4())}")
        index[element.tid] = element
        for attribute in element.__annotations__:
            member = element.__getattribute__(attribute)
            if isinstance(member, list):
                for item in member:
                    unwrap_tree(item, index)
            else:
                unwrap_tree(member, index)


def resolve_references(index: dict):
    """
    Little helper method to resolve references in the index based on the REF elements.

    Args:
        index: The index with all the elements identifiable by their unique key.
    """
    for key in index:
        if isinstance(index[key], HasRef):
            index[key].resolve_refs(index)


def index_modeldata(transfer: ImdTransfer) -> dict:
    """
    Little helper method to perform the indexing of the metamodel information in an
    easy-to-use one dimensional tree.
    Args:
        transfer: The full metamodel tree of dataclass objects which should be indexed.

    Returns: The index containing the already resolved references between the dataclass objects.
    """

    index = {}
    for item in transfer.datasection.ModelData:
        unwrap_tree(item, index)

    resolve_references(index)
    return index
