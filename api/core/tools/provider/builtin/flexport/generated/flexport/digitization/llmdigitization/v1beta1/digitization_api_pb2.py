# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/digitization/llmdigitization/v1beta1/digitization_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nDflexport/digitization/llmdigitization/v1beta1/digitization_api.proto\x12-flexport.digitization.llmdigitization.v1beta1\x1a\x1cgoogle/protobuf/struct.proto"b\n\x19\x43reateDigitizationRequest\x12\x16\n\x0e\x65xtractor_name\x18\x01 \x01(\t\x12\x14\n\x0c\x64ocument_fid\x18\x02 \x01(\t\x12\x17\n\x0f\x66ile_object_fid\x18\x03 \x01(\t"\xbf\x01\n\x1a\x43reateDigitizationResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x02 \x01(\t\x12\x17\n\x0f\x66ile_object_fid\x18\x03 \x01(\t\x12\x14\n\x0c\x64ocument_fid\x18\x04 \x01(\t\x12\x16\n\x0e\x65xtractor_name\x18\x05 \x01(\t\x12\x34\n\x13response_annotation\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct"(\n\x16GetDigitizationRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t"\xbc\x01\n\x17GetDigitizationResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x02 \x01(\t\x12\x17\n\x0f\x66ile_object_fid\x18\x03 \x01(\t\x12\x14\n\x0c\x64ocument_fid\x18\x04 \x01(\t\x12\x16\n\x0e\x65xtractor_name\x18\x05 \x01(\t\x12\x34\n\x13response_annotation\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct"\xbf\x02\n\x15\x43reateFeedbackRequest\x12\x16\n\x0e\x65xtractor_name\x18\x01 \x01(\t\x12\x14\n\x0c\x64ocument_fid\x18\x02 \x01(\t\x12\x17\n\x0f\x66ile_object_fid\x18\x03 \x01(\t\x12-\n\x0cground_truth\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12-\n\x0c\x66ield_audits\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06source\x18\x06 \x01(\t\x12\x1c\n\x14\x64igitization_task_id\x18\x07 \x01(\t\x12S\n\x0fis_audit_passed\x18\x08 \x01(\x0e\x32:.flexport.digitization.llmdigitization.v1beta1.AuditStatus")\n\x16\x43reateFeedbackResponse\x12\x0f\n\x07message\x18\x01 \x01(\t*s\n\x0b\x41uditStatus\x12\x18\n\x14\x41UDIT_STATUS_INVALID\x10\x00\x12\x17\n\x13\x41UDIT_STATUS_PASSED\x10\x01\x12\x17\n\x13\x41UDIT_STATUS_FAILED\x10\x02\x12\x18\n\x14\x41UDIT_STATUS_UNKNOWN\x10\x03\x32\x80\x04\n\x0f\x44igitizationAPI\x12\xa9\x01\n\x12\x43reateDigitization\x12H.flexport.digitization.llmdigitization.v1beta1.CreateDigitizationRequest\x1aI.flexport.digitization.llmdigitization.v1beta1.CreateDigitizationResponse\x12\xa0\x01\n\x0fGetDigitization\x12\x45.flexport.digitization.llmdigitization.v1beta1.GetDigitizationRequest\x1a\x46.flexport.digitization.llmdigitization.v1beta1.GetDigitizationResponse\x12\x9d\x01\n\x0e\x43reateFeedback\x12\x44.flexport.digitization.llmdigitization.v1beta1.CreateFeedbackRequest\x1a\x45.flexport.digitization.llmdigitization.v1beta1.CreateFeedbackResponseB~\n1com.flexport.digitization.llmdigitization.v1beta1B\x14\x44igitizationAPIProtoP\x01\xea\x02\x30\x46lexport::Digitization::LLMDigitization::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.digitization.llmdigitization.v1beta1.digitization_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n1com.flexport.digitization.llmdigitization.v1beta1B\024DigitizationAPIProtoP\001\352\0020Flexport::Digitization::LLMDigitization::V1Beta1"
    _globals["_AUDITSTATUS"]._serialized_start = 1041
    _globals["_AUDITSTATUS"]._serialized_end = 1156
    _globals["_CREATEDIGITIZATIONREQUEST"]._serialized_start = 149
    _globals["_CREATEDIGITIZATIONREQUEST"]._serialized_end = 247
    _globals["_CREATEDIGITIZATIONRESPONSE"]._serialized_start = 250
    _globals["_CREATEDIGITIZATIONRESPONSE"]._serialized_end = 441
    _globals["_GETDIGITIZATIONREQUEST"]._serialized_start = 443
    _globals["_GETDIGITIZATIONREQUEST"]._serialized_end = 483
    _globals["_GETDIGITIZATIONRESPONSE"]._serialized_start = 486
    _globals["_GETDIGITIZATIONRESPONSE"]._serialized_end = 674
    _globals["_CREATEFEEDBACKREQUEST"]._serialized_start = 677
    _globals["_CREATEFEEDBACKREQUEST"]._serialized_end = 996
    _globals["_CREATEFEEDBACKRESPONSE"]._serialized_start = 998
    _globals["_CREATEFEEDBACKRESPONSE"]._serialized_end = 1039
    _globals["_DIGITIZATIONAPI"]._serialized_start = 1159
    _globals["_DIGITIZATIONAPI"]._serialized_end = 1671
# @@protoc_insertion_point(module_scope)