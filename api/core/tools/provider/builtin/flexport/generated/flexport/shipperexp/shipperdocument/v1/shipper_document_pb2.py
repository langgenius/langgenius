# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/shipperexp/shipperdocument/v1/shipper_document.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n=flexport/shipperexp/shipperdocument/v1/shipper_document.proto\x12&flexport.shipperexp.shipperdocument.v1\x1aQflexport/shipperexp/shipperdocumentbasicdata/v1/shipper_document_basic_data.proto"\x85\x01\n\x0fShipperDocument\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x02 \x01(\t\x12O\n\x07\x63ontent\x18\x03 \x01(\x0b\x32>.flexport.shipperexp.shipperdocument.v1.ShipperDocumentContent"\xca\x08\n\x16ShipperDocumentContent\x12\x12\n\nversion_id\x18\x01 \x01(\t\x12\x13\n\x0bshipper_fid\x18\x02 \x01(\t\x12!\n\x19\x66ormatted_shipper_address\x18\x03 \x01(\t\x12\x15\n\rconsignee_fid\x18\x04 \x01(\t\x12#\n\x1b\x66ormatted_consignee_address\x18\x05 \x01(\t\x12\x18\n\x10notify_party_fid\x18\x06 \x01(\t\x12&\n\x1e\x66ormatted_notify_party_address\x18\x07 \x01(\t\x12V\n\x0erelease_method\x18\x08 \x01(\x0e\x32>.flexport.shipperexp.shipperdocumentbasicdata.v1.ReleaseMethod\x12k\n bill_of_lading_transmission_mode\x18\t \x01(\x0e\x32\x41.flexport.shipperexp.shipperdocumentbasicdata.v1.TransmissionMode\x12\x1f\n\x17\x65xport_reference_number\x18\n \x01(\t\x12+\n#bill_of_lading_special_instructions\x18\x0b \x01(\t\x12v\n\x1fverified_gross_mass_declaration\x18\x0c \x01(\x0b\x32M.flexport.shipperexp.shipperdocumentbasicdata.v1.VerifiedGrossMassDeclaration\x12X\n\nshipper_si\x18\r \x01(\x0b\x32\x44.flexport.shipperexp.shipperdocumentbasicdata.v1.DocumentInformation\x12Z\n\x0cshipper_ccam\x18\x0e \x01(\x0b\x32\x44.flexport.shipperexp.shipperdocumentbasicdata.v1.DocumentInformation\x12Y\n\x0bshipper_vgm\x18\x0f \x01(\x0b\x32\x44.flexport.shipperexp.shipperdocumentbasicdata.v1.DocumentInformation\x12n\n\x1bshipper_document_containers\x18\x10 \x03(\x0b\x32I.flexport.shipperexp.shipperdocumentbasicdata.v1.ShipperDocumentContainer\x12Z\n\x12unit_type_on_total\x18\x11 \x01(\x0e\x32>.flexport.shipperexp.shipperdocumentbasicdata.v1.CargoUnitTypeBp\n*com.flexport.shipperexp.shipperdocument.v1B\x14ShipperDocumentProtoP\x01\xea\x02)Flexport::ShipperExp::ShipperDocument::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.shipperexp.shipperdocument.v1.shipper_document_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n*com.flexport.shipperexp.shipperdocument.v1B\024ShipperDocumentProtoP\001\352\002)Flexport::ShipperExp::ShipperDocument::V1"
    _globals["_SHIPPERDOCUMENT"]._serialized_start = 189
    _globals["_SHIPPERDOCUMENT"]._serialized_end = 322
    _globals["_SHIPPERDOCUMENTCONTENT"]._serialized_start = 325
    _globals["_SHIPPERDOCUMENTCONTENT"]._serialized_end = 1423
# @@protoc_insertion_point(module_scope)