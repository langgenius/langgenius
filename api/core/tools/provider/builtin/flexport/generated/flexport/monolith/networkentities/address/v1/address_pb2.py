# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/networkentities/address/v1/address.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n:flexport/monolith/networkentities/address/v1/address.proto\x12,flexport.monolith.networkentities.address.v1\x1a\x1egoogle/protobuf/wrappers.proto"\x94\x05\n\nAddressDTO\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0estreet_address\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0fstreet_address2\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04\x63ity\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x63ountry_code\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\ncompany_id\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x36\n\x10\x63ompiled_address\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0clocation_fid\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x03lat\x18\t \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12)\n\x03lng\x18\n \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x36\n\x10subdivision_code\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x63ountry_name\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08timezone\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValueBu\n0com.flexport.monolith.networkentities.address.v1B\x0c\x41\x64\x64ressProtoP\x01\xea\x02\x30\x46lexport::Monolith::NetworkEntities::Address::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.networkentities.address.v1.address_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n0com.flexport.monolith.networkentities.address.v1B\014AddressProtoP\001\352\0020Flexport::Monolith::NetworkEntities::Address::V1"
    _globals["_ADDRESSDTO"]._serialized_start = 141
    _globals["_ADDRESSDTO"]._serialized_end = 801
# @@protoc_insertion_point(module_scope)