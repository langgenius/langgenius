# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/executionoffering/v1/transit/trucking_only_execution_offering.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\naflexport/executioncoordinator/executionoffering/v1/transit/trucking_only_execution_offering.proto\x12\x32\x66lexport.executioncoordinator.executionoffering.v1\x1aGflexport/executioncoordinator/executionoffering/v1/transit/common.proto\x1a\x39\x66lexport/os/v1/types/walltimedate/v1/wall_time_date.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xa8\x05\n\x1dTruckingOnlyExecutionOffering\x12_\n\x10specific_carrier\x18\x01 \x01(\x0b\x32\x43.flexport.executioncoordinator.executionoffering.v1.SpecificCarrierH\x00\x12W\n\x0copen_carrier\x18\x02 \x01(\x0b\x32?.flexport.executioncoordinator.executionoffering.v1.OpenCarrierH\x00\x12O\n\x05stops\x18\x03 \x03(\x0b\x32@.flexport.executioncoordinator.executionoffering.v1.TruckingStop\x12W\n\rtrucking_mode\x18\x04 \x01(\x0e\x32@.flexport.executioncoordinator.executionoffering.v1.TruckingMode\x12\x1b\n\x13\x66reight_partner_fid\x18\x05 \x01(\t\x12_\n\x11main_freight_role\x18\x06 \x01(\x0e\x32\x44.flexport.executioncoordinator.executionoffering.v1.TruckingOnlyRole\x12\x34\n\x10is_international\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x64\n\x13quoted_transit_time\x18\x08 \x01(\x0b\x32G.flexport.executioncoordinator.executionoffering.v1.TruckingTransitTimeB\t\n\x07\x63\x61rrier"\xe1\x01\n\x0cTruckingStop\x12\x13\n\x0b\x61\x64\x64ress_fid\x18\x01 \x01(\t\x12T\n\x06pickup\x18\x03 \x01(\x0b\x32\x42.flexport.executioncoordinator.executionoffering.v1.TruckingPickupH\x00\x12V\n\x07\x64ropoff\x18\x04 \x01(\x0b\x32\x43.flexport.executioncoordinator.executionoffering.v1.TruckingDropoffH\x00\x42\x0e\n\x0cstop_details"\x84\x01\n\x13TruckingTransitTime\x12O\n\x13\x62\x61sed_on_start_date\x18\x01 \x01(\x0b\x32\x32.flexport.os.v1.types.walltimedate.v1.WallTimeDate\x12\x1c\n\x14\x64\x65stination_timezone\x18\x02 \x01(\t"^\n\x0eTruckingPickup\x12L\n\x10\x63\x61rgo_ready_date\x18\x01 \x01(\x0b\x32\x32.flexport.os.v1.types.walltimedate.v1.WallTimeDate"\x11\n\x0fTruckingDropoff*n\n\x0cTruckingMode\x12\x19\n\x15TRUCKING_MODE_INVALID\x10\x00\x12\x15\n\x11TRUCKING_MODE_ANY\x10\x01\x12\x15\n\x11TRUCKING_MODE_LTL\x10\x02\x12\x15\n\x11TRUCKING_MODE_FTL\x10\x03*~\n\x10TruckingOnlyRole\x12\x1e\n\x1aTRUCKING_ONLY_ROLE_INVALID\x10\x00\x12#\n\x1fTRUCKING_ONLY_ROLE_FULL_SERVICE\x10\x01\x12%\n!TRUCKING_ONLY_ROLE_NO_INVOLVEMENT\x10\x02\x42\x96\x01\n6com.flexport.executioncoordinator.executionoffering.v1B"TruckingOnlyExecutionOfferingProtoP\x01\xea\x02\x35\x46lexport::ExecutionCoordinator::ExecutionOffering::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.executioncoordinator.executionoffering.v1.transit.trucking_only_execution_offering_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b'\n6com.flexport.executioncoordinator.executionoffering.v1B"TruckingOnlyExecutionOfferingProtoP\001\352\0025Flexport::ExecutionCoordinator::ExecutionOffering::V1'
    _globals["_TRUCKINGMODE"]._serialized_start = 1478
    _globals["_TRUCKINGMODE"]._serialized_end = 1588
    _globals["_TRUCKINGONLYROLE"]._serialized_start = 1590
    _globals["_TRUCKINGONLYROLE"]._serialized_end = 1716
    _globals["_TRUCKINGONLYEXECUTIONOFFERING"]._serialized_start = 318
    _globals["_TRUCKINGONLYEXECUTIONOFFERING"]._serialized_end = 998
    _globals["_TRUCKINGSTOP"]._serialized_start = 1001
    _globals["_TRUCKINGSTOP"]._serialized_end = 1226
    _globals["_TRUCKINGTRANSITTIME"]._serialized_start = 1229
    _globals["_TRUCKINGTRANSITTIME"]._serialized_end = 1361
    _globals["_TRUCKINGPICKUP"]._serialized_start = 1363
    _globals["_TRUCKINGPICKUP"]._serialized_end = 1457
    _globals["_TRUCKINGDROPOFF"]._serialized_start = 1459
    _globals["_TRUCKINGDROPOFF"]._serialized_end = 1476
# @@protoc_insertion_point(module_scope)