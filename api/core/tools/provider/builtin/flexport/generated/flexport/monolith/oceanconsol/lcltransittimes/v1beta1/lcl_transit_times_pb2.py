# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/oceanconsol/lcltransittimes/v1beta1/lcl_transit_times.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nMflexport/monolith/oceanconsol/lcltransittimes/v1beta1/lcl_transit_times.proto\x12\x35\x66lexport.monolith.oceanconsol.lcltransittimes.v1beta1\x1a\x1egoogle/protobuf/wrappers.proto"\xcb\x04\n\x16LclTransitTimesRequest\x12\x11\n\torigin_id\x18\x01 \x01(\x05\x12\x16\n\x0e\x64\x65stination_id\x18\x02 \x01(\x05\x12\x32\n\rorigin_via_id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x37\n\x12\x64\x65stination_via_id\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12Z\n\rservice_level\x18\x05 \x01(\x0e\x32\x43.flexport.monolith.oceanconsol.lcltransittimes.v1beta1.ServiceLevel\x12.\n\tclient_id\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x35\n\x10transit_time_min\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x35\n\x10transit_time_max\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x32\n\rorigin_cfs_id\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x37\n\x12\x64\x65stination_cfs_id\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x32\n\rinland_cfs_id\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int32Value"\xe2\x02\n\x17LclTransitTimesResponse\x12p\n\x19lcl_transit_times_request\x18\x01 \x01(\x0b\x32M.flexport.monolith.oceanconsol.lcltransittimes.v1beta1.LclTransitTimesRequest\x12l\n\x17on_time_execution_times\x18\x02 \x01(\x0b\x32K.flexport.monolith.oceanconsol.lcltransittimes.v1beta1.OnTimeExecutionTimes\x12g\n\x14quoted_transit_times\x18\x03 \x01(\x0b\x32I.flexport.monolith.oceanconsol.lcltransittimes.v1beta1.QuotedTransitTimes"\x91\x02\n\x14OnTimeExecutionTimes\x12%\n\x1d\x63onsolidation_processing_days\x18\x01 \x01(\t\x12\x1d\n\x15\x64\x65livery_to_port_days\x18\x02 \x01(\t\x12$\n\x1corigin_ingate_departure_days\x18\x03 \x01(\t\x12\x19\n\x11port_to_port_days\x18\x04 \x01(\t\x12-\n%destination_arrival_avail_unload_days\x18\x05 \x01(\t\x12\x1a\n\x12port_recovery_days\x18\x06 \x01(\t\x12\'\n\x1f\x64\x65\x63onsolidation_processing_days\x18\x07 \x01(\t"\xa4\x01\n\x12QuotedTransitTimes\x12\x1a\n\x12\x63onsolidation_days\x18\x01 \x01(\x05\x12\x19\n\x11origin_dwell_days\x18\x02 \x01(\x05\x12\x19\n\x11port_to_port_days\x18\x03 \x01(\x05\x12\x1e\n\x16\x64\x65stination_dwell_days\x18\x04 \x01(\x05\x12\x1c\n\x14\x64\x65\x63onsolidation_days\x18\x05 \x01(\x05*|\n\x0cServiceLevel\x12\x19\n\x15SERVICE_LEVEL_INVALID\x10\x00\x12\x19\n\x15SERVICE_LEVEL_PREMIUM\x10\x01\x12\x1a\n\x16SERVICE_LEVEL_STANDARD\x10\x02\x12\x1a\n\x16SERVICE_LEVEL_FLEXIBLE\x10\x03\x42\x8f\x01\n9com.flexport.monolith.oceanconsol.lcltransittimes.v1beta1B\x14LclTransitTimesProtoP\x01\xea\x02\x39\x46lexport::Monolith::OceanConsol::LclTransitTimes::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.oceanconsol.lcltransittimes.v1beta1.lcl_transit_times_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n9com.flexport.monolith.oceanconsol.lcltransittimes.v1beta1B\024LclTransitTimesProtoP\001\352\0029Flexport::Monolith::OceanConsol::LclTransitTimes::V1Beta1"
    _globals["_SERVICELEVEL"]._serialized_start = 1558
    _globals["_SERVICELEVEL"]._serialized_end = 1682
    _globals["_LCLTRANSITTIMESREQUEST"]._serialized_start = 169
    _globals["_LCLTRANSITTIMESREQUEST"]._serialized_end = 756
    _globals["_LCLTRANSITTIMESRESPONSE"]._serialized_start = 759
    _globals["_LCLTRANSITTIMESRESPONSE"]._serialized_end = 1113
    _globals["_ONTIMEEXECUTIONTIMES"]._serialized_start = 1116
    _globals["_ONTIMEEXECUTIONTIMES"]._serialized_end = 1389
    _globals["_QUOTEDTRANSITTIMES"]._serialized_start = 1392
    _globals["_QUOTEDTRANSITTIMES"]._serialized_end = 1556
# @@protoc_insertion_point(module_scope)