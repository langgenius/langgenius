# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/assignment/model/v1/shipment_data.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n0flexport/assignment/model/v1/shipment_data.proto\x12\x1c\x66lexport.assignment.model.v1"\xae\x02\n\x0cShipmentData\x12\x12\n\nclient_fid\x18\x01 \x01(\t\x12\x15\n\rshipment_mode\x18\x02 \x01(\t\x12\x1b\n\x13port_of_loading_fid\x18\x03 \x01(\t\x12$\n\x1cport_of_loading_country_code\x18\x04 \x01(\t\x12\x1d\n\x15port_of_unloading_fid\x18\x05 \x01(\t\x12&\n\x1eport_of_unloading_country_code\x18\x06 \x01(\t\x12\x1a\n\x12quoted_carrier_fid\x18\x07 \x01(\t\x12#\n\x1borigin_address_country_code\x18\x08 \x01(\t\x12(\n destination_address_country_code\x18\t \x01(\tBY\n com.flexport.assignment.model.v1B\x11ShipmentDataProtoP\x01\xea\x02\x1f\x46lexport::Assignment::Model::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.assignment.model.v1.shipment_data_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n com.flexport.assignment.model.v1B\021ShipmentDataProtoP\001\352\002\037Flexport::Assignment::Model::V1"
    )
    _globals["_SHIPMENTDATA"]._serialized_start = 83
    _globals["_SHIPMENTDATA"]._serialized_end = 385
# @@protoc_insertion_point(module_scope)