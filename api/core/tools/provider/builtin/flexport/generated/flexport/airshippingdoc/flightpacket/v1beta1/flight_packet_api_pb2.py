# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/airshippingdoc/flightpacket/v1beta1/flight_packet_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nDflexport/airshippingdoc/flightpacket/v1beta1/flight_packet_api.proto\x12,flexport.airshippingdoc.flightpacket.v1beta1\x1a@flexport/airshippingdoc/flightpacket/v1beta1/flight_packet.proto\x1a\x1egoogle/protobuf/wrappers.proto"d\n\x19\x43reateFlightPacketRequest\x12\x31\n\x0bmawb_number\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x14\n\x0cshipment_ids\x18\x02 \x03(\r"_\n\x1a\x43reateFlightPacketResponse\x12\x31\n\x0bmawb_number\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t"L\n\x17ListFlightPacketRequest\x12\x31\n\x0bmawb_number\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue"}\n\x18ListFlightPacketResponse\x12Q\n\rflight_packet\x18\x01 \x01(\x0b\x32:.flexport.airshippingdoc.flightpacket.v1beta1.FlightPacket\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t"\x9f\x01\n\x17SaveFlightPacketRequest\x12Q\n\rflight_packet\x18\x01 \x01(\x0b\x32:.flexport.airshippingdoc.flightpacket.v1beta1.FlightPacket\x12\x31\n\x0bmawb_number\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue"]\n\x18SaveFlightPacketResponse\x12\x31\n\x0bmawb_number\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t2\x83\x04\n\x0f\x46lightPacketAPI\x12\xa1\x01\n\x10ListFlightPacket\x12\x45.flexport.airshippingdoc.flightpacket.v1beta1.ListFlightPacketRequest\x1a\x46.flexport.airshippingdoc.flightpacket.v1beta1.ListFlightPacketResponse\x12\xa1\x01\n\x10SaveFlightPacket\x12\x45.flexport.airshippingdoc.flightpacket.v1beta1.SaveFlightPacketRequest\x1a\x46.flexport.airshippingdoc.flightpacket.v1beta1.SaveFlightPacketResponse\x12\xa7\x01\n\x12\x43reateFlightPacket\x12G.flexport.airshippingdoc.flightpacket.v1beta1.CreateFlightPacketRequest\x1aH.flexport.airshippingdoc.flightpacket.v1beta1.CreateFlightPacketResponseB|\n0com.flexport.airshippingdoc.flightpacket.v1beta1B\x14\x46lightPacketApiProtoP\x01\xea\x02/Flexport::AirShippingDoc::FlightPacket::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.airshippingdoc.flightpacket.v1beta1.flight_packet_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n0com.flexport.airshippingdoc.flightpacket.v1beta1B\024FlightPacketApiProtoP\001\352\002/Flexport::AirShippingDoc::FlightPacket::V1Beta1"
    _globals["_CREATEFLIGHTPACKETREQUEST"]._serialized_start = 216
    _globals["_CREATEFLIGHTPACKETREQUEST"]._serialized_end = 316
    _globals["_CREATEFLIGHTPACKETRESPONSE"]._serialized_start = 318
    _globals["_CREATEFLIGHTPACKETRESPONSE"]._serialized_end = 413
    _globals["_LISTFLIGHTPACKETREQUEST"]._serialized_start = 415
    _globals["_LISTFLIGHTPACKETREQUEST"]._serialized_end = 491
    _globals["_LISTFLIGHTPACKETRESPONSE"]._serialized_start = 493
    _globals["_LISTFLIGHTPACKETRESPONSE"]._serialized_end = 618
    _globals["_SAVEFLIGHTPACKETREQUEST"]._serialized_start = 621
    _globals["_SAVEFLIGHTPACKETREQUEST"]._serialized_end = 780
    _globals["_SAVEFLIGHTPACKETRESPONSE"]._serialized_start = 782
    _globals["_SAVEFLIGHTPACKETRESPONSE"]._serialized_end = 875
    _globals["_FLIGHTPACKETAPI"]._serialized_start = 878
    _globals["_FLIGHTPACKETAPI"]._serialized_end = 1393
# @@protoc_insertion_point(module_scope)