# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executiontaskstateevent/v1/details/trucking_drayage_warehouse_visit_type_changed.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\ntflexport/executioncoordinator/executiontaskstateevent/v1/details/trucking_drayage_warehouse_visit_type_changed.proto\x12\x38\x66lexport.executioncoordinator.executiontaskstateevent.v1\x1aOflexport/executioncoordinator/types/enums/v1/drayage_warehouse_visit_type.proto"\x80\x03\n(TruckingDrayageWarehouseVisitTypeChanged\x12\x11\n\tcargo_fid\x18\x01 \x01(\t\x12\x1a\n\x12origin_address_fid\x18\x02 \x01(\t\x12\x1f\n\x17\x64\x65stination_address_fid\x18\x03 \x01(\t\x12\x64\n\x13original_visit_type\x18\x04 \x01(\x0e\x32G.flexport.executioncoordinator.types.enums.v1.DrayageWarehouseVisitType\x12_\n\x0enew_visit_type\x18\x05 \x01(\x0e\x32G.flexport.executioncoordinator.types.enums.v1.DrayageWarehouseVisitType\x12\x19\n\x11\x65xception_message\x18\x06 \x01(\t\x12"\n\x1amessaging_linked_object_id\x18\x07 \x01(\tB\xad\x01\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B-TruckingDrayageWarehouseVisitTypeChangedProtoP\x01\xea\x02;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.executioncoordinator.executiontaskstateevent.v1.details.trucking_drayage_warehouse_visit_type_changed_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B-TruckingDrayageWarehouseVisitTypeChangedProtoP\001\352\002;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1"
    _globals["_TRUCKINGDRAYAGEWAREHOUSEVISITTYPECHANGED"]._serialized_start = 260
    _globals["_TRUCKINGDRAYAGEWAREHOUSEVISITTYPECHANGED"]._serialized_end = 644
# @@protoc_insertion_point(module_scope)