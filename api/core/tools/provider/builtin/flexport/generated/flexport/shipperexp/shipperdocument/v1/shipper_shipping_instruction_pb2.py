# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/shipperexp/shipperdocument/v1/shipper_shipping_instruction.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nIflexport/shipperexp/shipperdocument/v1/shipper_shipping_instruction.proto\x12&flexport.shipperexp.shipperdocument.v1\x1aQflexport/shipperexp/shipperdocumentbasicdata/v1/shipper_document_basic_data.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x9c\x03\n\x1aShipperShippingInstruction\x12\x1c\n\x14shipper_document_fid\x18\x01 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x02 \x01(\t\x12Z\n\x07\x63ontent\x18\x03 \x01(\x0b\x32I.flexport.shipperexp.shipperdocument.v1.ShipperShippingInstructionContent\x12\x33\n\x0f\x63reated_at_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x0e\x63reated_by_fid\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0eupdated_by_fid\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x18\n\x10user_company_fid\x18\x08 \x01(\t"\xd9\x05\n!ShipperShippingInstructionContent\x12\x13\n\x0bshipper_fid\x18\x01 \x01(\t\x12!\n\x19\x66ormatted_shipper_address\x18\x02 \x01(\t\x12\x15\n\rconsignee_fid\x18\x03 \x01(\t\x12#\n\x1b\x66ormatted_consignee_address\x18\x04 \x01(\t\x12\x18\n\x10notify_party_fid\x18\x05 \x01(\t\x12&\n\x1e\x66ormatted_notify_party_address\x18\x06 \x01(\t\x12V\n\x0erelease_method\x18\x07 \x01(\x0e\x32>.flexport.shipperexp.shipperdocumentbasicdata.v1.ReleaseMethod\x12k\n bill_of_lading_transmission_mode\x18\x08 \x01(\x0e\x32\x41.flexport.shipperexp.shipperdocumentbasicdata.v1.TransmissionMode\x12\x1f\n\x17\x65xport_reference_number\x18\t \x01(\t\x12+\n#bill_of_lading_special_instructions\x18\n \x01(\t\x12|\n\'shipper_shipping_instruction_containers\x18\x0b \x03(\x0b\x32K.flexport.shipperexp.shipperdocument.v1.ShipperShippingInstructionContainer\x12\x11\n\tfinalized\x18\x0c \x01(\x08\x12Z\n\x12unit_type_on_total\x18\r \x01(\x0e\x32>.flexport.shipperexp.shipperdocumentbasicdata.v1.CargoUnitType"\xeb\x01\n#ShipperShippingInstructionContainer\x12\x13\n\x0bseal_number\x18\x01 \x01(\t\x12M\n\tcontainer\x18\x02 \x01(\x0b\x32:.flexport.shipperexp.shipperdocumentbasicdata.v1.Container\x12`\n\x06\x63\x61rgos\x18\x03 \x03(\x0b\x32P.flexport.shipperexp.shipperdocument.v1.ShipperShippingInstructionContainerCargo"\xd9\x02\n(ShipperShippingInstructionContainerCargo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x15product_cargo_enabled\x18\x02 \x01(\x08\x12+\n#marks_and_numbers_on_bill_of_lading\x18\x03 \x01(\t\x12%\n\x1d\x64\x65scription_on_bill_of_lading\x18\x04 \x01(\t\x12O\n\x0btotal_cargo\x18\x05 \x01(\x0b\x32:.flexport.shipperexp.shipperdocumentbasicdata.v1.BaseCargo\x12[\n\x08products\x18\x06 \x03(\x0b\x32I.flexport.shipperexp.shipperdocument.v1.ShipperShippingInstructionProduct"\xb8\x01\n!ShipperShippingInstructionProduct\x12H\n\x07hs_code\x18\x01 \x01(\x0b\x32\x37.flexport.shipperexp.shipperdocumentbasicdata.v1.HsCode\x12I\n\x05\x63\x61rgo\x18\x02 \x01(\x0b\x32:.flexport.shipperexp.shipperdocumentbasicdata.v1.BaseCargoB{\n*com.flexport.shipperexp.shipperdocument.v1B\x1fShipperShippingInstructionProtoP\x01\xea\x02)Flexport::ShipperExp::ShipperDocument::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.shipperexp.shipperdocument.v1.shipper_shipping_instruction_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n*com.flexport.shipperexp.shipperdocument.v1B\037ShipperShippingInstructionProtoP\001\352\002)Flexport::ShipperExp::ShipperDocument::V1"
    _globals["_SHIPPERSHIPPINGINSTRUCTION"]._serialized_start = 266
    _globals["_SHIPPERSHIPPINGINSTRUCTION"]._serialized_end = 678
    _globals["_SHIPPERSHIPPINGINSTRUCTIONCONTENT"]._serialized_start = 681
    _globals["_SHIPPERSHIPPINGINSTRUCTIONCONTENT"]._serialized_end = 1410
    _globals["_SHIPPERSHIPPINGINSTRUCTIONCONTAINER"]._serialized_start = 1413
    _globals["_SHIPPERSHIPPINGINSTRUCTIONCONTAINER"]._serialized_end = 1648
    _globals["_SHIPPERSHIPPINGINSTRUCTIONCONTAINERCARGO"]._serialized_start = 1651
    _globals["_SHIPPERSHIPPINGINSTRUCTIONCONTAINERCARGO"]._serialized_end = 1996
    _globals["_SHIPPERSHIPPINGINSTRUCTIONPRODUCT"]._serialized_start = 1999
    _globals["_SHIPPERSHIPPINGINSTRUCTIONPRODUCT"]._serialized_end = 2183
# @@protoc_insertion_point(module_scope)