# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customs/declaration/gb/v1beta1/import_declaration_item.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nEflexport/customs/declaration/gb/v1beta1/import_declaration_item.proto\x12\'flexport.customs.declaration.gb.v1beta1\x1a@flexport/customs/declaration/gb/v1beta1/addition_deduction.proto\x1aKflexport/customs/declaration/gb/v1beta1/detail_additional_information.proto\x1a<flexport/customs/declaration/gb/v1beta1/involved_party.proto\x1a:flexport/customs/declaration/gb/v1beta1/package_type.proto\x1a?flexport/customs/declaration/gb/v1beta1/previous_document.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x16google/type/date.proto\x1a\x17google/type/money.proto"\xb8\x14\n\x15ImportDeclarationItem\x12\x19\n\x11goods_item_number\x18\x01 \x01(\r\x12\x16\n\x0eprocedure_code\x18\x02 \x01(\t\x12!\n\x19\x61\x64\x64itional_procedure_code\x18\x03 \x03(\t\x12U\n\x12previous_documents\x18\x04 \x03(\x0b\x32\x39.flexport.customs.declaration.gb.v1beta1.PreviousDocument\x12\x64\n\x16\x61\x64\x64itional_information\x18\x05 \x03(\x0b\x32\x44.flexport.customs.declaration.gb.v1beta1.DetailAdditionalInformation\x12[\n\x15\x61\x64\x64itional_references\x18\x06 \x03(\x0b\x32<.flexport.customs.declaration.gb.v1beta1.AdditionalReference\x12\x0b\n\x03ucr\x18\x07 \x01(\t\x12M\n\x08\x65xporter\x18\x08 \x01(\x0b\x32\x36.flexport.customs.declaration.gb.v1beta1.InvolvedPartyH\x00\x88\x01\x01\x12\x33\n\rexporter_eori\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12K\n\x06seller\x18\n \x01(\x0b\x32\x36.flexport.customs.declaration.gb.v1beta1.InvolvedPartyH\x01\x88\x01\x01\x12\x31\n\x0bseller_eori\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12J\n\x05\x62uyer\x18\x0c \x01(\x0b\x32\x36.flexport.customs.declaration.gb.v1beta1.InvolvedPartyH\x02\x88\x01\x01\x12\x30\n\nbuyer_eori\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12v\n!additional_supply_chain_actor_ids\x18\x0e \x03(\x0b\x32K.flexport.customs.declaration.gb.v1beta1.AdditionalSupplyChainActorIdNumber\x12n\n\x14\x61\x64\x64itional_fiscal_id\x18\x0f \x01(\x0b\x32K.flexport.customs.declaration.gb.v1beta1.AdditionalFiscalReferencesIdNumberH\x03\x88\x01\x01\x12P\n\x0ftax_calculation\x18\x10 \x01(\x0b\x32\x37.flexport.customs.declaration.gb.v1beta1.TaxCalculation\x12X\n\x14\x61\x64\x64itions_deductions\x18\x11 \x03(\x0b\x32:.flexport.customs.declaration.gb.v1beta1.AdditionDeduction\x12\x39\n\x13valuation_indicator\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12&\n\nitem_price\x18\x13 \x01(\x0b\x32\x12.google.type.Money\x12m\n\x10valuation_method\x18\x14 \x01(\x0e\x32N.flexport.customs.declaration.gb.v1beta1.ImportDeclarationItem.ValuationMethodH\x04\x88\x01\x01\x12\x30\n\npreference\x18\x15 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12 \n\x18\x64\x65stination_country_code\x18\x18 \x01(\t\x12\x1b\n\x13origin_country_code\x18\x19 \x01(\t\x12\x46\n preferential_origin_country_code\x18\x1a \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x08net_mass\x18\x1b \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x38\n\x13supplementary_units\x18\x1c \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12/\n\ngross_mass\x18\x1d \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x1c\n\x14\x64\x65scription_of_goods\x18\x1e \x01(\t\x12\x45\n\tpackaging\x18\x1f \x03(\x0b\x32\x32.flexport.customs.declaration.gb.v1beta1.Packaging\x12.\n\x08\x63us_code\x18  \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x19\n\x11\x63ommodity_code_cn\x18! \x01(\t\x12:\n\x14\x63ommodity_code_taric\x18" \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x45\n\x1f\x63ommodity_code_taric_additional\x18# \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12>\n\x18national_additional_code\x18$ \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1c\n\x14\x63ontainer_id_numbers\x18% \x03(\t\x12\x14\n\x0cquota_number\x18& \x01(\t\x12\x1d\n\x15nature_of_transaction\x18\' \x01(\t\x12\x19\n\x11statistical_value\x18( \x01(\x02"\xa9\x02\n\x0fValuationMethod\x12\x1c\n\x18VALUATION_METHOD_INVALID\x10\x00\x12&\n"VALUATION_METHOD_TRANSACTION_VALUE\x10\x01\x12\x36\n2VALUATION_METHOD_TRANSACTION_VALUE_IDENTICAL_GOODS\x10\x02\x12\x34\n0VALUATION_METHOD_TRANSACTION_VALUE_SIMILAR_GOODS\x10\x03\x12\x1e\n\x1aVALUATION_METHOD_DEDUCTIVE\x10\x04\x12#\n\x1fVALUATION_METHOD_COMPUTED_VALUE\x10\x05\x12\x1d\n\x19VALUATION_METHOD_FALLBACK\x10\x06\x42\x0b\n\t_exporterB\t\n\x07_sellerB\x08\n\x06_buyerB\x17\n\x15_additional_fiscal_idB\x13\n\x11_valuation_methodJ\x04\x08\x16\x10\x17J\x04\x08\x17\x10\x18"\xf3\x01\n\x13\x41\x64\x64itionalReference\x12\x15\n\rdocument_type\x18\x01 \x01(\t\x12\x1a\n\x12\x64ocument_reference\x18\x02 \x01(\t\x12\x17\n\x0f\x64ocument_status\x18\x03 \x01(\t\x12\x17\n\x0f\x64ocument_reason\x18\x04 \x01(\t\x12\x1e\n\x16issuing_authority_name\x18\x05 \x01(\t\x12\x18\n\x10measurement_unit\x18\x06 \x01(\t\x12\x10\n\x08quantity\x18\x07 \x01(\r\x12+\n\x10\x64\x61te_of_validity\x18\x08 \x01(\x0b\x32\x11.google.type.Date"\xd6\x04\n\x0eTaxCalculation\x12\x62\n\x11method_of_payment\x18\x05 \x03(\x0e\x32G.flexport.customs.declaration.gb.v1beta1.TaxCalculation.MethodOfPayment"\xd9\x03\n\x0fMethodOfPayment\x12\x1d\n\x19METHOD_OF_PAYMENT_INVALID\x10\x00\x12\x17\n\x13METHOD_OF_PAYMENT_A\x10\x01\x12\x17\n\x13METHOD_OF_PAYMENT_B\x10\x02\x12\x17\n\x13METHOD_OF_PAYMENT_C\x10\x03\x12\x17\n\x13METHOD_OF_PAYMENT_D\x10\x04\x12\x17\n\x13METHOD_OF_PAYMENT_E\x10\x05\x12\x17\n\x13METHOD_OF_PAYMENT_H\x10\x06\x12\x17\n\x13METHOD_OF_PAYMENT_M\x10\x07\x12\x17\n\x13METHOD_OF_PAYMENT_N\x10\x08\x12\x17\n\x13METHOD_OF_PAYMENT_O\x10\t\x12\x17\n\x13METHOD_OF_PAYMENT_P\x10\n\x12\x17\n\x13METHOD_OF_PAYMENT_R\x10\x0b\x12\x17\n\x13METHOD_OF_PAYMENT_S\x10\x0c\x12\x17\n\x13METHOD_OF_PAYMENT_T\x10\r\x12\x17\n\x13METHOD_OF_PAYMENT_U\x10\x0e\x12\x17\n\x13METHOD_OF_PAYMENT_V\x10\x0f\x12\x17\n\x13METHOD_OF_PAYMENT_X\x10\x10\x12\x17\n\x13METHOD_OF_PAYMENT_Z\x10\x11J\x04\x08\x01\x10\x05"\x8b\x01\n\tPackaging\x12J\n\x0cpackage_type\x18\x01 \x01(\x0e\x32\x34.flexport.customs.declaration.gb.v1beta1.PackageType\x12\x1a\n\x12number_of_packages\x18\x02 \x01(\r\x12\x16\n\x0eshipping_marks\x18\x03 \x01(\tB]\n+com.flexport.customs.declaration.gb.v1beta1P\x01\xea\x02+Flexport::Customs::Declaration::GB::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customs.declaration.gb.v1beta1.import_declaration_item_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n+com.flexport.customs.declaration.gb.v1beta1P\001\352\002+Flexport::Customs::Declaration::GB::V1Beta1"
    )
    _globals["_IMPORTDECLARATIONITEM"]._serialized_start = 526
    _globals["_IMPORTDECLARATIONITEM"]._serialized_end = 3142
    _globals["_IMPORTDECLARATIONITEM_VALUATIONMETHOD"]._serialized_start = 2753
    _globals["_IMPORTDECLARATIONITEM_VALUATIONMETHOD"]._serialized_end = 3050
    _globals["_ADDITIONALREFERENCE"]._serialized_start = 3145
    _globals["_ADDITIONALREFERENCE"]._serialized_end = 3388
    _globals["_TAXCALCULATION"]._serialized_start = 3391
    _globals["_TAXCALCULATION"]._serialized_end = 3989
    _globals["_TAXCALCULATION_METHODOFPAYMENT"]._serialized_start = 3510
    _globals["_TAXCALCULATION_METHODOFPAYMENT"]._serialized_end = 3983
    _globals["_PACKAGING"]._serialized_start = 3992
    _globals["_PACKAGING"]._serialized_end = 4131
# @@protoc_insertion_point(module_scope)