# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/trucking/truck_load/v2beta1/truck_load_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nBflexport/monolith/trucking/truck_load/v2beta1/truck_load_api.proto\x12-flexport.monolith.trucking.truck_load.v2beta1\x1a>flexport/monolith/trucking/truck_load/v2beta1/truck_load.proto\x1a;flexport/os/v1/types/walltimerange/v1/wall_time_range.proto"\xaf\x03\n\x14GetTruckLoadsRequest\x12n\n\x1dtruck_load_warehouse_statuses\x18\x01 \x03(\x0e\x32G.flexport.monolith.trucking.truck_load.v2beta1.TruckLoadWarehouseStatus\x12l\n\x1ctruck_load_planning_statuses\x18\x02 \x03(\x0e\x32\x46.flexport.monolith.trucking.truck_load.v2beta1.TruckLoadPlanningStatus\x12\x61\n\x16truck_load_route_types\x18\x03 \x03(\x0e\x32\x41.flexport.monolith.trucking.truck_load.v2beta1.TruckLoadRouteType\x12V\n\x18\x64ispatch_date_time_range\x18\x04 \x01(\x0b\x32\x34.flexport.os.v1.types.walltimerange.v1.WallTimeRange"f\n\x15GetTruckLoadsResponse\x12M\n\x0btruck_loads\x18\x01 \x03(\x0b\x32\x38.flexport.monolith.trucking.truck_load.v2beta1.TruckLoad2\xab\x01\n\x0cTruckLoadAPI\x12\x9a\x01\n\rGetTruckLoads\x12\x43.flexport.monolith.trucking.truck_load.v2beta1.GetTruckLoadsRequest\x1a\x44.flexport.monolith.trucking.truck_load.v2beta1.GetTruckLoadsResponseBz\n0com.flexport.monolith.trucking.truckload.v2beta1B\x11TruckLoadApiProtoP\x01\xea\x02\x30\x46lexport::Monolith::Trucking::TruckLoad::V2Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.trucking.truck_load.v2beta1.truck_load_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n0com.flexport.monolith.trucking.truckload.v2beta1B\021TruckLoadApiProtoP\001\352\0020Flexport::Monolith::Trucking::TruckLoad::V2Beta1"
    _globals["_GETTRUCKLOADSREQUEST"]._serialized_start = 243
    _globals["_GETTRUCKLOADSREQUEST"]._serialized_end = 674
    _globals["_GETTRUCKLOADSRESPONSE"]._serialized_start = 676
    _globals["_GETTRUCKLOADSRESPONSE"]._serialized_end = 778
    _globals["_TRUCKLOADAPI"]._serialized_start = 781
    _globals["_TRUCKLOADAPI"]._serialized_end = 952
# @@protoc_insertion_point(module_scope)