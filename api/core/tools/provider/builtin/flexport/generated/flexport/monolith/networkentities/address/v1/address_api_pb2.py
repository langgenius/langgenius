# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/networkentities/address/v1/address_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n>flexport/monolith/networkentities/address/v1/address_api.proto\x12,flexport.monolith.networkentities.address.v1\x1a:flexport/monolith/networkentities/address/v1/address.proto"(\n\x11GetAddressRequest\x12\x13\n\x0b\x61\x64\x64ress_fid\x18\x01 \x01(\t"c\n\x12GetAddressResponse\x12M\n\x0b\x61\x64\x64ress_dto\x18\x01 \x01(\x0b\x32\x38.flexport.monolith.networkentities.address.v1.AddressDTO"6\n\x1dGetFidsForAddressDbidsRequest\x12\x15\n\raddress_dbids\x18\x01 \x03(\x05"M\n\x1eGetFidsForAddressDbidsResponse\x12\x15\n\raddress_dbids\x18\x01 \x03(\x05\x12\x14\n\x0c\x61\x64\x64ress_fids\x18\x02 \x03(\t2\xd4\x02\n\nAddressAPI\x12\x8f\x01\n\nGetAddress\x12?.flexport.monolith.networkentities.address.v1.GetAddressRequest\x1a@.flexport.monolith.networkentities.address.v1.GetAddressResponse\x12\xb3\x01\n\x16GetFidsForAddressDbids\x12K.flexport.monolith.networkentities.address.v1.GetFidsForAddressDbidsRequest\x1aL.flexport.monolith.networkentities.address.v1.GetFidsForAddressDbidsResponseBx\n0com.flexport.monolith.networkentities.address.v1B\x0f\x41\x64\x64ressApiProtoP\x01\xea\x02\x30\x46lexport::Monolith::NetworkEntities::Address::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.networkentities.address.v1.address_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n0com.flexport.monolith.networkentities.address.v1B\017AddressApiProtoP\001\352\0020Flexport::Monolith::NetworkEntities::Address::V1"
    _globals["_GETADDRESSREQUEST"]._serialized_start = 172
    _globals["_GETADDRESSREQUEST"]._serialized_end = 212
    _globals["_GETADDRESSRESPONSE"]._serialized_start = 214
    _globals["_GETADDRESSRESPONSE"]._serialized_end = 313
    _globals["_GETFIDSFORADDRESSDBIDSREQUEST"]._serialized_start = 315
    _globals["_GETFIDSFORADDRESSDBIDSREQUEST"]._serialized_end = 369
    _globals["_GETFIDSFORADDRESSDBIDSRESPONSE"]._serialized_start = 371
    _globals["_GETFIDSFORADDRESSDBIDSRESPONSE"]._serialized_end = 448
    _globals["_ADDRESSAPI"]._serialized_start = 451
    _globals["_ADDRESSAPI"]._serialized_end = 791
# @@protoc_insertion_point(module_scope)