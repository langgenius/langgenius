# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/documentflow/documentdigitization/v1beta1/document_digitization.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nNflexport/documentflow/documentdigitization/v1beta1/document_digitization.proto\x12\x32\x66lexport.documentflow.documentdigitization.v1beta1\x1aLflexport/documentflow/documentdigitization/enums/v1beta1/audit_results.proto\x1aKflexport/documentflow/documentdigitization/enums/v1beta1/audit_source.proto\x1aMflexport/documentflow/documentdigitization/enums/v1beta1/json_operation.proto\x1aJflexport/documentflow/documentdigitization/enums/v1beta1/task_status.proto\x1aLflexport/documentflow/documentdigitization/enums/v1beta1/update_reason.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb4\x05\n\x14\x44ocumentDigitization\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x64ocument_fid\x18\x02 \x01(\t\x12\x1a\n\x12\x64ocument_type_slug\x18\x03 \x01(\t\x12\x1b\n\x0e\x65xtractor_name\x18\x04 \x01(\tH\x00\x88\x01\x01\x12!\n\x14\x64igitization_task_id\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x35\n\x0finitial_results\x18\x0b \x01(\x0b\x32\x17.google.protobuf.StructH\x02\x88\x01\x01\x12\x35\n\x0f\x63urrent_results\x18\x0c \x01(\x0b\x32\x17.google.protobuf.StructH\x03\x88\x01\x01\x12T\n\x06status\x18\r \x01(\x0e\x32\x44.flexport.documentflow.documentdigitization.enums.v1beta1.TaskStatus\x12.\n\ncreated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\ncreated_by\x18\x18 \x01(\tH\x04\x88\x01\x01\x12\x17\n\nupdated_by\x18\x19 \x01(\tH\x05\x88\x01\x01\x12\x17\n\ndeleted_by\x18\x1a \x01(\tH\x06\x88\x01\x01\x42\x11\n\x0f_extractor_nameB\x17\n\x15_digitization_task_idB\x12\n\x10_initial_resultsB\x12\n\x10_current_resultsB\r\n\x0b_created_byB\r\n\x0b_updated_byB\r\n\x0b_deleted_by"\xd5\x03\n\tChangeLog\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0f\x64igitization_id\x18\x02 \x01(\t\x12Z\n\toperation\x18\x0b \x01(\x0e\x32G.flexport.documentflow.documentdigitization.enums.v1beta1.JsonOperation\x12\x12\n\nfield_path\x18\x0c \x01(\t\x12\x11\n\told_value\x18\r \x01(\t\x12\x11\n\tnew_value\x18\x0e \x01(\t\x12]\n\x0eupdater_source\x18\x15 \x01(\x0e\x32\x45.flexport.documentflow.documentdigitization.enums.v1beta1.AuditSource\x12V\n\x06reason\x18\x16 \x01(\x0e\x32\x46.flexport.documentflow.documentdigitization.enums.v1beta1.UpdateReason\x12.\n\ncreated_at\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\ncreated_by\x18\x18 \x01(\tH\x00\x88\x01\x01\x42\r\n\x0b_created_by"\xec\x02\n\rAuditFeedback\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0f\x64igitization_id\x18\x02 \x01(\t\x12[\n\x0c\x61udit_source\x18\x0b \x01(\x0e\x32\x45.flexport.documentflow.documentdigitization.enums.v1beta1.AuditSource\x12]\n\raudit_results\x18\x0c \x01(\x0e\x32\x46.flexport.documentflow.documentdigitization.enums.v1beta1.AuditResults\x12\x15\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\r \x01(\tH\x00\x88\x01\x01\x12.\n\ncreated_at\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\ncreated_by\x18\x17 \x01(\tH\x01\x88\x01\x01\x42\x0b\n\t_feedbackB\r\n\x0b_created_byB\x8d\x01\n6com.flexport.documentflow.documentdigitization.v1beta1B\x19\x44ocumentDigitizationProtoP\x01\xea\x02\x35\x46lexport::DocumentFlow::DocumentDigitization::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.documentflow.documentdigitization.v1beta1.document_digitization_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n6com.flexport.documentflow.documentdigitization.v1beta1B\031DocumentDigitizationProtoP\001\352\0025Flexport::DocumentFlow::DocumentDigitization::V1Beta1"
    _globals["_DOCUMENTDIGITIZATION"]._serialized_start = 586
    _globals["_DOCUMENTDIGITIZATION"]._serialized_end = 1278
    _globals["_CHANGELOG"]._serialized_start = 1281
    _globals["_CHANGELOG"]._serialized_end = 1750
    _globals["_AUDITFEEDBACK"]._serialized_start = 1753
    _globals["_AUDITFEEDBACK"]._serialized_end = 2117
# @@protoc_insertion_point(module_scope)