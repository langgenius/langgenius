# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executiontaskstateevent/v1/details/air_consignee_notified.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n]flexport/executioncoordinator/executiontaskstateevent/v1/details/air_consignee_notified.proto\x12\x38\x66lexport.executioncoordinator.executiontaskstateevent.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xda\x01\n\x14\x41irConsigneeNotified\x12\x15\n\tcargo_fid\x18\x01 \x01(\tB\x02\x18\x01\x12\x10\n\x08port_fid\x18\x02 \x01(\t\x12\x38\n\x14\x63\x61rgo_available_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x1e\x65stimated_cargo_available_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13route_shape_leg_fid\x18\x05 \x01(\tB\x99\x01\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B\x19\x41irConsigneeNotifiedProtoP\x01\xea\x02;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executioncoordinator.executiontaskstateevent.v1.details.air_consignee_notified_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B\031AirConsigneeNotifiedProtoP\001\352\002;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1"
    _globals["_AIRCONSIGNEENOTIFIED"].fields_by_name["cargo_fid"]._options = None
    _globals["_AIRCONSIGNEENOTIFIED"].fields_by_name["cargo_fid"]._serialized_options = b"\030\001"
    _globals["_AIRCONSIGNEENOTIFIED"]._serialized_start = 189
    _globals["_AIRCONSIGNEENOTIFIED"]._serialized_end = 407
# @@protoc_insertion_point(module_scope)