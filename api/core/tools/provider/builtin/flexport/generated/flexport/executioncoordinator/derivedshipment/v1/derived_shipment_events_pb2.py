# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/derivedshipment/v1/derived_shipment_events.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nNflexport/executioncoordinator/derivedshipment/v1/derived_shipment_events.proto\x12\x30\x66lexport.executioncoordinator.derivedshipment.v1\x1aGflexport/executioncoordinator/derivedshipment/v1/derived_shipment.proto\x1aMflexport/executioncoordinator/derivedshipment/v1/derived_shipment_route.proto"\x9b\x01\n\x1f\x41irConsolDerivedShipmentCreated\x12\x1b\n\x13\x65xecution_order_fid\x18\x01 \x01(\t\x12[\n\x10\x64\x65rived_shipment\x18\x02 \x01(\x0b\x32\x41.flexport.executioncoordinator.derivedshipment.v1.DerivedShipment"\x80\x02\n\x1f\x41irConsolDerivedShipmentChanged\x12\x1b\n\x13\x65xecution_order_fid\x18\x01 \x01(\t\x12_\n\x14old_derived_shipment\x18\x02 \x01(\x0b\x32\x41.flexport.executioncoordinator.derivedshipment.v1.DerivedShipment\x12_\n\x14new_derived_shipment\x18\x03 \x01(\x0b\x32\x41.flexport.executioncoordinator.derivedshipment.v1.DerivedShipment"\x9b\x02\n$AirConsolDerivedShipmentRouteChanged\x12\x1b\n\x13\x65xecution_order_fid\x18\x01 \x01(\t\x12j\n\x1aold_derived_shipment_route\x18\x02 \x01(\x0b\x32\x46.flexport.executioncoordinator.derivedshipment.v1.DerivedShipmentRoute\x12j\n\x1anew_derived_shipment_route\x18\x03 \x01(\x0b\x32\x46.flexport.executioncoordinator.derivedshipment.v1.DerivedShipmentRoute"u\n\x16\x44\x65rivedShipmentCreated\x12[\n\x10\x64\x65rived_shipment\x18\x01 \x01(\x0b\x32\x41.flexport.executioncoordinator.derivedshipment.v1.DerivedShipment"\xd6\x01\n\x16\x44\x65rivedShipmentChanged\x12[\n\x10\x64\x65rived_shipment\x18\x01 \x01(\x0b\x32\x41.flexport.executioncoordinator.derivedshipment.v1.DerivedShipment\x12_\n\x14old_derived_shipment\x18\x02 \x01(\x0b\x32\x41.flexport.executioncoordinator.derivedshipment.v1.DerivedShipment"\xa8\x02\n\x1b\x44\x65rivedShipmentRouteChanged\x12\x1b\n\x13\x65xecution_order_fid\x18\x01 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x02 \x01(\t\x12j\n\x1aold_derived_shipment_route\x18\x03 \x01(\x0b\x32\x46.flexport.executioncoordinator.derivedshipment.v1.DerivedShipmentRoute\x12j\n\x1anew_derived_shipment_route\x18\x04 \x01(\x0b\x32\x46.flexport.executioncoordinator.derivedshipment.v1.DerivedShipmentRouteB\x8a\x01\n4com.flexport.executioncoordinator.derivedshipment.v1B\x1a\x44\x65rivedShipmentEventsProtoP\x01\xea\x02\x33\x46lexport::ExecutionCoordinator::DerivedShipment::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executioncoordinator.derivedshipment.v1.derived_shipment_events_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n4com.flexport.executioncoordinator.derivedshipment.v1B\032DerivedShipmentEventsProtoP\001\352\0023Flexport::ExecutionCoordinator::DerivedShipment::V1"
    _globals["_AIRCONSOLDERIVEDSHIPMENTCREATED"]._serialized_start = 285
    _globals["_AIRCONSOLDERIVEDSHIPMENTCREATED"]._serialized_end = 440
    _globals["_AIRCONSOLDERIVEDSHIPMENTCHANGED"]._serialized_start = 443
    _globals["_AIRCONSOLDERIVEDSHIPMENTCHANGED"]._serialized_end = 699
    _globals["_AIRCONSOLDERIVEDSHIPMENTROUTECHANGED"]._serialized_start = 702
    _globals["_AIRCONSOLDERIVEDSHIPMENTROUTECHANGED"]._serialized_end = 985
    _globals["_DERIVEDSHIPMENTCREATED"]._serialized_start = 987
    _globals["_DERIVEDSHIPMENTCREATED"]._serialized_end = 1104
    _globals["_DERIVEDSHIPMENTCHANGED"]._serialized_start = 1107
    _globals["_DERIVEDSHIPMENTCHANGED"]._serialized_end = 1321
    _globals["_DERIVEDSHIPMENTROUTECHANGED"]._serialized_start = 1324
    _globals["_DERIVEDSHIPMENTROUTECHANGED"]._serialized_end = 1620
# @@protoc_insertion_point(module_scope)