# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executiontask/v1/params/ocean_consol_execution_task_params.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n^flexport/executioncoordinator/executiontask/v1/params/ocean_consol_execution_task_params.proto\x12.flexport.executioncoordinator.executiontask.v1\x1a\x45\x66lexport/executioncoordinator/executioncargo/v1/execution_cargo.proto\x1a[flexport/executioncoordinator/executiontask/v1/params/ocean_fcl_execution_task_params.proto\x1aZflexport/executioncoordinator/executiontask/v1/params/trucking_execution_task_params.proto"\xbc\x05\n\x1eOceanConsolExecutionTaskParams\x12_\n\tinsourced\x18\x02 \x01(\x0b\x32J.flexport.executioncoordinator.executiontask.v1.InsourcedOceanConsolParamsH\x00\x12\x61\n\noutsourced\x18\x03 \x01(\x0b\x32K.flexport.executioncoordinator.executiontask.v1.OutsourcedOceanConsolParamsH\x00\x12N\n\x05\x63\x61rgo\x18\n \x01(\x0b\x32?.flexport.executioncoordinator.executioncargo.v1.ExecutionCargo\x12\x19\n\x11ocean_carrier_fid\x18\x0b \x01(\t\x12\x1d\n\x15\x63onsolidation_cfs_fid\x18\x04 \x01(\t\x12\x1f\n\x17\x64\x65\x63onsolidation_cfs_fid\x18\x05 \x01(\t\x12\x1b\n\x13port_of_loading_fid\x18\x06 \x01(\t\x12\x1d\n\x15port_of_unloading_fid\x18\x07 \x01(\t\x12\x17\n\x0finland_port_fid\x18\x08 \x01(\t\x12X\n\x11planned_fcl_route\x18\t \x01(\x0b\x32=.flexport.executioncoordinator.executiontask.v1.OceanFclRoute\x12l\n\x17managed_trucking_params\x18\x0c \x03(\x0b\x32K.flexport.executioncoordinator.executiontask.v1.TruckingExecutionTaskParamsB\x0e\n\x0c\x63onsolidator"@\n\x1aInsourcedOceanConsolParams\x12"\n\x1aparent_execution_order_fid\x18\x01 \x01(\t"V\n\x1bOutsourcedOceanConsolParams\x12\x14\n\x0c\x63oloader_fid\x18\x01 \x01(\t\x12!\n\x19\x63oloader_reference_number\x18\x02 \x01(\tB\x8f\x01\n2com.flexport.executioncoordinator.executiontask.v1B#OceanConsolExecutionTaskParamsProtoP\x01\xea\x02\x31\x46lexport::ExecutionCoordinator::ExecutionTask::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executioncoordinator.executiontask.v1.params.ocean_consol_execution_task_params_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n2com.flexport.executioncoordinator.executiontask.v1B#OceanConsolExecutionTaskParamsProtoP\001\352\0021Flexport::ExecutionCoordinator::ExecutionTask::V1"
    _globals["_OCEANCONSOLEXECUTIONTASKPARAMS"]._serialized_start = 403
    _globals["_OCEANCONSOLEXECUTIONTASKPARAMS"]._serialized_end = 1103
    _globals["_INSOURCEDOCEANCONSOLPARAMS"]._serialized_start = 1105
    _globals["_INSOURCEDOCEANCONSOLPARAMS"]._serialized_end = 1169
    _globals["_OUTSOURCEDOCEANCONSOLPARAMS"]._serialized_start = 1171
    _globals["_OUTSOURCEDOCEANCONSOLPARAMS"]._serialized_end = 1257
# @@protoc_insertion_point(module_scope)