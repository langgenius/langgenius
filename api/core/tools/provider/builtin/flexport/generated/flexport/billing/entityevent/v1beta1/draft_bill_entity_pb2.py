# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/billing/entityevent/v1beta1/draft_bill_entity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n<flexport/billing/entityevent/v1beta1/draft_bill_entity.proto\x12$flexport.billing.entityevent.v1beta1\x1a\x31\x66lexport/billing/entityevent/v1beta1/shared.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xa5\x06\n\x0f\x44raftBillEntity\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x31\n\x0b\x62ill_number\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12issuing_entity_fid\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14receiving_entity_fid\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x12\n\nvendor_fid\x18\x06 \x01(\t\x12/\n\x0b\x64ue_at_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0eissued_at_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nreview_fid\x18\t \x01(\t\x12\x19\n\rhas_conflicts\x18\n \x01(\x08\x42\x02\x18\x01\x12\x18\n\x10source_bill_fids\x18\x0b \x03(\t\x12S\n\x0b\x61llocations\x18\x0c \x03(\x0b\x32>.flexport.billing.entityevent.v1beta1.DraftBillAllocationValue\x12\x33\n\x0f\x63reated_at_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12O\n\x10transaction_type\x18\x0f \x01(\x0e\x32\x35.flexport.billing.entityevent.v1beta1.TransactionType\x12K\n\x0csource_bills\x18\x10 \x03(\x0b\x32\x35.flexport.billing.entityevent.v1beta1.SourceBillValue\x12=\n\x17primary_source_bill_fid\x18\x11 \x01(\x0b\x32\x1c.google.protobuf.StringValue"\xd0\x01\n\x0fSourceBillValue\x12\x17\n\x0fsource_bill_fid\x18\x01 \x01(\t\x12M\n\x0f\x64ocument_source\x18\x02 \x01(\x0e\x32\x34.flexport.billing.entityevent.v1beta1.DocumentSource\x12U\n\x13\x64igitization_method\x18\x03 \x01(\x0e\x32\x38.flexport.billing.entityevent.v1beta1.DigitizationMethod"\xe3\x02\n\x18\x44raftBillAllocationValue\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x38\n\x12supply_service_fid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12G\n\x05items\x18\x03 \x03(\x0b\x32\x38.flexport.billing.entityevent.v1beta1.DraftBillItemValue\x12\x32\n\x0cshipment_fid\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10reference_number\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12K\n\x0ereference_type\x18\x06 \x01(\x0e\x32\x33.flexport.billing.entityevent.v1beta1.ReferenceType"\xf4\x01\n\x12\x44raftBillItemValue\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12,\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rcurrency_code\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15line_item_mapping_fid\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bvendor_text\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueBl\n(com.flexport.billing.entityevent.v1beta1B\x14\x44raftBillEntityProtoP\x01\xea\x02\'Flexport::Billing::EntityEvent::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.billing.entityevent.v1beta1.draft_bill_entity_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n(com.flexport.billing.entityevent.v1beta1B\024DraftBillEntityProtoP\001\352\002'Flexport::Billing::EntityEvent::V1Beta1"
    _globals["_DRAFTBILLENTITY"].fields_by_name["has_conflicts"]._options = None
    _globals["_DRAFTBILLENTITY"].fields_by_name["has_conflicts"]._serialized_options = b"\030\001"
    _globals["_DRAFTBILLENTITY"]._serialized_start = 219
    _globals["_DRAFTBILLENTITY"]._serialized_end = 1024
    _globals["_SOURCEBILLVALUE"]._serialized_start = 1027
    _globals["_SOURCEBILLVALUE"]._serialized_end = 1235
    _globals["_DRAFTBILLALLOCATIONVALUE"]._serialized_start = 1238
    _globals["_DRAFTBILLALLOCATIONVALUE"]._serialized_end = 1593
    _globals["_DRAFTBILLITEMVALUE"]._serialized_start = 1596
    _globals["_DRAFTBILLITEMVALUE"]._serialized_end = 1840
# @@protoc_insertion_point(module_scope)