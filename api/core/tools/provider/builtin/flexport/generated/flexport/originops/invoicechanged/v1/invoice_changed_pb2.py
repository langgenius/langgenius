# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/originops/invoicechanged/v1/invoice_changed.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n:flexport/originops/invoicechanged/v1/invoice_changed.proto\x12$flexport.originops.invoicechanged.v1\x1a?flexport/originops/eventrootcontext/v1/event_root_context.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd6\x04\n\x0eInvoiceChanged\x12\n\n\x02id\x18\x01 \x01(\t\x12\x43\n\x06status\x18\x02 \x01(\x0e\x32\x33.flexport.originops.invoicechanged.v1.InvoiceStatus\x12\x14\n\x0cshipment_fid\x18\x03 \x01(\t\x12\x33\n\x0f\x63reated_at_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12T\n\x12\x65vent_root_context\x18\x06 \x01(\x0b\x32\x38.flexport.originops.eventrootcontext.v1.EventRootContext\x12\x1c\n\x14receiving_entity_fid\x18\x07 \x01(\t\x12\x14\n\x0ctotal_amount\x18\x08 \x01(\t\x12\x1a\n\x12\x62\x61se_currency_code\x18\t \x01(\t\x12.\n\nissue_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10payment_due_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10\x63redit_term_days\x18\x0c \x01(\x03\x12\x1f\n\x17\x63redit_profile_approved\x18\r \x01(\x08\x12\x12\n\ninvoice_id\x18\x0e \x01(\t\x12\x18\n\x10total_usd_amount\x18\x0f \x01(\t*\xda\x01\n\rInvoiceStatus\x12\x1a\n\x16INVOICE_STATUS_INVALID\x10\x00\x12\x1e\n\x1aINVOICE_STATUS_OUTSTANDING\x10\x01\x12\x1b\n\x17INVOICE_STATUS_UNSHARED\x10\x02\x12"\n\x1eINVOICE_STATUS_PAYMENT_PENDING\x10\x03\x12\x17\n\x13INVOICE_STATUS_PAID\x10\x04\x12\x1a\n\x16INVOICE_STATUS_DELETED\x10\x05\x12\x17\n\x13INVOICE_STATUS_VOID\x10\x06\x42k\n(com.flexport.originops.invoicechanged.v1B\x13InvoiceChangedProtoP\x01\xea\x02\'Flexport::OriginOps::InvoiceChanged::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.originops.invoicechanged.v1.invoice_changed_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n(com.flexport.originops.invoicechanged.v1B\023InvoiceChangedProtoP\001\352\002'Flexport::OriginOps::InvoiceChanged::V1"
    _globals["_INVOICESTATUS"]._serialized_start = 800
    _globals["_INVOICESTATUS"]._serialized_end = 1018
    _globals["_INVOICECHANGED"]._serialized_start = 199
    _globals["_INVOICECHANGED"]._serialized_end = 797
# @@protoc_insertion_point(module_scope)