# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executionoffering/v1/transit/ocean_non_fcl_execution_offering.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\naflexport/executioncoordinator/executionoffering/v1/transit/ocean_non_fcl_execution_offering.proto\x12\x32\x66lexport.executioncoordinator.executionoffering.v1\x1a%flexport/catalog/enums/v1/enums.proto\x1aSflexport/executioncoordinator/executionoffering/v1/transit/auxiliary_trucking.proto\x1aGflexport/executioncoordinator/executionoffering/v1/transit/common.proto\x1aPflexport/executioncoordinator/executionoffering/v1/transit/nra_constraints.proto\x1a\x39\x66lexport/os/v1/types/walltimedate/v1/wall_time_date.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xf3\r\n\x1cOceanNonFclExecutionOffering\x12\\\n\x07pickups\x18\x0c \x03(\x0b\x32K.flexport.executioncoordinator.executionoffering.v1.AuxiliaryTruckingPickup\x12\x61\n\ndeliveries\x18\r \x03(\x0b\x32M.flexport.executioncoordinator.executionoffering.v1.AuxiliaryTruckingDelivery\x12~\n\x1dorigin_transloading_truckings\x18\x10 \x03(\x0b\x32W.flexport.executioncoordinator.executionoffering.v1.AuxiliaryOriginTransloadingTrucking\x12\x88\x01\n"destination_transloading_truckings\x18\x11 \x03(\x0b\x32\\.flexport.executioncoordinator.executionoffering.v1.AuxiliaryDestinationTransloadingTrucking\x12_\n\x10specific_carrier\x18\x07 \x01(\x0b\x32\x43.flexport.executioncoordinator.executionoffering.v1.SpecificCarrierH\x00\x12W\n\x0copen_carrier\x18\x08 \x01(\x0b\x32?.flexport.executioncoordinator.executionoffering.v1.OpenCarrierH\x00\x12\x66\n\x0especific_route\x18\t \x01(\x0b\x32L.flexport.executioncoordinator.executionoffering.v1.OceanNonFclSpecificRouteH\x01\x12S\n\nopen_route\x18\n \x01(\x0b\x32=.flexport.executioncoordinator.executionoffering.v1.OpenRouteH\x01\x12\x1b\n\x13\x66reight_partner_fid\x18\x0b \x01(\t\x12g\n\x13quoted_transit_time\x18\x0e \x01(\x0b\x32J.flexport.executioncoordinator.executionoffering.v1.OceanNonFclTransitTime\x12\x64\n\x0eote_milestones\x18\x18 \x01(\x0b\x32L.flexport.executioncoordinator.executionoffering.v1.OceanNonFcLOteMilestones\x12\x32\n\x0eis_ocean_match\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0eis_flow_direct\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12;\n\x17is_global_conveyor_belt\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12;\n\x17is_buyers_consolidation\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12^\n\x11main_freight_role\x18\x01 \x01(\x0e\x32\x43.flexport.executioncoordinator.executionoffering.v1.OceanNonFclRole\x12k\n\x11\x66ull_service_info\x18\x02 \x01(\x0b\x32N.flexport.executioncoordinator.executionoffering.v1.OceanNonFclFullServiceInfoH\x02\x12"\n\x1amain_freight_service_level\x18\x12 \x01(\t\x12i\n\x1fmain_freight_service_level_enum\x18\x16 \x01(\x0e\x32@.flexport.executioncoordinator.executionoffering.v1.ServiceLevel\x12=\n\x0c\x63\x61talog_tier\x18\x17 \x01(\x0e\x32\'.flexport.catalog.enums.v1.OceanTierDtoB\t\n\x07\x63\x61rrierB\x07\n\x05routeB\x13\n\x11role_related_info"\xd8\x01\n\x1aOceanNonFclFullServiceInfo\x12]\n\x0chbl_boundary\x18\x01 \x01(\x0e\x32G.flexport.executioncoordinator.executionoffering.v1.OceanNonFclBoundary\x12[\n\x0fnra_constraints\x18\x02 \x01(\x0b\x32\x42.flexport.executioncoordinator.executionoffering.v1.NraConstraints"\xa6\x04\n\x16OceanNonFclTransitTime\x12\x10\n\x08min_days\x18\x02 \x01(\x05\x12\x10\n\x08max_days\x18\x03 \x01(\x05\x12^\n\x05start\x18\x04 \x01(\x0e\x32O.flexport.executioncoordinator.executionoffering.v1.OceanNonFclTransitTimeStart\x12Z\n\x03\x65nd\x18\x05 \x01(\x0e\x32M.flexport.executioncoordinator.executionoffering.v1.OceanNonFclTransitTimeEnd\x12O\n\x13\x62\x61sed_on_start_date\x18\x06 \x01(\x0b\x32\x32.flexport.os.v1.types.walltimedate.v1.WallTimeDate\x12\x1c\n\x14\x64\x65stination_timezone\x18\x07 \x01(\t\x12\x13\n\x0borigin_days\x18\x08 \x01(\x05\x12\x1a\n\x12\x63onsolidation_days\x18\t \x01(\x05\x12\x19\n\x11origin_dwell_days\x18\n \x01(\x05\x12\x19\n\x11port_to_port_days\x18\x0b \x01(\x05\x12\x1e\n\x16\x64\x65stination_dwell_days\x18\x0c \x01(\x05\x12\x1c\n\x14\x64\x65\x63onsolidation_days\x18\r \x01(\x05\x12\x18\n\x10\x64\x65stination_days\x18\x0e \x01(\x05"\xa5\x02\n\x18OceanNonFcLOteMilestones\x12\x1b\n\x13\x64oor_to_cfs_or_port\x18\x01 \x01(\x02\x12 \n\x18\x63onsolidation_processing\x18\t \x01(\x02\x12\x18\n\x10\x64\x65livery_to_port\x18\x02 \x01(\x02\x12\x1f\n\x17origin_ingate_departure\x18\x03 \x01(\x02\x12\x14\n\x0cport_to_port\x18\x04 \x01(\x02\x12!\n\x19\x64\x65st_arrival_avail_unload\x18\x05 \x01(\x02\x12\x15\n\rport_recovery\x18\x06 \x01(\x02\x12"\n\x1a\x64\x65\x63onsolidation_processing\x18\x07 \x01(\x02\x12\x1b\n\x13\x63\x66s_or_port_to_door\x18\x08 \x01(\x02"\xd3\x01\n\x18OceanNonFclSpecificRoute\x12\x16\n\x0eorigin_cfs_fid\x18\x01 \x01(\t\x12\x1b\n\x13port_of_loading_fid\x18\x02 \x01(\t\x12\x15\n\rvia_port_fids\x18\x03 \x03(\t\x12\x1d\n\x15port_of_unloading_fid\x18\x04 \x01(\t\x12\x17\n\x0finland_port_fid\x18\x05 \x01(\t\x12\x1b\n\x13\x64\x65stination_cfs_fid\x18\x06 \x01(\t\x12\x16\n\x0einland_cfs_fid\x18\x07 \x01(\t*\xb4\x01\n\x1bOceanNonFclTransitTimeStart\x12,\n(OCEAN_NON_FCL_TRANSIT_TIME_START_INVALID\x10\x00\x12\x35\n1OCEAN_NON_FCL_TRANSIT_TIME_START_DOOR_CARGO_READY\x10\x01\x12\x30\n,OCEAN_NON_FCL_TRANSIT_TIME_START_CFS_ARRIVAL\x10\x02*\xb5\x01\n\x19OceanNonFclTransitTimeEnd\x12*\n&OCEAN_NON_FCL_TRANSIT_TIME_END_INVALID\x10\x00\x12/\n+OCEAN_NON_FCL_TRANSIT_TIME_END_DOOR_ARRIVAL\x10\x01\x12;\n7OCEAN_NON_FCL_TRANSIT_TIME_END_CFS_AVAILABLE_FOR_PICKUP\x10\x02*}\n\x0fOceanNonFclRole\x12\x1e\n\x1aOCEAN_NON_FCL_ROLE_INVALID\x10\x00\x12#\n\x1fOCEAN_NON_FCL_ROLE_FULL_SERVICE\x10\x01\x12%\n!OCEAN_NON_FCL_ROLE_NO_INVOLVEMENT\x10\x04*\x98\x03\n\x13OceanNonFclBoundary\x12"\n\x1eOCEAN_NON_FCL_BOUNDARY_INVALID\x10\x00\x12%\n!OCEAN_NON_FCL_BOUNDARY_CFS_TO_CFS\x10\x01\x12$\n OCEAN_NON_FCL_BOUNDARY_CFS_TO_CY\x10\x02\x12&\n"OCEAN_NON_FCL_BOUNDARY_CFS_TO_DOOR\x10\x03\x12$\n OCEAN_NON_FCL_BOUNDARY_CY_TO_CFS\x10\x04\x12#\n\x1fOCEAN_NON_FCL_BOUNDARY_CY_TO_CY\x10\x05\x12%\n!OCEAN_NON_FCL_BOUNDARY_CY_TO_DOOR\x10\x06\x12&\n"OCEAN_NON_FCL_BOUNDARY_DOOR_TO_CFS\x10\x07\x12%\n!OCEAN_NON_FCL_BOUNDARY_DOOR_TO_CY\x10\x08\x12\'\n#OCEAN_NON_FCL_BOUNDARY_DOOR_TO_DOOR\x10\tB\x95\x01\n6com.flexport.executioncoordinator.executionoffering.v1B!OceanNonFclExecutionOfferingProtoP\x01\xea\x02\x35\x46lexport::ExecutionCoordinator::ExecutionOffering::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.executioncoordinator.executionoffering.v1.transit.ocean_non_fcl_execution_offering_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n6com.flexport.executioncoordinator.executionoffering.v1B!OceanNonFclExecutionOfferingProtoP\001\352\0025Flexport::ExecutionCoordinator::ExecutionOffering::V1"
    _globals["_OCEANNONFCLTRANSITTIMESTART"]._serialized_start = 3588
    _globals["_OCEANNONFCLTRANSITTIMESTART"]._serialized_end = 3768
    _globals["_OCEANNONFCLTRANSITTIMEEND"]._serialized_start = 3771
    _globals["_OCEANNONFCLTRANSITTIMEEND"]._serialized_end = 3952
    _globals["_OCEANNONFCLROLE"]._serialized_start = 3954
    _globals["_OCEANNONFCLROLE"]._serialized_end = 4079
    _globals["_OCEANNONFCLBOUNDARY"]._serialized_start = 4082
    _globals["_OCEANNONFCLBOUNDARY"]._serialized_end = 4490
    _globals["_OCEANNONFCLEXECUTIONOFFERING"]._serialized_start = 524
    _globals["_OCEANNONFCLEXECUTIONOFFERING"]._serialized_end = 2303
    _globals["_OCEANNONFCLFULLSERVICEINFO"]._serialized_start = 2306
    _globals["_OCEANNONFCLFULLSERVICEINFO"]._serialized_end = 2522
    _globals["_OCEANNONFCLTRANSITTIME"]._serialized_start = 2525
    _globals["_OCEANNONFCLTRANSITTIME"]._serialized_end = 3075
    _globals["_OCEANNONFCLOTEMILESTONES"]._serialized_start = 3078
    _globals["_OCEANNONFCLOTEMILESTONES"]._serialized_end = 3371
    _globals["_OCEANNONFCLSPECIFICROUTE"]._serialized_start = 3374
    _globals["_OCEANNONFCLSPECIFICROUTE"]._serialized_end = 3585
# @@protoc_insertion_point(module_scope)