# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/authorization/retriever/v1beta1/retriever_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n<flexport/authorization/retriever/v1beta1/retriever_api.proto\x12(flexport.authorization.retriever.v1beta1\x1a&flexport/authorization/v1/common.proto\x1a&flexport/authorization/v2/common.proto"`\n\x14GetOperationsRequest\x12\x34\n\x06\x61\x63tors\x18\x03 \x03(\x0b\x32 .flexport.authorization.v1.ActorB\x02\x18\x01\x12\x12\n\nactor_fids\x18\x04 \x03(\t"\xf7\x01\n\x15GetOperationsResponse\x12j\n\x11\x61\x63tors_operations\x18\x02 \x03(\x0b\x32O.flexport.authorization.retriever.v1beta1.GetOperationsResponse.ActorOperations\x1ar\n\x0f\x41\x63torOperations\x12\x33\n\x05\x61\x63tor\x18\x01 \x01(\x0b\x32 .flexport.authorization.v1.ActorB\x02\x18\x01\x12\x17\n\x0foperation_slugs\x18\x02 \x03(\t\x12\x11\n\tactor_fid\x18\x03 \x01(\t"\xa6\x01\n\x1fGetResourcesForOperationRequest\x12\x33\n\x05\x61\x63tor\x18\x01 \x01(\x0b\x32 .flexport.authorization.v1.ActorB\x02\x18\x01\x12\x37\n\toperation\x18\x02 \x01(\x0b\x32$.flexport.authorization.v1.Operation\x12\x11\n\tactor_fid\x18\x03 \x01(\t:\x02\x18\x01"Z\n GetResourcesForOperationResponse\x12\x36\n\tresources\x18\x01 \x03(\x0b\x32#.flexport.authorization.v1.Resource"\xf8\x01\n"FilterResourcesForOperationRequest\x12\x33\n\x05\x61\x63tor\x18\x01 \x01(\x0b\x32 .flexport.authorization.v1.ActorB\x02\x18\x01\x12\x37\n\toperation\x18\x02 \x01(\x0b\x32$.flexport.authorization.v1.Operation\x12:\n\tresources\x18\x03 \x03(\x0b\x32#.flexport.authorization.v1.ResourceB\x02\x18\x01\x12\x15\n\rresource_fids\x18\x04 \x03(\t\x12\x11\n\tactor_fid\x18\x05 \x01(\t"x\n#FilterResourcesForOperationResponse\x12:\n\tresources\x18\x01 \x03(\x0b\x32#.flexport.authorization.v1.ResourceB\x02\x18\x01\x12\x15\n\rresource_fids\x18\x02 \x03(\t"\xd7\x01\n FilterPermissionsForActorRequest\x12\x33\n\x05\x61\x63tor\x18\x01 \x01(\x0b\x32 .flexport.authorization.v1.ActorB\x02\x18\x01\x12\x43\n\x14permissions_with_fid\x18\x03 \x03(\x0b\x32%.flexport.authorization.v2.Permission\x12\x11\n\tactor_fid\x18\x04 \x01(\t\x12&\n\x1e\x66ilter_out_invalid_permissions\x18\x05 \x01(\x08"_\n!FilterPermissionsForActorResponse\x12:\n\x0bpermissions\x18\x02 \x03(\x0b\x32%.flexport.authorization.v2.Permission2\xc9\x05\n\x0cRetrieverAPI\x12\x90\x01\n\rGetOperations\x12>.flexport.authorization.retriever.v1beta1.GetOperationsRequest\x1a?.flexport.authorization.retriever.v1beta1.GetOperationsResponse\x12\xb1\x01\n\x18GetResourcesForOperation\x12I.flexport.authorization.retriever.v1beta1.GetResourcesForOperationRequest\x1aJ.flexport.authorization.retriever.v1beta1.GetResourcesForOperationResponse\x12\xba\x01\n\x1b\x46ilterResourcesForOperation\x12L.flexport.authorization.retriever.v1beta1.FilterResourcesForOperationRequest\x1aM.flexport.authorization.retriever.v1beta1.FilterResourcesForOperationResponse\x12\xb4\x01\n\x19\x46ilterPermissionsForActor\x12J.flexport.authorization.retriever.v1beta1.FilterPermissionsForActorRequest\x1aK.flexport.authorization.retriever.v1beta1.FilterPermissionsForActorResponseBq\n,com.flexport.authorization.retriever.v1beta1B\x11RetrieverApiProtoP\x01\xea\x02+Flexport::Authorization::Retriever::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.authorization.retriever.v1beta1.retriever_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n,com.flexport.authorization.retriever.v1beta1B\021RetrieverApiProtoP\001\352\002+Flexport::Authorization::Retriever::V1Beta1"
    _globals["_GETOPERATIONSREQUEST"].fields_by_name["actors"]._options = None
    _globals["_GETOPERATIONSREQUEST"].fields_by_name["actors"]._serialized_options = b"\030\001"
    _globals["_GETOPERATIONSRESPONSE_ACTOROPERATIONS"].fields_by_name["actor"]._options = None
    _globals["_GETOPERATIONSRESPONSE_ACTOROPERATIONS"].fields_by_name["actor"]._serialized_options = b"\030\001"
    _globals["_GETRESOURCESFOROPERATIONREQUEST"].fields_by_name["actor"]._options = None
    _globals["_GETRESOURCESFOROPERATIONREQUEST"].fields_by_name["actor"]._serialized_options = b"\030\001"
    _globals["_GETRESOURCESFOROPERATIONREQUEST"]._options = None
    _globals["_GETRESOURCESFOROPERATIONREQUEST"]._serialized_options = b"\030\001"
    _globals["_FILTERRESOURCESFOROPERATIONREQUEST"].fields_by_name["actor"]._options = None
    _globals["_FILTERRESOURCESFOROPERATIONREQUEST"].fields_by_name["actor"]._serialized_options = b"\030\001"
    _globals["_FILTERRESOURCESFOROPERATIONREQUEST"].fields_by_name["resources"]._options = None
    _globals["_FILTERRESOURCESFOROPERATIONREQUEST"].fields_by_name["resources"]._serialized_options = b"\030\001"
    _globals["_FILTERRESOURCESFOROPERATIONRESPONSE"].fields_by_name["resources"]._options = None
    _globals["_FILTERRESOURCESFOROPERATIONRESPONSE"].fields_by_name["resources"]._serialized_options = b"\030\001"
    _globals["_FILTERPERMISSIONSFORACTORREQUEST"].fields_by_name["actor"]._options = None
    _globals["_FILTERPERMISSIONSFORACTORREQUEST"].fields_by_name["actor"]._serialized_options = b"\030\001"
    _globals["_GETOPERATIONSREQUEST"]._serialized_start = 186
    _globals["_GETOPERATIONSREQUEST"]._serialized_end = 282
    _globals["_GETOPERATIONSRESPONSE"]._serialized_start = 285
    _globals["_GETOPERATIONSRESPONSE"]._serialized_end = 532
    _globals["_GETOPERATIONSRESPONSE_ACTOROPERATIONS"]._serialized_start = 418
    _globals["_GETOPERATIONSRESPONSE_ACTOROPERATIONS"]._serialized_end = 532
    _globals["_GETRESOURCESFOROPERATIONREQUEST"]._serialized_start = 535
    _globals["_GETRESOURCESFOROPERATIONREQUEST"]._serialized_end = 701
    _globals["_GETRESOURCESFOROPERATIONRESPONSE"]._serialized_start = 703
    _globals["_GETRESOURCESFOROPERATIONRESPONSE"]._serialized_end = 793
    _globals["_FILTERRESOURCESFOROPERATIONREQUEST"]._serialized_start = 796
    _globals["_FILTERRESOURCESFOROPERATIONREQUEST"]._serialized_end = 1044
    _globals["_FILTERRESOURCESFOROPERATIONRESPONSE"]._serialized_start = 1046
    _globals["_FILTERRESOURCESFOROPERATIONRESPONSE"]._serialized_end = 1166
    _globals["_FILTERPERMISSIONSFORACTORREQUEST"]._serialized_start = 1169
    _globals["_FILTERPERMISSIONSFORACTORREQUEST"]._serialized_end = 1384
    _globals["_FILTERPERMISSIONSFORACTORRESPONSE"]._serialized_start = 1386
    _globals["_FILTERPERMISSIONSFORACTORRESPONSE"]._serialized_end = 1481
    _globals["_RETRIEVERAPI"]._serialized_start = 1484
    _globals["_RETRIEVERAPI"]._serialized_end = 2197
# @@protoc_insertion_point(module_scope)