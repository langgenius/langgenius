# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/network/v1beta1/entity_weekly_hours.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n2flexport/network/v1beta1/entity_weekly_hours.proto\x12\x18\x66lexport.network.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xd5\x06\n\x11\x45ntityWeeklyHours\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tentity_id\x18\x02 \x01(\x03\x12\x13\n\x0b\x65ntity_type\x18\x03 \x01(\t\x12\x32\n\x06monday\x18\x04 \x03(\x0b\x32".flexport.network.v1beta1.Timespan\x12\x17\n\x0fmonday_24_hours\x18\x10 \x01(\x08\x12\x33\n\x07tuesday\x18\x05 \x03(\x0b\x32".flexport.network.v1beta1.Timespan\x12\x18\n\x10tuesday_24_hours\x18\x11 \x01(\x08\x12\x35\n\twednesday\x18\x06 \x03(\x0b\x32".flexport.network.v1beta1.Timespan\x12\x1a\n\x12wednesday_24_hours\x18\x12 \x01(\x08\x12\x34\n\x08thursday\x18\x07 \x03(\x0b\x32".flexport.network.v1beta1.Timespan\x12\x19\n\x11thursday_24_hours\x18\x13 \x01(\x08\x12\x32\n\x06\x66riday\x18\x08 \x03(\x0b\x32".flexport.network.v1beta1.Timespan\x12\x17\n\x0f\x66riday_24_hours\x18\x14 \x01(\x08\x12\x34\n\x08saturday\x18\t \x03(\x0b\x32".flexport.network.v1beta1.Timespan\x12\x19\n\x11saturday_24_hours\x18\x15 \x01(\x08\x12\x32\n\x06sunday\x18\n \x03(\x0b\x32".flexport.network.v1beta1.Timespan\x12\x17\n\x0fsunday_24_hours\x18\x16 \x01(\x08\x12/\n\ttime_zone\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12<\n\rtype_of_hours\x18\x0c \x01(\x0e\x32%.flexport.network.v1beta1.TypeOfHours\x12\x12\n\noverridden\x18\x0f \x01(\x08\x12.\n\ncreated_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp"\x1e\n\x08Timespan\x12\x12\n\ntime_value\x18\x01 \x03(\t*\x90\x01\n\x0bTypeOfHours\x12\x19\n\x15TYPE_OF_HOURS_INVALID\x10\x00\x12 \n\x1cTYPE_OF_HOURS_BUSINESS_HOURS\x10\x01\x12!\n\x1dTYPE_OF_HOURS_RECEIVING_HOURS\x10\x02\x12!\n\x1dTYPE_OF_HOURS_OPERATING_HOURS\x10\x03\x42U\n\x1c\x63om.flexport.network.v1beta1B\x16\x45ntityWeeklyHoursProtoP\x01\xea\x02\x1a\x46lexport::Network::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.network.v1beta1.entity_weekly_hours_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n\034com.flexport.network.v1beta1B\026EntityWeeklyHoursProtoP\001\352\002\032Flexport::Network::V1Beta1"
    )
    _globals["_TYPEOFHOURS"]._serialized_start = 1034
    _globals["_TYPEOFHOURS"]._serialized_end = 1178
    _globals["_ENTITYWEEKLYHOURS"]._serialized_start = 146
    _globals["_ENTITYWEEKLYHOURS"]._serialized_end = 999
    _globals["_TIMESPAN"]._serialized_start = 1001
    _globals["_TIMESPAN"]._serialized_end = 1031
# @@protoc_insertion_point(module_scope)