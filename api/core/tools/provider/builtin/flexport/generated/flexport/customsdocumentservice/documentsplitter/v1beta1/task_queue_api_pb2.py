# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customsdocumentservice/documentsplitter/v1beta1/task_queue_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nMflexport/customsdocumentservice/documentsplitter/v1beta1/task_queue_api.proto\x12\x38\x66lexport.customsdocumentservice.documentsplitter.v1beta1"R\n\tQueueItem\x12\x14\n\x0c\x64ocument_fid\x18\x01 \x01(\t\x12\x1c\n\x14uploaded_by_user_fid\x18\x02 \x01(\t\x12\x11\n\tclient_id\x18\x03 \x01(\t"\x13\n\x11\x43learQueueRequest")\n\x12\x43learQueueResponse\x12\x13\n\x0bnum_removed\x18\x01 \x01(\x05"\x12\n\x10ListQueueRequest"m\n\x11ListQueueResponse\x12X\n\x0bqueue_items\x18\x01 \x03(\x0b\x32\x43.flexport.customsdocumentservice.documentsplitter.v1beta1.QueueItem2\xe3\x02\n\x0cTaskQueueAPI\x12\xa9\x01\n\nClearQueue\x12K.flexport.customsdocumentservice.documentsplitter.v1beta1.ClearQueueRequest\x1aL.flexport.customsdocumentservice.documentsplitter.v1beta1.ClearQueueResponse"\x00\x12\xa6\x01\n\tListQueue\x12J.flexport.customsdocumentservice.documentsplitter.v1beta1.ListQueueRequest\x1aK.flexport.customsdocumentservice.documentsplitter.v1beta1.ListQueueResponse"\x00\x42\x98\x01\n<com.flexport.customsdocumentservice.documentsplitter.v1beta1B\x18\x44ocumentSplitterAPIProtoP\x01\xea\x02;Flexport::CustomsDocumentService::DocumentSplitter::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customsdocumentservice.documentsplitter.v1beta1.task_queue_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n<com.flexport.customsdocumentservice.documentsplitter.v1beta1B\030DocumentSplitterAPIProtoP\001\352\002;Flexport::CustomsDocumentService::DocumentSplitter::V1Beta1"
    _globals["_QUEUEITEM"]._serialized_start = 139
    _globals["_QUEUEITEM"]._serialized_end = 221
    _globals["_CLEARQUEUEREQUEST"]._serialized_start = 223
    _globals["_CLEARQUEUEREQUEST"]._serialized_end = 242
    _globals["_CLEARQUEUERESPONSE"]._serialized_start = 244
    _globals["_CLEARQUEUERESPONSE"]._serialized_end = 285
    _globals["_LISTQUEUEREQUEST"]._serialized_start = 287
    _globals["_LISTQUEUEREQUEST"]._serialized_end = 305
    _globals["_LISTQUEUERESPONSE"]._serialized_start = 307
    _globals["_LISTQUEUERESPONSE"]._serialized_end = 416
    _globals["_TASKQUEUEAPI"]._serialized_start = 419
    _globals["_TASKQUEUEAPI"]._serialized_end = 774
# @@protoc_insertion_point(module_scope)