# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/consolplanner/air/v1beta1/mawb_epc_updated_event.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n?flexport/consolplanner/air/v1beta1/mawb_epc_updated_event.proto\x12"flexport.consolplanner.air.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\xa2\x02\n\x13MawbEpcUpdatedEvent\x12\x15\n\rmawb_plan_fid\x18\x01 \x01(\t\x12\x1b\n\x13parent_shipment_fid\x18\x05 \x01(\t\x12\x13\n\x0bmawb_number\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\rupdate_reason\x18\x03 \x03(\x0b\x32\x30.flexport.consolplanner.air.v1beta1.UpdateReason\x12I\n\x0eoperation_type\x18\x04 \x01(\x0e\x32\x31.flexport.consolplanner.air.v1beta1.OperationType"\xa7\x02\n\x0cUpdateReason\x12K\n\x0fupdate_category\x18\x01 \x01(\x0e\x32\x32.flexport.consolplanner.air.v1beta1.UpdateCategory\x12\x17\n\rmawb_plan_fid\x18\x02 \x01(\tH\x00\x12\x16\n\x0cshipment_fid\x18\x03 \x01(\tH\x00\x12-\n#air_allotment_schedule_instance_fid\x18\x04 \x01(\tH\x00\x12\x1d\n\x13\x63ontract_identifier\x18\x05 \x01(\tH\x00\x12\x18\n\x0eroute_term_fid\x18\x06 \x01(\tH\x00\x12\x1c\n\x12\x61ir_build_plan_fid\x18\x07 \x01(\tH\x00\x42\x13\n\x11\x65ntity_identifier*\xe2\x04\n\x0eUpdateCategory\x12\x1b\n\x17UPDATE_CATEGORY_INVALID\x10\x00\x12*\n&UPDATE_CATEGORY_SHIPMENT_WEIGHT_VOLUME\x10\x01\x12&\n"UPDATE_CATEGORY_SHIPMENT_DG_REVIEW\x10\x02\x12*\n&UPDATE_CATEGORY_SHIPMENT_STAGE_CHANGED\x10\x03\x12$\n UPDATE_CATEGORY_SHIPMENT_REMOVED\x10\x04\x12&\n"UPDATE_CATEGORY_MAWB_CW_DESIGNATED\x10\x05\x12(\n$UPDATE_CATEGORY_BUILD_PLAN_FINALIZED\x10\x0b\x12(\n$UPDATE_CATEGORY_BUILD_PLAN_REPLANNED\x10\x06\x12\x32\n.UPDATE_CATEGORY_AIR_ALLOTMENT_CONTRACT_UPDATED\x10\x07\x12\x35\n1UPDATE_CATEGORY_AIR_ALLOTMENT_UTILIZATION_UPDATED\x10\x08\x12.\n*UPDATE_CATEGORY_AIR_CONTRACT_TERMS_UPDATED\x10\t\x12\x1c\n\x18UPDATE_CATEGORY_BACKFILL\x10\n\x12+\n\'UPDATE_CATEGORY_OUTSOURCED_MAWB_CREATED\x10\x0c\x12+\n\'UPDATE_CATEGORY_OUTSOURCED_MAWB_UPDATED\x10\r*|\n\rOperationType\x12\x1a\n\x16OPERATION_TYPE_INVALID\x10\x00\x12\x19\n\x15OPERATION_TYPE_CREATE\x10\x01\x12\x19\n\x15OPERATION_TYPE_UPDATE\x10\x02\x12\x19\n\x15OPERATION_TYPE_DELETE\x10\x03\x42R\n&com.flexport.consolplanner.air.v1beta1P\x01\xea\x02%Flexport::ConsolPlanner::Air::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.consolplanner.air.v1beta1.mawb_epc_updated_event_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n&com.flexport.consolplanner.air.v1beta1P\001\352\002%Flexport::ConsolPlanner::Air::V1Beta1"
    )
    _globals["_UPDATECATEGORY"]._serialized_start = 728
    _globals["_UPDATECATEGORY"]._serialized_end = 1338
    _globals["_OPERATIONTYPE"]._serialized_start = 1340
    _globals["_OPERATIONTYPE"]._serialized_end = 1464
    _globals["_MAWBEPCUPDATEDEVENT"]._serialized_start = 137
    _globals["_MAWBEPCUPDATEDEVENT"]._serialized_end = 427
    _globals["_UPDATEREASON"]._serialized_start = 430
    _globals["_UPDATEREASON"]._serialized_end = 725
# @@protoc_insertion_point(module_scope)