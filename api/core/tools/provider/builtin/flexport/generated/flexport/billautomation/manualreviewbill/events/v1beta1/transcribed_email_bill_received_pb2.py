# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/billautomation/manualreviewbill/events/v1beta1/transcribed_email_bill_received.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n]flexport/billautomation/manualreviewbill/events/v1beta1/transcribed_email_bill_received.proto\x12\x37\x66lexport.billautomation.manualreviewbill.events.v1beta1\x1aMflexport/billautomation/manualreviewbill/v1beta1/transcribed_email_bill.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x9b\x02\n\x1cTranscribedEmailBillReceived\x12\x66\n\x16transcribed_email_bill\x18\x01 \x01(\x0b\x32\x46.flexport.billautomation.manualreviewbill.v1beta1.TranscribedEmailBill\x12=\n\x17\x64ocument_extraction_fid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x10received_at_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1e\n\x16\x61ttachment_fingerprint\x18\x04 \x01(\tB\xa0\x01\n;com.flexport.billautomation.manualreviewbill.events.v1beta1B!TranscribedEmailBillReceivedProtoP\x01\xea\x02;Flexport::BillAutomation::ManualReviewBill::Events::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.billautomation.manualreviewbill.events.v1beta1.transcribed_email_bill_received_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n;com.flexport.billautomation.manualreviewbill.events.v1beta1B!TranscribedEmailBillReceivedProtoP\001\352\002;Flexport::BillAutomation::ManualReviewBill::Events::V1Beta1"
    _globals["_TRANSCRIBEDEMAILBILLRECEIVED"]._serialized_start = 299
    _globals["_TRANSCRIBEDEMAILBILLRECEIVED"]._serialized_end = 582
# @@protoc_insertion_point(module_scope)