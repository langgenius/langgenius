# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/exceptionmanagement/entityevent/v1beta1/operational_exception_entity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nSflexport/exceptionmanagement/entityevent/v1beta1/operational_exception_entity.proto\x12\x30\x66lexport.exceptionmanagement.entityevent.v1beta1\x1a\x43\x66lexport/exceptionmanagement/enums/v1beta1/exception_priority.proto\x1a\x46\x66lexport/exceptionmanagement/enums/v1beta1/exception_reason_code.proto\x1a\x41\x66lexport/exceptionmanagement/enums/v1beta1/exception_status.proto\x1a\x46\x66lexport/exceptionmanagement/enums/v1beta1/exception_target_type.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xe2\x0b\n\x1aOperationalExceptionEntity\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x31\n\x0blegacy_uuid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1a\n\x12\x65xception_type_fid\x18\x03 \x01(\t\x12T\n\x0btarget_type\x18\x04 \x01(\x0e\x32?.flexport.exceptionmanagement.enums.v1beta1.ExceptionTargetType\x12\x12\n\ntarget_fid\x18\x05 \x01(\t\x12\x37\n\x11\x61ssigned_user_fid\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\rdue_date_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\tmessaging\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1b\n\x13visible_party_slugs\x18\t \x03(\t\x12O\n\x08priority\x18\n \x01(\x0e\x32=.flexport.exceptionmanagement.enums.v1beta1.ExceptionPriority\x12K\n\x06status\x18\x0b \x01(\x0e\x32;.flexport.exceptionmanagement.enums.v1beta1.ExceptionStatus\x12\x10\n\x08revision\x18\x0c \x01(\r\x12+\n\x05\x61ttrs\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x39\n\x13\x63reated_by_user_fid\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0f\x63reated_at_time\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x13updated_by_user_fid\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0fupdated_at_time\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x13\x64\x65leted_by_user_fid\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0f\x64\x65leted_at_time\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12T\n\x0breason_code\x18\x14 \x01(\x0e\x32?.flexport.exceptionmanagement.enums.v1beta1.ExceptionReasonCode\x12\x33\n\rcontainer_fid\x18\x15 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0e\x61ttached_files\x18\x16 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x66\x66\x61_work_item_fid\x18\x17 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nroot_cause\x18\x18 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x17time_of_occurrence_time\x18\x19 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12;\n\x17\x61\x63tual_resolved_at_time\x18\x1a \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x1d\x65stimated_transit_time_impact\x18\x1b \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x0c\n\x04\x64\x62id\x18\x1c \x01(\x03\x12\x1f\n\x17\x65xception_type_revision\x18\x1d \x01(\rB\x8f\x01\n4com.flexport.exceptionmanagement.entityevent.v1beta1B\x1fOperationalExceptionEntityProtoP\x01\xea\x02\x33\x46lexport::ExceptionManagement::EntityEvent::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.exceptionmanagement.entityevent.v1beta1.operational_exception_entity_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n4com.flexport.exceptionmanagement.entityevent.v1beta1B\037OperationalExceptionEntityProtoP\001\352\0023Flexport::ExceptionManagement::EntityEvent::V1Beta1"
    _globals["_OPERATIONALEXCEPTIONENTITY"]._serialized_start = 483
    _globals["_OPERATIONALEXCEPTIONENTITY"]._serialized_end = 1989
# @@protoc_insertion_point(module_scope)