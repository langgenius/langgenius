# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/billing/entityevent/v1beta1/reviewed_bill_entity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n?flexport/billing/entityevent/v1beta1/reviewed_bill_entity.proto\x12$flexport.billing.entityevent.v1beta1\x1a\x31\x66lexport/billing/entityevent/v1beta1/shared.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xc8\x05\n\x12ReviewedBillEntity\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x31\n\x0b\x62ill_number\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12issuing_entity_fid\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14receiving_entity_fid\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x12\n\nvendor_fid\x18\x05 \x01(\t\x12/\n\x0b\x64ue_at_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0eissued_at_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nreview_fid\x18\x08 \x01(\t\x12V\n\x0b\x61llocations\x18\t \x03(\x0b\x32\x41.flexport.billing.entityevent.v1beta1.ReviewedBillAllocationValue\x12\x33\n\x0f\x63reated_at_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12O\n\x10transaction_type\x18\x0c \x01(\x0e\x32\x35.flexport.billing.entityevent.v1beta1.TransactionType\x12+\n\x05notes\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x18\n\x10payment_required\x18\x0e \x01(\x08\x12\x15\n\rpending_audit\x18\x0f \x01(\x08"\xe9\x02\n\x1bReviewedBillAllocationValue\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x38\n\x12supply_service_fid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12J\n\x05items\x18\x03 \x03(\x0b\x32;.flexport.billing.entityevent.v1beta1.ReviewedBillItemValue\x12\x32\n\x0cshipment_fid\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10reference_number\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12K\n\x0ereference_type\x18\x06 \x01(\x0e\x32\x33.flexport.billing.entityevent.v1beta1.ReferenceType"\xf7\x01\n\x15ReviewedBillItemValue\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12,\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rcurrency_code\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15line_item_mapping_fid\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bvendor_text\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueBo\n(com.flexport.billing.entityevent.v1beta1B\x17ReviewedBillEntityProtoP\x01\xea\x02\'Flexport::Billing::EntityEvent::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.billing.entityevent.v1beta1.reviewed_bill_entity_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n(com.flexport.billing.entityevent.v1beta1B\027ReviewedBillEntityProtoP\001\352\002'Flexport::Billing::EntityEvent::V1Beta1"
    _globals["_REVIEWEDBILLENTITY"]._serialized_start = 222
    _globals["_REVIEWEDBILLENTITY"]._serialized_end = 934
    _globals["_REVIEWEDBILLALLOCATIONVALUE"]._serialized_start = 937
    _globals["_REVIEWEDBILLALLOCATIONVALUE"]._serialized_end = 1298
    _globals["_REVIEWEDBILLITEMVALUE"]._serialized_start = 1301
    _globals["_REVIEWEDBILLITEMVALUE"]._serialized_end = 1548
# @@protoc_insertion_point(module_scope)