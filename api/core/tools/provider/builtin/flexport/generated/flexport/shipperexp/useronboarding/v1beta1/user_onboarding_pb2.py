# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/shipperexp/useronboarding/v1beta1/user_onboarding.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n@flexport/shipperexp/useronboarding/v1beta1/user_onboarding.proto\x12*flexport.shipperexp.useronboarding.v1beta1\x1a\x41\x66lexport/shipperexp/asyncjobvalues/v1beta1/async_job_values.proto\x1a\x46\x66lexport/shipperexp/shipperonboarding/v1beta1/shipper_onboarding.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9b\x02\n\x17UserOnboardingSubmitted\x12\x18\n\x10invitation_token\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12\x35\n\x11submitted_at_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12J\n\tuser_info\x18\x04 \x01(\x0b\x32\x37.flexport.shipperexp.shipperonboarding.v1beta1.UserInfo\x12T\n\x10\x61sync_job_values\x18\x05 \x01(\x0b\x32:.flexport.shipperexp.asyncjobvalues.v1beta1.AsyncJobValuesBw\n.com.flexport.shipperexp.useronboarding.v1beta1B\x13UserOnboardingProtoP\x01\xea\x02-Flexport::ShipperExp::UserOnboarding::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.shipperexp.useronboarding.v1beta1.user_onboarding_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n.com.flexport.shipperexp.useronboarding.v1beta1B\023UserOnboardingProtoP\001\352\002-Flexport::ShipperExp::UserOnboarding::V1Beta1"
    _globals["_USERONBOARDINGSUBMITTED"]._serialized_start = 285
    _globals["_USERONBOARDINGSUBMITTED"]._serialized_end = 568
# @@protoc_insertion_point(module_scope)