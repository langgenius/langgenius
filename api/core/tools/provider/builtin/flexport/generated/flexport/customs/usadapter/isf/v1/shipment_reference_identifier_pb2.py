# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customs/usadapter/isf/v1/shipment_reference_identifier.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nEflexport/customs/usadapter/isf/v1/shipment_reference_identifier.proto\x12!flexport.customs.usadapter.isf.v1"\x97\x01\n\x1bShipmentReferenceIdentifier\x12Z\n\x0ereference_type\x18\x01 \x01(\x0e\x32\x42.flexport.customs.usadapter.isf.v1.ShipmentReferenceIdentifierType\x12\x1c\n\x14reference_identifier\x18\x02 \x01(\t*\xcb\x01\n\x1fShipmentReferenceIdentifierType\x12.\n*SHIPMENT_REFERENCE_IDENTIFIER_TYPE_INVALID\x10\x00\x12;\n7SHIPMENT_REFERENCE_IDENTIFIER_TYPE_OCEAN_BILL_OF_LADING\x10\x01\x12;\n7SHIPMENT_REFERENCE_IDENTIFIER_TYPE_HOUSE_BILL_OF_LADING\x10\x02\x42Q\n%com.flexport.customs.usadapter.isf.v1P\x01\xea\x02%Flexport::Customs::UsAdapter::Isf::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customs.usadapter.isf.v1.shipment_reference_identifier_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n%com.flexport.customs.usadapter.isf.v1P\001\352\002%Flexport::Customs::UsAdapter::Isf::V1"
    )
    _globals["_SHIPMENTREFERENCEIDENTIFIERTYPE"]._serialized_start = 263
    _globals["_SHIPMENTREFERENCEIDENTIFIERTYPE"]._serialized_end = 466
    _globals["_SHIPMENTREFERENCEIDENTIFIER"]._serialized_start = 109
    _globals["_SHIPMENTREFERENCEIDENTIFIER"]._serialized_end = 260
# @@protoc_insertion_point(module_scope)