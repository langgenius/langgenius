# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/document_processor/document/v1beta1/referenced_entity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nDflexport/document_processor/document/v1beta1/referenced_entity.proto\x12+flexport.documentprocessor.document.v1beta1\x1a\x34\x66lexport/document_processor/util/v1beta1/utils.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xef\x01\n\x10ReferencedEntity\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x14\n\x0c\x64ocument_fid\x18\x02 \x01(\t\x12\x12\n\nentity_fid\x18\x03 \x01(\t\x12\x33\n\x0f\x63reated_at_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x14referenced_group_fid\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue"p\n\x12ReferencedEntities\x12Z\n\x13referenced_entities\x18\x01 \x03(\x0b\x32=.flexport.documentprocessor.document.v1beta1.ReferencedEntity"\x8e\x02\n\x17ReferencedEntityFilters\x12\x0c\n\x04\x66ids\x18\x01 \x03(\t\x12\x15\n\rdocument_fids\x18\x02 \x03(\t\x12\x13\n\x0b\x65ntity_fids\x18\x03 \x03(\t\x12L\n\x10\x63reated_at_range\x18\x04 \x01(\x0b\x32\x32.flexport.documentprocessor.util.v1beta1.DateRange\x12L\n\x10updated_at_range\x18\x05 \x01(\x0b\x32\x32.flexport.documentprocessor.util.v1beta1.DateRange\x12\x1d\n\x15referenced_group_fids\x18\x06 \x03(\tB{\n/com.flexport.documentprocessor.document.v1beta1B\x15ReferencedEntityProtoP\x01\xea\x02.Flexport::DocumentProcessor::Document::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.document_processor.document.v1beta1.referenced_entity_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n/com.flexport.documentprocessor.document.v1beta1B\025ReferencedEntityProtoP\001\352\002.Flexport::DocumentProcessor::Document::V1Beta1"
    _globals["_REFERENCEDENTITY"]._serialized_start = 237
    _globals["_REFERENCEDENTITY"]._serialized_end = 476
    _globals["_REFERENCEDENTITIES"]._serialized_start = 478
    _globals["_REFERENCEDENTITIES"]._serialized_end = 590
    _globals["_REFERENCEDENTITYFILTERS"]._serialized_start = 593
    _globals["_REFERENCEDENTITYFILTERS"]._serialized_end = 863
# @@protoc_insertion_point(module_scope)