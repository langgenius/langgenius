# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executiontaskstateevent/v1/details/rail_container_actual_placement_occurred.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\noflexport/executioncoordinator/executiontaskstateevent/v1/details/rail_container_actual_placement_occurred.proto\x12\x38\x66lexport.executioncoordinator.executiontaskstateevent.v1\x1a\x42\x66lexport/os/v1/types/walltimedatetime/v1/wall_time_date_time.proto"\x82\x02\n$RailContainerActualPlacementOccurred\x12\x15\n\rcontainer_fid\x18\x08 \x01(\t\x12\x18\n\x10\x63ontainer_number\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\t\x12\x11\n\tlongitude\x18\x03 \x01(\t\x12Q\n\rsighting_time\x18\x04 \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTime\x12\x14\n\x0cstation_name\x18\x05 \x01(\t\x12\r\n\x05state\x18\x06 \x01(\t\x12\x0c\n\x04splc\x18\x07 \x01(\tB\xa9\x01\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B)RailContainerActualPlacementOccurredProtoP\x01\xea\x02;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.executioncoordinator.executiontaskstateevent.v1.details.rail_container_actual_placement_occurred_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B)RailContainerActualPlacementOccurredProtoP\001\352\002;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1"
    _globals["_RAILCONTAINERACTUALPLACEMENTOCCURRED"]._serialized_start = 242
    _globals["_RAILCONTAINERACTUALPLACEMENTOCCURRED"]._serialized_end = 500
# @@protoc_insertion_point(module_scope)