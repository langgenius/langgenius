# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/warehouse/v1beta1/warehouse_event.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n9flexport/monolith/warehouse/v1beta1/warehouse_event.proto\x12#flexport.monolith.warehouse.v1beta1\x1a\x35\x66lexport/monolith/warehouse/v1beta1/cargo_group.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x89\x01\n\x10ReadyForOutbound\x12>\n\x05\x63\x61rgo\x18\x01 \x03(\x0b\x32/.flexport.monolith.warehouse.v1beta1.CargoGroup\x12\x35\n\x11gate_in_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"\x85\x01\n\x0c\x43\x61rgoReceipt\x12\x35\n\x11gate_in_timestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12>\n\x05\x63\x61rgo\x18\x01 \x03(\x0b\x32/.flexport.monolith.warehouse.v1beta1.CargoGroup"\\\n\x0e\x43ustomsUpdated\x12J\n\x0e\x63ustoms_status\x18\x01 \x01(\x0e\x32\x32.flexport.monolith.warehouse.v1beta1.CustomsStatus"\xf4\x04\n\x0eWarehouseEvent\x12\x1c\n\x14warehouse_request_id\x18\x01 \x01(\t\x12\x63\n\x1bwarehouse_request_namespace\x18\x02 \x01(\x0e\x32>.flexport.monolith.warehouse.v1beta1.WarehouseRequestNamespace\x12\x1d\n\x15warehouse_address_fid\x18\x03 \x01(\t\x12\x16\n\x0ewarehouse_name\x18\x04 \x01(\t\x12-\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12S\n\x12ready_for_outbound\x18\x07 \x01(\x0b\x32\x35.flexport.monolith.warehouse.v1beta1.ReadyForOutboundH\x00\x12J\n\rcargo_receipt\x18\x08 \x01(\x0b\x32\x31.flexport.monolith.warehouse.v1beta1.CargoReceiptH\x00\x12N\n\x0f\x63ustoms_updated\x18\t \x01(\x0b\x32\x33.flexport.monolith.warehouse.v1beta1.CustomsUpdatedH\x00\x12\x16\n\x0ewarehouse_code\x18\n \x01(\t\x12]\n\x1cshipment_transportation_mode\x18\x0b \x01(\x0e\x32\x37.flexport.monolith.warehouse.v1beta1.TransportationModeB\x11\n\x0f\x65vent_type_data*m\n\x19WarehouseRequestNamespace\x12\'\n#WAREHOUSE_REQUEST_NAMESPACE_INVALID\x10\x00\x12\'\n#WAREHOUSE_REQUEST_NAMESPACE_FLEX_ID\x10\x01*\x93\x01\n\tEventType\x12\x16\n\x12\x45VENT_TYPE_INVALID\x10\x00\x12\x1c\n\x18\x45VENT_TYPE_CARGO_RECEIPT\x10\x01\x12*\n&EVENT_TYPE_READY_FOR_OUTBOUND_PLANNING\x10\x02\x12$\n EVENT_TYPE_CUSTOMS_STATUS_UPDATE\x10\x03*c\n\rCustomsStatus\x12\x1a\n\x16\x43USTOMS_STATUS_INVALID\x10\x00\x12\x1a\n\x16\x43USTOMS_STATUS_PENDING\x10\x01\x12\x1a\n\x16\x43USTOMS_STATUS_CLEARED\x10\x02*\xc1\x02\n\x12TransportationMode\x12\x1f\n\x1bTRANSPORTATION_MODE_INVALID\x10\x00\x12\x1b\n\x17TRANSPORTATION_MODE_AIR\x10\x01\x12\x1d\n\x19TRANSPORTATION_MODE_OCEAN\x10\x02\x12\x1d\n\x19TRANSPORTATION_MODE_TRUCK\x10\x03\x12\x1c\n\x18TRANSPORTATION_MODE_RAIL\x10\x04\x12\x1f\n\x1bTRANSPORTATION_MODE_UNKNOWN\x10\x05\x12!\n\x1dTRANSPORTATION_MODE_OCEAN_AIR\x10\x06\x12"\n\x1eTRANSPORTATION_MODE_TRUCK_INTL\x10\x07\x12)\n%TRANSPORTATION_MODE_WAREHOUSE_STORAGE\x10\x08\x42i\n\'com.flexport.monolith.warehouse.v1beta1B\x13WarehouseEventProtoP\x01\xea\x02&Flexport::Monolith::Warehouse::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.monolith.warehouse.v1beta1.warehouse_event_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n'com.flexport.monolith.warehouse.v1beta1B\023WarehouseEventProtoP\001\352\002&Flexport::Monolith::Warehouse::V1Beta1"
    _globals["_WAREHOUSEREQUESTNAMESPACE"]._serialized_start = 1187
    _globals["_WAREHOUSEREQUESTNAMESPACE"]._serialized_end = 1296
    _globals["_EVENTTYPE"]._serialized_start = 1299
    _globals["_EVENTTYPE"]._serialized_end = 1446
    _globals["_CUSTOMSSTATUS"]._serialized_start = 1448
    _globals["_CUSTOMSSTATUS"]._serialized_end = 1547
    _globals["_TRANSPORTATIONMODE"]._serialized_start = 1550
    _globals["_TRANSPORTATIONMODE"]._serialized_end = 1871
    _globals["_READYFOROUTBOUND"]._serialized_start = 187
    _globals["_READYFOROUTBOUND"]._serialized_end = 324
    _globals["_CARGORECEIPT"]._serialized_start = 327
    _globals["_CARGORECEIPT"]._serialized_end = 460
    _globals["_CUSTOMSUPDATED"]._serialized_start = 462
    _globals["_CUSTOMSUPDATED"]._serialized_end = 554
    _globals["_WAREHOUSEEVENT"]._serialized_start = 557
    _globals["_WAREHOUSEEVENT"]._serialized_end = 1185
# @@protoc_insertion_point(module_scope)