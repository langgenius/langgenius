# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/warehouse/inventory/events/v1/inventory_record_updated.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nEflexport/warehouse/inventory/events/v1/inventory_record_updated.proto\x12&flexport.warehouse.inventory.events.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x93\x02\n\x16InventoryRecordUpdated\x12\x45\n\nevent_type\x18\x01 \x01(\x0e\x32\x31.flexport.warehouse.inventory.events.v1.EventType\x12\x19\n\x11\x65vent_subject_fid\x18\x02 \x01(\t\x12\x15\n\revent_version\x18\x03 \x01(\x05\x12.\n\nevent_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tactor_fid\x18\x05 \x01(\t\x12\x10\n\x08trace_id\x18\x06 \x01(\t\x12+\n\nevent_data\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct*w\n\tEventType\x12\x16\n\x12\x45VENT_TYPE_INVALID\x10\x00\x12(\n$EVENT_TYPE_INVENTORY_RECORD_RECEIVED\x10\x01\x12(\n$EVENT_TYPE_INVENTORY_RECORD_DEPARTED\x10\x02\x42w\n*com.flexport.warehouse.inventory.events.v1B\x1aWarehouseInventoryApiProtoP\x01\xea\x02*Flexport::Warehouse::Inventory::Events::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.warehouse.inventory.events.v1.inventory_record_updated_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n*com.flexport.warehouse.inventory.events.v1B\032WarehouseInventoryApiProtoP\001\352\002*Flexport::Warehouse::Inventory::Events::V1"
    _globals["_EVENTTYPE"]._serialized_start = 454
    _globals["_EVENTTYPE"]._serialized_end = 573
    _globals["_INVENTORYRECORDUPDATED"]._serialized_start = 177
    _globals["_INVENTORYRECORDUPDATED"]._serialized_end = 452
# @@protoc_insertion_point(module_scope)