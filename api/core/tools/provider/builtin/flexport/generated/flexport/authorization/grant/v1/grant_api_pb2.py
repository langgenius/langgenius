# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/authorization/grant/v1/grant_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n/flexport/authorization/grant/v1/grant_api.proto\x12\x1f\x66lexport.authorization.grant.v1\x1a&flexport/authorization/v1/common.proto"\x9c\x01\n\x10GrantRoleRequest\x12/\n\x05\x61\x63tor\x18\x01 \x01(\x0b\x32 .flexport.authorization.v1.Actor\x12\x11\n\trole_name\x18\x02 \x01(\t\x12@\n\x0erole_parameter\x18\x03 \x01(\x0b\x32(.flexport.authorization.v1.RoleParameter:\x02\x18\x01"Q\n\x11GrantRoleResponse\x12\x38\n\nrole_grant\x18\x01 \x01(\x0b\x32$.flexport.authorization.v1.RoleGrant:\x02\x18\x01"G\n\x10GetGrantsRequest\x12/\n\x05\x61\x63tor\x18\x01 \x01(\x0b\x32 .flexport.authorization.v1.Actor:\x02\x18\x01"Q\n\x11GetGrantsResponse\x12\x38\n\nrole_grant\x18\x01 \x03(\x0b\x32$.flexport.authorization.v1.RoleGrant:\x02\x18\x01"\x9e\x01\n\x12RevokeGrantRequest\x12/\n\x05\x61\x63tor\x18\x01 \x01(\x0b\x32 .flexport.authorization.v1.Actor\x12\x11\n\trole_name\x18\x02 \x01(\t\x12@\n\x0erole_parameter\x18\x03 \x01(\x0b\x32(.flexport.authorization.v1.RoleParameter:\x02\x18\x01"\x15\n\x13RevokeGrantResponse2\xfb\x02\n\x08GrantAPI\x12w\n\tGrantRole\x12\x31.flexport.authorization.grant.v1.GrantRoleRequest\x1a\x32.flexport.authorization.grant.v1.GrantRoleResponse"\x03\x88\x02\x01\x12w\n\tGetGrants\x12\x31.flexport.authorization.grant.v1.GetGrantsRequest\x1a\x32.flexport.authorization.grant.v1.GetGrantsResponse"\x03\x88\x02\x01\x12}\n\x0bRevokeGrant\x12\x33.flexport.authorization.grant.v1.RevokeGrantRequest\x1a\x34.flexport.authorization.grant.v1.RevokeGrantResponse"\x03\x88\x02\x01\x42[\n#com.flexport.authorization.grant.v1B\rGrantApiProtoP\x01\xea\x02"Flexport::Authorization::Grant::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.authorization.grant.v1.grant_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b'\n#com.flexport.authorization.grant.v1B\rGrantApiProtoP\001\352\002"Flexport::Authorization::Grant::V1'
    )
    _globals["_GRANTROLEREQUEST"]._options = None
    _globals["_GRANTROLEREQUEST"]._serialized_options = b"\030\001"
    _globals["_GRANTROLERESPONSE"]._options = None
    _globals["_GRANTROLERESPONSE"]._serialized_options = b"\030\001"
    _globals["_GETGRANTSREQUEST"]._options = None
    _globals["_GETGRANTSREQUEST"]._serialized_options = b"\030\001"
    _globals["_GETGRANTSRESPONSE"]._options = None
    _globals["_GETGRANTSRESPONSE"]._serialized_options = b"\030\001"
    _globals["_REVOKEGRANTREQUEST"]._options = None
    _globals["_REVOKEGRANTREQUEST"]._serialized_options = b"\030\001"
    _globals["_GRANTAPI"].methods_by_name["GrantRole"]._options = None
    _globals["_GRANTAPI"].methods_by_name["GrantRole"]._serialized_options = b"\210\002\001"
    _globals["_GRANTAPI"].methods_by_name["GetGrants"]._options = None
    _globals["_GRANTAPI"].methods_by_name["GetGrants"]._serialized_options = b"\210\002\001"
    _globals["_GRANTAPI"].methods_by_name["RevokeGrant"]._options = None
    _globals["_GRANTAPI"].methods_by_name["RevokeGrant"]._serialized_options = b"\210\002\001"
    _globals["_GRANTROLEREQUEST"]._serialized_start = 125
    _globals["_GRANTROLEREQUEST"]._serialized_end = 281
    _globals["_GRANTROLERESPONSE"]._serialized_start = 283
    _globals["_GRANTROLERESPONSE"]._serialized_end = 364
    _globals["_GETGRANTSREQUEST"]._serialized_start = 366
    _globals["_GETGRANTSREQUEST"]._serialized_end = 437
    _globals["_GETGRANTSRESPONSE"]._serialized_start = 439
    _globals["_GETGRANTSRESPONSE"]._serialized_end = 520
    _globals["_REVOKEGRANTREQUEST"]._serialized_start = 523
    _globals["_REVOKEGRANTREQUEST"]._serialized_end = 681
    _globals["_REVOKEGRANTRESPONSE"]._serialized_start = 683
    _globals["_REVOKEGRANTRESPONSE"]._serialized_end = 704
    _globals["_GRANTAPI"]._serialized_start = 707
    _globals["_GRANTAPI"]._serialized_end = 1086
# @@protoc_insertion_point(module_scope)