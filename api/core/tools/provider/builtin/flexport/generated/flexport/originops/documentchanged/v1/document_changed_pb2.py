# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/originops/documentchanged/v1/document_changed.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n<flexport/originops/documentchanged/v1/document_changed.proto\x12%flexport.originops.documentchanged.v1\x1a?flexport/originops/eventrootcontext/v1/event_root_context.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa0\x05\n\x0f\x44ocumentChanged\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0f\x64ocumentable_id\x18\x02 \x01(\t\x12\x19\n\x11\x64ocumentable_type\x18\x03 \x01(\t\x12\x18\n\x10\x64ocument_type_id\x18\x04 \x01(\t\x12\x1a\n\x12\x64ocument_type_name\x18\x05 \x01(\t\x12\x1b\n\x13\x61ttachment_filename\x18\x06 \x01(\t\x12\x1f\n\x17\x61ttachment_content_type\x18\x07 \x01(\t\x12\x1b\n\x13uploaded_by_user_id\x18\x08 \x01(\t\x12\x33\n\x0f\x63reated_at_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10\x61rchived_at_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x12\x64ocument_type_slug\x18\x0c \x01(\t\x12T\n\x12\x65vent_root_context\x18\r \x01(\x0b\x32\x38.flexport.originops.eventrootcontext.v1.EventRootContext\x12>\n\x1a\x61ttachment_updated_at_time\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07u_u_i_d\x18\x0f \x01(\t\x12\x1d\n\x15uploaded_by_user_name\x18\x10 \x01(\t\x12\x1b\n\x13\x61rchived_by_user_id\x18\x11 \x01(\t\x12\x1d\n\x15\x61rchived_by_user_name\x18\x12 \x01(\tBn\n)com.flexport.originops.documentchanged.v1B\x14\x44ocumentChangedProtoP\x01\xea\x02(Flexport::OriginOps::DocumentChanged::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.originops.documentchanged.v1.document_changed_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n)com.flexport.originops.documentchanged.v1B\024DocumentChangedProtoP\001\352\002(Flexport::OriginOps::DocumentChanged::V1"
    _globals["_DOCUMENTCHANGED"]._serialized_start = 202
    _globals["_DOCUMENTCHANGED"]._serialized_end = 874
# @@protoc_insertion_point(module_scope)