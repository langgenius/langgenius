# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customs/documentdigitization/usergroups/v1beta1/user_groups_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nNflexport/customs/documentdigitization/usergroups/v1beta1/user_groups_api.proto\x12\x38\x66lexport.customs.documentdigitization.usergroups.v1beta1\x1a-flexport/rulesengine/options/v1/options.proto"3\n\x14GetUserGroupsRequest\x12\x1b\n\x07user_id\x18\x01 \x01(\x05\x42\n\x8a\xf7\x02\x06\n\x04User",\n\x15GetUserGroupsResponse\x12\x13\n\x0bgroup_names\x18\x01 \x03(\t2\xb9\x02\n\rUserGroupsAPI\x12\x8d\x02\n\rGetUserGroups\x12N.flexport.customs.documentdigitization.usergroups.v1beta1.GetUserGroupsRequest\x1aO.flexport.customs.documentdigitization.usergroups.v1beta1.GetUserGroupsResponse"[\x8a\xf7\x02W\x12\x34\x63om.flexport.customs.documentdigitization.usergroups\x1a\x0buser groups"\x12\x63ommercial_invoice\x1a\x18\x8a\xf7\x02\x14\n\x12\x63ommercial_invoiceB\x93\x01\n<com.flexport.customs.documentdigitization.usergroups.v1beta1B\x12UserGroupsApiProtoP\x01\xea\x02<Flexport::Customs::DocumentDigitization::UserGroups::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customs.documentdigitization.usergroups.v1beta1.user_groups_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n<com.flexport.customs.documentdigitization.usergroups.v1beta1B\022UserGroupsApiProtoP\001\352\002<Flexport::Customs::DocumentDigitization::UserGroups::V1Beta1"
    _globals["_GETUSERGROUPSREQUEST"].fields_by_name["user_id"]._options = None
    _globals["_GETUSERGROUPSREQUEST"].fields_by_name["user_id"]._serialized_options = b"\212\367\002\006\n\004User"
    _globals["_USERGROUPSAPI"]._options = None
    _globals["_USERGROUPSAPI"]._serialized_options = b"\212\367\002\024\n\022commercial_invoice"
    _globals["_USERGROUPSAPI"].methods_by_name["GetUserGroups"]._options = None
    _globals["_USERGROUPSAPI"].methods_by_name[
        "GetUserGroups"
    ]._serialized_options = b'\212\367\002W\0224com.flexport.customs.documentdigitization.usergroups\032\013user groups"\022commercial_invoice'
    _globals["_GETUSERGROUPSREQUEST"]._serialized_start = 187
    _globals["_GETUSERGROUPSREQUEST"]._serialized_end = 238
    _globals["_GETUSERGROUPSRESPONSE"]._serialized_start = 240
    _globals["_GETUSERGROUPSRESPONSE"]._serialized_end = 284
    _globals["_USERGROUPSAPI"]._serialized_start = 287
    _globals["_USERGROUPSAPI"]._serialized_end = 600
# @@protoc_insertion_point(module_scope)