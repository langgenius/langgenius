# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customs/cargotracking/nl/events/v1beta1/commercial_released.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nJflexport/customs/cargotracking/nl/events/v1beta1/commercial_released.proto\x12\x30\x66lexport.customs.cargotracking.nl.events.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\xf3\x01\n\x17\x43ommercialReleasedEvent\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x1cmaster_bill_of_lading_number\x18\x02 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12`\n\x13\x63ommercial_releases\x18\x05 \x03(\x0b\x32\x43.flexport.customs.cargotracking.nl.events.v1beta1.CommercialRelease"\xb3\x01\n\x11\x43ommercialRelease\x12\x18\n\x10\x63ontainer_number\x18\x01 \x01(\t\x12\x1d\n\x15release_to_party_name\x18\x02 \x01(\t\x12"\n\x1arelease_to_party_scac_code\x18\x03 \x01(\t\x12\x41\n\x1drelease_valid_until_date_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampBp\n4com.flexport.customs.cargotracking.nl.events.v1beta1P\x01\xea\x02\x35\x46lexport::Customs::CargoTracking::Nl::Events::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customs.cargotracking.nl.events.v1beta1.commercial_released_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n4com.flexport.customs.cargotracking.nl.events.v1beta1P\001\352\0025Flexport::Customs::CargoTracking::Nl::Events::V1Beta1"
    _globals["_COMMERCIALRELEASEDEVENT"]._serialized_start = 162
    _globals["_COMMERCIALRELEASEDEVENT"]._serialized_end = 405
    _globals["_COMMERCIALRELEASE"]._serialized_start = 408
    _globals["_COMMERCIALRELEASE"]._serialized_end = 587
# @@protoc_insertion_point(module_scope)