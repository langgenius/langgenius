# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customsopsworkflow/useroverridestate/v1/user_override_state.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nJflexport/customsopsworkflow/useroverridestate/v1/user_override_state.proto\x12\x30\x66lexport.customsopsworkflow.useroverridestate.v1"\xe5\x01\n\x11UserOverrideState\x12\x65\n\x1c\x63ustoms_entry_override_state\x18\x01 \x01(\x0b\x32?.flexport.customsopsworkflow.useroverridestate.v1.OverrideState\x12i\n customs_unloading_override_state\x18\x02 \x01(\x0b\x32?.flexport.customsopsworkflow.useroverridestate.v1.OverrideState"\xa4\x01\n\rOverrideState\x12\x15\n\ris_overridden\x18\x01 \x01(\x08\x12\x18\n\x10last_modified_by\x18\x02 \x01(\t\x12\x62\n\x14override_entry_point\x18\x03 \x01(\x0e\x32\x44.flexport.customsopsworkflow.useroverridestate.v1.OverrideEntryPoint*w\n\x12OverrideEntryPoint\x12 \n\x1cOVERRIDE_ENTRY_POINT_INVALID\x10\x00\x12\x1c\n\x18OVERRIDE_ENTRY_POINT_FFA\x10\x01\x12!\n\x1dOVERRIDE_ENTRY_POINT_MONOLITH\x10\x02\x42_\n!com.flexport.useroverridestate.v1B\x16UserOverrideStateProtoP\x01\xea\x02\x1f\x46lexport::UserOverrideState::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customsopsworkflow.useroverridestate.v1.user_override_state_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n!com.flexport.useroverridestate.v1B\026UserOverrideStateProtoP\001\352\002\037Flexport::UserOverrideState::V1"
    _globals["_OVERRIDEENTRYPOINT"]._serialized_start = 527
    _globals["_OVERRIDEENTRYPOINT"]._serialized_end = 646
    _globals["_USEROVERRIDESTATE"]._serialized_start = 129
    _globals["_USEROVERRIDESTATE"]._serialized_end = 358
    _globals["_OVERRIDESTATE"]._serialized_start = 361
    _globals["_OVERRIDESTATE"]._serialized_end = 525
# @@protoc_insertion_point(module_scope)