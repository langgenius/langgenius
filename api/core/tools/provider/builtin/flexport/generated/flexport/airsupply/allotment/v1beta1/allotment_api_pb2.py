# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/airsupply/allotment/v1beta1/allotment_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n8flexport/airsupply/allotment/v1beta1/allotment_api.proto\x12$flexport.airsupply.allotment.v1beta1\x1a\x34\x66lexport/airsupply/allotment/v1beta1/allotment.proto"/\n\x15ListAllotmentsRequest\x12\x16\n\x0e\x61llotment_fids\x18\x01 \x03(\t"]\n\x16ListAllotmentsResponse\x12\x43\n\nallotments\x18\x01 \x03(\x0b\x32/.flexport.airsupply.allotment.v1beta1.Allotment2\x9c\x01\n\x0c\x41llotmentAPI\x12\x8b\x01\n\x0eListAllotments\x12;.flexport.airsupply.allotment.v1beta1.ListAllotmentsRequest\x1a<.flexport.airsupply.allotment.v1beta1.ListAllotmentsResponseBi\n(com.flexport.airsupply.allotment.v1beta1B\x11\x41llotmentApiProtoP\x01\xea\x02\'Flexport::AirSupply::Allotment::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.airsupply.allotment.v1beta1.allotment_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n(com.flexport.airsupply.allotment.v1beta1B\021AllotmentApiProtoP\001\352\002'Flexport::AirSupply::Allotment::V1Beta1"
    _globals["_LISTALLOTMENTSREQUEST"]._serialized_start = 152
    _globals["_LISTALLOTMENTSREQUEST"]._serialized_end = 199
    _globals["_LISTALLOTMENTSRESPONSE"]._serialized_start = 201
    _globals["_LISTALLOTMENTSRESPONSE"]._serialized_end = 294
    _globals["_ALLOTMENTAPI"]._serialized_start = 297
    _globals["_ALLOTMENTAPI"]._serialized_end = 453
# @@protoc_insertion_point(module_scope)