# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/billing/allocation/v1beta1/allocation_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nAflexport/monolith/billing/allocation/v1beta1/allocation_api.proto\x12,flexport.monolith.billing.allocation.v1beta1\x1a\x30\x66lexport/billing/util/v1beta1/error_result.proto\x1a\x46\x66lexport/monolith/billing/allocation/v1beta1/shipment_allocation.proto"\x84\x01\n\x1cGetShipmentAllocationRequest\x12\x12\n\nvendor_fid\x18\x01 \x01(\t\x12\x15\n\rshipment_fids\x18\x02 \x03(\t\x12\x1e\n\x16\x62ill_of_lading_numbers\x18\x03 \x03(\t\x12\x19\n\x11\x63ontainer_numbers\x18\x04 \x03(\t"\xcb\x01\n\x1dGetShipmentAllocationResponse\x12Z\n\x0esuccess_result\x18\x01 \x01(\x0b\x32@.flexport.monolith.billing.allocation.v1beta1.ShipmentAllocationH\x00\x12\x44\n\x0e\x66\x61ilure_result\x18\x02 \x01(\x0b\x32*.flexport.billing.util.v1beta1.ErrorResultH\x00\x42\x08\n\x06result"5\n\x1c\x45xpandConsolShipmentsRequest\x12\x15\n\rshipment_fids\x18\x01 \x03(\t"\xcb\x01\n\x1d\x45xpandConsolShipmentsResponse\x12Z\n\x0esuccess_result\x18\x01 \x01(\x0b\x32@.flexport.monolith.billing.allocation.v1beta1.ShipmentAllocationH\x00\x12\x44\n\x0e\x66\x61ilure_result\x18\x02 \x01(\x0b\x32*.flexport.billing.util.v1beta1.ErrorResultH\x00\x42\x08\n\x06result2\xf5\x02\n\rAllocationAPI\x12\xb0\x01\n\x15GetShipmentAllocation\x12J.flexport.monolith.billing.allocation.v1beta1.GetShipmentAllocationRequest\x1aK.flexport.monolith.billing.allocation.v1beta1.GetShipmentAllocationResponse\x12\xb0\x01\n\x15\x45xpandConsolShipments\x12J.flexport.monolith.billing.allocation.v1beta1.ExpandConsolShipmentsRequest\x1aK.flexport.monolith.billing.allocation.v1beta1.ExpandConsolShipmentsResponseB{\n0com.flexport.monolith.billing.allocation.v1beta1B\x12\x41llocationApiProtoP\x01\xea\x02\x30\x46lexport::Monolith::Billing::Allocation::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.billing.allocation.v1beta1.allocation_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n0com.flexport.monolith.billing.allocation.v1beta1B\022AllocationApiProtoP\001\352\0020Flexport::Monolith::Billing::Allocation::V1Beta1"
    _globals["_GETSHIPMENTALLOCATIONREQUEST"]._serialized_start = 238
    _globals["_GETSHIPMENTALLOCATIONREQUEST"]._serialized_end = 370
    _globals["_GETSHIPMENTALLOCATIONRESPONSE"]._serialized_start = 373
    _globals["_GETSHIPMENTALLOCATIONRESPONSE"]._serialized_end = 576
    _globals["_EXPANDCONSOLSHIPMENTSREQUEST"]._serialized_start = 578
    _globals["_EXPANDCONSOLSHIPMENTSREQUEST"]._serialized_end = 631
    _globals["_EXPANDCONSOLSHIPMENTSRESPONSE"]._serialized_start = 634
    _globals["_EXPANDCONSOLSHIPMENTSRESPONSE"]._serialized_end = 837
    _globals["_ALLOCATIONAPI"]._serialized_start = 840
    _globals["_ALLOCATIONAPI"]._serialized_end = 1213
# @@protoc_insertion_point(module_scope)