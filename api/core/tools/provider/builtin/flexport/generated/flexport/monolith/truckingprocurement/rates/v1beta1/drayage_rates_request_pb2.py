# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/truckingprocurement/rates/v1beta1/drayage_rates_request.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nOflexport/monolith/truckingprocurement/rates/v1beta1/drayage_rates_request.proto\x12\x33\x66lexport.monolith.truckingprocurement.rates.v1beta1\x1aGflexport/monolith/truckingprocurement/rates/v1beta1/delivery_info.proto\x1a?flexport/monolith/truckingprocurement/rates/v1beta1/enums.proto\x1a\x45\x66lexport/monolith/truckingprocurement/rates/v1beta1/pickup_info.proto"\x9e\x04\n\x17\x44rayageRatesRequestItem\x12T\n\x0bpickup_info\x18\x01 \x01(\x0b\x32?.flexport.monolith.truckingprocurement.rates.v1beta1.PickupInfo\x12X\n\rdelivery_info\x18\x02 \x01(\x0b\x32\x41.flexport.monolith.truckingprocurement.rates.v1beta1.DeliveryInfo\x12`\n\x0b\x64river_type\x18\x03 \x01(\x0e\x32K.flexport.monolith.truckingprocurement.rates.v1beta1.TruckingRateDriverType\x12~\n\x0e\x65quipment_type\x18\x04 \x01(\x0e\x32\x66.flexport.monolith.truckingprocurement.rates.v1beta1.DrayageRatesRequestItem.TruckingRateEquipmentType"q\n\x19TruckingRateEquipmentType\x12(\n$TRUCKING_RATE_EQUIPMENT_TYPE_INVALID\x10\x00\x12*\n&TRUCKING_RATE_EQUIPMENT_TYPE_CONTAINER\x10\x01"x\n\x16GetDrayageRatesRequest\x12^\n\x08requests\x18\x01 \x03(\x0b\x32L.flexport.monolith.truckingprocurement.rates.v1beta1.DrayageRatesRequestItemB\x8a\x01\n7com.flexport.monolith.truckingprocurement.rates.v1beta1B\x13\x44rayageRatesRequestP\x01\xea\x02\x37\x46lexport::Monolith::TruckingProcurement::Rates::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.truckingprocurement.rates.v1beta1.drayage_rates_request_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n7com.flexport.monolith.truckingprocurement.rates.v1beta1B\023DrayageRatesRequestP\001\352\0027Flexport::Monolith::TruckingProcurement::Rates::V1Beta1"
    _globals["_DRAYAGERATESREQUESTITEM"]._serialized_start = 346
    _globals["_DRAYAGERATESREQUESTITEM"]._serialized_end = 888
    _globals["_DRAYAGERATESREQUESTITEM_TRUCKINGRATEEQUIPMENTTYPE"]._serialized_start = 775
    _globals["_DRAYAGERATESREQUESTITEM_TRUCKINGRATEEQUIPMENTTYPE"]._serialized_end = 888
    _globals["_GETDRAYAGERATESREQUEST"]._serialized_start = 890
    _globals["_GETDRAYAGERATESREQUEST"]._serialized_end = 1010
# @@protoc_insertion_point(module_scope)