# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/example/customer/v1beta1/customer_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n4flexport/example/customer/v1beta1/customer_api.proto\x12!flexport.example.customer.v1beta1\x1a\x30\x66lexport/example/customer/v1beta1/customer.proto"%\n\x15\x43reateCustomerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"W\n\x16\x43reateCustomerResponse\x12=\n\x08\x63ustomer\x18\x01 \x01(\x0b\x32+.flexport.example.customer.v1beta1.Customer"!\n\x12GetCustomerRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"T\n\x13GetCustomerResponse\x12=\n\x08\x63ustomer\x18\x01 \x01(\x0b\x32+.flexport.example.customer.v1beta1.Customer2\x93\x02\n\x0b\x43ustomerAPI\x12\x85\x01\n\x0e\x43reateCustomer\x12\x38.flexport.example.customer.v1beta1.CreateCustomerRequest\x1a\x39.flexport.example.customer.v1beta1.CreateCustomerResponse\x12|\n\x0bGetCustomer\x12\x35.flexport.example.customer.v1beta1.GetCustomerRequest\x1a\x36.flexport.example.customer.v1beta1.GetCustomerResponseBb\n%com.flexport.example.customer.v1beta1B\x10\x43ustomerApiProtoP\x01\xea\x02$Flexport::Example::Customer::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.example.customer.v1beta1.customer_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n%com.flexport.example.customer.v1beta1B\020CustomerApiProtoP\001\352\002$Flexport::Example::Customer::V1Beta1"
    _globals["_CREATECUSTOMERREQUEST"]._serialized_start = 141
    _globals["_CREATECUSTOMERREQUEST"]._serialized_end = 178
    _globals["_CREATECUSTOMERRESPONSE"]._serialized_start = 180
    _globals["_CREATECUSTOMERRESPONSE"]._serialized_end = 267
    _globals["_GETCUSTOMERREQUEST"]._serialized_start = 269
    _globals["_GETCUSTOMERREQUEST"]._serialized_end = 302
    _globals["_GETCUSTOMERRESPONSE"]._serialized_start = 304
    _globals["_GETCUSTOMERRESPONSE"]._serialized_end = 388
    _globals["_CUSTOMERAPI"]._serialized_start = 391
    _globals["_CUSTOMERAPI"]._serialized_end = 666
# @@protoc_insertion_point(module_scope)