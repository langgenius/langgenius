# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executionoverride/v1/execution_override_status_info.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nWflexport/executioncoordinator/executionoverride/v1/execution_override_status_info.proto\x12\x32\x66lexport.executioncoordinator.executionoverride.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xce\x03\n\x1b\x45xecutionOverrideStatusInfo\x12\x30\n\x0c\x63reated_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10\x65\x63_consumed_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12>\n\x1a\x65\x63_writeback_consumed_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12?\n\x1b\x65\x63_writeback_succeeded_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12<\n\x18\x65\x63_writeback_failed_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\x1f\x64\x65rived_shipment_extracted_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\x1f\x64\x65rived_shipment_persisted_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x94\x01\n6com.flexport.executioncoordinator.executionoverride.v1B ExecutionOverrideStatusInfoProtoP\x01\xea\x02\x35\x46lexport::ExecutionCoordinator::ExecutionOverride::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executioncoordinator.executionoverride.v1.execution_override_status_info_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n6com.flexport.executioncoordinator.executionoverride.v1B ExecutionOverrideStatusInfoProtoP\001\352\0025Flexport::ExecutionCoordinator::ExecutionOverride::V1"
    _globals["_EXECUTIONOVERRIDESTATUSINFO"]._serialized_start = 177
    _globals["_EXECUTIONOVERRIDESTATUSINFO"]._serialized_end = 639
# @@protoc_insertion_point(module_scope)