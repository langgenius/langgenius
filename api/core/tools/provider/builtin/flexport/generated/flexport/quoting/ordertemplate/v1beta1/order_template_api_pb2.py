# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/quoting/ordertemplate/v1beta1/order_template_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n?flexport/quoting/ordertemplate/v1beta1/order_template_api.proto\x12&flexport.quoting.ordertemplate.v1beta1\x1a;flexport/quoting/ordertemplate/v1beta1/order_template.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto"W\n\x1c\x42\x61tchGetOrderTemplateRequest\x12\x37\n\x12order_template_ids\x18\x01 \x03(\x0b\x32\x1b.google.protobuf.Int64Value"x\n\x1d\x42\x61tchGetOrderTemplateResponse\x12W\n\x14order_template_infos\x18\x01 \x03(\x0b\x32\x39.flexport.quoting.ordertemplate.v1beta1.OrderTemplateInfo"t\n\x1aUpsertOrderTemplateRequest\x12V\n\x13order_template_info\x18\x01 \x01(\x0b\x32\x39.flexport.quoting.ordertemplate.v1beta1.OrderTemplateInfo"\x94\x01\n\x1bUpsertOrderTemplateResponse\x12"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12;\n\x11order_template_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueH\x00\x88\x01\x01\x42\x14\n\x12_order_template_id"\x9f\x01\n\x1b\x41rchiveOrderTemplateRequest\x12\x36\n\x11order_template_id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x37\n\x0c\x61rchiver_fid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x88\x01\x01\x42\x0f\n\r_archiver_fid"B\n\x1c\x41rchiveOrderTemplateResponse\x12"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status2\xfe\x03\n\x10OrderTemplateAPI\x12\xa4\x01\n\x15\x42\x61tchGetOrderTemplate\x12\x44.flexport.quoting.ordertemplate.v1beta1.BatchGetOrderTemplateRequest\x1a\x45.flexport.quoting.ordertemplate.v1beta1.BatchGetOrderTemplateResponse\x12\x9e\x01\n\x13UpsertOrderTemplate\x12\x42.flexport.quoting.ordertemplate.v1beta1.UpsertOrderTemplateRequest\x1a\x43.flexport.quoting.ordertemplate.v1beta1.UpsertOrderTemplateResponse\x12\xa1\x01\n\x14\x41rchiveOrderTemplate\x12\x43.flexport.quoting.ordertemplate.v1beta1.ArchiveOrderTemplateRequest\x1a\x44.flexport.quoting.ordertemplate.v1beta1.ArchiveOrderTemplateResponseBq\n*com.flexport.quoting.ordertemplate.v1beta1B\x15OrderTemplateApiProtoP\x01\xea\x02)Flexport::Quoting::OrderTemplate::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.quoting.ordertemplate.v1beta1.order_template_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n*com.flexport.quoting.ordertemplate.v1beta1B\025OrderTemplateApiProtoP\001\352\002)Flexport::Quoting::OrderTemplate::V1Beta1"
    _globals["_BATCHGETORDERTEMPLATEREQUEST"]._serialized_start = 225
    _globals["_BATCHGETORDERTEMPLATEREQUEST"]._serialized_end = 312
    _globals["_BATCHGETORDERTEMPLATERESPONSE"]._serialized_start = 314
    _globals["_BATCHGETORDERTEMPLATERESPONSE"]._serialized_end = 434
    _globals["_UPSERTORDERTEMPLATEREQUEST"]._serialized_start = 436
    _globals["_UPSERTORDERTEMPLATEREQUEST"]._serialized_end = 552
    _globals["_UPSERTORDERTEMPLATERESPONSE"]._serialized_start = 555
    _globals["_UPSERTORDERTEMPLATERESPONSE"]._serialized_end = 703
    _globals["_ARCHIVEORDERTEMPLATEREQUEST"]._serialized_start = 706
    _globals["_ARCHIVEORDERTEMPLATEREQUEST"]._serialized_end = 865
    _globals["_ARCHIVEORDERTEMPLATERESPONSE"]._serialized_start = 867
    _globals["_ARCHIVEORDERTEMPLATERESPONSE"]._serialized_end = 933
    _globals["_ORDERTEMPLATEAPI"]._serialized_start = 936
    _globals["_ORDERTEMPLATEAPI"]._serialized_end = 1446
# @@protoc_insertion_point(module_scope)