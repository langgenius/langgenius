# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/rulesengine/clientcallback/v1beta1/client_callback_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nEflexport/rulesengine/clientcallback/v1beta1/client_callback_api.proto\x12+flexport.rulesengine.clientcallback.v1beta1"P\n\x15ValidateOutputRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x10\n\x08\x61pi_name\x18\x02 \x01(\t\x12\x0f\n\x07outputs\x18\x03 \x01(\x0c"\x9f\x01\n\x16ValidateOutputResponse\x12Y\n\x06\x65rrors\x18\x01 \x03(\x0b\x32I.flexport.rulesengine.clientcallback.v1beta1.ValidateOutputResponse.Error\x1a*\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t2\xaf\x01\n\x11\x43lientCallbackAPI\x12\x99\x01\n\x0eValidateOutput\x12\x42.flexport.rulesengine.clientcallback.v1beta1.ValidateOutputRequest\x1a\x43.flexport.rulesengine.clientcallback.v1beta1.ValidateOutputResponseB|\n/com.flexport.rulesengine.clientcallback.v1beta1B\x16\x43lientCallbackApiProtoP\x01\xea\x02.Flexport::RulesEngine::ClientCallback::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.rulesengine.clientcallback.v1beta1.client_callback_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n/com.flexport.rulesengine.clientcallback.v1beta1B\026ClientCallbackApiProtoP\001\352\002.Flexport::RulesEngine::ClientCallback::V1Beta1"
    _globals["_VALIDATEOUTPUTREQUEST"]._serialized_start = 118
    _globals["_VALIDATEOUTPUTREQUEST"]._serialized_end = 198
    _globals["_VALIDATEOUTPUTRESPONSE"]._serialized_start = 201
    _globals["_VALIDATEOUTPUTRESPONSE"]._serialized_end = 360
    _globals["_VALIDATEOUTPUTRESPONSE_ERROR"]._serialized_start = 318
    _globals["_VALIDATEOUTPUTRESPONSE_ERROR"]._serialized_end = 360
    _globals["_CLIENTCALLBACKAPI"]._serialized_start = 363
    _globals["_CLIENTCALLBACKAPI"]._serialized_end = 538
# @@protoc_insertion_point(module_scope)