# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/freightinvoice/leakagereview/v1beta1/leakage_review.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nBflexport/freightinvoice/leakagereview/v1beta1/leakage_review.proto\x12-flexport.freightinvoice.leakagereview.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xa0\x01\n\x13LeakageReviewReport\x12\x14\n\x0cshipment_fid\x18\x01 \x01(\t\x12\x15\n\rcurrency_code\x18\x02 \x01(\t\x12\\\n\x13lr_category_reports\x18\x03 \x03(\x0b\x32?.flexport.freightinvoice.leakagereview.v1beta1.LRCategoryReport"\xbb\x01\n\x10LRCategoryReport\x12\x13\n\x0blr_category\x18\x01 \x01(\t\x12\x33\n\x0frequires_action\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12]\n\x0c\x65xplanations\x18\x03 \x03(\x0b\x32G.flexport.freightinvoice.leakagereview.v1beta1.LeakageReviewExplanation"p\n\x18LeakageReviewExplanation\x12\x35\n\x11\x65xplained_at_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\x15\x65xplained_by_user_fid\x18\x02 \x01(\t"O\n\x19LeakageExplanationCreated\x12\x14\n\x0cshipment_fid\x18\x01 \x01(\t\x12\x1c\n\x14vendor_bill_item_fid\x18\x02 \x01(\tB|\n1com.flexport.freightinvoice.leakagereview.v1beta1B\x12LeakageReviewProtoP\x01\xea\x02\x30\x46lexport::FreightInvoice::LeakageReview::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.freightinvoice.leakagereview.v1beta1.leakage_review_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n1com.flexport.freightinvoice.leakagereview.v1beta1B\022LeakageReviewProtoP\001\352\0020Flexport::FreightInvoice::LeakageReview::V1Beta1"
    _globals["_LEAKAGEREVIEWREPORT"]._serialized_start = 183
    _globals["_LEAKAGEREVIEWREPORT"]._serialized_end = 343
    _globals["_LRCATEGORYREPORT"]._serialized_start = 346
    _globals["_LRCATEGORYREPORT"]._serialized_end = 533
    _globals["_LEAKAGEREVIEWEXPLANATION"]._serialized_start = 535
    _globals["_LEAKAGEREVIEWEXPLANATION"]._serialized_end = 647
    _globals["_LEAKAGEEXPLANATIONCREATED"]._serialized_start = 649
    _globals["_LEAKAGEEXPLANATIONCREATED"]._serialized_end = 728
# @@protoc_insertion_point(module_scope)