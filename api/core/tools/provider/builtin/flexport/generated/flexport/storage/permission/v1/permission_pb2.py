# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/storage/permission/v1/permission.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n/flexport/storage/permission/v1/permission.proto\x12\x1e\x66lexport.storage.permission.v1"\xc8\x02\n\nPermission\x12J\n\x0b\x61\x63tion_type\x18\x01 \x01(\x0e\x32\x35.flexport.storage.permission.v1.Permission.ActionType\x12\x33\n\x05rules\x18\x02 \x03(\x0b\x32$.flexport.storage.permission.v1.Rule"\xb8\x01\n\nActionType\x12\x17\n\x13\x41\x43TION_TYPE_INVALID\x10\x00\x12\x1a\n\x16\x41\x43TION_TYPE_PERMISSION\x10\x01\x12\x14\n\x10\x41\x43TION_TYPE_READ\x10\x02\x12\x16\n\x12\x41\x43TION_TYPE_UPDATE\x10\x03\x12\x17\n\x13\x41\x43TION_TYPE_ARCHIVE\x10\x04\x12\x16\n\x12\x41\x43TION_TYPE_DELETE\x10\x05\x12\x16\n\x12\x41\x43TION_TYPE_CREATE\x10\x06"\xc4\x01\n\x04Rule\x12I\n\x0fpermission_rule\x18\x01 \x01(\x0b\x32..flexport.storage.permission.v1.PermissionRuleH\x00\x12\x64\n\x1dparameterized_permission_rule\x18\x02 \x01(\x0b\x32;.flexport.storage.permission.v1.ParameterizedPermissionRuleH\x00\x42\x0b\n\trule_type"(\n\x0ePermissionRule\x12\x16\n\x0eoperation_slug\x18\x01 \x01(\t"K\n\x1bParameterizedPermissionRule\x12\x16\n\x0eoperation_slug\x18\x01 \x01(\t\x12\x14\n\x0cresource_fid\x18\x02 \x01(\tB[\n"com.flexport.storage.permission.v1B\x0fPermissionProtoP\x01\xea\x02!Flexport::Storage::Permission::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.storage.permission.v1.permission_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b'\n"com.flexport.storage.permission.v1B\017PermissionProtoP\001\352\002!Flexport::Storage::Permission::V1'
    )
    _globals["_PERMISSION"]._serialized_start = 84
    _globals["_PERMISSION"]._serialized_end = 412
    _globals["_PERMISSION_ACTIONTYPE"]._serialized_start = 228
    _globals["_PERMISSION_ACTIONTYPE"]._serialized_end = 412
    _globals["_RULE"]._serialized_start = 415
    _globals["_RULE"]._serialized_end = 611
    _globals["_PERMISSIONRULE"]._serialized_start = 613
    _globals["_PERMISSIONRULE"]._serialized_end = 653
    _globals["_PARAMETERIZEDPERMISSIONRULE"]._serialized_start = 655
    _globals["_PARAMETERIZEDPERMISSIONRULE"]._serialized_end = 730
# @@protoc_insertion_point(module_scope)