# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/billing/entityevent/v1beta1/bill_audit_entity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n<flexport/billing/entityevent/v1beta1/bill_audit_entity.proto\x12$flexport.billing.entityevent.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xd0\x04\n\x0f\x42illAuditEntity\x12)\n\x03\x66id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x62ill_fid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0brisk_rating\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x45\n\x06status\x18\x04 \x01(\x0e\x32\x35.flexport.billing.entityevent.v1beta1.BillAuditStatus\x12\x35\n\x0f\x61ssigned_to_fid\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x0b\x64ue_at_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0f\x63reated_at_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12L\n\x07\x63ontext\x18\t \x01(\x0b\x32;.flexport.billing.entityevent.v1beta1.BillAuditContextValue\x12H\n\x05issue\x18\n \x03(\x0b\x32\x39.flexport.billing.entityevent.v1beta1.BillAuditIssueValue"\xfe\x01\n\x15\x42illAuditContextValue\x12-\n\x08revision\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0f\x63reated_at_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12L\n\x07section\x18\x04 \x03(\x0b\x32;.flexport.billing.entityevent.v1beta1.BillAuditSectionValue"\xf5\x08\n\x15\x42illAuditSectionValue\x12)\n\x03key\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12H\n\x04type\x18\x02 \x01(\x0e\x32:.flexport.billing.entityevent.v1beta1.BillAuditSectionType\x12\x33\n\x0f\x63reated_at_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12y\n$bill_epc_data_audit_section_metadata\x18\x05 \x01(\x0b\x32\x45.flexport.billing.entityevent.v1beta1.BillEpcDataAuditSectionMetadataB\x02\x18\x01H\x00\x12|\n\'shipment_details_audit_section_metadata\x18\x06 \x01(\x0b\x32I.flexport.billing.entityevent.v1beta1.ShipmentDetailsAuditSectionMetadataH\x00\x12\x81\x01\n(shipment_epc_data_audit_section_metadata\x18\x07 \x01(\x0b\x32I.flexport.billing.entityevent.v1beta1.ShipmentEpcDataAuditSectionMetadataB\x02\x18\x01H\x00\x12\x87\x01\n+vendor_currency_data_audit_section_metadata\x18\x08 \x01(\x0b\x32L.flexport.billing.entityevent.v1beta1.VendorCurrencyDataAuditSectionMetadataB\x02\x18\x01H\x00\x12|\n%shipment_flags_audit_section_metadata\x18\t \x01(\x0b\x32G.flexport.billing.entityevent.v1beta1.ShipmentFlagsAuditSectionMetadataB\x02\x18\x01H\x00\x12l\n\x1f\x65pc_data_audit_section_metadata\x18\n \x01(\x0b\x32\x41.flexport.billing.entityevent.v1beta1.EpcDataAuditSectionMetadataH\x00\x12~\n(shipment_messages_audit_section_metadata\x18\x0b \x01(\x0b\x32J.flexport.billing.entityevent.v1beta1.ShipmentMessagesAuditSectionMetadataH\x00\x42\n\n\x08metadata"!\n\x1f\x42illEpcDataAuditSectionMetadata"%\n#ShipmentDetailsAuditSectionMetadata"%\n#ShipmentEpcDataAuditSectionMetadata"(\n&VendorCurrencyDataAuditSectionMetadata"#\n!ShipmentFlagsAuditSectionMetadata"\x1d\n\x1b\x45pcDataAuditSectionMetadata"&\n$ShipmentMessagesAuditSectionMetadata"\x89\r\n\x13\x42illAuditIssueValue\x12\x46\n\x04type\x18\x01 \x01(\x0e\x32\x38.flexport.billing.entityevent.v1beta1.BillAuditIssueType\x12\x36\n\x10source_validator\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x61\x66\x66\x65\x63ted_feature\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nrisk_score\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x33\n\x0f\x63reated_at_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12l\n\x1d\x62\x63o_bill_audit_issue_metadata\x18\x07 \x01(\x0b\x32?.flexport.billing.entityevent.v1beta1.BcoBillAuditIssueMetadataB\x02\x18\x01H\x00\x12n\n missing_epc_audit_issue_metadata\x18\x08 \x01(\x0b\x32\x42.flexport.billing.entityevent.v1beta1.MissingEpcAuditIssueMetadataH\x00\x12|\n\'possible_duplicate_audit_issue_metadata\x18\t \x01(\x0b\x32I.flexport.billing.entityevent.v1beta1.PossibleDuplicateAuditIssueMetadataH\x00\x12}\n(potential_late_bill_audit_issue_metadata\x18\n \x01(\x0b\x32I.flexport.billing.entityevent.v1beta1.PotentialLateBillAuditIssueMetadataH\x00\x12}\n(charge_epc_mismatch_audit_issue_metadata\x18\x0b \x01(\x0b\x32I.flexport.billing.entityevent.v1beta1.ChargeEpcMismatchAuditIssueMetadataH\x00\x12z\n\'flagged_do_not_pay_audit_issue_metadata\x18\x0c \x01(\x0b\x32G.flexport.billing.entityevent.v1beta1.FlaggedDoNotPayAuditIssueMetadataH\x00\x12\x8d\x01\n1billed_cost_out_of_tolerance_audit_issue_metadata\x18\r \x01(\x0b\x32P.flexport.billing.entityevent.v1beta1.BilledCostOutOfToleranceAuditIssueMetadataH\x00\x12\x8f\x01\n/unexpected_vendor_currency_audit_issue_metadata\x18\x0e \x01(\x0b\x32P.flexport.billing.entityevent.v1beta1.UnexpectedVendorCurrencyAuditIssueMetadataB\x02\x18\x01H\x00\x12\x81\x01\n*missing_audit_section_audit_issue_metadata\x18\x0f \x01(\x0b\x32K.flexport.billing.entityevent.v1beta1.MissingAuditSectionAuditIssueMetadataH\x00\x12\x95\x01\n5missing_audit_section_data_point_audit_issue_metadata\x18\x10 \x01(\x0b\x32T.flexport.billing.entityevent.v1beta1.MissingAuditSectionDataPointAuditIssueMetadataH\x00\x42\n\n\x08metadata"\x1b\n\x19\x42\x63oBillAuditIssueMetadata"\x1e\n\x1cMissingEpcAuditIssueMetadata"%\n#PossibleDuplicateAuditIssueMetadata"%\n#PotentialLateBillAuditIssueMetadata"%\n#ChargeEpcMismatchAuditIssueMetadata"#\n!FlaggedDoNotPayAuditIssueMetadata",\n*BilledCostOutOfToleranceAuditIssueMetadata",\n*UnexpectedVendorCurrencyAuditIssueMetadata"\'\n%MissingAuditSectionAuditIssueMetadata"0\n.MissingAuditSectionDataPointAuditIssueMetadata*\xb5\x02\n\x0f\x42illAuditStatus\x12\x1d\n\x19\x42ILL_AUDIT_STATUS_INVALID\x10\x00\x12"\n\x1e\x42ILL_AUDIT_STATUS_INITIALIZING\x10\x01\x12\x1d\n\x19\x42ILL_AUDIT_STATUS_PENDING\x10\x02\x12\x1e\n\x1a\x42ILL_AUDIT_STATUS_DISPUTED\x10\x03\x12\x1f\n\x1b\x42ILL_AUDIT_STATUS_ESCALATED\x10\x04\x12\x1e\n\x1a\x42ILL_AUDIT_STATUS_APPROVED\x10\x05\x12\x1e\n\x1a\x42ILL_AUDIT_STATUS_REOPENED\x10\x06\x12\x1e\n\x1a\x42ILL_AUDIT_STATUS_REJECTED\x10\x07\x12\x1f\n\x1b\x42ILL_AUDIT_STATUS_CANCELLED\x10\x08*\x86\x03\n\x14\x42illAuditSectionType\x12#\n\x1f\x42ILL_AUDIT_SECTION_TYPE_INVALID\x10\x00\x12-\n%BILL_AUDIT_SECTION_TYPE_BILL_EPC_DATA\x10\x01\x1a\x02\x08\x01\x12,\n(BILL_AUDIT_SECTION_TYPE_SHIPMENT_DETAILS\x10\x02\x12\x31\n)BILL_AUDIT_SECTION_TYPE_SHIPMENT_EPC_DATA\x10\x03\x1a\x02\x08\x01\x12\x34\n,BILL_AUDIT_SECTION_TYPE_VENDOR_CURRENCY_DATA\x10\x04\x1a\x02\x08\x01\x12.\n&BILL_AUDIT_SECTION_TYPE_SHIPMENT_FLAGS\x10\x05\x1a\x02\x08\x01\x12$\n BILL_AUDIT_SECTION_TYPE_EPC_DATA\x10\x06\x12-\n)BILL_AUDIT_SECTION_TYPE_SHIPMENT_MESSAGES\x10\x07*\x9f\x04\n\x12\x42illAuditIssueType\x12!\n\x1d\x42ILL_AUDIT_ISSUE_TYPE_INVALID\x10\x00\x12%\n!BILL_AUDIT_ISSUE_TYPE_MISSING_EPC\x10\x01\x12,\n(BILL_AUDIT_ISSUE_TYPE_POSSIBLE_DUPLICATE\x10\x02\x12-\n)BILL_AUDIT_ISSUE_TYPE_POTENTIAL_LATE_BILL\x10\x03\x12-\n)BILL_AUDIT_ISSUE_TYPE_CHARGE_EPC_MISMATCH\x10\x04\x12,\n(BILL_AUDIT_ISSUE_TYPE_FLAGGED_DO_NOT_PAY\x10\x05\x12\x36\n2BILL_AUDIT_ISSUE_TYPE_BILLED_COST_OUT_OF_TOLERANCE\x10\x06\x12&\n\x1e\x42ILL_AUDIT_ISSUE_TYPE_BCO_BILL\x10\x07\x1a\x02\x08\x01\x12\x38\n0BILL_AUDIT_ISSUE_TYPE_UNEXPECTED_VENDOR_CURRENCY\x10\x08\x1a\x02\x08\x01\x12/\n+BILL_AUDIT_ISSUE_TYPE_MISSING_AUDIT_SECTION\x10\t\x12:\n6BILL_AUDIT_ISSUE_TYPE_MISSING_AUDIT_SECTION_DATA_POINT\x10\nBl\n(com.flexport.billing.entityevent.v1beta1B\x14\x42illAuditEntityProtoP\x01\xea\x02\'Flexport::Billing::EntityEvent::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.billing.entityevent.v1beta1.bill_audit_entity_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n(com.flexport.billing.entityevent.v1beta1B\024BillAuditEntityProtoP\001\352\002'Flexport::Billing::EntityEvent::V1Beta1"
    _globals["_BILLAUDITSECTIONTYPE"].values_by_name["BILL_AUDIT_SECTION_TYPE_BILL_EPC_DATA"]._options = None
    _globals["_BILLAUDITSECTIONTYPE"].values_by_name[
        "BILL_AUDIT_SECTION_TYPE_BILL_EPC_DATA"
    ]._serialized_options = b"\010\001"
    _globals["_BILLAUDITSECTIONTYPE"].values_by_name["BILL_AUDIT_SECTION_TYPE_SHIPMENT_EPC_DATA"]._options = None
    _globals["_BILLAUDITSECTIONTYPE"].values_by_name[
        "BILL_AUDIT_SECTION_TYPE_SHIPMENT_EPC_DATA"
    ]._serialized_options = b"\010\001"
    _globals["_BILLAUDITSECTIONTYPE"].values_by_name["BILL_AUDIT_SECTION_TYPE_VENDOR_CURRENCY_DATA"]._options = None
    _globals["_BILLAUDITSECTIONTYPE"].values_by_name[
        "BILL_AUDIT_SECTION_TYPE_VENDOR_CURRENCY_DATA"
    ]._serialized_options = b"\010\001"
    _globals["_BILLAUDITSECTIONTYPE"].values_by_name["BILL_AUDIT_SECTION_TYPE_SHIPMENT_FLAGS"]._options = None
    _globals["_BILLAUDITSECTIONTYPE"].values_by_name[
        "BILL_AUDIT_SECTION_TYPE_SHIPMENT_FLAGS"
    ]._serialized_options = b"\010\001"
    _globals["_BILLAUDITISSUETYPE"].values_by_name["BILL_AUDIT_ISSUE_TYPE_BCO_BILL"]._options = None
    _globals["_BILLAUDITISSUETYPE"].values_by_name["BILL_AUDIT_ISSUE_TYPE_BCO_BILL"]._serialized_options = b"\010\001"
    _globals["_BILLAUDITISSUETYPE"].values_by_name["BILL_AUDIT_ISSUE_TYPE_UNEXPECTED_VENDOR_CURRENCY"]._options = None
    _globals["_BILLAUDITISSUETYPE"].values_by_name[
        "BILL_AUDIT_ISSUE_TYPE_UNEXPECTED_VENDOR_CURRENCY"
    ]._serialized_options = b"\010\001"
    _globals["_BILLAUDITSECTIONVALUE"].fields_by_name["bill_epc_data_audit_section_metadata"]._options = None
    _globals["_BILLAUDITSECTIONVALUE"].fields_by_name[
        "bill_epc_data_audit_section_metadata"
    ]._serialized_options = b"\030\001"
    _globals["_BILLAUDITSECTIONVALUE"].fields_by_name["shipment_epc_data_audit_section_metadata"]._options = None
    _globals["_BILLAUDITSECTIONVALUE"].fields_by_name[
        "shipment_epc_data_audit_section_metadata"
    ]._serialized_options = b"\030\001"
    _globals["_BILLAUDITSECTIONVALUE"].fields_by_name["vendor_currency_data_audit_section_metadata"]._options = None
    _globals["_BILLAUDITSECTIONVALUE"].fields_by_name[
        "vendor_currency_data_audit_section_metadata"
    ]._serialized_options = b"\030\001"
    _globals["_BILLAUDITSECTIONVALUE"].fields_by_name["shipment_flags_audit_section_metadata"]._options = None
    _globals["_BILLAUDITSECTIONVALUE"].fields_by_name[
        "shipment_flags_audit_section_metadata"
    ]._serialized_options = b"\030\001"
    _globals["_BILLAUDITISSUEVALUE"].fields_by_name["bco_bill_audit_issue_metadata"]._options = None
    _globals["_BILLAUDITISSUEVALUE"].fields_by_name["bco_bill_audit_issue_metadata"]._serialized_options = b"\030\001"
    _globals["_BILLAUDITISSUEVALUE"].fields_by_name["unexpected_vendor_currency_audit_issue_metadata"]._options = None
    _globals["_BILLAUDITISSUEVALUE"].fields_by_name[
        "unexpected_vendor_currency_audit_issue_metadata"
    ]._serialized_options = b"\030\001"
    _globals["_BILLAUDITSTATUS"]._serialized_start = 4501
    _globals["_BILLAUDITSTATUS"]._serialized_end = 4810
    _globals["_BILLAUDITSECTIONTYPE"]._serialized_start = 4813
    _globals["_BILLAUDITSECTIONTYPE"]._serialized_end = 5203
    _globals["_BILLAUDITISSUETYPE"]._serialized_start = 5206
    _globals["_BILLAUDITISSUETYPE"]._serialized_end = 5749
    _globals["_BILLAUDITENTITY"]._serialized_start = 168
    _globals["_BILLAUDITENTITY"]._serialized_end = 760
    _globals["_BILLAUDITCONTEXTVALUE"]._serialized_start = 763
    _globals["_BILLAUDITCONTEXTVALUE"]._serialized_end = 1017
    _globals["_BILLAUDITSECTIONVALUE"]._serialized_start = 1020
    _globals["_BILLAUDITSECTIONVALUE"]._serialized_end = 2161
    _globals["_BILLEPCDATAAUDITSECTIONMETADATA"]._serialized_start = 2163
    _globals["_BILLEPCDATAAUDITSECTIONMETADATA"]._serialized_end = 2196
    _globals["_SHIPMENTDETAILSAUDITSECTIONMETADATA"]._serialized_start = 2198
    _globals["_SHIPMENTDETAILSAUDITSECTIONMETADATA"]._serialized_end = 2235
    _globals["_SHIPMENTEPCDATAAUDITSECTIONMETADATA"]._serialized_start = 2237
    _globals["_SHIPMENTEPCDATAAUDITSECTIONMETADATA"]._serialized_end = 2274
    _globals["_VENDORCURRENCYDATAAUDITSECTIONMETADATA"]._serialized_start = 2276
    _globals["_VENDORCURRENCYDATAAUDITSECTIONMETADATA"]._serialized_end = 2316
    _globals["_SHIPMENTFLAGSAUDITSECTIONMETADATA"]._serialized_start = 2318
    _globals["_SHIPMENTFLAGSAUDITSECTIONMETADATA"]._serialized_end = 2353
    _globals["_EPCDATAAUDITSECTIONMETADATA"]._serialized_start = 2355
    _globals["_EPCDATAAUDITSECTIONMETADATA"]._serialized_end = 2384
    _globals["_SHIPMENTMESSAGESAUDITSECTIONMETADATA"]._serialized_start = 2386
    _globals["_SHIPMENTMESSAGESAUDITSECTIONMETADATA"]._serialized_end = 2424
    _globals["_BILLAUDITISSUEVALUE"]._serialized_start = 2427
    _globals["_BILLAUDITISSUEVALUE"]._serialized_end = 4100
    _globals["_BCOBILLAUDITISSUEMETADATA"]._serialized_start = 4102
    _globals["_BCOBILLAUDITISSUEMETADATA"]._serialized_end = 4129
    _globals["_MISSINGEPCAUDITISSUEMETADATA"]._serialized_start = 4131
    _globals["_MISSINGEPCAUDITISSUEMETADATA"]._serialized_end = 4161
    _globals["_POSSIBLEDUPLICATEAUDITISSUEMETADATA"]._serialized_start = 4163
    _globals["_POSSIBLEDUPLICATEAUDITISSUEMETADATA"]._serialized_end = 4200
    _globals["_POTENTIALLATEBILLAUDITISSUEMETADATA"]._serialized_start = 4202
    _globals["_POTENTIALLATEBILLAUDITISSUEMETADATA"]._serialized_end = 4239
    _globals["_CHARGEEPCMISMATCHAUDITISSUEMETADATA"]._serialized_start = 4241
    _globals["_CHARGEEPCMISMATCHAUDITISSUEMETADATA"]._serialized_end = 4278
    _globals["_FLAGGEDDONOTPAYAUDITISSUEMETADATA"]._serialized_start = 4280
    _globals["_FLAGGEDDONOTPAYAUDITISSUEMETADATA"]._serialized_end = 4315
    _globals["_BILLEDCOSTOUTOFTOLERANCEAUDITISSUEMETADATA"]._serialized_start = 4317
    _globals["_BILLEDCOSTOUTOFTOLERANCEAUDITISSUEMETADATA"]._serialized_end = 4361
    _globals["_UNEXPECTEDVENDORCURRENCYAUDITISSUEMETADATA"]._serialized_start = 4363
    _globals["_UNEXPECTEDVENDORCURRENCYAUDITISSUEMETADATA"]._serialized_end = 4407
    _globals["_MISSINGAUDITSECTIONAUDITISSUEMETADATA"]._serialized_start = 4409
    _globals["_MISSINGAUDITSECTIONAUDITISSUEMETADATA"]._serialized_end = 4448
    _globals["_MISSINGAUDITSECTIONDATAPOINTAUDITISSUEMETADATA"]._serialized_start = 4450
    _globals["_MISSINGAUDITSECTIONDATAPOINTAUDITISSUEMETADATA"]._serialized_end = 4498
# @@protoc_insertion_point(module_scope)