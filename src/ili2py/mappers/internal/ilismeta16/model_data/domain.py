def Code(value: int):
    """
    Enforces the IlisMeta16.ModelData.Code Domain definition in the ilismeta16 model.

    Raises:
        AssertionError when value does not match rules.
    """
    assert isinstance(value, int)
    assert 0 <= value <= 255


def MultRange(value: int):
    """
    Enforces the IlisMeta16.ModelData.MultRange Domain definition in the ilismeta16 model.

    Raises:
        AssertionError when value does not match rules.
    """
    assert isinstance(value, int)
    assert 0 <= value <= 2147483647


def LengthRange(value: int):
    """
    Enforces the IlisMeta16.ModelData.LengthRange Domain definition in the ilismeta16 model.

    Raises:
        AssertionError when value does not match rules.
    """
    assert isinstance(value, int)
    assert 1 <= value <= 2147483647
