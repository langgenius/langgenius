# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/network/v1beta1/network_order_by.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n/flexport/network/v1beta1/network_order_by.proto\x12\x18\x66lexport.network.v1beta1"\r\n\x0bOrderByName"+\n\x0fOrderByDistance\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lng\x18\x02 \x01(\x01"a\n\x16OrderByAddressDistance\x12\x14\n\naddress_id\x18\x01 \x01(\x05H\x00\x12\x15\n\x0b\x61\x64\x64ress_fid\x18\x02 \x01(\tH\x00\x42\x1a\n\x18\x61\x64\x64ress_id_discriminatorBR\n\x1c\x63om.flexport.network.v1beta1B\x13NetworkOrderByProtoP\x01\xea\x02\x1a\x46lexport::Network::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.network.v1beta1.network_order_by_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n\034com.flexport.network.v1beta1B\023NetworkOrderByProtoP\001\352\002\032Flexport::Network::V1Beta1"
    )
    _globals["_ORDERBYNAME"]._serialized_start = 77
    _globals["_ORDERBYNAME"]._serialized_end = 90
    _globals["_ORDERBYDISTANCE"]._serialized_start = 92
    _globals["_ORDERBYDISTANCE"]._serialized_end = 135
    _globals["_ORDERBYADDRESSDISTANCE"]._serialized_start = 137
    _globals["_ORDERBYADDRESSDISTANCE"]._serialized_end = 234
# @@protoc_insertion_point(module_scope)