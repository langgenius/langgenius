# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/workitems/changedevent/v1/work_item_changed_event.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n@flexport/workitems/changedevent/v1/work_item_changed_event.proto\x12"flexport.workitems.changedevent.v1\x1a:flexport/workitems/workitemservice/v1beta1/work_item.proto"\xf6\x01\n\x14WorkItemChangedEvent\x12G\n\twork_item\x18\x01 \x01(\x0b\x32\x34.flexport.workitems.workitemservice.v1beta1.WorkItem\x12K\n\rold_work_item\x18\x02 \x01(\x0b\x32\x34.flexport.workitems.workitemservice.v1beta1.WorkItem\x12H\n\x0ework_item_info\x18\x03 \x01(\x0b\x32\x30.flexport.workitems.changedevent.v1.WorkItemInfo"I\n\x0cWorkItemInfo\x12\x16\n\x0ework_item_type\x18\x01 \x01(\t\x12!\n\x19\x63\x61n_be_assigned_via_rules\x18\x02 \x01(\x08\x42m\n&com.flexport.workitems.changedevent.v1B\x19WorkItemChangedEventProtoP\x01\xea\x02%Flexport::WorkItems::ChangedEvent::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.workitems.changedevent.v1.work_item_changed_event_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n&com.flexport.workitems.changedevent.v1B\031WorkItemChangedEventProtoP\001\352\002%Flexport::WorkItems::ChangedEvent::V1"
    _globals["_WORKITEMCHANGEDEVENT"]._serialized_start = 165
    _globals["_WORKITEMCHANGEDEVENT"]._serialized_end = 411
    _globals["_WORKITEMINFO"]._serialized_start = 413
    _globals["_WORKITEMINFO"]._serialized_end = 486
# @@protoc_insertion_point(module_scope)