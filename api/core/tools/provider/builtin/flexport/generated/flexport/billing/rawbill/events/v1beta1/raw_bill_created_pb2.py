# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/billing/rawbill/events/v1beta1/raw_bill_created.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n>flexport/billing/rawbill/events/v1beta1/raw_bill_created.proto\x12'flexport.billing.rawbill.events.v1beta1\x1a(flexport/billing/bill/v1beta1/bill.proto\x1a?flexport/billing/rawbill/events/v1beta1/raw_bill_metadata.proto\"\x8f\x01\n\x0eRawBillCreated\x12\x31\n\x04\x62ill\x18\x01 \x01(\x0b\x32#.flexport.billing.bill.v1beta1.Bill\x12J\n\x08metadata\x18\x02 \x01(\x0b\x32\x38.flexport.billing.rawbill.events.v1beta1.RawBillMetadataBr\n+com.flexport.billing.rawbill.events.v1beta1B\x13RawBillCreatedProtoP\x01\xea\x02+Flexport::Billing::RawBill::Events::V1Beta1b\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.billing.rawbill.events.v1beta1.raw_bill_created_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n+com.flexport.billing.rawbill.events.v1beta1B\023RawBillCreatedProtoP\001\352\002+Flexport::Billing::RawBill::Events::V1Beta1"
    _globals["_RAWBILLCREATED"]._serialized_start = 215
    _globals["_RAWBILLCREATED"]._serialized_end = 358
# @@protoc_insertion_point(module_scope)