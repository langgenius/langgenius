# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/assignment/publishing/v1/assignment_changed.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n:flexport/assignment/publishing/v1/assignment_changed.proto\x12!flexport.assignment.publishing.v1\x1a-flexport/assignment/model/v1/assignment.proto"\xb1\x01\n\x11\x41ssignmentChanged\x12\x17\n\x0fidempotency_key\x18\x01 \x01(\t\x12<\n\nassignment\x18\x02 \x01(\x0b\x32(.flexport.assignment.model.v1.Assignment\x12\x45\n\x04type\x18\x03 \x01(\x0e\x32\x37.flexport.assignment.publishing.v1.AssignmentChangeType*\xa2\x01\n\x14\x41ssignmentChangeType\x12"\n\x1e\x41SSIGNMENT_CHANGE_TYPE_INVALID\x10\x00\x12\x1e\n\x1a\x41SSIGNMENT_CHANGE_TYPE_ADD\x10\x01\x12!\n\x1d\x41SSIGNMENT_CHANGE_TYPE_DELETE\x10\x02\x12#\n\x1f\x41SSIGNMENT_CHANGE_TYPE_REASSIGN\x10\x03\x42h\n%com.flexport.assignment.publishing.v1B\x16\x41ssignmentChangedProtoP\x01\xea\x02$Flexport::Assignment::Publishing::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.assignment.publishing.v1.assignment_changed_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n%com.flexport.assignment.publishing.v1B\026AssignmentChangedProtoP\001\352\002$Flexport::Assignment::Publishing::V1"
    _globals["_ASSIGNMENTCHANGETYPE"]._serialized_start = 325
    _globals["_ASSIGNMENTCHANGETYPE"]._serialized_end = 487
    _globals["_ASSIGNMENTCHANGED"]._serialized_start = 145
    _globals["_ASSIGNMENTCHANGED"]._serialized_end = 322
# @@protoc_insertion_point(module_scope)