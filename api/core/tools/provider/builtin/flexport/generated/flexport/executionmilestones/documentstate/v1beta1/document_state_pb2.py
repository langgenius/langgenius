# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executionmilestones/documentstate/v1beta1/document_state.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nGflexport/executionmilestones/documentstate/v1beta1/document_state.proto\x12\x32\x66lexport.executionmilestones.documentstate.v1beta1\x1aOflexport/monolith/documents/monolith_documents/v1beta1/monolith_documents.proto"\xe7\x01\n\rDocumentState\x12\x63\n\tdocuments\x18\x01 \x03(\x0b\x32P.flexport.executionmilestones.documentstate.v1beta1.DocumentState.DocumentsEntry\x1aq\n\x0e\x44ocumentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0b\x32?.flexport.monolith.documents.monolithdocuments.v1beta1.Document:\x02\x38\x01\x42N\n6com.flexport.executionmilestones.documentstate.v1beta1B\x12\x44ocumentStateProtoP\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executionmilestones.documentstate.v1beta1.document_state_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n6com.flexport.executionmilestones.documentstate.v1beta1B\022DocumentStateProtoP\001"
    _globals["_DOCUMENTSTATE_DOCUMENTSENTRY"]._options = None
    _globals["_DOCUMENTSTATE_DOCUMENTSENTRY"]._serialized_options = b"8\001"
    _globals["_DOCUMENTSTATE"]._serialized_start = 209
    _globals["_DOCUMENTSTATE"]._serialized_end = 440
    _globals["_DOCUMENTSTATE_DOCUMENTSENTRY"]._serialized_start = 327
    _globals["_DOCUMENTSTATE_DOCUMENTSENTRY"]._serialized_end = 440
# @@protoc_insertion_point(module_scope)