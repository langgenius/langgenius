# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/consolplanner/entityevent/v1/air_build_plan_entity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\nAflexport/consolplanner/entityevent/v1/air_build_plan_entity.proto\x12%flexport.consolplanner.entityevent.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb3\x06\n\x12\x41irBuildPlanEntity\x12\n\n\x02id\x18\x01 \x01(\x03\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x0e \x01(\t\x12\x17\n\x0flast_updated_by\x18\x0f \x01(\t\x12'\n\x1f\x61llotment_schedule_instance_fid\x18\x05 \x01(\t\x12\x1b\n\x13\x65quipment_type_fids\x18\x06 \x03(\t\x12\x1a\n\x12origin_airport_fid\x18\x07 \x01(\t\x12=\n\x06status\x18\x08 \x01(\x0e\x32-.flexport.consolplanner.entityevent.v1.Status\x12J\n\rhandling_type\x18\t \x01(\x0e\x32\x33.flexport.consolplanner.entityevent.v1.HandlingType\x12 \n\x13\x65xecution_order_fid\x18\n \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0eorigin_cfs_fid\x18\x0b \x01(\tH\x01\x88\x01\x01\x12 \n\x13\x64\x65stination_cfs_fid\x18\x0c \x01(\tH\x02\x88\x01\x01\x12\x17\n\nclient_fid\x18\r \x01(\tH\x03\x88\x01\x01\x12'\n\x1a\x65quipment_type_shared_from\x18\x10 \x01(\x03H\x04\x88\x01\x01\x12S\n\x12selected_rate_type\x18\x11 \x01(\x0e\x32\x37.flexport.consolplanner.entityevent.v1.SelectedRateTypeB\x16\n\x14_execution_order_fidB\x11\n\x0f_origin_cfs_fidB\x16\n\x14_destination_cfs_fidB\r\n\x0b_client_fidB\x1d\n\x1b_equipment_type_shared_from*@\n\x06Status\x12\x12\n\x0eSTATUS_INVALID\x10\x00\x12\x10\n\x0cSTATUS_DRAFT\x10\x01\x12\x10\n\x0cSTATUS_FINAL\x10\x02*y\n\x0cHandlingType\x12\x19\n\x15HANDLING_TYPE_INVALID\x10\x00\x12\x18\n\x14HANDLING_TYPE_INTACT\x10\x01\x12\x17\n\x13HANDLING_TYPE_LOOSE\x10\x02\x12\x1b\n\x17HANDLING_TYPE_BREAKDOWN\x10\x03*q\n\x10SelectedRateType\x12\x1e\n\x1aSELECTED_RATE_TYPE_INVALID\x10\x00\x12\x1c\n\x18SELECTED_RATE_TYPE_FIXED\x10\x01\x12\x1f\n\x1bSELECTED_RATE_TYPE_FLOATING\x10\x02\x42q\n)com.flexport.consolplanner.entityevent.v1B\x17\x41irBuildPlanEntityProtoP\x01\xea\x02(Flexport::ConsolPlanner::EntityEvent::V1b\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.consolplanner.entityevent.v1.air_build_plan_entity_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n)com.flexport.consolplanner.entityevent.v1B\027AirBuildPlanEntityProtoP\001\352\002(Flexport::ConsolPlanner::EntityEvent::V1"
    _globals["_STATUS"]._serialized_start = 963
    _globals["_STATUS"]._serialized_end = 1027
    _globals["_HANDLINGTYPE"]._serialized_start = 1029
    _globals["_HANDLINGTYPE"]._serialized_end = 1150
    _globals["_SELECTEDRATETYPE"]._serialized_start = 1152
    _globals["_SELECTEDRATETYPE"]._serialized_end = 1265
    _globals["_AIRBUILDPLANENTITY"]._serialized_start = 142
    _globals["_AIRBUILDPLANENTITY"]._serialized_end = 961
# @@protoc_insertion_point(module_scope)