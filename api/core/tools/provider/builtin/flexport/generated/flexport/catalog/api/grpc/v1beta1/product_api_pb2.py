# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/catalog/api/grpc/v1beta1/product_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n3flexport/catalog/api/grpc/v1beta1/product_api.proto\x12!flexport.catalog.api.grpc.v1beta1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17google/rpc/status.proto""\n\x14ProductEntryInstance\x12\n\n\x02id\x18\x01 \x01(\t"\x99\x01\n\x1a\x43reateProductEntryResponse\x12"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12L\n\x06\x65ntity\x18\x02 \x01(\x0b\x32\x37.flexport.catalog.api.grpc.v1beta1.ProductEntryInstanceH\x00\x88\x01\x01\x42\t\n\x07_entity"\xa7\x01\n\x19\x43reateProductEntryRequest\x12\x11\n\tschema_id\x18\x01 \x01(\t\x12\x36\n\x10\x61ttribute_values\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x88\x01\x01\x12\x19\n\x0c\x64istinct_key\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x13\n\x11_attribute_valuesB\x0f\n\r_distinct_key"E\n\x1bSearchProductEntriesRequest\x12&\n\x05query\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct"t\n\x1cSearchProductEntriesResponse\x12"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x30\n\x0fproduct_entries\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct2\xbf\x02\n\x0fProductEntryAPI\x12\x91\x01\n\x12\x43reateProductEntry\x12<.flexport.catalog.api.grpc.v1beta1.CreateProductEntryRequest\x1a=.flexport.catalog.api.grpc.v1beta1.CreateProductEntryResponse\x12\x97\x01\n\x14SearchProductEntries\x12>.flexport.catalog.api.grpc.v1beta1.SearchProductEntriesRequest\x1a?.flexport.catalog.api.grpc.v1beta1.SearchProductEntriesResponseBb\n-com.flexport.catalog.product.api.grpc.v1beta1P\x01\xea\x02.Flexport::Catalog::Product::Api::Gprc::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.catalog.api.grpc.v1beta1.product_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n-com.flexport.catalog.product.api.grpc.v1beta1P\001\352\002.Flexport::Catalog::Product::Api::Gprc::V1Beta1"
    )
    _globals["_PRODUCTENTRYINSTANCE"]._serialized_start = 145
    _globals["_PRODUCTENTRYINSTANCE"]._serialized_end = 179
    _globals["_CREATEPRODUCTENTRYRESPONSE"]._serialized_start = 182
    _globals["_CREATEPRODUCTENTRYRESPONSE"]._serialized_end = 335
    _globals["_CREATEPRODUCTENTRYREQUEST"]._serialized_start = 338
    _globals["_CREATEPRODUCTENTRYREQUEST"]._serialized_end = 505
    _globals["_SEARCHPRODUCTENTRIESREQUEST"]._serialized_start = 507
    _globals["_SEARCHPRODUCTENTRIESREQUEST"]._serialized_end = 576
    _globals["_SEARCHPRODUCTENTRIESRESPONSE"]._serialized_start = 578
    _globals["_SEARCHPRODUCTENTRIESRESPONSE"]._serialized_end = 694
    _globals["_PRODUCTENTRYAPI"]._serialized_start = 697
    _globals["_PRODUCTENTRYAPI"]._serialized_end = 1016
# @@protoc_insertion_point(module_scope)