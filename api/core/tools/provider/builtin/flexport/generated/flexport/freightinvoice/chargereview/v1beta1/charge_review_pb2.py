# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/freightinvoice/chargereview/v1beta1/charge_review.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n@flexport/freightinvoice/chargereview/v1beta1/charge_review.proto\x12,flexport.freightinvoice.chargereview.v1beta1\x1a\x45\x66lexport/freightinvoice/draftinvoice/v1beta1/draft_invoice_item.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xa0\x02\n\x0c\x43hargeReview\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12[\n\x13\x63harge_review_items\x18\x02 \x03(\x0b\x32>.flexport.freightinvoice.chargereview.v1beta1.ChargeReviewItem\x12\x32\n\x0cshipment_fid\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x12last_actioned_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x14last_actioned_by_fid\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xa0\x02\n\x10\x43hargeReviewItem\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12g\n\x19\x63harge_review_item_status\x18\x02 \x01(\x0e\x32\x44.flexport.freightinvoice.chargereview.v1beta1.ChargeReviewItemStatus\x12Z\n\x12\x64raft_invoice_item\x18\x03 \x01(\x0b\x32>.flexport.freightinvoice.draftinvoice.v1beta1.DraftInvoiceItem\x12:\n\x14last_actioned_by_fid\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue*\xdd\x02\n\x16\x43hargeReviewItemStatus\x12%\n!CHARGE_REVIEW_ITEM_STATUS_INVALID\x10\x00\x12%\n!CHARGE_REVIEW_ITEM_STATUS_PENDING\x10\x01\x12#\n\x1f\x43HARGE_REVIEW_ITEM_STATUS_READY\x10\x02\x12&\n\"CHARGE_REVIEW_ITEM_STATUS_REJECTED\x10\x03\x12+\n'CHARGE_REVIEW_ITEM_STATUS_USER_ACCEPTED\x10\x04\x12'\n#CHARGE_REVIEW_ITEM_STATUS_NO_CHARGE\x10\x05\x12+\n'CHARGE_REVIEW_ITEM_STATUS_AUTO_ACCEPTED\x10\x06\x12%\n!CHARGE_REVIEW_ITEM_STATUS_DELETED\x10\x07\x42y\n0com.flexport.freightinvoice.chargereview.v1beta1B\x11\x43hargeReviewProtoP\x01\xea\x02/Flexport::FreightInvoice::ChargeReview::V1Beta1b\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.freightinvoice.chargereview.v1beta1.charge_review_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n0com.flexport.freightinvoice.chargereview.v1beta1B\021ChargeReviewProtoP\001\352\002/Flexport::FreightInvoice::ChargeReview::V1Beta1"
    _globals["_CHARGEREVIEWITEMSTATUS"]._serialized_start = 833
    _globals["_CHARGEREVIEWITEMSTATUS"]._serialized_end = 1182
    _globals["_CHARGEREVIEW"]._serialized_start = 251
    _globals["_CHARGEREVIEW"]._serialized_end = 539
    _globals["_CHARGEREVIEWITEM"]._serialized_start = 542
    _globals["_CHARGEREVIEWITEM"]._serialized_end = 830
# @@protoc_insertion_point(module_scope)