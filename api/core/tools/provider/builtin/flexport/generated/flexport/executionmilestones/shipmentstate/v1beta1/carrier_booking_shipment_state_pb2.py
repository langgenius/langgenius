# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executionmilestones/shipmentstate/v1beta1/carrier_booking_shipment_state.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nWflexport/executionmilestones/shipmentstate/v1beta1/carrier_booking_shipment_state.proto\x12\x32\x66lexport.executionmilestones.shipmentstate.v1beta1\x1a\x42\x66lexport/os/v1/types/walltimedatetime/v1/wall_time_date_time.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa0\x01\n\x1b\x43\x61rrierBookingShipmentState\x12\x14\n\x0cshipment_fid\x18\x01 \x01(\t\x12k\n\x18\x63\x61rrier_booking_extracts\x18\x02 \x03(\x0b\x32I.flexport.executionmilestones.shipmentstate.v1beta1.CarrierBookingExtract"\xac\x0c\n\x15\x43\x61rrierBookingExtract\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x16\n\x0e\x62ooking_number\x18\x04 \x01(\t\x12L\n\x08\x65td_time\x18\x06 \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTime\x12R\n\x0esi_cutoff_time\x18\x07 \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTime\x12S\n\x0fvgm_cutoff_time\x18\x08 \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTime\x12R\n\x0e\x63y_cutoff_time\x18\t \x01(\x0b\x32:.flexport.os.v1.types.walltimedatetime.v1.WallTimeDateTime\x12]\n\x0bstatus_enum\x18\n \x01(\x0e\x32H.flexport.executionmilestones.shipmentstate.v1beta1.CarrierBookingStatus\x12l\n\x13release_status_enum\x18\x0b \x01(\x0e\x32O.flexport.executionmilestones.shipmentstate.v1beta1.CarrierBookingReleaseStatus\x12\x82\x01\n"carrier_booking_container_requests\x18\x0c \x03(\x0b\x32R.flexport.executionmilestones.shipmentstate.v1beta1.CarrierBookingContainerRequestB\x02\x18\x01\x12\x12\n\nso_numbers\x18\r \x03(\t\x12`\n\x12\x63ontainer_requests\x18\x0e \x03(\x0b\x32\x44.flexport.executionmilestones.shipmentstate.v1beta1.BookingContainer\x12\x63\n\x13\x62ooking_integration\x18\x0f \x01(\x0b\x32\x46.flexport.executionmilestones.shipmentstate.v1beta1.BookingIntegration\x12\x18\n\x10so_document_fids\x18\x10 \x03(\t\x12\x1c\n\x14\x61ll_so_document_fids\x18\x11 \x03(\t\x12]\n\x10\x63\x61rrier_contract\x18\x12 \x01(\x0b\x32\x43.flexport.executionmilestones.shipmentstate.v1beta1.CarrierContract\x12/\n\x0b\x61ttached_at\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12 \n\x13updated_by_user_fid\x18\x14 \x01(\tH\x00\x88\x01\x01\x12=\n\x14updated_by_user_time\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x12#\n\x16so_updated_by_user_fid\x18\x16 \x01(\tH\x02\x88\x01\x01\x12\x36\n\rso_updated_at\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x03\x88\x01\x01\x12\x13\n\x0b\x63\x61rrier_fid\x18\x18 \x01(\t\x12Z\n\x0fshipping_orders\x18\x19 \x03(\x0b\x32\x41.flexport.executionmilestones.shipmentstate.v1beta1.ShippingOrder\x12!\n\x19uploaded_so_document_fids\x18\x1a \x03(\tB\x16\n\x14_updated_by_user_fidB\x17\n\x15_updated_by_user_timeB\x19\n\x17_so_updated_by_user_fidB\x10\n\x0e_so_updated_at"\x89\x01\n\rShippingOrder\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x17\n\ncreated_by\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x33\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x42\r\n\x0b_created_byB\r\n\x0b_created_at"v\n\x1e\x43\x61rrierBookingContainerRequest\x12\x16\n\x0e\x63ontainer_type\x18\x01 \x01(\t\x12\x15\n\rcontaine_size\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x13\n\x0b\x63\x61rrier_teu\x18\x04 \x01(\x05"@\n\x10\x42ookingContainer\x12\x1a\n\x12iso_container_type\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x03"\xb5\x05\n\x12\x42ookingIntegration\x12\x82\x01\n\x13integration_partner\x18\x01 \x01(\x0e\x32`.flexport.executionmilestones.shipmentstate.v1beta1.BookingIntegration.BookingIntegrationPartnerH\x00\x88\x01\x01\x12\x1f\n\x12internal_reference\x18\x0e \x01(\tH\x01\x88\x01\x01"\xb0\x02\n\x19\x42ookingIntegrationPartner\x12\'\n#BOOKING_INTEGRATION_PARTNER_INVALID\x10\x00\x12&\n"BOOKING_INTEGRATION_PARTNER_INTTRA\x10\x01\x12#\n\x1f\x42OOKING_INTEGRATION_PARTNER_CMA\x10\x02\x12%\n!BOOKING_INTEGRATION_PARTNER_BOOMI\x10\x03\x12#\n\x1f\x42OOKING_INTEGRATION_PARTNER_OIT\x10\x04\x12*\n&BOOKING_INTEGRATION_PARTNER_TRANSOCEAN\x10\x05\x12%\n!BOOKING_INTEGRATION_PARTNER_CMLOG\x10\x06"\x96\x01\n\x17\x42ookingPlacedExternally\x12%\n!BOOKING_PLACED_EXTERNALLY_INVALID\x10\x00\x12#\n\x1f\x42OOKING_PLACED_EXTERNALLY_OTHER\x10\x01\x12/\n+BOOKING_PLACED_EXTERNALLY_SYNCONHUB_WEBSITE\x10\x02\x42\x16\n\x14_integration_partnerB\x15\n\x13_internal_reference"7\n\x0f\x43\x61rrierContract\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontract_number\x18\x02 \x01(\t*\xaf\x03\n\x14\x43\x61rrierBookingStatus\x12"\n\x1e\x43\x41RRIER_BOOKING_STATUS_INVALID\x10\x00\x12"\n\x1e\x43\x41RRIER_BOOKING_STATUS_CREATED\x10\x01\x12$\n CARRIER_BOOKING_STATUS_REQUESTED\x10\x02\x12"\n\x1e\x43\x41RRIER_BOOKING_STATUS_PENDING\x10\x03\x12$\n CARRIER_BOOKING_STATUS_CONFIRMED\x10\x04\x12#\n\x1f\x43\x41RRIER_BOOKING_STATUS_DECLINED\x10\x05\x12$\n CARRIER_BOOKING_STATUS_CANCELLED\x10\x06\x12#\n\x1f\x43\x41RRIER_BOOKING_STATUS_UNBOOKED\x10\x07\x12 \n\x1c\x43\x41RRIER_BOOKING_STATUS_ERROR\x10\x08\x12(\n$CARRIER_BOOKING_STATUS_SLA_VIOLATION\x10\t\x12#\n\x1f\x43\x41RRIER_BOOKING_STATUS_REVISING\x10\n*\xe4\x01\n\x1b\x43\x61rrierBookingReleaseStatus\x12*\n&CARRIER_BOOKING_RELEASE_STATUS_INVALID\x10\x00\x12\x31\n-CARRIER_BOOKING_RELEASE_STATUS_FULLY_RELEASED\x10\x01\x12\x35\n1CARRIER_BOOKING_RELEASE_STATUS_PARTIALLY_RELEASED\x10\x02\x12/\n+CARRIER_BOOKING_RELEASE_STATUS_NOT_RELEASED\x10\x03\x42\x94\x01\n6com.flexport.executionmilestones.shipmentstate.v1beta1B CarrierBookingShipmentStateProtoP\x01\xea\x02\x35\x46lexport::ExecutionMilestones::ShipmentState::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executionmilestones.shipmentstate.v1beta1.carrier_booking_shipment_state_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n6com.flexport.executionmilestones.shipmentstate.v1beta1B CarrierBookingShipmentStateProtoP\001\352\0025Flexport::ExecutionMilestones::ShipmentState::V1Beta1"
    _globals["_CARRIERBOOKINGEXTRACT"].fields_by_name["carrier_booking_container_requests"]._options = None
    _globals["_CARRIERBOOKINGEXTRACT"].fields_by_name[
        "carrier_booking_container_requests"
    ]._serialized_options = b"\030\001"
    _globals["_CARRIERBOOKINGSTATUS"]._serialized_start = 3070
    _globals["_CARRIERBOOKINGSTATUS"]._serialized_end = 3501
    _globals["_CARRIERBOOKINGRELEASESTATUS"]._serialized_start = 3504
    _globals["_CARRIERBOOKINGRELEASESTATUS"]._serialized_end = 3732
    _globals["_CARRIERBOOKINGSHIPMENTSTATE"]._serialized_start = 245
    _globals["_CARRIERBOOKINGSHIPMENTSTATE"]._serialized_end = 405
    _globals["_CARRIERBOOKINGEXTRACT"]._serialized_start = 408
    _globals["_CARRIERBOOKINGEXTRACT"]._serialized_end = 1988
    _globals["_SHIPPINGORDER"]._serialized_start = 1991
    _globals["_SHIPPINGORDER"]._serialized_end = 2128
    _globals["_CARRIERBOOKINGCONTAINERREQUEST"]._serialized_start = 2130
    _globals["_CARRIERBOOKINGCONTAINERREQUEST"]._serialized_end = 2248
    _globals["_BOOKINGCONTAINER"]._serialized_start = 2250
    _globals["_BOOKINGCONTAINER"]._serialized_end = 2314
    _globals["_BOOKINGINTEGRATION"]._serialized_start = 2317
    _globals["_BOOKINGINTEGRATION"]._serialized_end = 3010
    _globals["_BOOKINGINTEGRATION_BOOKINGINTEGRATIONPARTNER"]._serialized_start = 2506
    _globals["_BOOKINGINTEGRATION_BOOKINGINTEGRATIONPARTNER"]._serialized_end = 2810
    _globals["_BOOKINGINTEGRATION_BOOKINGPLACEDEXTERNALLY"]._serialized_start = 2813
    _globals["_BOOKINGINTEGRATION_BOOKINGPLACEDEXTERNALLY"]._serialized_end = 2963
    _globals["_CARRIERCONTRACT"]._serialized_start = 3012
    _globals["_CARRIERCONTRACT"]._serialized_end = 3067
# @@protoc_insertion_point(module_scope)