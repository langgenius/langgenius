# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/networkentities/port/v1/port_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n8flexport/monolith/networkentities/port/v1/port_api.proto\x12)flexport.monolith.networkentities.port.v1\x1a\x34\x66lexport/monolith/networkentities/port/v1/port.proto"%\n\x10ListPortsRequest\x12\x11\n\tport_fids\x18\x01 \x03(\t"S\n\x11ListPortsResponse\x12>\n\x05ports\x18\x01 \x03(\x0b\x32/.flexport.monolith.networkentities.port.v1.Port"+\n\x18\x46indPortsByLocodeRequest\x12\x0f\n\x07locodes\x18\x01 \x03(\t"[\n\x19\x46indPortsByLocodeResponse\x12>\n\x05ports\x18\x01 \x03(\x0b\x32/.flexport.monolith.networkentities.port.v1.Port".\n\x1b\x46indSeaPortsByLocodeRequest\x12\x0f\n\x07locodes\x18\x01 \x03(\t"^\n\x1c\x46indSeaPortsByLocodeResponse\x12>\n\x05ports\x18\x01 \x03(\x0b\x32/.flexport.monolith.networkentities.port.v1.Port"0\n\x1a\x46indPortsByIataCodeRequest\x12\x12\n\niata_codes\x18\x01 \x03(\t"]\n\x1b\x46indPortsByIataCodeResponse\x12>\n\x05ports\x18\x01 \x03(\x0b\x32/.flexport.monolith.networkentities.port.v1.Port2\x84\x05\n\x07PortAPI\x12\x86\x01\n\tListPorts\x12;.flexport.monolith.networkentities.port.v1.ListPortsRequest\x1a<.flexport.monolith.networkentities.port.v1.ListPortsResponse\x12\x9e\x01\n\x11\x46indPortsByLocode\x12\x43.flexport.monolith.networkentities.port.v1.FindPortsByLocodeRequest\x1a\x44.flexport.monolith.networkentities.port.v1.FindPortsByLocodeResponse\x12\xa7\x01\n\x14\x46indSeaPortsByLocode\x12\x46.flexport.monolith.networkentities.port.v1.FindSeaPortsByLocodeRequest\x1aG.flexport.monolith.networkentities.port.v1.FindSeaPortsByLocodeResponse\x12\xa4\x01\n\x13\x46indPortsByIataCode\x12\x45.flexport.monolith.networkentities.port.v1.FindPortsByIataCodeRequest\x1a\x46.flexport.monolith.networkentities.port.v1.FindPortsByIataCodeResponseBo\n-com.flexport.monolith.networkentities.port.v1B\x0cPortApiProtoP\x01\xea\x02-Flexport::Monolith::NetworkEntities::Port::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.monolith.networkentities.port.v1.port_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n-com.flexport.monolith.networkentities.port.v1B\014PortApiProtoP\001\352\002-Flexport::Monolith::NetworkEntities::Port::V1"
    _globals["_LISTPORTSREQUEST"]._serialized_start = 157
    _globals["_LISTPORTSREQUEST"]._serialized_end = 194
    _globals["_LISTPORTSRESPONSE"]._serialized_start = 196
    _globals["_LISTPORTSRESPONSE"]._serialized_end = 279
    _globals["_FINDPORTSBYLOCODEREQUEST"]._serialized_start = 281
    _globals["_FINDPORTSBYLOCODEREQUEST"]._serialized_end = 324
    _globals["_FINDPORTSBYLOCODERESPONSE"]._serialized_start = 326
    _globals["_FINDPORTSBYLOCODERESPONSE"]._serialized_end = 417
    _globals["_FINDSEAPORTSBYLOCODEREQUEST"]._serialized_start = 419
    _globals["_FINDSEAPORTSBYLOCODEREQUEST"]._serialized_end = 465
    _globals["_FINDSEAPORTSBYLOCODERESPONSE"]._serialized_start = 467
    _globals["_FINDSEAPORTSBYLOCODERESPONSE"]._serialized_end = 561
    _globals["_FINDPORTSBYIATACODEREQUEST"]._serialized_start = 563
    _globals["_FINDPORTSBYIATACODEREQUEST"]._serialized_end = 611
    _globals["_FINDPORTSBYIATACODERESPONSE"]._serialized_start = 613
    _globals["_FINDPORTSBYIATACODERESPONSE"]._serialized_end = 706
    _globals["_PORTAPI"]._serialized_start = 709
    _globals["_PORTAPI"]._serialized_end = 1353
# @@protoc_insertion_point(module_scope)