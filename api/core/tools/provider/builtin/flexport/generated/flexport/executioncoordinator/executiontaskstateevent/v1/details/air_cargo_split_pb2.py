# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executiontaskstateevent/v1/details/air_cargo_split.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nVflexport/executioncoordinator/executiontaskstateevent/v1/details/air_cargo_split.proto\x12\x38\x66lexport.executioncoordinator.executiontaskstateevent.v1\x1a>flexport/executioncoordinator/types/enums/v1/entry_point.proto\x1a\x42\x66lexport/os/v1/types/walltimedatetime/v1/wall_time_date_time.proto"\xc1\x01\n\rAirCargoSplit\x12W\n\x08old_legs\x18\x01 \x03(\x0b\x32\x45.flexport.executioncoordinator.executiontaskstateevent.v1.ScheduleLeg\x12W\n\x08new_legs\x18\x02 \x03(\x0b\x32\x45.flexport.executioncoordinator.executiontaskstateevent.v1.ScheduleLeg"\xe9\x05\n\x0bScheduleLeg\x12\x0c\n\x04mawb\x18\x01 \x01(\t\x12\x15\n\rflight_number\x18\x02 \x01(\t\x12\x0e\n\x06origin\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x04 \x01(\t\x12G\n\x03\x65td\x18\x05 \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTime\x12L\n\netd_source\x18\x06 \x01(\x0e\x32\x38.flexport.executioncoordinator.types.enums.v1.EntryPoint\x12G\n\x03\x61td\x18\x07 \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTime\x12L\n\natd_source\x18\x08 \x01(\x0e\x32\x38.flexport.executioncoordinator.types.enums.v1.EntryPoint\x12G\n\x03\x65ta\x18\t \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTime\x12L\n\neta_source\x18\n \x01(\x0e\x32\x38.flexport.executioncoordinator.types.enums.v1.EntryPoint\x12G\n\x03\x61ta\x18\x0b \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTime\x12L\n\nata_source\x18\x0c \x01(\x0e\x32\x38.flexport.executioncoordinator.types.enums.v1.EntryPoint\x12\x1a\n\x12has_schedule_event\x18\r \x01(\x08\x12\x18\n\x10number_of_pieces\x18\x0e \x01(\rB\x92\x01\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B\x12\x41irCargoSplitProtoP\x01\xea\x02;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executioncoordinator.executiontaskstateevent.v1.details.air_cargo_split_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B\022AirCargoSplitProtoP\001\352\002;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1"
    _globals["_AIRCARGOSPLIT"]._serialized_start = 281
    _globals["_AIRCARGOSPLIT"]._serialized_end = 474
    _globals["_SCHEDULELEG"]._serialized_start = 477
    _globals["_SCHEDULELEG"]._serialized_end = 1222
# @@protoc_insertion_point(module_scope)