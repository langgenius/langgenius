# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/authorization/grant/v2/grant_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n/flexport/authorization/grant/v2/grant_api.proto\x12\x1f\x66lexport.authorization.grant.v2\x1a\x1cgoogle/api/annotations.proto\x1a&flexport/authorization/v1/common.proto"\xd1\x01\n\x16\x43reateRoleGrantRequest\x12\x33\n\x05\x61\x63tor\x18\x01 \x01(\x0b\x32 .flexport.authorization.v1.ActorB\x02\x18\x01\x12\x11\n\trole_slug\x18\x02 \x01(\t\x12@\n\x0erole_parameter\x18\x03 \x01(\x0b\x32(.flexport.authorization.v1.RoleParameter\x12\x1a\n\x12\x63reated_by_user_id\x18\x04 \x01(\t\x12\x11\n\tactor_fid\x18\x05 \x01(\t"S\n\x17\x43reateRoleGrantResponse\x12\x38\n\nrole_grant\x18\x01 \x01(\x0b\x32$.flexport.authorization.v1.RoleGrant"r\n\x14GetRoleGrantsRequest\x12\x33\n\x05\x61\x63tor\x18\x01 \x01(\x0b\x32 .flexport.authorization.v1.ActorB\x02\x18\x01\x12\x11\n\tactor_fid\x18\x02 \x01(\t\x12\x12\n\napp_filter\x18\x03 \x01(\t"R\n\x15GetRoleGrantsResponse\x12\x39\n\x0brole_grants\x18\x01 \x03(\x0b\x32$.flexport.authorization.v1.RoleGrant"\xd1\x01\n\x16RevokeRoleGrantRequest\x12\x33\n\x05\x61\x63tor\x18\x01 \x01(\x0b\x32 .flexport.authorization.v1.ActorB\x02\x18\x01\x12\x11\n\trole_slug\x18\x02 \x01(\t\x12@\n\x0erole_parameter\x18\x03 \x01(\x0b\x32(.flexport.authorization.v1.RoleParameter\x12\x1a\n\x12revoked_by_user_id\x18\x04 \x01(\t\x12\x11\n\tactor_fid\x18\x05 \x01(\t"\x19\n\x17RevokeRoleGrantResponse"$\n\x15GetRolesForAppRequest\x12\x0b\n\x03\x61pp\x18\x01 \x01(\t"+\n\x16GetRolesForAppResponse\x12\x11\n\trole_slug\x18\x01 \x03(\t"1\n\x1cListRoleGrantsForRoleRequest\x12\x11\n\trole_slug\x18\x01 \x01(\t"2\n\x1dListRoleGrantsForRoleResponse\x12\x11\n\tactor_fid\x18\x01 \x01(\t2\x87\x06\n\x08GrantAPI\x12\x9c\x01\n\x0f\x43reateRoleGrant\x12\x37.flexport.authorization.grant.v2.CreateRoleGrantRequest\x1a\x38.flexport.authorization.grant.v2.CreateRoleGrantResponse"\x16\x82\xd3\xe4\x93\x02\x10"\x0e/v2/rolegrants\x12\x96\x01\n\rGetRoleGrants\x12\x35.flexport.authorization.grant.v2.GetRoleGrantsRequest\x1a\x36.flexport.authorization.grant.v2.GetRoleGrantsResponse"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v2/rolegrants\x12\xa3\x01\n\x0fRevokeRoleGrant\x12\x37.flexport.authorization.grant.v2.RevokeRoleGrantRequest\x1a\x38.flexport.authorization.grant.v2.RevokeRoleGrantResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x15/v2/rolegrants/revoke\x12\x81\x01\n\x0eGetRolesForApp\x12\x36.flexport.authorization.grant.v2.GetRolesForAppRequest\x1a\x37.flexport.authorization.grant.v2.GetRolesForAppResponse\x12\x98\x01\n\x15ListRoleGrantsForRole\x12=.flexport.authorization.grant.v2.ListRoleGrantsForRoleRequest\x1a>.flexport.authorization.grant.v2.ListRoleGrantsForRoleResponse0\x01\x42[\n#com.flexport.authorization.grant.v2B\rGrantApiProtoP\x01\xea\x02"Flexport::Authorization::Grant::V2b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.authorization.grant.v2.grant_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b'\n#com.flexport.authorization.grant.v2B\rGrantApiProtoP\001\352\002"Flexport::Authorization::Grant::V2'
    )
    _globals["_CREATEROLEGRANTREQUEST"].fields_by_name["actor"]._options = None
    _globals["_CREATEROLEGRANTREQUEST"].fields_by_name["actor"]._serialized_options = b"\030\001"
    _globals["_GETROLEGRANTSREQUEST"].fields_by_name["actor"]._options = None
    _globals["_GETROLEGRANTSREQUEST"].fields_by_name["actor"]._serialized_options = b"\030\001"
    _globals["_REVOKEROLEGRANTREQUEST"].fields_by_name["actor"]._options = None
    _globals["_REVOKEROLEGRANTREQUEST"].fields_by_name["actor"]._serialized_options = b"\030\001"
    _globals["_GRANTAPI"].methods_by_name["CreateRoleGrant"]._options = None
    _globals["_GRANTAPI"].methods_by_name[
        "CreateRoleGrant"
    ]._serialized_options = b'\202\323\344\223\002\020"\016/v2/rolegrants'
    _globals["_GRANTAPI"].methods_by_name["GetRoleGrants"]._options = None
    _globals["_GRANTAPI"].methods_by_name[
        "GetRoleGrants"
    ]._serialized_options = b"\202\323\344\223\002\020\022\016/v2/rolegrants"
    _globals["_GRANTAPI"].methods_by_name["RevokeRoleGrant"]._options = None
    _globals["_GRANTAPI"].methods_by_name[
        "RevokeRoleGrant"
    ]._serialized_options = b'\202\323\344\223\002\027"\025/v2/rolegrants/revoke'
    _globals["_CREATEROLEGRANTREQUEST"]._serialized_start = 155
    _globals["_CREATEROLEGRANTREQUEST"]._serialized_end = 364
    _globals["_CREATEROLEGRANTRESPONSE"]._serialized_start = 366
    _globals["_CREATEROLEGRANTRESPONSE"]._serialized_end = 449
    _globals["_GETROLEGRANTSREQUEST"]._serialized_start = 451
    _globals["_GETROLEGRANTSREQUEST"]._serialized_end = 565
    _globals["_GETROLEGRANTSRESPONSE"]._serialized_start = 567
    _globals["_GETROLEGRANTSRESPONSE"]._serialized_end = 649
    _globals["_REVOKEROLEGRANTREQUEST"]._serialized_start = 652
    _globals["_REVOKEROLEGRANTREQUEST"]._serialized_end = 861
    _globals["_REVOKEROLEGRANTRESPONSE"]._serialized_start = 863
    _globals["_REVOKEROLEGRANTRESPONSE"]._serialized_end = 888
    _globals["_GETROLESFORAPPREQUEST"]._serialized_start = 890
    _globals["_GETROLESFORAPPREQUEST"]._serialized_end = 926
    _globals["_GETROLESFORAPPRESPONSE"]._serialized_start = 928
    _globals["_GETROLESFORAPPRESPONSE"]._serialized_end = 971
    _globals["_LISTROLEGRANTSFORROLEREQUEST"]._serialized_start = 973
    _globals["_LISTROLEGRANTSFORROLEREQUEST"]._serialized_end = 1022
    _globals["_LISTROLEGRANTSFORROLERESPONSE"]._serialized_start = 1024
    _globals["_LISTROLEGRANTSFORROLERESPONSE"]._serialized_end = 1074
    _globals["_GRANTAPI"]._serialized_start = 1077
    _globals["_GRANTAPI"]._serialized_end = 1852
# @@protoc_insertion_point(module_scope)