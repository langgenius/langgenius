# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/storage/events/v1beta1/file_object_updated.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n9flexport/storage/events/v1beta1/file_object_updated.proto\x12\x1f\x66lexport.storage.events.v1beta1\x1a/flexport/storage/permission/v1/permission.proto\x1a&flexport/storage/tag/v1beta1/tag.proto"\xa3\x02\n\x11\x46ileObjectUpdated\x12\x17\n\x0f\x66ile_object_fid\x18\x01 \x01(\t\x12/\n\x04tags\x18\x02 \x03(\x0b\x32!.flexport.storage.tag.v1beta1.Tag\x12R\n\x08metadata\x18\x03 \x03(\x0b\x32@.flexport.storage.events.v1beta1.FileObjectUpdated.MetadataEntry\x12?\n\x0bpermissions\x18\x04 \x03(\x0b\x32*.flexport.storage.permission.v1.Permission\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x64\n#com.flexport.storage.events.v1beta1B\x16\x46ileObjectUpdatedProtoP\x01\xea\x02"Flexport::Storage::Events::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.storage.events.v1beta1.file_object_updated_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b'\n#com.flexport.storage.events.v1beta1B\026FileObjectUpdatedProtoP\001\352\002"Flexport::Storage::Events::V1Beta1'
    _globals["_FILEOBJECTUPDATED_METADATAENTRY"]._options = None
    _globals["_FILEOBJECTUPDATED_METADATAENTRY"]._serialized_options = b"8\001"
    _globals["_FILEOBJECTUPDATED"]._serialized_start = 184
    _globals["_FILEOBJECTUPDATED"]._serialized_end = 475
    _globals["_FILEOBJECTUPDATED_METADATAENTRY"]._serialized_start = 428
    _globals["_FILEOBJECTUPDATED_METADATAENTRY"]._serialized_end = 475
# @@protoc_insertion_point(module_scope)