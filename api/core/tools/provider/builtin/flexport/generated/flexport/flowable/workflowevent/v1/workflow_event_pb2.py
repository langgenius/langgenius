# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/flowable/workflowevent/v1/workflow_event.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n7flexport/flowable/workflowevent/v1/workflow_event.proto\x12"flexport.flowable.workflowevent.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\x89\x01\n\rWorkflowEvent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0e\n\x06tenant\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\t\x12.\n\nevent_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04info\x18\x06 \x01(\tBf\n&com.flexport.flowable.workflowevent.v1B\x12WorkflowEventProtoP\x01\xea\x02%Flexport::Flowable::WorkflowEvent::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.flowable.workflowevent.v1.workflow_event_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n&com.flexport.flowable.workflowevent.v1B\022WorkflowEventProtoP\001\352\002%Flexport::Flowable::WorkflowEvent::V1"
    _globals["_WORKFLOWEVENT"]._serialized_start = 129
    _globals["_WORKFLOWEVENT"]._serialized_end = 266
# @@protoc_insertion_point(module_scope)