# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/authorization/apicredentials/v1beta1/api_credentials_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nGflexport/authorization/apicredentials/v1beta1/api_credentials_api.proto\x12-flexport.authorization.apicredentials.v1beta1\x1a\x1egoogle/protobuf/wrappers.proto"\xa7\x01\n\x13\x43reateClientRequest\x12\x16\n\x0e\x61pi_entity_fid\x18\x01 \x01(\t\x12\x31\n\x0b\x63ompany_fid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nclient_fid\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x13\n\x0b\x65ntity_name\x18\x04 \x01(\t")\n\x14\x43reateClientResponse\x12\x11\n\tclient_id\x18\x01 \x01(\t"5\n\x1bGetClientCredentialsRequest\x12\x16\n\x0e\x61pi_entity_fid\x18\x01 \x01(\t"H\n\x1cGetClientCredentialsResponse\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x15\n\rclient_secret\x18\x02 \x01(\t"-\n\x13\x44\x65leteClientRequest\x12\x16\n\x0e\x61pi_entity_fid\x18\x01 \x01(\t"F\n\x14\x44\x65leteClientResponse\x12.\n\nis_deleted\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue"3\n\x19RotateClientSecretRequest\x12\x16\n\x0e\x61pi_entity_fid\x18\x01 \x01(\t"F\n\x1aRotateClientSecretResponse\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x15\n\rclient_secret\x18\x02 \x01(\t2\xa5\x05\n\x11\x41piCredentialsAPI\x12\x97\x01\n\x0c\x43reateClient\x12\x42.flexport.authorization.apicredentials.v1beta1.CreateClientRequest\x1a\x43.flexport.authorization.apicredentials.v1beta1.CreateClientResponse\x12\xaf\x01\n\x14GetClientCredentials\x12J.flexport.authorization.apicredentials.v1beta1.GetClientCredentialsRequest\x1aK.flexport.authorization.apicredentials.v1beta1.GetClientCredentialsResponse\x12\x97\x01\n\x0c\x44\x65leteClient\x12\x42.flexport.authorization.apicredentials.v1beta1.DeleteClientRequest\x1a\x43.flexport.authorization.apicredentials.v1beta1.DeleteClientResponse\x12\xa9\x01\n\x12RotateClientSecret\x12H.flexport.authorization.apicredentials.v1beta1.RotateClientSecretRequest\x1aI.flexport.authorization.apicredentials.v1beta1.RotateClientSecretResponseB\x80\x01\n1com.flexport.authorization.apicredentials.v1beta1B\x16\x41piCredentialsApiProtoP\x01\xea\x02\x30\x46lexport::Authorization::ApiCredentials::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.authorization.apicredentials.v1beta1.api_credentials_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n1com.flexport.authorization.apicredentials.v1beta1B\026ApiCredentialsApiProtoP\001\352\0020Flexport::Authorization::ApiCredentials::V1Beta1"
    _globals["_CREATECLIENTREQUEST"]._serialized_start = 155
    _globals["_CREATECLIENTREQUEST"]._serialized_end = 322
    _globals["_CREATECLIENTRESPONSE"]._serialized_start = 324
    _globals["_CREATECLIENTRESPONSE"]._serialized_end = 365
    _globals["_GETCLIENTCREDENTIALSREQUEST"]._serialized_start = 367
    _globals["_GETCLIENTCREDENTIALSREQUEST"]._serialized_end = 420
    _globals["_GETCLIENTCREDENTIALSRESPONSE"]._serialized_start = 422
    _globals["_GETCLIENTCREDENTIALSRESPONSE"]._serialized_end = 494
    _globals["_DELETECLIENTREQUEST"]._serialized_start = 496
    _globals["_DELETECLIENTREQUEST"]._serialized_end = 541
    _globals["_DELETECLIENTRESPONSE"]._serialized_start = 543
    _globals["_DELETECLIENTRESPONSE"]._serialized_end = 613
    _globals["_ROTATECLIENTSECRETREQUEST"]._serialized_start = 615
    _globals["_ROTATECLIENTSECRETREQUEST"]._serialized_end = 666
    _globals["_ROTATECLIENTSECRETRESPONSE"]._serialized_start = 668
    _globals["_ROTATECLIENTSECRETRESPONSE"]._serialized_end = 738
    _globals["_APICREDENTIALSAPI"]._serialized_start = 741
    _globals["_APICREDENTIALSAPI"]._serialized_end = 1418
# @@protoc_insertion_point(module_scope)