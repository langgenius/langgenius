# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/shipmentoverride/v1/shipment_override_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nMflexport/executioncoordinator/shipmentoverride/v1/shipment_override_api.proto\x12\x31\x66lexport.executioncoordinator.shipmentoverride.v1\x1aGflexport/executioncoordinator/derivedshipment/v1/derived_shipment.proto\x1aJflexport/executioncoordinator/shipmentoverride/v1/task_transit_dates.proto\x1a>flexport/executioncoordinator/types/enums/v1/entry_point.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xa4\x03\n#OverrideShipmentTransitDatesRequest\x12\x14\n\x0cshipment_fid\x18\x01 \x01(\t\x12\x10\n\x08user_fid\x18\x02 \x01(\t\x12_\n\x12task_transit_dates\x18\x03 \x03(\x0b\x32\x43.flexport.executioncoordinator.shipmentoverride.v1.TaskTransitDates\x12M\n\x0b\x65ntry_point\x18\x04 \x01(\x0e\x32\x38.flexport.executioncoordinator.types.enums.v1.EntryPoint\x12\x33\n\x0fignore_warnings\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x31\n\rignore_errors\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12!\n\x19\x64\x65rived_shipment_revision\x18\x07 \x01(\r\x12\x1a\n\x12itinerary_revision\x18\x08 \x01(\r"\x83\x01\n$OverrideShipmentTransitDatesResponse\x12[\n\x10\x64\x65rived_shipment\x18\x01 \x01(\x0b\x32\x41.flexport.executioncoordinator.derivedshipment.v1.DerivedShipment2\xe7\x01\n\x13ShipmentOverrideAPI\x12\xcf\x01\n\x1cOverrideShipmentTransitDates\x12V.flexport.executioncoordinator.shipmentoverride.v1.OverrideShipmentTransitDatesRequest\x1aW.flexport.executioncoordinator.shipmentoverride.v1.OverrideShipmentTransitDatesResponseB\x8a\x01\n5com.flexport.executioncoordinator.shipmentoverride.v1B\x18ShipmentOverrideApiProtoP\x01\xea\x02\x34\x46lexport::ExecutionCoordinator::ShipmentOverride::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executioncoordinator.shipmentoverride.v1.shipment_override_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n5com.flexport.executioncoordinator.shipmentoverride.v1B\030ShipmentOverrideApiProtoP\001\352\0024Flexport::ExecutionCoordinator::ShipmentOverride::V1"
    _globals["_OVERRIDESHIPMENTTRANSITDATESREQUEST"]._serialized_start = 378
    _globals["_OVERRIDESHIPMENTTRANSITDATESREQUEST"]._serialized_end = 798
    _globals["_OVERRIDESHIPMENTTRANSITDATESRESPONSE"]._serialized_start = 801
    _globals["_OVERRIDESHIPMENTTRANSITDATESRESPONSE"]._serialized_end = 932
    _globals["_SHIPMENTOVERRIDEAPI"]._serialized_start = 935
    _globals["_SHIPMENTOVERRIDEAPI"]._serialized_end = 1166
# @@protoc_insertion_point(module_scope)