# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executiontask/v1/execution_task_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nGflexport/executioncoordinator/executiontask/v1/execution_task_api.proto\x12.flexport.executioncoordinator.executiontask.v1\x1a\x43\x66lexport/executioncoordinator/executiontask/v1/execution_task.proto\x1aLflexport/executioncoordinator/executiontask/v1/nullable_execution_task.proto\x1a\x42\x66lexport/executioncoordinator/executiontask/v1/query_filters.proto\x1a:flexport/executioncoordinator/types/query/v1/filters.proto\x1a;flexport/executioncoordinator/types/query/v1/order_by.proto"8\n\x17GetExecutionTaskRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x10\n\x08revision\x18\x02 \x01(\r"q\n\x18GetExecutionTaskResponse\x12U\n\x0e\x65xecution_task\x18\x01 \x01(\x0b\x32=.flexport.executioncoordinator.executiontask.v1.ExecutionTask"\xd7\x07\n\x19ListExecutionTasksRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12S\n\x0c\x63reated_time\x18\x02 \x01(\x0b\x32=.flexport.executioncoordinator.types.query.v1.TimestampFilter\x12S\n\x0cupdated_time\x18\t \x01(\x0b\x32=.flexport.executioncoordinator.types.query.v1.TimestampFilter\x12W\n\x13\x65xecution_order_fid\x18\x04 \x01(\x0b\x32:.flexport.executioncoordinator.types.query.v1.StringFilter\x12^\n\x1aparent_execution_order_fid\x18\x08 \x01(\x0b\x32:.flexport.executioncoordinator.types.query.v1.StringFilter\x12P\n\x0cshipment_fid\x18\x05 \x01(\x0b\x32:.flexport.executioncoordinator.types.query.v1.StringFilter\x12O\n\x0bparams_case\x18\x07 \x01(\x0b\x32:.flexport.executioncoordinator.types.query.v1.StringFilter\x12T\n\x0frevision_number\x18\n \x01(\x0b\x32;.flexport.executioncoordinator.types.query.v1.IntegerFilter\x12V\n\x12\x63ompany_entity_fid\x18\x0c \x01(\x0b\x32:.flexport.executioncoordinator.types.query.v1.StringFilter\x12Y\n\x06params\x18\x03 \x01(\x0b\x32I.flexport.executioncoordinator.executiontask.v1.ExecutionTaskParamsFilter\x12S\n\x0fplanning_status\x18\x06 \x01(\x0b\x32:.flexport.executioncoordinator.types.query.v1.StringFilter\x12G\n\x08order_by\x18\x0b \x01(\x0e\x32\x35.flexport.executioncoordinator.types.query.v1.OrderBy"t\n\x1aListExecutionTasksResponse\x12V\n\x0f\x65xecution_tasks\x18\x01 \x03(\x0b\x32=.flexport.executioncoordinator.executiontask.v1.ExecutionTask"0\n!ListExecutionTaskRevisionsRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"v\n"ListExecutionTaskRevisionsResponse\x12P\n\trevisions\x18\x01 \x03(\x0b\x32=.flexport.executioncoordinator.executiontask.v1.ExecutionTask"-\n\x1d\x42\x61tchGetExecutionTasksRequest\x12\x0c\n\x04\x66ids\x18\x01 \x03(\t"\x89\x01\n\x1e\x42\x61tchGetExecutionTasksResponse\x12g\n\x18nullable_execution_tasks\x18\x01 \x03(\x0b\x32\x45.flexport.executioncoordinator.executiontask.v1.NullableExecutionTask2\xe8\x05\n\x10\x45xecutionTaskAPI\x12\xa5\x01\n\x10GetExecutionTask\x12G.flexport.executioncoordinator.executiontask.v1.GetExecutionTaskRequest\x1aH.flexport.executioncoordinator.executiontask.v1.GetExecutionTaskResponse\x12\xab\x01\n\x12ListExecutionTasks\x12I.flexport.executioncoordinator.executiontask.v1.ListExecutionTasksRequest\x1aJ.flexport.executioncoordinator.executiontask.v1.ListExecutionTasksResponse\x12\xc3\x01\n\x1aListExecutionTaskRevisions\x12Q.flexport.executioncoordinator.executiontask.v1.ListExecutionTaskRevisionsRequest\x1aR.flexport.executioncoordinator.executiontask.v1.ListExecutionTaskRevisionsResponse\x12\xb7\x01\n\x16\x42\x61tchGetExecutionTasks\x12M.flexport.executioncoordinator.executiontask.v1.BatchGetExecutionTasksRequest\x1aN.flexport.executioncoordinator.executiontask.v1.BatchGetExecutionTasksResponseB\x81\x01\n2com.flexport.executioncoordinator.executiontask.v1B\x15\x45xecutionTaskApiProtoP\x01\xea\x02\x31\x46lexport::ExecutionCoordinator::ExecutionTask::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executioncoordinator.executiontask.v1.execution_task_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n2com.flexport.executioncoordinator.executiontask.v1B\025ExecutionTaskApiProtoP\001\352\0021Flexport::ExecutionCoordinator::ExecutionTask::V1"
    _globals["_GETEXECUTIONTASKREQUEST"]._serialized_start = 459
    _globals["_GETEXECUTIONTASKREQUEST"]._serialized_end = 515
    _globals["_GETEXECUTIONTASKRESPONSE"]._serialized_start = 517
    _globals["_GETEXECUTIONTASKRESPONSE"]._serialized_end = 630
    _globals["_LISTEXECUTIONTASKSREQUEST"]._serialized_start = 633
    _globals["_LISTEXECUTIONTASKSREQUEST"]._serialized_end = 1616
    _globals["_LISTEXECUTIONTASKSRESPONSE"]._serialized_start = 1618
    _globals["_LISTEXECUTIONTASKSRESPONSE"]._serialized_end = 1734
    _globals["_LISTEXECUTIONTASKREVISIONSREQUEST"]._serialized_start = 1736
    _globals["_LISTEXECUTIONTASKREVISIONSREQUEST"]._serialized_end = 1784
    _globals["_LISTEXECUTIONTASKREVISIONSRESPONSE"]._serialized_start = 1786
    _globals["_LISTEXECUTIONTASKREVISIONSRESPONSE"]._serialized_end = 1904
    _globals["_BATCHGETEXECUTIONTASKSREQUEST"]._serialized_start = 1906
    _globals["_BATCHGETEXECUTIONTASKSREQUEST"]._serialized_end = 1951
    _globals["_BATCHGETEXECUTIONTASKSRESPONSE"]._serialized_start = 1954
    _globals["_BATCHGETEXECUTIONTASKSRESPONSE"]._serialized_end = 2091
    _globals["_EXECUTIONTASKAPI"]._serialized_start = 2094
    _globals["_EXECUTIONTASKAPI"]._serialized_end = 2838
# @@protoc_insertion_point(module_scope)