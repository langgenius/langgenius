# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/freightinvoice/draftinvoice/v1beta1/draft_invoice.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n@flexport/freightinvoice/draftinvoice/v1beta1/draft_invoice.proto\x12,flexport.freightinvoice.draftinvoice.v1beta1\x1a\x45\x66lexport/freightinvoice/draftinvoice/v1beta1/draft_invoice_item.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xcc\x07\n\x0c\x44raftInvoice\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x33\n\x0f\x63reated_at_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12M\n\x05items\x18\x03 \x03(\x0b\x32>.flexport.freightinvoice.draftinvoice.v1beta1.DraftInvoiceItem\x12\x17\n\x0finvoiceable_fid\x18\x04 \x01(\t\x12\x1c\n\x14invoicing_entity_fid\x18\x05 \x01(\t\x12\x1c\n\x14receiving_entity_fid\x18\x06 \x01(\t\x12O\n\x0cinvoice_type\x18\x07 \x01(\x0e\x32\x39.flexport.freightinvoice.draftinvoice.v1beta1.InvoiceType\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x12\n\nwas_shared\x18\t \x01(\x08\x12\x38\n\x14\x66irst_shared_at_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05notes\x18\x0b \x01(\t\x12\x18\n\x10\x65xchange_rate_id\x18\x0c \x01(\x05\x12\x33\n\x0fupdated_at_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x12is_capital_invoice\x18\x0e \x01(\x08\x12\x33\n\rrecipient_fid\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0e\x64\x65leted_by_fid\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0f\x64\x65leted_at_time\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\rshared_by_fid\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0e\x63reated_by_fid\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12W\n\x10invoiceable_type\x18\x14 \x01(\x0e\x32=.flexport.freightinvoice.draftinvoice.v1beta1.InvoiceableType\x12K\n\x06status\x18\x15 \x01(\x0e\x32;.flexport.freightinvoice.draftinvoice.v1beta1.InvoiceStatus*\xba\x01\n\x0bInvoiceType\x12\x18\n\x14INVOICE_TYPE_INVALID\x10\x00\x12\x18\n\x14INVOICE_TYPE_GENERAL\x10\x01\x12\x18\n\x14INVOICE_TYPE_CUSTOMS\x10\x02\x12\x18\n\x14INVOICE_TYPE_SHIPPER\x10\x03\x12\x19\n\x15INVOICE_TYPE_DRAWBACK\x10\x04\x12(\n$INVOICE_TYPE_DETENTION_AND_DEMURRAGE\x10\x05*k\n\x0fInvoiceableType\x12\x1c\n\x18INVOICEABLE_TYPE_INVALID\x10\x00\x12\x1d\n\x19INVOICEABLE_TYPE_SHIPMENT\x10\x01\x12\x1b\n\x17INVOICEABLE_TYPE_CLIENT\x10\x02*\xda\x01\n\rInvoiceStatus\x12\x1a\n\x16INVOICE_STATUS_INVALID\x10\x00\x12\x1b\n\x17INVOICE_STATUS_UNSHARED\x10\x01\x12\x1e\n\x1aINVOICE_STATUS_OUTSTANDING\x10\x02\x12"\n\x1eINVOICE_STATUS_PAYMENT_PENDING\x10\x03\x12\x17\n\x13INVOICE_STATUS_PAID\x10\x04\x12\x1a\n\x16INVOICE_STATUS_DELETED\x10\x05\x12\x17\n\x13INVOICE_STATUS_VOID\x10\x06\x42y\n0com.flexport.freightinvoice.draftinvoice.v1beta1B\x11\x44raftInvoiceProtoP\x01\xea\x02/Flexport::FreightInvoice::DraftInvoice::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.freightinvoice.draftinvoice.v1beta1.draft_invoice_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n0com.flexport.freightinvoice.draftinvoice.v1beta1B\021DraftInvoiceProtoP\001\352\002/Flexport::FreightInvoice::DraftInvoice::V1Beta1"
    _globals["_INVOICETYPE"]._serialized_start = 1226
    _globals["_INVOICETYPE"]._serialized_end = 1412
    _globals["_INVOICEABLETYPE"]._serialized_start = 1414
    _globals["_INVOICEABLETYPE"]._serialized_end = 1521
    _globals["_INVOICESTATUS"]._serialized_start = 1524
    _globals["_INVOICESTATUS"]._serialized_end = 1742
    _globals["_DRAFTINVOICE"]._serialized_start = 251
    _globals["_DRAFTINVOICE"]._serialized_end = 1223
# @@protoc_insertion_point(module_scope)