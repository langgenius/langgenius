# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/customs/events/v1beta1/ams_filing_updated.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nAflexport/monolith/customs/events/v1beta1/ams_filing_updated.proto\x12(flexport.monolith.customs.events.v1beta1\x1a/flexport/monolith/customs/v1beta1/ams_api.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb2\x01\n\x10\x41msFilingUpdated\x12\x13\n\x0b\x62ill_number\x18\x01 \x01(\t\x12\x42\n\x06status\x18\x02 \x01(\x0e\x32\x32.flexport.monolith.customs.v1beta1.AmsFilingStatus\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rshipment_fids\x18\x04 \x03(\tBv\n,com.flexport.monolith.customs.events.v1beta1B\x15\x41msFilingUpdatedProtoP\x01\xea\x02,Flexport::Monolith::Customs::Events::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.customs.events.v1beta1.ams_filing_updated_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n,com.flexport.monolith.customs.events.v1beta1B\025AmsFilingUpdatedProtoP\001\352\002,Flexport::Monolith::Customs::Events::V1Beta1"
    _globals["_AMSFILINGUPDATED"]._serialized_start = 194
    _globals["_AMSFILINGUPDATED"]._serialized_end = 372
# @@protoc_insertion_point(module_scope)