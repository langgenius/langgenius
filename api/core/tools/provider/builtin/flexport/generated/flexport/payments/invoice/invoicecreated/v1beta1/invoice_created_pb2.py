# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/payments/invoice/invoicecreated/v1beta1/invoice_created.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nFflexport/payments/invoice/invoicecreated/v1beta1/invoice_created.proto\x12\x30\x66lexport.payments.invoice.invoicecreated.v1beta1\x1a/flexport/payments/invoice/v1beta1/invoice.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x9d\x01\n\x0eInvoiceCreated\x12;\n\x07invoice\x18\x01 \x01(\x0b\x32*.flexport.payments.invoice.v1beta1.Invoice\x12\x17\n\x0f\x61\x63ting_user_fid\x18\x02 \x01(\t\x12\x35\n\x10\x61\x63ting_user_dbid\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueB\x84\x01\n4com.flexport.payments.invoice.invoicecreated.v1beta1B\x13InvoiceCreatedProtoP\x01\xea\x02\x34\x46lexport::Payments::Invoice::InvoiceCreated::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.payments.invoice.invoicecreated.v1beta1.invoice_created_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n4com.flexport.payments.invoice.invoicecreated.v1beta1B\023InvoiceCreatedProtoP\001\352\0024Flexport::Payments::Invoice::InvoiceCreated::V1Beta1"
    _globals["_INVOICECREATED"]._serialized_start = 206
    _globals["_INVOICECREATED"]._serialized_end = 363
# @@protoc_insertion_point(module_scope)