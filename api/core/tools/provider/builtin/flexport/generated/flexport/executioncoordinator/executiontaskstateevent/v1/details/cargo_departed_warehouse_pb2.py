# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executiontaskstateevent/v1/details/cargo_departed_warehouse.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n_flexport/executioncoordinator/executiontaskstateevent/v1/details/cargo_departed_warehouse.proto\x12\x38\x66lexport.executioncoordinator.executiontaskstateevent.v1\x1a\x42\x66lexport/os/v1/types/walltimedatetime/v1/wall_time_date_time.proto"\xa3\x01\n\x16\x43\x61rgoDepartedWarehouse\x12R\n\x0e\x64\x65parture_time\x18\x01 \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTime\x12\x1f\n\x17\x64\x65stination_address_fid\x18\x02 \x01(\t\x12\x14\n\x0cpallet_count\x18\x03 \x01(\x05\x42\x9b\x01\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B\x1b\x43\x61rgoDepartedWarehouseProtoP\x01\xea\x02;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.executioncoordinator.executiontaskstateevent.v1.details.cargo_departed_warehouse_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B\033CargoDepartedWarehouseProtoP\001\352\002;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1"
    _globals["_CARGODEPARTEDWAREHOUSE"]._serialized_start = 226
    _globals["_CARGODEPARTEDWAREHOUSE"]._serialized_end = 389
# @@protoc_insertion_point(module_scope)