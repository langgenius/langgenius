# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executiontask/v1/params/trucking_direct_execution_task_params.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\naflexport/executioncoordinator/executiontask/v1/params/trucking_direct_execution_task_params.proto\x12.flexport.executioncoordinator.executiontask.v1\x1a\x45\x66lexport/executioncoordinator/executioncargo/v1/execution_cargo.proto\x1a\x45\x66lexport/executioncoordinator/types/cartageinfo/v1/cartage_info.proto\x1aPflexport/os/v1/types/walltimedateordatetime/v1/wall_time_date_or_date_time.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xcf\x03\n!TruckingDirectExecutionTaskParams\x12\x12\n\norigin_fid\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65stination_fid\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61rrier_fid\x18\x03 \x01(\t\x12\x1b\n\x13origin_terminal_fid\x18\x07 \x01(\t\x12 \n\x18\x64\x65stination_terminal_fid\x18\x08 \x01(\t\x12\x1b\n\x13\x66reight_partner_fid\x18\x04 \x01(\t\x12\x12\n\nbroker_fid\x18\x10 \x01(\t\x12@\n\x1crequires_additional_tracking\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12_\n\x0c\x63\x61rgo_params\x18\x06 \x03(\x0b\x32I.flexport.executioncoordinator.executiontask.v1.TruckingDirectCargoParams\x12U\n\x0c\x63\x61rtage_info\x18\x0f \x01(\x0b\x32?.flexport.executioncoordinator.types.cartageinfo.v1.CartageInfo"\xdc\x02\n\x19TruckingDirectCargoParams\x12\x66\n\x12\x64\x65parture_estimate\x18\x06 \x01(\x0b\x32\x46.flexport.os.v1.types.walltimedateordatetime.v1.WallTimeDateOrDateTimeB\x02\x18\x01\x12\x64\n\x10\x61rrival_estimate\x18\x07 \x01(\x0b\x32\x46.flexport.os.v1.types.walltimedateordatetime.v1.WallTimeDateOrDateTimeB\x02\x18\x01\x12X\n\x0f\x65xecution_cargo\x18\x04 \x01(\x0b\x32?.flexport.executioncoordinator.executioncargo.v1.ExecutionCargo\x12\x17\n\x0ftracking_number\x18\x05 \x01(\tB\x92\x01\n2com.flexport.executioncoordinator.executiontask.v1B&TruckingDirectExecutionTaskParamsProtoP\x01\xea\x02\x31\x46lexport::ExecutionCoordinator::ExecutionTask::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.executioncoordinator.executiontask.v1.params.trucking_direct_execution_task_params_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n2com.flexport.executioncoordinator.executiontask.v1B&TruckingDirectExecutionTaskParamsProtoP\001\352\0021Flexport::ExecutionCoordinator::ExecutionTask::V1"
    _globals["_TRUCKINGDIRECTCARGOPARAMS"].fields_by_name["departure_estimate"]._options = None
    _globals["_TRUCKINGDIRECTCARGOPARAMS"].fields_by_name["departure_estimate"]._serialized_options = b"\030\001"
    _globals["_TRUCKINGDIRECTCARGOPARAMS"].fields_by_name["arrival_estimate"]._options = None
    _globals["_TRUCKINGDIRECTCARGOPARAMS"].fields_by_name["arrival_estimate"]._serialized_options = b"\030\001"
    _globals["_TRUCKINGDIRECTEXECUTIONTASKPARAMS"]._serialized_start = 406
    _globals["_TRUCKINGDIRECTEXECUTIONTASKPARAMS"]._serialized_end = 869
    _globals["_TRUCKINGDIRECTCARGOPARAMS"]._serialized_start = 872
    _globals["_TRUCKINGDIRECTCARGOPARAMS"]._serialized_end = 1220
# @@protoc_insertion_point(module_scope)