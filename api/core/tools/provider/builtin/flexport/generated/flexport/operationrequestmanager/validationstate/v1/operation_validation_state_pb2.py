# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/operationrequestmanager/validationstate/v1/operation_validation_state.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nTflexport/operationrequestmanager/validationstate/v1/operation_validation_state.proto\x12\x33\x66lexport.operationrequestmanager.validationstate.v1\x1aMflexport/executionmilestones/dataqualitystate/v1beta1/data_quality_info.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xd6\x02\n\x18OperationValidationState\x12\x32\n\x0cshipment_fid\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0etriggered_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08resolved\x18\x03 \x01(\x08\x12\x35\n\x0fresolved_by_fid\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12_\n\nissue_type\x18\x05 \x01(\x0e\x32K.flexport.executionmilestones.dataqualitystate.v1beta1.DataQualityIssueType\x12(\n\x07\x63ontext\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructBZ\n7com.flexport.operationrequestmanager.validationstate.v1B\x1dOperationValidationStateProtoP\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.operationrequestmanager.validationstate.v1.operation_validation_state_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n7com.flexport.operationrequestmanager.validationstate.v1B\035OperationValidationStateProtoP\001"
    )
    _globals["_OPERATIONVALIDATIONSTATE"]._serialized_start = 316
    _globals["_OPERATIONVALIDATIONSTATE"]._serialized_end = 658
# @@protoc_insertion_point(module_scope)