import pytest
from xsdata.formats.converter import converter

from ili2py.readers.xtf.converters import (
    BinBlBoxConverter,
    SpecialTypeConverter,
    registered_types,
)


@pytest.fixture
def uuid_oid() -> type:
    # the rendered libraries subclass str for special types like INTERLIS.UUIDOID
    class UUIDOID(str):
        pass

    return UUIDOID


@pytest.fixture
def bin_bl_box() -> type:
    # and bytes for BLACKBOX BINARY
    class BinBlBox(bytes):
        pass

    return BinBlBox


class TestSpecialTypeConverter:
    def test_reads_and_writes_the_special_type(self, uuid_oid):
        type_converter = SpecialTypeConverter(uuid_oid)
        value = type_converter.deserialize("8b6d2d9a-4f5e-4b8a-9a3b-3e2f1c0d4a5b")
        # the value read is of the special type, not a plain str
        assert type(value) is uuid_oid
        assert type_converter.serialize(value) == "8b6d2d9a-4f5e-4b8a-9a3b-3e2f1c0d4a5b"

    def test_none_stays_none(self, uuid_oid):
        assert SpecialTypeConverter(uuid_oid).deserialize(None) is None
        assert SpecialTypeConverter(uuid_oid).serialize(None) is None


class TestBinBlBoxConverter:
    def test_reads_and_writes_base64(self, bin_bl_box):
        type_converter = BinBlBoxConverter(bin_bl_box)
        # the XTF holds the bytes base64 encoded
        value = type_converter.deserialize("aWxpMnB5")
        assert value == b"ili2py"
        assert type(value) is bin_bl_box
        assert type_converter.serialize(value) == "aWxpMnB5"


class TestRegisteredTypes:
    def test_types_are_registered_inside_the_block_only(self, uuid_oid, bin_bl_box):
        with registered_types(bin_bl_box, [uuid_oid]):
            assert uuid_oid in converter.registry
            assert bin_bl_box in converter.registry
        # the registry of xsdata is global, so nothing may stay behind
        assert uuid_oid not in converter.registry
        assert bin_bl_box not in converter.registry

    def test_nested_blocks_leave_the_types_to_the_outer_one(self, uuid_oid, bin_bl_box):
        with registered_types(bin_bl_box, [uuid_oid]):
            outer_converter = converter.registry[uuid_oid]
            with registered_types(bin_bl_box, [uuid_oid]):
                # the inner block does not replace the converter of the outer one
                assert converter.registry[uuid_oid] is outer_converter
            # and it does not unregister it on exit
            assert converter.registry[uuid_oid] is outer_converter
        assert uuid_oid not in converter.registry
