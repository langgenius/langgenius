# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executionorder/v1/execution_order_events.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nLflexport/executioncoordinator/executionorder/v1/execution_order_events.proto\x12/flexport.executioncoordinator.executionorder.v1\x1a\x45\x66lexport/executioncoordinator/executionorder/v1/execution_order.proto"\xb1\x01\n\x15\x45xecutionOrderCreated\x12\x1b\n\x13\x65xecution_order_fid\x18\x01 \x01(\t\x12X\n\x0f\x65xecution_order\x18\x02 \x01(\x0b\x32?.flexport.executioncoordinator.executionorder.v1.ExecutionOrder\x12!\n\x19\x65xecution_order_event_fid\x18\x03 \x01(\t"\x94\x02\n\x15\x45xecutionOrderChanged\x12\x1b\n\x13\x65xecution_order_fid\x18\x01 \x01(\t\x12X\n\x0f\x65xecution_order\x18\x02 \x01(\x0b\x32?.flexport.executioncoordinator.executionorder.v1.ExecutionOrder\x12\x61\n\x18previous_execution_order\x18\x04 \x01(\x0b\x32?.flexport.executioncoordinator.executionorder.v1.ExecutionOrder\x12!\n\x19\x65xecution_order_event_fid\x18\x03 \x01(\tB\x87\x01\n3com.flexport.executioncoordinator.executionorder.v1B\x19\x45xecutionOrderEventsProtoP\x01\xea\x02\x32\x46lexport::ExecutionCoordinator::ExecutionOrder::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executioncoordinator.executionorder.v1.execution_order_events_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n3com.flexport.executioncoordinator.executionorder.v1B\031ExecutionOrderEventsProtoP\001\352\0022Flexport::ExecutionCoordinator::ExecutionOrder::V1"
    _globals["_EXECUTIONORDERCREATED"]._serialized_start = 201
    _globals["_EXECUTIONORDERCREATED"]._serialized_end = 378
    _globals["_EXECUTIONORDERCHANGED"]._serialized_start = 381
    _globals["_EXECUTIONORDERCHANGED"]._serialized_end = 657
# @@protoc_insertion_point(module_scope)