# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/oceanfmtassignment/fmtassignment/v1beta1/fmt_assignment.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nOflexport/monolith/oceanfmtassignment/fmtassignment/v1beta1/fmt_assignment.proto\x12:flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1\x1a\x39\x66lexport/os/v1/types/walltimedate/v1/wall_time_date.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xa6\x0b\n\rFmtAssignment\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12@\n\x1aocean_supply_inventory_fid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12G\n!ocean_supply_inventory_bucket_fid\x18# \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x46\n ocean_supply_carrier_profile_fid\x18\x16 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14legacy_allocation_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0c\n\x04teus\x18\x04 \x01(\x05\x12\x10\n\x08\x65td_week\x18\x05 \x01(\x05\x12\x10\n\x08\x65td_year\x18\x06 \x01(\x05\x12\x30\n\x0c\x63reated_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x64\x65leted_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0c\x63\x61rrier_name\x18\t \x01(\t\x12\x17\n\x0f\x63ontract_number\x18\n \x01(\t\x12\x16\n\x0e\x63\x61rrier_string\x18\x0b \x01(\t\x12\x1a\n\x12mother_vessel_name\x18\x0c \x01(\t\x12\x35\n\x11\x65td_proforma_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10origin_port_name\x18\x0e \x01(\t\x12:\n\x14origin_via_port_name\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12?\n\x19\x64\x65stination_via_port_name\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1d\n\x15\x64\x65stination_port_name\x18\x11 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x12 \x01(\t\x12%\n\x1dinventory_backed_offering_fid\x18\x13 \x01(\t\x12P\n\x05route\x18\x14 \x01(\x0b\x32\x41.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.Route\x12\x37\n\x13ibo_inputs_modified\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x15\n\rorigin_locode\x18\x17 \x01(\t\x12\x19\n\x11origin_via_locode\x18\x18 \x01(\t\x12\x1e\n\x16\x64\x65stination_via_locode\x18\x19 \x01(\t\x12\x1a\n\x12\x64\x65stination_locode\x18\x1a \x01(\t\x12\x17\n\x0f\x61ssignment_note\x18  \x01(\t\x12\x11\n\tclient_id\x18" \x01(\x05\x12\x37\n\x11\x63\x61rrier_scac_code\x18$ \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x15\n\rcontract_type\x18% \x01(\t\x12\x1d\n\x15premium_service_names\x18& \x03(\t\x12\x37\n\x11\x63\x61rrier_space_key\x18\' \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1b\n\x13\x63reated_by_user_fid\x18( \x01(\t\x12\x17\n\x0foverride_reason\x18) \x01(\t\x12\x18\n\x10\x61ssignment_flags\x18* \x03(\t\x12\x1d\n\x15\x65stimated_cost_micros\x18+ \x01(\x03\x12\x1a\n\x12system_commit_type\x18, \x01(\t"c\n\x05Route\x12Z\n\x08segments\x18\x01 \x03(\x0b\x32H.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.RouteSegment"\xc1\x04\n\x0cRouteSegment\x12^\n\x10origin_port_call\x18\x01 \x01(\x0b\x32\x44.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.PortCall\x12\x63\n\x15\x64\x65stination_port_call\x18\x02 \x01(\x0b\x32\x44.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.PortCall\x12\x16\n\x0e\x63\x61rrier_string\x18\x03 \x01(\t\x12k\n\x13transportation_mode\x18\x04 \x01(\x0e\x32N.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.TransportationMode\x12\x19\n\x11vessel_imo_number\x18\x05 \x01(\t\x12\x13\n\x0bvessel_name\x18\x06 \x01(\t\x12\x15\n\rvoyage_number\x18\x07 \x01(\t\x12[\n\x0bvoyage_type\x18\x08 \x01(\x0e\x32\x46.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.VoyageType\x12\x1e\n\x16\x65stimated_schedule_fid\x18\t \x01(\t\x12#\n\x1b\x63onnecting_leg_schedule_fid\x18\n \x01(\t"\xc4\x01\n\x08PortCall\x12\x11\n\tport_name\x18\x01 \x01(\t\x12I\n\rproforma_date\x18\x02 \x01(\x0b\x32\x32.flexport.os.v1.types.walltimedate.v1.WallTimeDate\x12J\n\x0e\x65stimated_date\x18\x03 \x01(\x0b\x32\x32.flexport.os.v1.types.walltimedate.v1.WallTimeDate\x12\x0e\n\x06locode\x18\x04 \x01(\t"\xae\x02\n\x14\x46mtAssignmentCreated\x12\x16\n\x0e\x61ssignment_fid\x18\x01 \x01(\t\x12]\n\nassignment\x18\x02 \x01(\x0b\x32I.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.FmtAssignment\x12i\n\ncreated_by\x18\x04 \x01(\x0e\x32U.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.FmtAssignmentUpdateSource\x12\x34\n\x0c\x63reated_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01"\xae\x02\n\x14\x46mtAssignmentDeleted\x12\x16\n\x0e\x61ssignment_fid\x18\x01 \x01(\t\x12]\n\nassignment\x18\x02 \x01(\x0b\x32I.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.FmtAssignment\x12i\n\ndeleted_by\x18\x04 \x01(\x0e\x32U.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.FmtAssignmentUpdateSource\x12\x34\n\x0c\x64\x65leted_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01*\x91\x01\n\x12TransportationMode\x12\x1f\n\x1bTRANSPORTATION_MODE_INVALID\x10\x00\x12\x1d\n\x19TRANSPORTATION_MODE_OCEAN\x10\x02\x12\x1c\n\x18TRANSPORTATION_MODE_RAIL\x10\x03\x12\x1d\n\x19TRANSPORTATION_MODE_TRUCK\x10\x04*\xb4\x01\n\nVoyageType\x12\x17\n\x13VOYAGE_TYPE_INVALID\x10\x00\x12\x1d\n\x19VOYAGE_TYPE_MOTHER_VESSEL\x10\x01\x12\x1d\n\x19VOYAGE_TYPE_FEEDER_VESSEL\x10\x02\x12$\n VOYAGE_TYPE_ORIGIN_TRANSSHIPMENT\x10\x03\x12)\n%VOYAGE_TYPE_DESTINATION_TRANSSHIPMENT\x10\x04*\x9d\x01\n\x19\x46mtAssignmentUpdateSource\x12(\n$FMT_ASSIGNMENT_UPDATE_SOURCE_INVALID\x10\x00\x12%\n!FMT_ASSIGNMENT_UPDATE_SOURCE_CORE\x10\x01\x12/\n+FMT_ASSIGNMENT_UPDATE_SOURCE_OCEAN_PLANNING\x10\x02\x42\x97\x01\n>com.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1B\x12\x46mtAssignmentProtoP\x01\xea\x02>Flexport::Monolith::OceanFmtAssignment::FmtAssignment::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1.fmt_assignment_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n>com.flexport.monolith.oceanfmtassignment.fmtassignment.v1beta1B\022FmtAssignmentProtoP\001\352\002>Flexport::Monolith::OceanFmtAssignment::FmtAssignment::V1Beta1"
    _globals["_FMTASSIGNMENTCREATED"].fields_by_name["created_time"]._options = None
    _globals["_FMTASSIGNMENTCREATED"].fields_by_name["created_time"]._serialized_options = b"\030\001"
    _globals["_FMTASSIGNMENTDELETED"].fields_by_name["deleted_time"]._options = None
    _globals["_FMTASSIGNMENTDELETED"].fields_by_name["deleted_time"]._serialized_options = b"\030\001"
    _globals["_TRANSPORTATIONMODE"]._serialized_start = 3207
    _globals["_TRANSPORTATIONMODE"]._serialized_end = 3352
    _globals["_VOYAGETYPE"]._serialized_start = 3355
    _globals["_VOYAGETYPE"]._serialized_end = 3535
    _globals["_FMTASSIGNMENTUPDATESOURCE"]._serialized_start = 3538
    _globals["_FMTASSIGNMENTUPDATESOURCE"]._serialized_end = 3695
    _globals["_FMTASSIGNMENT"]._serialized_start = 268
    _globals["_FMTASSIGNMENT"]._serialized_end = 1714
    _globals["_ROUTE"]._serialized_start = 1716
    _globals["_ROUTE"]._serialized_end = 1815
    _globals["_ROUTESEGMENT"]._serialized_start = 1818
    _globals["_ROUTESEGMENT"]._serialized_end = 2395
    _globals["_PORTCALL"]._serialized_start = 2398
    _globals["_PORTCALL"]._serialized_end = 2594
    _globals["_FMTASSIGNMENTCREATED"]._serialized_start = 2597
    _globals["_FMTASSIGNMENTCREATED"]._serialized_end = 2899
    _globals["_FMTASSIGNMENTDELETED"]._serialized_start = 2902
    _globals["_FMTASSIGNMENTDELETED"]._serialized_end = 3204
# @@protoc_insertion_point(module_scope)