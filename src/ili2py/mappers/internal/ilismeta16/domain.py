def BasketOID(value: str):
    """
    Enforces the IlisMeta16.BasketOID Domain definition in the ilismeta16 model.

    Raises:
        AssertionError when value does not match rules.
    """
    assert isinstance(value, str)


def MetaElemOID(value: int):
    """
    Enforces the IlisMeta16.MetaElemOID Domain definition in the ilismeta16 model.

    Raises:
        AssertionError when value does not match rules.
    """
    assert isinstance(value, str)


def LanguageCode(value: str):
    """
    Enforces the IlisMeta16.LanguageCode Domain definition in the ilismeta16 model.

    Raises:
        AssertionError when value does not match rules.
    """
    assert isinstance(value, str)
    assert len(value) <= 5
