# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/storage/tag/v1beta1/tag_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n*flexport/storage/tag/v1beta1/tag_api.proto\x12\x1c\x66lexport.storage.tag.v1beta1\x1a&flexport/storage/tag/v1beta1/tag.proto"B\n\x10\x43reateTagRequest\x12.\n\x03tag\x18\x01 \x01(\x0b\x32!.flexport.storage.tag.v1beta1.Tag"8\n\x11\x43reateTagResponse\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\x12\x0f\n\x07tag_fid\x18\x02 \x01(\t")\n\x0eGetTagsRequest\x12\x17\n\x0f\x66ile_object_fid\x18\x01 \x01(\t"B\n\x0fGetTagsResponse\x12/\n\x04tags\x18\x01 \x03(\x0b\x32!.flexport.storage.tag.v1beta1.Tag"\xa2\x01\n\x11UpsertTagsRequest\x12\x17\n\x0f\x66ile_object_fid\x18\x01 \x01(\t\x12G\n\x04tags\x18\x02 \x03(\x0b\x32\x39.flexport.storage.tag.v1beta1.UpsertTagsRequest.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"(\n\x12UpsertTagsResponse\x12\x12\n\nsuccessful\x18\x01 \x01(\x08"\xb6\x01\n\x15UpsertMetadataRequest\x12\x17\n\x0f\x66ile_object_fid\x18\x01 \x01(\t\x12S\n\x08metadata\x18\x02 \x03(\x0b\x32\x41.flexport.storage.tag.v1beta1.UpsertMetadataRequest.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"=\n\x16UpsertMetadataResponse\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\x12\x0f\n\x07tag_fid\x18\x02 \x01(\t"-\n\x12GetMetadataRequest\x12\x17\n\x0f\x66ile_object_fid\x18\x01 \x01(\t"\x99\x01\n\x13GetMetadataResponse\x12Q\n\x08metadata\x18\x01 \x03(\x0b\x32?.flexport.storage.tag.v1beta1.GetMetadataResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xc0\x04\n\x06TagAPI\x12l\n\tCreateTag\x12..flexport.storage.tag.v1beta1.CreateTagRequest\x1a/.flexport.storage.tag.v1beta1.CreateTagResponse\x12\x66\n\x07GetTags\x12,.flexport.storage.tag.v1beta1.GetTagsRequest\x1a-.flexport.storage.tag.v1beta1.GetTagsResponse\x12o\n\nUpsertTags\x12/.flexport.storage.tag.v1beta1.UpsertTagsRequest\x1a\x30.flexport.storage.tag.v1beta1.UpsertTagsResponse\x12{\n\x0eUpsertMetadata\x12\x33.flexport.storage.tag.v1beta1.UpsertMetadataRequest\x1a\x34.flexport.storage.tag.v1beta1.UpsertMetadataResponse\x12r\n\x0bGetMetadata\x12\x30.flexport.storage.tag.v1beta1.GetMetadataRequest\x1a\x31.flexport.storage.tag.v1beta1.GetMetadataResponseBS\n com.flexport.storage.tag.v1beta1B\x0bTagApiProtoP\x01\xea\x02\x1f\x46lexport::Storage::Tag::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.storage.tag.v1beta1.tag_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n com.flexport.storage.tag.v1beta1B\013TagApiProtoP\001\352\002\037Flexport::Storage::Tag::V1Beta1"
    )
    _globals["_UPSERTTAGSREQUEST_TAGSENTRY"]._options = None
    _globals["_UPSERTTAGSREQUEST_TAGSENTRY"]._serialized_options = b"8\001"
    _globals["_UPSERTMETADATAREQUEST_METADATAENTRY"]._options = None
    _globals["_UPSERTMETADATAREQUEST_METADATAENTRY"]._serialized_options = b"8\001"
    _globals["_GETMETADATARESPONSE_METADATAENTRY"]._options = None
    _globals["_GETMETADATARESPONSE_METADATAENTRY"]._serialized_options = b"8\001"
    _globals["_CREATETAGREQUEST"]._serialized_start = 116
    _globals["_CREATETAGREQUEST"]._serialized_end = 182
    _globals["_CREATETAGRESPONSE"]._serialized_start = 184
    _globals["_CREATETAGRESPONSE"]._serialized_end = 240
    _globals["_GETTAGSREQUEST"]._serialized_start = 242
    _globals["_GETTAGSREQUEST"]._serialized_end = 283
    _globals["_GETTAGSRESPONSE"]._serialized_start = 285
    _globals["_GETTAGSRESPONSE"]._serialized_end = 351
    _globals["_UPSERTTAGSREQUEST"]._serialized_start = 354
    _globals["_UPSERTTAGSREQUEST"]._serialized_end = 516
    _globals["_UPSERTTAGSREQUEST_TAGSENTRY"]._serialized_start = 473
    _globals["_UPSERTTAGSREQUEST_TAGSENTRY"]._serialized_end = 516
    _globals["_UPSERTTAGSRESPONSE"]._serialized_start = 518
    _globals["_UPSERTTAGSRESPONSE"]._serialized_end = 558
    _globals["_UPSERTMETADATAREQUEST"]._serialized_start = 561
    _globals["_UPSERTMETADATAREQUEST"]._serialized_end = 743
    _globals["_UPSERTMETADATAREQUEST_METADATAENTRY"]._serialized_start = 696
    _globals["_UPSERTMETADATAREQUEST_METADATAENTRY"]._serialized_end = 743
    _globals["_UPSERTMETADATARESPONSE"]._serialized_start = 745
    _globals["_UPSERTMETADATARESPONSE"]._serialized_end = 806
    _globals["_GETMETADATAREQUEST"]._serialized_start = 808
    _globals["_GETMETADATAREQUEST"]._serialized_end = 853
    _globals["_GETMETADATARESPONSE"]._serialized_start = 856
    _globals["_GETMETADATARESPONSE"]._serialized_end = 1009
    _globals["_GETMETADATARESPONSE_METADATAENTRY"]._serialized_start = 696
    _globals["_GETMETADATARESPONSE_METADATAENTRY"]._serialized_end = 743
    _globals["_TAGAPI"]._serialized_start = 1012
    _globals["_TAGAPI"]._serialized_end = 1588
# @@protoc_insertion_point(module_scope)