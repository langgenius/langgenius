# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/shipperexp/userlocalinfo/v1beta1/user_local_info.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n?flexport/shipperexp/userlocalinfo/v1beta1/user_local_info.proto\x12)flexport.shipperexp.userlocalinfo.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\x98\x02\n\x13UserLocalInfoEntity\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x10\n\x08user_fid\x18\x02 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t\x12\x18\n\x10local_first_name\x18\x04 \x01(\t\x12\x17\n\x0flocal_last_name\x18\x05 \x01(\t\x12\x17\n\x0flocal_full_name\x18\x06 \x01(\t\x12\x16\n\x0elocal_language\x18\x07 \x01(\t\x12\x33\n\x0f\x63reated_at_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampBt\n-com.flexport.shipperexp.userlocalinfo.v1beta1B\x12UserLocalInfoProtoP\x01\xea\x02,Flexport::ShipperExp::UserLocalInfo::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.shipperexp.userlocalinfo.v1beta1.user_local_info_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n-com.flexport.shipperexp.userlocalinfo.v1beta1B\022UserLocalInfoProtoP\001\352\002,Flexport::ShipperExp::UserLocalInfo::V1Beta1"
    _globals["_USERLOCALINFOENTITY"]._serialized_start = 144
    _globals["_USERLOCALINFOENTITY"]._serialized_end = 424
# @@protoc_insertion_point(module_scope)