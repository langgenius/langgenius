# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executionmilestones/shipmentstate/v1beta1/ocean_carrier_booking_mismatch_state.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n]flexport/executionmilestones/shipmentstate/v1beta1/ocean_carrier_booking_mismatch_state.proto\x12\x32\x66lexport.executionmilestones.shipmentstate.v1beta1\x1awflexport/executioncoordinator/executiontaskstateevent/v1/details/ocean_carrier_booking_mismatch_detection_updated.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xed\x02\n OceanCarrierBookingMismatchState\x12\x14\n\x0cshipment_fid\x18\x01 \x01(\t\x12\x9b\x01\n\x1dmismatches_by_carrier_booking\x18\x02 \x03(\x0b\x32t.flexport.executionmilestones.shipmentstate.v1beta1.OceanCarrierBookingMismatchState.MismatchesByCarrierBookingEntry\x1a\x94\x01\n\x1fMismatchesByCarrierBookingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12`\n\x05value\x18\x02 \x01(\x0b\x32Q.flexport.executionmilestones.shipmentstate.v1beta1.OceanCarrierBookingMismatches:\x02\x38\x01"\xb0\x02\n\x1dOceanCarrierBookingMismatches\x12\x83\x01\n\x12mismatches_by_type\x18\x01 \x03(\x0b\x32g.flexport.executionmilestones.shipmentstate.v1beta1.OceanCarrierBookingMismatches.MismatchesByTypeEntry\x1a\x88\x01\n\x15MismatchesByTypeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12^\n\x05value\x18\x02 \x01(\x0b\x32O.flexport.executionmilestones.shipmentstate.v1beta1.OceanCarrierBookingMismatch:\x02\x38\x01"\x88\x02\n\x1bOceanCarrierBookingMismatch\x12\x88\x01\n\x19mismatch_detection_update\x18\x01 \x01(\x0b\x32\x65.flexport.executioncoordinator.executiontaskstateevent.v1.OceanCarrierBookingMismatchDetectionUpdated\x12\x12\n\nis_ignored\x18\x02 \x01(\x08\x12-\n\tupdate_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13updated_by_user_fid\x18\x04 \x01(\tB\x99\x01\n6com.flexport.executionmilestones.shipmentstate.v1beta1B%OceanCarrierBookingMismatchStateProtoP\x01\xea\x02\x35\x46lexport::ExecutionMilestones::ShipmentState::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executionmilestones.shipmentstate.v1beta1.ocean_carrier_booking_mismatch_state_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n6com.flexport.executionmilestones.shipmentstate.v1beta1B%OceanCarrierBookingMismatchStateProtoP\001\352\0025Flexport::ExecutionMilestones::ShipmentState::V1Beta1"
    _globals["_OCEANCARRIERBOOKINGMISMATCHSTATE_MISMATCHESBYCARRIERBOOKINGENTRY"]._options = None
    _globals["_OCEANCARRIERBOOKINGMISMATCHSTATE_MISMATCHESBYCARRIERBOOKINGENTRY"]._serialized_options = b"8\001"
    _globals["_OCEANCARRIERBOOKINGMISMATCHES_MISMATCHESBYTYPEENTRY"]._options = None
    _globals["_OCEANCARRIERBOOKINGMISMATCHES_MISMATCHESBYTYPEENTRY"]._serialized_options = b"8\001"
    _globals["_OCEANCARRIERBOOKINGMISMATCHSTATE"]._serialized_start = 304
    _globals["_OCEANCARRIERBOOKINGMISMATCHSTATE"]._serialized_end = 669
    _globals["_OCEANCARRIERBOOKINGMISMATCHSTATE_MISMATCHESBYCARRIERBOOKINGENTRY"]._serialized_start = 521
    _globals["_OCEANCARRIERBOOKINGMISMATCHSTATE_MISMATCHESBYCARRIERBOOKINGENTRY"]._serialized_end = 669
    _globals["_OCEANCARRIERBOOKINGMISMATCHES"]._serialized_start = 672
    _globals["_OCEANCARRIERBOOKINGMISMATCHES"]._serialized_end = 976
    _globals["_OCEANCARRIERBOOKINGMISMATCHES_MISMATCHESBYTYPEENTRY"]._serialized_start = 840
    _globals["_OCEANCARRIERBOOKINGMISMATCHES_MISMATCHESBYTYPEENTRY"]._serialized_end = 976
    _globals["_OCEANCARRIERBOOKINGMISMATCH"]._serialized_start = 979
    _globals["_OCEANCARRIERBOOKINGMISMATCH"]._serialized_end = 1243
# @@protoc_insertion_point(module_scope)