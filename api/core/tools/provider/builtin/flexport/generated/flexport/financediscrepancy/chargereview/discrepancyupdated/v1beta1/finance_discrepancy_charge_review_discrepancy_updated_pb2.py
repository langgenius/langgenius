# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/financediscrepancy/chargereview/discrepancyupdated/v1beta1/finance_discrepancy_charge_review_discrepancy_updated.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x7f\x66lexport/financediscrepancy/chargereview/discrepancyupdated/v1beta1/finance_discrepancy_charge_review_discrepancy_updated.proto\x12\x43\x66lexport.financediscrepancy.chargereview.discrepancyupdated.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\xc3\x02\n\x12\x44iscrepancyUpdated\x12\x19\n\x11\x63harge_review_fid\x18\x01 \x01(\t\x12\x1e\n\x16\x63harge_review_item_fid\x18\x02 \x01(\t\x12*\n"charge_review_item_discrepancy_fid\x18\x03 \x01(\t\x12\x34\n\x10resolved_at_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x14resolved_by_user_fid\x18\x05 \x01(\t\x12r\n\x12\x64iscrepancy_status\x18\x06 \x01(\x0e\x32V.flexport.financediscrepancy.chargereview.discrepancyupdated.v1beta1.DiscrepancyStatus*\x7f\n\x11\x44iscrepancyStatus\x12\x1e\n\x1a\x44ISCREPANCY_STATUS_INVALID\x10\x00\x12)\n%DISCREPANCY_STATUS_OFFERING_CORRECTED\x10\x01\x12\x1f\n\x1b\x44ISCREPANCY_STATUS_DISAGREE\x10\x02\x42\xcc\x01\nGcom.flexport.financediscrepancy.chargereview.discrepancyupdated.v1beta1B5FinanceDiscrepancyChargeReviewDiscrepancyUpdatedProtoP\x01\xea\x02GFlexport::FinanceDiscrepancy::ChargeReview::DiscrepancyUpdated::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.financediscrepancy.chargereview.discrepancyupdated.v1beta1.finance_discrepancy_charge_review_discrepancy_updated_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\nGcom.flexport.financediscrepancy.chargereview.discrepancyupdated.v1beta1B5FinanceDiscrepancyChargeReviewDiscrepancyUpdatedProtoP\001\352\002GFlexport::FinanceDiscrepancy::ChargeReview::DiscrepancyUpdated::V1Beta1"
    _globals["_DISCREPANCYSTATUS"]._serialized_start = 559
    _globals["_DISCREPANCYSTATUS"]._serialized_end = 686
    _globals["_DISCREPANCYUPDATED"]._serialized_start = 234
    _globals["_DISCREPANCYUPDATED"]._serialized_end = 557
# @@protoc_insertion_point(module_scope)