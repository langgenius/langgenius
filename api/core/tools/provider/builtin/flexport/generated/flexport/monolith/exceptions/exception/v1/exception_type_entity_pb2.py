# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/exceptions/exception/v1/exception_type_entity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nEflexport/monolith/exceptions/exception/v1/exception_type_entity.proto\x12)flexport.monolith.exceptions.exception.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xc3\x06\n\x13\x45xceptionTypeEntity\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04slug\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x35\n\x0frecommended_use\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x13\n\x0btarget_type\x18\x05 \x01(\r\x12\x17\n\x0fresolution_type\x18\x06 \x01(\r\x12/\n\tsla_hours\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x1d\n\x15\x64\x65\x66\x61ult_assigned_team\x18\x08 \x01(\x04\x12\x1c\n\x14\x64\x65\x66\x61ult_notify_teams\x18\t \x03(\t\x12\x1a\n\x12\x64\x65\x66\x61ult_root_cause\x18\n \x01(\r\x12>\n\x18\x64\x65\x66\x61ult_external_message\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x13\x61pplicable_criteria\x18\x0c \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x10\x64\x65\x66\x61ult_priority\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\tis_active\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0f\x63reated_at_time\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0eviewer_parties\x18\x11 \x03(\t\x12\x17\n\x0f\x63reator_parties\x18\x12 \x03(\t\x12\x33\n\rcreated_by_id\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x33\n\rupdated_by_id\x18\x14 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x33\n\rdeleted_by_id\x18\x15 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB{\n-com.flexport.monolith.exceptions.exception.v1B\x18\x45xceptionTypeEntityProtoP\x01\xea\x02-Flexport::Monolith::Exceptions::Exception::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.exceptions.exception.v1.exception_type_entity_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n-com.flexport.monolith.exceptions.exception.v1B\030ExceptionTypeEntityProtoP\001\352\002-Flexport::Monolith::Exceptions::Exception::V1"
    _globals["_EXCEPTIONTYPEENTITY"]._serialized_start = 212
    _globals["_EXCEPTIONTYPEENTITY"]._serialized_end = 1047
# @@protoc_insertion_point(module_scope)