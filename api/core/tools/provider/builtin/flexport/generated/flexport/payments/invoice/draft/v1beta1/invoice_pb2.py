# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/payments/invoice/draft/v1beta1/invoice.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n5flexport/payments/invoice/draft/v1beta1/invoice.proto\x12\'flexport.payments.invoice.draft.v1beta1\x1a\x36\x66lexport/payments/creditmemo/v1beta1/credit_memo.proto\x1a\x39\x66lexport/payments/exchangerate/v1/exchange_rate_dto.proto\x1a,flexport/payments/invoice/date/v1/date.proto\x1a\x35\x66lexport/payments/payment/draft/v1beta1/payment.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xd9\x02\n\x04Item\x12\x15\n\ramount_micros\x18\x01 \x01(\x03\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x15\n\rcurrency_code\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0bnetsuite_id\x18\x05 \x01(\x05\x12%\n\x04meta\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x1c\n\x14quantity_description\x18\x07 \x01(\t\x12\x18\n\x10rate_description\x18\x08 \x01(\t\x12\x19\n\x11\x63ontainer_numbers\x18\t \x03(\t\x12\x0c\n\x04slug\x18\n \x01(\t\x12\x30\n\x0frate_attributes\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x34\n\x13quantity_attributes\x18\x0c \x01(\x0b\x32\x17.google.protobuf.Struct"\xed\x04\n\x07Invoice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x39\n\x08\x64ue_date\x18\x02 \x01(\x0b\x32\'.flexport.payments.invoice.date.v1.Date\x12\x32\n\x0eissued_at_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rcurrency_code\x18\x04 \x01(\t\x12\x30\n\x0f\x64isplay_context\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x30\n\x0f\x66ormatted_notes\x18\x06 \x03(\x0b\x32\x17.google.protobuf.Struct\x12(\n invoiceable_subledger_account_id\x18\x07 \x01(\x05\x12\x19\n\x11issuing_entity_id\x18\x08 \x01(\x05\x12\x1b\n\x13receiving_entity_id\x18\t \x01(\x05\x12\x1b\n\x13is_late_fee_invoice\x18\n \x01(\x08\x12\x1e\n\x16principle_invoice_name\x18\x0b \x01(\t\x12R\n\x10netsuite_context\x18\x0c \x01(\x0b\x32\x38.flexport.payments.invoice.draft.v1beta1.NetsuiteContext\x12\x1f\n\x17should_sync_to_netsuite\x18\r \x01(\x08\x12\x18\n\x10\x65xchange_rate_id\x18\x0e \x01(\x05\x12<\n\x05items\x18\x0f \x03(\x0b\x32-.flexport.payments.invoice.draft.v1beta1.Item"[\n\x0fNetsuiteContext\x12\x13\n\x0b\x63lient_name\x18\x01 \x01(\t\x12\x16\n\x0e\x63lient_segment\x18\x02 \x01(\t\x12\x1b\n\x13\x63lient_credit_terms\x18\x03 \x01(\x05"\xfd\x13\n\nInvoiceDto\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x30\n\x0b\x61mount_paid\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12;\n\x15\x61mount_paid_formatted\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x12\x61mount_paid_micros\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x35\n\x10\x61mount_remaining\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12@\n\x1a\x61mount_remaining_formatted\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12<\n\x17\x61mount_remaining_micros\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x05total\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x35\n\x0ftotal_formatted\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0ctotal_micros\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x37\n\x12items_total_micros\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0f\x63reated_at_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0foverdue_at_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0eissued_at_time\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0evoided_at_time\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\noverdue_by\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x30\n\x0cpaid_at_time\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0f\x61mended_at_time\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0eissuing_entity\x18\x13 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\x10receiving_entity\x18\x14 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x11issuing_entity_id\x18\x15 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x38\n\x13receiving_entity_id\x18\x16 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x39\n\x08\x64ue_date\x18\x17 \x01(\x0b\x32\'.flexport.payments.invoice.date.v1.Date\x12\x34\n\x0f\x63redits_applied\x18\x18 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12/\n\nitem_count\x18\x19 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12*\n\x04name\x18\x1a \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x62\x61se64_uu_id\x18\x1b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rcurrency_code\x18\x1c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12!\n\x19\x63onsolidated_invoice_fids\x18\x1d \x03(\t\x12,\n$unarchived_consolidated_invoice_fids\x18\x1e \x03(\t\x12\x30\n\x0f\x64isplay_context\x18\x1f \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x30\n\x0f\x66ormatted_notes\x18  \x03(\x0b\x32\x17.google.protobuf.Struct\x12(\n\x04void\x18! \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12(\n\x04paid\x18" \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x0boutstanding\x18# \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0epartially_paid\x18$ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x08\x66inanced\x18% \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\x11repayment_invoice\x18& \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x45\n invoiceable_subledger_account_id\x18\' \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12W\n\x12payment_line_items\x18( \x03(\x0b\x32;.flexport.payments.payment.draft.v1beta1.PaymentLineItemDto\x12R\n\x0fsurcharge_items\x18) \x03(\x0b\x32\x39.flexport.payments.payment.draft.v1beta1.SurchargeItemDto\x12I\n\x0c\x63redit_memos\x18* \x03(\x0b\x32\x33.flexport.payments.creditmemo.v1beta1.CreditMemoDto\x12I\n\rexchange_rate\x18+ \x01(\x0b\x32\x32.flexport.payments.exchangerate.v1.ExchangeRateDto\x12\x46\n\x06status\x18, \x01(\x0e\x32\x36.flexport.payments.invoice.draft.v1beta1.InvoiceStatus\x12\x34\n\x0ftotal_with_fees\x18- \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x46\n\x05items\x18. \x03(\x0b\x32\x37.flexport.payments.invoice.draft.v1beta1.InvoiceItemDto"\xfc\x05\n\x0eInvoiceItemDto\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12:\n\x15\x64raft_service_item_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x33\n\rcurrency_code\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x63\x61tegory\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0craw_category\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04slug\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14quantity_description\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x06\x61mount\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x32\n\ramount_micros\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\x16principle_invoice_name\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10rate_description\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\x0frate_attributes\x18\r \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x34\n\x13quantity_attributes\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x19\n\x11\x63ontainer_numbers\x18\x0f \x03(\t*\xbe\x01\n\rInvoiceStatus\x12\x1a\n\x16INVOICE_STATUS_INVALID\x10\x00\x12\x1b\n\x17INVOICE_STATUS_PAST_DUE\x10\x01\x12\x1e\n\x1aINVOICE_STATUS_OUTSTANDING\x10\x02\x12"\n\x1eINVOICE_STATUS_PAYMENT_PENDING\x10\x03\x12\x17\n\x13INVOICE_STATUS_PAID\x10\x04\x12\x17\n\x13INVOICE_STATUS_VOID\x10\x05\x42k\n+com.flexport.payments.invoice.draft.v1beta1B\x0cInvoiceProtoP\x01\xea\x02+Flexport::Payments::Invoice::Draft::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.payments.invoice.draft.v1beta1.invoice_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n+com.flexport.payments.invoice.draft.v1beta1B\014InvoiceProtoP\001\352\002+Flexport::Payments::Invoice::Draft::V1Beta1"
    _globals["_INVOICESTATUS"]._serialized_start = 4802
    _globals["_INVOICESTATUS"]._serialized_end = 4992
    _globals["_ITEM"]._serialized_start = 410
    _globals["_ITEM"]._serialized_end = 755
    _globals["_INVOICE"]._serialized_start = 758
    _globals["_INVOICE"]._serialized_end = 1379
    _globals["_NETSUITECONTEXT"]._serialized_start = 1381
    _globals["_NETSUITECONTEXT"]._serialized_end = 1472
    _globals["_INVOICEDTO"]._serialized_start = 1475
    _globals["_INVOICEDTO"]._serialized_end = 4032
    _globals["_INVOICEITEMDTO"]._serialized_start = 4035
    _globals["_INVOICEITEMDTO"]._serialized_end = 4799
# @@protoc_insertion_point(module_scope)