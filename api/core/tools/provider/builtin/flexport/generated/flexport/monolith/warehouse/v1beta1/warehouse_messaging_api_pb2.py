# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/warehouse/v1beta1/warehouse_messaging_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nAflexport/monolith/warehouse/v1beta1/warehouse_messaging_api.proto\x12#flexport.monolith.warehouse.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\xa8\x01\n\x1d\x46\x65tchWarehouseMessagesRequest\x12\x0f\n\x07\x66lex_id\x18\x01 \x01(\t\x12\x43\n\x04type\x18\x02 \x01(\x0e\x32\x30.flexport.monolith.warehouse.v1beta1.MessageTypeH\x00\x88\x01\x01\x12\x16\n\x0ewarehouse_code\x18\x03 \x01(\t\x12\x10\n\x08user_fid\x18\x04 \x01(\tB\x07\n\x05_type"\x80\x01\n\x1e\x46\x65tchWarehouseMessagesResponse\x12\x0f\n\x07\x66lex_id\x18\x01 \x01(\t\x12=\n\x07message\x18\x02 \x03(\x0b\x32,.flexport.monolith.warehouse.v1beta1.Message\x12\x0e\n\x06\x65rrors\x18\x03 \x03(\t"\xb2\x03\n\x07Message\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x46\n\x0cmessage_type\x18\x02 \x01(\x0e\x32\x30.flexport.monolith.warehouse.v1beta1.MessageType\x12\x0f\n\x07\x66lex_id\x18\x03 \x01(\t\x12\x41\n\x07\x63reator\x18\x04 \x01(\x0b\x32\x30.flexport.monolith.warehouse.v1beta1.MessageUser\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x62ody\x18\x06 \x01(\t\x12H\n\rviewing_party\x18\x07 \x03(\x0b\x32\x31.flexport.monolith.warehouse.v1beta1.ViewingParty\x12\x43\n\nattachment\x18\x08 \x03(\x0b\x32/.flexport.monolith.warehouse.v1beta1.Attachment\x12\x13\n\x0breply_to_id\x18\t \x01(\t\x12\x15\n\rreply_root_id\x18\n \x01(\t"\x7f\n\x0bMessageUser\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x63ompany_fid\x18\x04 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x07 \x01(\t"9\n\x0cViewingParty\x12\x13\n\x0b\x63ompany_fid\x18\x01 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x02 \x01(\t"=\n\nAttachment\x12\x17\n\x0f\x61ttachment_name\x18\x01 \x01(\t\x12\x16\n\x0e\x61ttachment_url\x18\x02 \x01(\t*u\n\x0bMessageType\x12\x18\n\x14MESSAGE_TYPE_INVALID\x10\x00\x12\x18\n\x14MESSAGE_TYPE_MESSAGE\x10\x01\x12\x16\n\x12MESSAGE_TYPE_EVENT\x10\x02\x12\x1a\n\x16MESSAGE_TYPE_EXCEPTION\x10\x03\x32\xbb\x01\n\x15WarehouseMessagingAPI\x12\xa1\x01\n\x16\x46\x65tchWarehouseMessages\x12\x42.flexport.monolith.warehouse.v1beta1.FetchWarehouseMessagesRequest\x1a\x43.flexport.monolith.warehouse.v1beta1.FetchWarehouseMessagesResponseBp\n\'com.flexport.monolith.warehouse.v1beta1B\x1aWarehouseMessagingApiProtoP\x01\xea\x02&Flexport::Monolith::Warehouse::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.warehouse.v1beta1.warehouse_messaging_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n'com.flexport.monolith.warehouse.v1beta1B\032WarehouseMessagingApiProtoP\001\352\002&Flexport::Monolith::Warehouse::V1Beta1"
    _globals["_MESSAGETYPE"]._serialized_start = 1129
    _globals["_MESSAGETYPE"]._serialized_end = 1246
    _globals["_FETCHWAREHOUSEMESSAGESREQUEST"]._serialized_start = 140
    _globals["_FETCHWAREHOUSEMESSAGESREQUEST"]._serialized_end = 308
    _globals["_FETCHWAREHOUSEMESSAGESRESPONSE"]._serialized_start = 311
    _globals["_FETCHWAREHOUSEMESSAGESRESPONSE"]._serialized_end = 439
    _globals["_MESSAGE"]._serialized_start = 442
    _globals["_MESSAGE"]._serialized_end = 876
    _globals["_MESSAGEUSER"]._serialized_start = 878
    _globals["_MESSAGEUSER"]._serialized_end = 1005
    _globals["_VIEWINGPARTY"]._serialized_start = 1007
    _globals["_VIEWINGPARTY"]._serialized_end = 1064
    _globals["_ATTACHMENT"]._serialized_start = 1066
    _globals["_ATTACHMENT"]._serialized_end = 1127
    _globals["_WAREHOUSEMESSAGINGAPI"]._serialized_start = 1249
    _globals["_WAREHOUSEMESSAGINGAPI"]._serialized_end = 1436
# @@protoc_insertion_point(module_scope)