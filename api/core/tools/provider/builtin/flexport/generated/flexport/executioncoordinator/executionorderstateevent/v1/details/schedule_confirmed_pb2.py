# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executionorderstateevent/v1/details/schedule_confirmed.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nZflexport/executioncoordinator/executionorderstateevent/v1/details/schedule_confirmed.proto\x12\x39\x66lexport.executioncoordinator.executionorderstateevent.v1\x1aMflexport/executioncoordinator/derivedshipment/v1/derived_shipment_route.proto\x1a\x39\x66lexport/os/v1/types/walltimedate/v1/wall_time_date.proto\x1a\x42\x66lexport/os/v1/types/walltimedatetime/v1/wall_time_date_time.proto"\xfc\x02\n\x11ScheduleConfirmed\x12]\n\rderived_route\x18\x01 \x01(\x0b\x32\x46.flexport.executioncoordinator.derivedshipment.v1.DerivedShipmentRoute\x12S\n\x17global_cargo_ready_date\x18\x03 \x01(\x0b\x32\x32.flexport.os.v1.types.walltimedate.v1.WallTimeDate\x12W\n\x1bglobal_target_delivery_date\x18\x04 \x01(\x0b\x32\x32.flexport.os.v1.types.walltimedate.v1.WallTimeDate\x12Z\n\x16\x64\x65livered_in_full_date\x18\x05 \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTimeB\x98\x01\n=com.flexport.executioncoordinator.executionorderstateevent.v1B\x16ScheduleConfirmedProtoP\x01\xea\x02<Flexport::ExecutionCoordinator::ExecutionOrderStateEvent::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executioncoordinator.executionorderstateevent.v1.details.schedule_confirmed_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n=com.flexport.executioncoordinator.executionorderstateevent.v1B\026ScheduleConfirmedProtoP\001\352\002<Flexport::ExecutionCoordinator::ExecutionOrderStateEvent::V1"
    _globals["_SCHEDULECONFIRMED"]._serialized_start = 360
    _globals["_SCHEDULECONFIRMED"]._serialized_end = 740
# @@protoc_insertion_point(module_scope)