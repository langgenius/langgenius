# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executiontaskstateevent/v1/details/cfs_inbound_workflow_updated.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\ncflexport/executioncoordinator/executiontaskstateevent/v1/details/cfs_inbound_workflow_updated.proto\x12\x38\x66lexport.executioncoordinator.executiontaskstateevent.v1"\x80\x01\n\x19\x43\x66sInboundWorkflowUpdated\x12\x63\n\x0bupdate_type\x18\x01 \x01(\x0e\x32N.flexport.executioncoordinator.executiontaskstateevent.v1.CfsInboundUpdateType*\xb0\x04\n\x14\x43\x66sInboundUpdateType\x12#\n\x1f\x43\x46S_INBOUND_UPDATE_TYPE_INVALID\x10\x00\x12/\n+CFS_INBOUND_UPDATE_TYPE_CONFIRMED_DOCUMENTS\x10\x01\x12.\n*CFS_INBOUND_UPDATE_TYPE_CONFIRMED_PLANNING\x10\x02\x12@\n<CFS_INBOUND_UPDATE_TYPE_CONFIRMED_ARRIVAL_AT_INLAND_RAILYARD\x10\x03\x12\x35\n1CFS_INBOUND_UPDATE_TYPE_CONFIRMED_ARRIVAL_AT_PORT\x10\x04\x12\x46\nBCFS_INBOUND_UPDATE_TYPE_CONFIRMED_AVAILABILITY_AT_PORT_OR_RAILYARD\x10\x05\x12,\n(CFS_INBOUND_UPDATE_TYPE_CONFIRMED_PICKUP\x10\x06\x12\x34\n0CFS_INBOUND_UPDATE_TYPE_CONFIRMED_ARRIVAL_TO_CFS\x10\x07\x12\x39\n5CFS_INBOUND_UPDATE_TYPE_CONFIRMED_AVAILABILITY_AT_CFS\x10\x08\x12\x32\n.CFS_INBOUND_UPDATE_TYPE_UNDO_LAST_CONFIRMATION\x10\tB\x9e\x01\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B\x1e\x43\x66sInboundWorkflowUpdatedProtoP\x01\xea\x02;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.executioncoordinator.executiontaskstateevent.v1.details.cfs_inbound_workflow_updated_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n<com.flexport.executioncoordinator.executiontaskstateevent.v1B\036CfsInboundWorkflowUpdatedProtoP\001\352\002;Flexport::ExecutionCoordinator::ExecutionTaskStateEvent::V1"
    _globals["_CFSINBOUNDUPDATETYPE"]._serialized_start = 293
    _globals["_CFSINBOUNDUPDATETYPE"]._serialized_end = 853
    _globals["_CFSINBOUNDWORKFLOWUPDATED"]._serialized_start = 162
    _globals["_CFSINBOUNDWORKFLOWUPDATED"]._serialized_end = 290
# @@protoc_insertion_point(module_scope)