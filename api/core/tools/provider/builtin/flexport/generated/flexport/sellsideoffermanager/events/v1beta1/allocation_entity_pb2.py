# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/sellsideoffermanager/events/v1beta1/allocation_entity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nDflexport/sellsideoffermanager/events/v1beta1/allocation_entity.proto\x12,flexport.sellsideoffermanager.events.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x91\x07\n\x10\x41llocationEntity\x12,\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07\x63\x61rrier\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0borigin_port\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0f\x64\x65stination_via\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x64\x65stination_port\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x04year\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12)\n\x04week\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12/\n\ttradelane\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x62uffer\x18\t \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12.\n\tallocated\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12-\n\x08\x63onsumed\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12,\n\x07overage\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x36\n\x10line_of_business\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\nis_deleted\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12.\n\ndeleted_at\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\tyear_week\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12>\n\x18\x61llocation_composite_key\x18\x11 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rallocation_id\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValueb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.sellsideoffermanager.events.v1beta1.allocation_entity_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_ALLOCATIONENTITY"]._serialized_start = 184
    _globals["_ALLOCATIONENTITY"]._serialized_end = 1097
# @@protoc_insertion_point(module_scope)