# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/billing/review/v1beta1/assignment_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n4flexport/billing/review/v1beta1/assignment_api.proto\x12\x1f\x66lexport.billing.review.v1beta1\x1a(flexport/billing/team/v1beta1/team.proto\x1a\x30\x66lexport/billing/util/v1beta1/error_result.proto"-\n\x19GetTeamByMemberFidRequest\x12\x10\n\x08user_fid\x18\x01 \x01(\t"\xa1\x01\n\x1aGetTeamByMemberFidResponse\x12\x33\n\x04team\x18\x01 \x01(\x0b\x32#.flexport.billing.team.v1beta1.TeamH\x00\x12\x44\n\x0e\x66\x61ilure_result\x18\x02 \x01(\x0b\x32*.flexport.billing.util.v1beta1.ErrorResultH\x00\x42\x08\n\x06result2\x9f\x01\n\rAssignmentAPI\x12\x8d\x01\n\x12GetTeamByMemberFid\x12:.flexport.billing.review.v1beta1.GetTeamByMemberFidRequest\x1a;.flexport.billing.review.v1beta1.GetTeamByMemberFidResponseB`\n#com.flexport.billing.review.v1beta1B\x12\x41ssignmentApiProtoP\x01\xea\x02"Flexport::Billing::Review::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.billing.review.v1beta1.assignment_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b'\n#com.flexport.billing.review.v1beta1B\022AssignmentApiProtoP\001\352\002"Flexport::Billing::Review::V1Beta1'
    )
    _globals["_GETTEAMBYMEMBERFIDREQUEST"]._serialized_start = 181
    _globals["_GETTEAMBYMEMBERFIDREQUEST"]._serialized_end = 226
    _globals["_GETTEAMBYMEMBERFIDRESPONSE"]._serialized_start = 229
    _globals["_GETTEAMBYMEMBERFIDRESPONSE"]._serialized_end = 390
    _globals["_ASSIGNMENTAPI"]._serialized_start = 393
    _globals["_ASSIGNMENTAPI"]._serialized_end = 552
# @@protoc_insertion_point(module_scope)