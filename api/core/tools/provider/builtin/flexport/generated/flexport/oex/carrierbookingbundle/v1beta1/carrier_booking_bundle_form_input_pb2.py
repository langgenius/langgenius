# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/oex/carrierbookingbundle/v1beta1/carrier_booking_bundle_form_input.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nQflexport/oex/carrierbookingbundle/v1beta1/carrier_booking_bundle_form_input.proto\x12)flexport.oex.carrierbookingbundle.v1beta1\x1a\x46\x66lexport/oex/carrierbookingbundle/v1beta1/carrier_booking_bundle.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xec\x05\n\x13\x42ookingContentInput\x12\x11\n\tprebooked\x18\x01 \x01(\x08\x12\x13\n\x0b\x63\x61rrier_fid\x18\x02 \x01(\t\x12!\n\x14\x63\x61rrier_contract_fid\x18\x03 \x01(\tH\x00\x88\x01\x01\x12,\n\x1foffline_carrier_contract_number\x18\r \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11\x62ooking_party_fid\x18\n \x01(\tH\x02\x88\x01\x01\x12-\n\tcy_cutoff\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tsi_cutoff\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nvgm_cutoff\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10premium_services\x18\t \x03(\t\x12W\n\x06status\x18\x07 \x01(\x0e\x32G.flexport.oex.carrierbookingbundle.v1beta1.BookingContent.BookingStatus\x12\x66\n\x0erelease_status\x18\x08 \x01(\x0e\x32N.flexport.oex.carrierbookingbundle.v1beta1.BookingContent.BookingReleaseStatus\x12\'\n\x1asource_carrier_booking_fid\x18\x0b \x01(\tH\x03\x88\x01\x01\x12 \n\x13updated_by_user_fid\x18\x0c \x01(\tH\x04\x88\x01\x01\x42\x17\n\x15_carrier_contract_fidB"\n _offline_carrier_contract_numberB\x14\n\x12_booking_party_fidB\x1d\n\x1b_source_carrier_booking_fidB\x16\n\x14_updated_by_user_fid"\xe6\r\n\x17\x42ookingIntegrationInput\x12y\n\x13integration_partner\x18\x01 \x01(\x0e\x32W.flexport.oex.carrierbookingbundle.v1beta1.BookingIntegration.BookingIntegrationPartnerH\x00\x88\x01\x01\x12$\n\x17\x62ooking_office_port_fid\x18\x02 \x01(\tH\x01\x88\x01\x01\x12 \n\x13\x63ontract_client_fid\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x1a\n\rcontact_email\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x17\n\nrate_group\x18\x06 \x01(\tH\x04\x88\x01\x01\x12(\n\x1b\x65\x64ifact_booking_description\x18\x07 \x01(\tH\x05\x88\x01\x01\x12)\n\x1c\x65\x64ifact_description_of_goods\x18\x08 \x01(\tH\x06\x88\x01\x01\x12\x1b\n\x13\x65\x64ifact_commodities\x18\t \x03(\t\x12\x18\n\x10\x65\x64ifact_hs_codes\x18\n \x03(\t\x12\x1c\n\x0f\x65\x64ifact_package\x18\x0b \x01(\x03H\x07\x88\x01\x01\x12\x1b\n\x0e\x65\x64ifact_volume\x18\x0c \x01(\x01H\x08\x88\x01\x01\x12\x1b\n\x0e\x65\x64ifact_weight\x18\r \x01(\x01H\t\x88\x01\x01\x12u\n\x11placed_externally\x18\x0f \x01(\x0e\x32U.flexport.oex.carrierbookingbundle.v1beta1.BookingIntegration.BookingPlacedExternallyH\n\x88\x01\x01\x12\x1d\n\x15uses_partner_contract\x18\x10 \x01(\x08\x12\'\n\x1aspot_rate_offer_identifier\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x1f\n\x12internal_reference\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x19\n\x0c\x66reight_type\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x19\n\x0cpayment_term\x18\x14 \x01(\tH\x0e\x88\x01\x01\x12"\n\x15payment_location_code\x18\x15 \x01(\tH\x0f\x88\x01\x01\x12"\n\x15payment_location_name\x18\x16 \x01(\tH\x10\x88\x01\x01\x12s\n\x14\x63ontract_source_type\x18\x17 \x01(\x0e\x32P.flexport.oex.carrierbookingbundle.v1beta1.BookingIntegration.ContractSourceTypeH\x11\x88\x01\x01\x12+\n\x1e\x66lexport_operation_contact_fid\x18\x18 \x01(\tH\x12\x88\x01\x01\x12Q\n\x07shipper\x18\x19 \x01(\x0b\x32;.flexport.oex.carrierbookingbundle.v1beta1.IntegrationPartyH\x13\x88\x01\x01\x12S\n\tconsignee\x18\x1a \x01(\x0b\x32;.flexport.oex.carrierbookingbundle.v1beta1.IntegrationPartyH\x14\x88\x01\x01\x12V\n\x0cnotify_party\x18\x1b \x01(\x0b\x32;.flexport.oex.carrierbookingbundle.v1beta1.IntegrationPartyH\x15\x88\x01\x01\x42\x16\n\x14_integration_partnerB\x1a\n\x18_booking_office_port_fidB\x16\n\x14_contract_client_fidB\x10\n\x0e_contact_emailB\r\n\x0b_rate_groupB\x1e\n\x1c_edifact_booking_descriptionB\x1f\n\x1d_edifact_description_of_goodsB\x12\n\x10_edifact_packageB\x11\n\x0f_edifact_volumeB\x11\n\x0f_edifact_weightB\x14\n\x12_placed_externallyB\x1d\n\x1b_spot_rate_offer_identifierB\x15\n\x13_internal_referenceB\x0f\n\r_freight_typeB\x0f\n\r_payment_termB\x18\n\x16_payment_location_codeB\x18\n\x16_payment_location_nameB\x17\n\x15_contract_source_typeB!\n\x1f_flexport_operation_contact_fidB\n\n\x08_shipperB\x0c\n\n_consigneeB\x0f\n\r_notify_party"\xf6\x05\n\x12\x42ookingVoyageInput\x12\x11\n\x04uuid\x18\x01 \x01(\tH\x00\x88\x01\x01\x12h\n\x13transportation_mode\x18\x02 \x01(\x0e\x32K.flexport.oex.carrierbookingbundle.v1beta1.BookingVoyage.TransportationMode\x12 \n\x13\x66reight_carrier_fid\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x17\n\norigin_fid\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x1c\n\x0f\x64\x65stination_fid\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x37\n\x13scheduled_departure\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11scheduled_arrival\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\nvessel_fid\x18\n \x01(\tH\x04\x88\x01\x01\x12\x1a\n\rvoyage_number\x18\x0b \x01(\tH\x05\x88\x01\x01\x12#\n\x16operator_voyage_number\x18\x0f \x01(\tH\x06\x88\x01\x01\x12\'\n\x1a\x63\x61rrier_service_string_fid\x18\x0c \x01(\tH\x07\x88\x01\x01\x12 \n\x13\x63\x61rgosmart_route_id\x18\r \x01(\tH\x08\x88\x01\x01\x12#\n\x16\x65stimated_schedule_fid\x18\x0e \x01(\tH\t\x88\x01\x01\x42\x07\n\x05_uuidB\x16\n\x14_freight_carrier_fidB\r\n\x0b_origin_fidB\x12\n\x10_destination_fidB\r\n\x0b_vessel_fidB\x10\n\x0e_voyage_numberB\x19\n\x17_operator_voyage_numberB\x1d\n\x1b_carrier_service_string_fidB\x16\n\x14_cargosmart_route_idB\x19\n\x17_estimated_schedule_fid"\x8e\x04\n\x12ShippingOrderInput\x12\x11\n\x04uuid\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\x0e\x62ooking_number\x18\x02 \x01(\t\x12\x11\n\tso_number\x18\x03 \x01(\t\x12-\n\tcy_cutoff\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tsi_cutoff\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nvgm_cutoff\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12X\n\x13released_containers\x18\x07 \x03(\x0b\x32;.flexport.oex.carrierbookingbundle.v1beta1.BookingContainer\x12\x15\n\rdocument_fids\x18\x05 \x03(\t\x12\x16\n\x0esub_so_numbers\x18\x04 \x03(\t\x12\x17\n\nref_number\x18\x06 \x01(\tH\x01\x88\x01\x01\x12 \n\x13updated_by_user_fid\x18\x0b \x01(\tH\x02\x88\x01\x01\x12 \n\x13\x63reated_by_user_fid\x18\x0c \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_uuidB\r\n\x0b_ref_numberB\x16\n\x14_updated_by_user_fidB\x16\n\x14_created_by_user_fid"\xd7\x06\n\x19\x43\x61rrierBookingBundleInput\x12 \n\x13\x63\x61rrier_booking_fid\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cshipment_fid\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1b\n\x0e\x62ooking_number\x18\x03 \x01(\tH\x02\x88\x01\x01\x12W\n\x0f\x62ooking_content\x18\x04 \x01(\x0b\x32>.flexport.oex.carrierbookingbundle.v1beta1.BookingContentInput\x12_\n\x13\x62ooking_integration\x18\x05 \x01(\x0b\x32\x42.flexport.oex.carrierbookingbundle.v1beta1.BookingIntegrationInput\x12W\n\x12\x63ontainer_requests\x18\x06 \x03(\x0b\x32;.flexport.oex.carrierbookingbundle.v1beta1.BookingContainer\x12V\n\x0f\x62ooking_voyages\x18\x07 \x03(\x0b\x32=.flexport.oex.carrierbookingbundle.v1beta1.BookingVoyageInput\x12L\n\x0chbl_override\x18\x08 \x01(\x0b\x32\x36.flexport.oex.carrierbookingbundle.v1beta1.HblOverride\x12V\n\x0fshipping_orders\x18\t \x03(\x0b\x32=.flexport.oex.carrierbookingbundle.v1beta1.ShippingOrderInput\x12W\n\x0f\x63\x61rrier_haulage\x18\r \x01(\x0b\x32\x39.flexport.oex.carrierbookingbundle.v1beta1.CarrierHaulageH\x03\x88\x01\x01\x12&\n\x1e\x63reated_or_updated_by_user_fid\x18\n \x01(\tB\x16\n\x14_carrier_booking_fidB\x0f\n\r_shipment_fidB\x11\n\x0f_booking_numberB\x12\n\x10_carrier_haulage"\x93\x02\n\x1d\x43\x61rrierBookingBundleFormInput\x12\x64\n\x16\x63\x61rrier_booking_bundle\x18\x01 \x01(\x0b\x32\x44.flexport.oex.carrierbookingbundle.v1beta1.CarrierBookingBundleInput\x12\x19\n\x0c\x65vent_source\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rfrontend_view\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x1d\n\x10\x66rontend_feature\x18\x04 \x01(\tH\x02\x88\x01\x01\x42\x0f\n\r_event_sourceB\x10\n\x0e_frontend_viewB\x13\n\x11_frontend_featureB\x84\x01\n-com.flexport.oex.carrierbookingbundle.v1beta1B"CarrierBookingBundleFormInputProtoP\x01\xea\x02,Flexport::OEX::CarrierBookingBundle::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.oex.carrierbookingbundle.v1beta1.carrier_booking_bundle_form_input_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b'\n-com.flexport.oex.carrierbookingbundle.v1beta1B"CarrierBookingBundleFormInputProtoP\001\352\002,Flexport::OEX::CarrierBookingBundle::V1Beta1'
    _globals["_BOOKINGCONTENTINPUT"]._serialized_start = 234
    _globals["_BOOKINGCONTENTINPUT"]._serialized_end = 982
    _globals["_BOOKINGINTEGRATIONINPUT"]._serialized_start = 985
    _globals["_BOOKINGINTEGRATIONINPUT"]._serialized_end = 2751
    _globals["_BOOKINGVOYAGEINPUT"]._serialized_start = 2754
    _globals["_BOOKINGVOYAGEINPUT"]._serialized_end = 3512
    _globals["_SHIPPINGORDERINPUT"]._serialized_start = 3515
    _globals["_SHIPPINGORDERINPUT"]._serialized_end = 4041
    _globals["_CARRIERBOOKINGBUNDLEINPUT"]._serialized_start = 4044
    _globals["_CARRIERBOOKINGBUNDLEINPUT"]._serialized_end = 4899
    _globals["_CARRIERBOOKINGBUNDLEFORMINPUT"]._serialized_start = 4902
    _globals["_CARRIERBOOKINGBUNDLEFORMINPUT"]._serialized_end = 5177
# @@protoc_insertion_point(module_scope)