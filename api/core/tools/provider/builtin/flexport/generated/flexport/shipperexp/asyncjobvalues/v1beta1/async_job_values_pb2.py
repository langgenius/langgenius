# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/shipperexp/asyncjobvalues/v1beta1/async_job_values.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nAflexport/shipperexp/asyncjobvalues/v1beta1/async_job_values.proto\x12*flexport.shipperexp.asyncjobvalues.v1beta1"v\n\x0e\x41syncJobValues\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x42\n\x06status\x18\x02 \x01(\x0e\x32\x32.flexport.shipperexp.asyncjobvalues.v1beta1.Status\x12\x14\n\x0c\x65rror_reason\x18\x03 \x01(\t*X\n\x06Status\x12\x12\n\x0eSTATUS_INVALID\x10\x00\x12\x11\n\rSTATUS_ACTIVE\x10\x01\x12\x14\n\x10STATUS_COMPLETED\x10\x02\x12\x11\n\rSTATUS_FAILED\x10\x03\x42w\n.com.flexport.shipperexp.asyncjobvalues.v1beta1B\x13\x41syncJobValuesProtoP\x01\xea\x02-Flexport::ShipperExp::AsyncJobValues::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.shipperexp.asyncjobvalues.v1beta1.async_job_values_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n.com.flexport.shipperexp.asyncjobvalues.v1beta1B\023AsyncJobValuesProtoP\001\352\002-Flexport::ShipperExp::AsyncJobValues::V1Beta1"
    _globals["_STATUS"]._serialized_start = 233
    _globals["_STATUS"]._serialized_end = 321
    _globals["_ASYNCJOBVALUES"]._serialized_start = 113
    _globals["_ASYNCJOBVALUES"]._serialized_end = 231
# @@protoc_insertion_point(module_scope)