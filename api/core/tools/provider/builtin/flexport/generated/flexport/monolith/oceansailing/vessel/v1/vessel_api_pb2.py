# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/oceansailing/vessel/v1/vessel_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n9flexport/monolith/oceansailing/vessel/v1/vessel_api.proto\x12(flexport.monolith.oceansailing.vessel.v1\x1a\x35\x66lexport/monolith/oceansailing/vessel/v1/vessel.proto"&\n\x10GetVesselRequest\x12\x12\n\nvessel_fid\x18\x01 \x01(\t"U\n\x11GetVesselResponse\x12@\n\x06vessel\x18\x01 \x01(\x0b\x32\x30.flexport.monolith.oceansailing.vessel.v1.Vessel2\x92\x01\n\tVesselAPI\x12\x84\x01\n\tGetVessel\x12:.flexport.monolith.oceansailing.vessel.v1.GetVesselRequest\x1a;.flexport.monolith.oceansailing.vessel.v1.GetVesselResponseBo\n,com.flexport.monolith.oceansailing.vessel.v1B\x0eVesselApiProtoP\x01\xea\x02,Flexport::Monolith::OceanSailing::Vessel::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.monolith.oceansailing.vessel.v1.vessel_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n,com.flexport.monolith.oceansailing.vessel.v1B\016VesselApiProtoP\001\352\002,Flexport::Monolith::OceanSailing::Vessel::V1"
    _globals["_GETVESSELREQUEST"]._serialized_start = 158
    _globals["_GETVESSELREQUEST"]._serialized_end = 196
    _globals["_GETVESSELRESPONSE"]._serialized_start = 198
    _globals["_GETVESSELRESPONSE"]._serialized_end = 283
    _globals["_VESSELAPI"]._serialized_start = 286
    _globals["_VESSELAPI"]._serialized_end = 432
# @@protoc_insertion_point(module_scope)