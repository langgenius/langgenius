# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/exceptions/exception/v1/exception_revision_entity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nIflexport/monolith/exceptions/exception/v1/exception_revision_entity.proto\x12)flexport.monolith.exceptions.exception.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xbc\t\n\x17\x45xceptionRevisionEntity\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\x12\x14\n\x0c\x65xception_id\x18\x03 \x01(\t\x12\x1a\n\x12\x65xception_type_fid\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x10\n\x08severity\x18\x06 \x01(\t\x12-\n\x07message\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rinternal_note\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x42\n\x1d\x65stimated_transit_time_impact\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x31\n\rdue_date_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12R\n\x0fresolution_type\x18\x0b \x01(\x0e\x32\x39.flexport.monolith.exceptions.exception.v1.ResolutionType\x12\x34\n\x0eroot_cause_fid\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0eoccurence_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x14\x64omain_specific_info\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x1b\n\x13updated_by_user_fid\x18\x0f \x01(\t\x12\x37\n\x11\x61ssigned_user_fid\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x61ssigned_team_fid\x18\x11 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x19\n\x11notify_teams_fids\x18\x12 \x03(\t\x12\x33\n\x0f\x63reated_at_time\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10resolved_at_time\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x13\x65xception_type_slug\x18\x16 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0froot_cause_slug\x18\x17 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12\x61ssigned_team_slug\x18\x18 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1a\n\x12notify_teams_slugs\x18\x19 \x03(\t\x12;\n\x17\x61\x63tual_resolved_at_time\x18\x1a \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rcontainer_fid\x18\x1b \x01(\t*z\n\x0eResolutionType\x12\x1b\n\x17RESOLUTION_TYPE_INVALID\x10\x00\x12#\n\x1fRESOLUTION_TYPE_ACTION_REQUIRED\x10\x01\x12&\n"RESOLUTION_TYPE_NO_ACTION_REQUIRED\x10\x02\x42\x7f\n-com.flexport.monolith.exceptions.exception.v1B\x1c\x45xceptionRevisionEntityProtoP\x01\xea\x02-Flexport::Monolith::Exceptions::Exception::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.exceptions.exception.v1.exception_revision_entity_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n-com.flexport.monolith.exceptions.exception.v1B\034ExceptionRevisionEntityProtoP\001\352\002-Flexport::Monolith::Exceptions::Exception::V1"
    _globals["_RESOLUTIONTYPE"]._serialized_start = 1430
    _globals["_RESOLUTIONTYPE"]._serialized_end = 1552
    _globals["_EXCEPTIONREVISIONENTITY"]._serialized_start = 216
    _globals["_EXCEPTIONREVISIONENTITY"]._serialized_end = 1428
# @@protoc_insertion_point(module_scope)