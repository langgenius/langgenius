# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/shipperexp/shipperdocumentsubmitted/v1/shipper_document_submitted.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nPflexport/shipperexp/shipperdocumentsubmitted/v1/shipper_document_submitted.proto\x12/flexport.shipperexp.shipperdocumentsubmitted.v1\x1a\x41\x66lexport/shipperexp/asyncjobvalues/v1beta1/async_job_values.proto\x1aQflexport/shipperexp/shipperdocumentbasicdata/v1/shipper_document_basic_data.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xd7\x02\n\x18ShipperDocumentSubmitted\x12\x14\n\x0csubmitted_by\x18\x01 \x01(\t\x12\x35\n\x11submitted_at_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x0fimpersonated_by\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12T\n\x10\x61sync_job_values\x18\x04 \x01(\x0b\x32:.flexport.shipperexp.asyncjobvalues.v1beta1.AsyncJobValues\x12\x61\n\x07\x63ontent\x18\x05 \x01(\x0b\x32P.flexport.shipperexp.shipperdocumentsubmitted.v1.ShipperDocumentSubmittedContent"\x88\t\n\x1fShipperDocumentSubmittedContent\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x02 \x01(\t\x12\x12\n\nversion_id\x18\x03 \x01(\t\x12\x13\n\x0bshipper_fid\x18\x04 \x01(\t\x12!\n\x19\x66ormatted_shipper_address\x18\x05 \x01(\t\x12\x15\n\rconsignee_fid\x18\x06 \x01(\t\x12#\n\x1b\x66ormatted_consignee_address\x18\x07 \x01(\t\x12\x18\n\x10notify_party_fid\x18\x08 \x01(\t\x12&\n\x1e\x66ormatted_notify_party_address\x18\t \x01(\t\x12V\n\x0erelease_method\x18\n \x01(\x0e\x32>.flexport.shipperexp.shipperdocumentbasicdata.v1.ReleaseMethod\x12k\n bill_of_lading_transmission_mode\x18\x0b \x01(\x0e\x32\x41.flexport.shipperexp.shipperdocumentbasicdata.v1.TransmissionMode\x12\x1f\n\x17\x65xport_reference_number\x18\x0c \x01(\t\x12+\n#bill_of_lading_special_instructions\x18\r \x01(\t\x12v\n\x1fverified_gross_mass_declaration\x18\x0e \x01(\x0b\x32M.flexport.shipperexp.shipperdocumentbasicdata.v1.VerifiedGrossMassDeclaration\x12^\n\nshipper_si\x18\x0f \x01(\x0b\x32J.flexport.shipperexp.shipperdocumentbasicdata.v1.DocumentStatusInformation\x12`\n\x0cshipper_ccam\x18\x10 \x01(\x0b\x32J.flexport.shipperexp.shipperdocumentbasicdata.v1.DocumentStatusInformation\x12_\n\x0bshipper_vgm\x18\x11 \x01(\x0b\x32J.flexport.shipperexp.shipperdocumentbasicdata.v1.DocumentStatusInformation\x12n\n\x1bshipper_document_containers\x18\x12 \x03(\x0b\x32I.flexport.shipperexp.shipperdocumentbasicdata.v1.ShipperDocumentContainer\x12Z\n\x12unit_type_on_total\x18\x13 \x01(\x0e\x32>.flexport.shipperexp.shipperdocumentbasicdata.v1.CargoUnitTypeB\x8b\x01\n3com.flexport.shipperexp.shipperdocumentsubmitted.v1B\x1dShipperDocumentSubmittedProtoP\x01\xea\x02\x32\x46lexport::ShipperExp::ShipperDocumentSubmitted::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.shipperexp.shipperdocumentsubmitted.v1.shipper_document_submitted_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n3com.flexport.shipperexp.shipperdocumentsubmitted.v1B\035ShipperDocumentSubmittedProtoP\001\352\0022Flexport::ShipperExp::ShipperDocumentSubmitted::V1"
    _globals["_SHIPPERDOCUMENTSUBMITTED"]._serialized_start = 349
    _globals["_SHIPPERDOCUMENTSUBMITTED"]._serialized_end = 692
    _globals["_SHIPPERDOCUMENTSUBMITTEDCONTENT"]._serialized_start = 695
    _globals["_SHIPPERDOCUMENTSUBMITTEDCONTENT"]._serialized_end = 1855
# @@protoc_insertion_point(module_scope)