# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/shipperexp/shipperdocument/digitization/v1beta1/shipper_s_letter_of_instruction.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n^flexport/shipperexp/shipperdocument/digitization/v1beta1/shipper_s_letter_of_instruction.proto\x12\x38\x66lexport.shipperexp.shipperdocument.digitization.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\xa1\x01\n ShippersLetterOfInstructionEvent\x12}\n\x1eshippers_letter_of_instruction\x18\x01 \x01(\x0b\x32U.flexport.shipperexp.shipperdocument.digitization.v1beta1.ShippersLetterOfInstruction"\xb5\t\n\x1bShippersLetterOfInstruction\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0bshipment_id\x18\x02 \x01(\x05\x12\x13\n\x0b\x64ocument_id\x18\x03 \x01(\x03\x12"\n\x15is_routed_transaction\x18\x0b \x01(\x08H\x00\x88\x01\x01\x12"\n\x15is_hazardous_material\x18\x0c \x01(\x08H\x01\x88\x01\x01\x12#\n\x16is_to_be_sold_en_route\x18\r \x01(\x08H\x02\x88\x01\x01\x12\x1f\n\x12is_related_parties\x18\x0e \x01(\x08H\x03\x88\x01\x01\x12\x16\n\tun_number\x18\x15 \x01(\tH\x04\x88\x01\x01\x12\x18\n\x0binbond_type\x18\x16 \x01(\tH\x05\x88\x01\x01\x12S\n\x05usppi\x18\x1f \x01(\x0b\x32?.flexport.shipperexp.shipperdocument.digitization.v1beta1.UsppiH\x06\x88\x01\x01\x12$\n\x17usppi_company_entity_id\x18  \x01(\x05H\x07\x88\x01\x01\x12l\n\x12ultimate_consignee\x18! \x01(\x0b\x32K.flexport.shipperexp.shipperdocument.digitization.v1beta1.UltimateConsigneeH\x08\x88\x01\x01\x12\x31\n$ultimate_consignee_company_entity_id\x18" \x01(\x05H\t\x88\x01\x01\x12\x63\n\x11\x65xport_line_items\x18) \x03(\x0b\x32H.flexport.shipperexp.shipperdocument.digitization.v1beta1.ExportLineItem\x12\x1f\n\x12update_reason_code\x18\x33 \x01(\tH\n\x88\x01\x01\x12\x1a\n\rupdate_reason\x18\x34 \x01(\tH\x0b\x88\x01\x01\x12.\n\nupdated_at\x18\x35 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\nupdated_by\x18\x36 \x01(\x05H\x0c\x88\x01\x01\x12\x14\n\x0cis_confirmed\x18\x37 \x01(\x08\x12\x19\n\x0c\x63onfirmed_by\x18\x38 \x01(\x05H\r\x88\x01\x01\x12\x14\n\x07version\x18\x39 \x01(\x05H\x0e\x88\x01\x01\x12\x13\n\x0bis_archived\x18: \x01(\x08\x42\x18\n\x16_is_routed_transactionB\x18\n\x16_is_hazardous_materialB\x19\n\x17_is_to_be_sold_en_routeB\x15\n\x13_is_related_partiesB\x0c\n\n_un_numberB\x0e\n\x0c_inbond_typeB\x08\n\x06_usppiB\x1a\n\x18_usppi_company_entity_idB\x15\n\x13_ultimate_consigneeB\'\n%_ultimate_consignee_company_entity_idB\x15\n\x13_update_reason_codeB\x10\n\x0e_update_reasonB\r\n\x0b_updated_byB\x0f\n\r_confirmed_byB\n\n\x08_version"\xbd\x02\n\x05Usppi\x12\x17\n\nusppi_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nusppi_city\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\rusppi_country\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0cusppi_line_1\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x19\n\x0cusppi_line_2\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1e\n\x11usppi_postal_code\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x18\n\x0busppi_state\x18\x07 \x01(\tH\x06\x88\x01\x01\x42\r\n\x0b_usppi_nameB\r\n\x0b_usppi_cityB\x10\n\x0e_usppi_countryB\x0f\n\r_usppi_line_1B\x0f\n\r_usppi_line_2B\x14\n\x12_usppi_postal_codeB\x0e\n\x0c_usppi_state"\xb1\x03\n\x11UltimateConsignee\x12\x1b\n\x0e\x63onsignee_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0e\x63onsignee_city\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11\x63onsignee_country\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1d\n\x10\x63onsignee_line_1\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1d\n\x10\x63onsignee_line_2\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1b\n\x0e\x63onsignee_type\x18\x06 \x01(\tH\x05\x88\x01\x01\x12"\n\x15\x63onsignee_postal_code\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x1c\n\x0f\x63onsignee_state\x18\x08 \x01(\tH\x07\x88\x01\x01\x42\x11\n\x0f_consignee_nameB\x11\n\x0f_consignee_cityB\x14\n\x12_consignee_countryB\x13\n\x11_consignee_line_1B\x13\n\x11_consignee_line_2B\x11\n\x0f_consignee_typeB\x18\n\x16_consignee_postal_codeB\x12\n\x10_consignee_state"\xa4\x04\n\x0e\x45xportLineItem\x12\x18\n\x0b\x65xport_code\x18\x01 \x01(\tH\x00\x88\x01\x01\x12*\n\x1d\x65xport_control_classification\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0bis_domestic\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1e\n\x11license_authority\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x19\n\x0clicense_code\x18\x05 \x01(\tH\x04\x88\x01\x01\x12 \n\x13product_description\x18\x06 \x01(\tH\x05\x88\x01\x01\x12!\n\x14product_gross_weight\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x1a\n\rproduct_value\x18\x08 \x01(\tH\x07\x88\x01\x01\x12 \n\x13schedule_b_quantity\x18\t \x01(\tH\x08\x88\x01\x01\x12\x1c\n\x0fschedule_b_code\x18\n \x01(\tH\t\x88\x01\x01\x42\x0e\n\x0c_export_codeB \n\x1e_export_control_classificationB\x0e\n\x0c_is_domesticB\x14\n\x12_license_authorityB\x0f\n\r_license_codeB\x16\n\x14_product_descriptionB\x17\n\x15_product_gross_weightB\x10\n\x0e_product_valueB\x16\n\x14_schedule_b_quantityB\x12\n\x10_schedule_b_codeB\xa1\x01\n<com.flexport.shipperexp.shipperdocument.digitization.v1beta1B ShippersLetterOfInstructionProtoP\x01\xea\x02<Flexport::ShipperExp::ShipperDocument::Digitization::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.shipperexp.shipperdocument.digitization.v1beta1.shipper_s_letter_of_instruction_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n<com.flexport.shipperexp.shipperdocument.digitization.v1beta1B ShippersLetterOfInstructionProtoP\001\352\002<Flexport::ShipperExp::ShipperDocument::Digitization::V1Beta1"
    _globals["_SHIPPERSLETTEROFINSTRUCTIONEVENT"]._serialized_start = 190
    _globals["_SHIPPERSLETTEROFINSTRUCTIONEVENT"]._serialized_end = 351
    _globals["_SHIPPERSLETTEROFINSTRUCTION"]._serialized_start = 354
    _globals["_SHIPPERSLETTEROFINSTRUCTION"]._serialized_end = 1559
    _globals["_USPPI"]._serialized_start = 1562
    _globals["_USPPI"]._serialized_end = 1879
    _globals["_ULTIMATECONSIGNEE"]._serialized_start = 1882
    _globals["_ULTIMATECONSIGNEE"]._serialized_end = 2315
    _globals["_EXPORTLINEITEM"]._serialized_start = 2318
    _globals["_EXPORTLINEITEM"]._serialized_end = 2866
# @@protoc_insertion_point(module_scope)