# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/authorization/user/v1beta1/user_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n2flexport/authorization/user/v1beta1/user_api.proto\x12#flexport.authorization.user.v1beta1"-\n\x1c\x44\x65\x61\x63tivateUserByEmailRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t"\x1f\n\x1d\x44\x65\x61\x63tivateUserByEmailResponse"\x86\x01\n DeactivateUserByEmailErrorDetail\x12Q\n\x04type\x18\x01 \x01(\x0e\x32\x43.flexport.authorization.user.v1beta1.DeactivateUserByEmailErrorType\x12\x0f\n\x07message\x18\x02 \x01(\t*\x88\x01\n\x1e\x44\x65\x61\x63tivateUserByEmailErrorType\x12/\n+DEACTIVATE_USER_BY_EMAIL_ERROR_TYPE_INVALID\x10\x00\x12\x35\n1DEACTIVATE_USER_BY_EMAIL_ERROR_TYPE_INVALID_EMAIL\x10\x01\x32\xaa\x01\n\x07UserAPI\x12\x9e\x01\n\x15\x44\x65\x61\x63tivateUserByEmail\x12\x41.flexport.authorization.user.v1beta1.DeactivateUserByEmailRequest\x1a\x42.flexport.authorization.user.v1beta1.DeactivateUserByEmailResponseBb\n\'com.flexport.authorization.user.v1beta1B\x0cUserApiProtoP\x01\xea\x02&Flexport::Authorization::User::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.authorization.user.v1beta1.user_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n'com.flexport.authorization.user.v1beta1B\014UserApiProtoP\001\352\002&Flexport::Authorization::User::V1Beta1"
    _globals["_DEACTIVATEUSERBYEMAILERRORTYPE"]._serialized_start = 309
    _globals["_DEACTIVATEUSERBYEMAILERRORTYPE"]._serialized_end = 445
    _globals["_DEACTIVATEUSERBYEMAILREQUEST"]._serialized_start = 91
    _globals["_DEACTIVATEUSERBYEMAILREQUEST"]._serialized_end = 136
    _globals["_DEACTIVATEUSERBYEMAILRESPONSE"]._serialized_start = 138
    _globals["_DEACTIVATEUSERBYEMAILRESPONSE"]._serialized_end = 169
    _globals["_DEACTIVATEUSERBYEMAILERRORDETAIL"]._serialized_start = 172
    _globals["_DEACTIVATEUSERBYEMAILERRORDETAIL"]._serialized_end = 306
    _globals["_USERAPI"]._serialized_start = 448
    _globals["_USERAPI"]._serialized_end = 618
# @@protoc_insertion_point(module_scope)