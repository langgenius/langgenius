# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executionmilestones/shipmentschedulevalidation/v1beta1/shipment_schedule_validation_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nfflexport/executionmilestones/shipmentschedulevalidation/v1beta1/shipment_schedule_validation_api.proto\x12?flexport.executionmilestones.shipmentschedulevalidation.v1beta1"7\n\x1fValidateShipmentScheduleRequest\x12\x14\n\x0cshipment_fid\x18\x01 \x01(\t"D\n ValidateShipmentScheduleResponse\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t2\x81\x02\n\x1dShipmentScheduleValidationAPI\x12\xdf\x01\n\x18ValidateShipmentSchedule\x12`.flexport.executionmilestones.shipmentschedulevalidation.v1beta1.ValidateShipmentScheduleRequest\x1a\x61.flexport.executionmilestones.shipmentschedulevalidation.v1beta1.ValidateShipmentScheduleResponseB\xad\x01\nCcom.flexport.executionmilestones.shipmentschedulevalidation.v1beta1B\x1fShipmentScheduleValidationProtoP\x01\xea\x02\x42\x46lexport::ExecutionMilestones::ShipmentScheduleValidation::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.executionmilestones.shipmentschedulevalidation.v1beta1.shipment_schedule_validation_api_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\nCcom.flexport.executionmilestones.shipmentschedulevalidation.v1beta1B\037ShipmentScheduleValidationProtoP\001\352\002BFlexport::ExecutionMilestones::ShipmentScheduleValidation::V1Beta1"
    _globals["_VALIDATESHIPMENTSCHEDULEREQUEST"]._serialized_start = 171
    _globals["_VALIDATESHIPMENTSCHEDULEREQUEST"]._serialized_end = 226
    _globals["_VALIDATESHIPMENTSCHEDULERESPONSE"]._serialized_start = 228
    _globals["_VALIDATESHIPMENTSCHEDULERESPONSE"]._serialized_end = 296
    _globals["_SHIPMENTSCHEDULEVALIDATIONAPI"]._serialized_start = 299
    _globals["_SHIPMENTSCHEDULEVALIDATIONAPI"]._serialized_end = 556
# @@protoc_insertion_point(module_scope)