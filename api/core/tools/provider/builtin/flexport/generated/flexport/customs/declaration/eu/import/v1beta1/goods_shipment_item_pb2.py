# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customs/declaration/eu/import/v1beta1/goods_shipment_item.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nHflexport/customs/declaration/eu/import/v1beta1/goods_shipment_item.proto\x12.flexport.customs.declaration.eu.import.v1beta1\x1aGflexport/customs/declaration/eu/common/v1beta1/addition_deduction.proto\x1a?flexport/customs/declaration/eu/common/v1beta1/additional.proto\x1a\x42\x66lexport/customs/declaration/eu/common/v1beta1/authorisation.proto\x1a\x43\x66lexport/customs/declaration/eu/common/v1beta1/commodity_code.proto\x1a>flexport/customs/declaration/eu/common/v1beta1/documents.proto\x1a=flexport/customs/declaration/eu/common/v1beta1/duty_tax.proto\x1a\x45\x66lexport/customs/declaration/eu/common/v1beta1/involved_parties.proto\x1a>flexport/customs/declaration/eu/common/v1beta1/packaging.proto\x1a\x16google/type/date.proto\x1a\x17google/type/money.proto"\x90\x16\n\x11GoodsShipmentItem\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12^\n\tprocedure\x18\x02 \x01(\x0b\x32K.flexport.customs.declaration.eu.import.v1beta1.GoodsShipmentItem.Procedure\x12\x1c\n\x14\x61\x64\x64itional_procedure\x18\x03 \x01(\t\x12[\n\x11previous_document\x18\x04 \x03(\x0b\x32@.flexport.customs.declaration.eu.common.v1beta1.PreviousDocument\x12\x65\n\x16\x61\x64\x64itional_information\x18\x05 \x03(\x0b\x32\x45.flexport.customs.declaration.eu.common.v1beta1.AdditionalInformation\x12`\n\x14supporting_documents\x18\x06 \x03(\x0b\x32\x42.flexport.customs.declaration.eu.common.v1beta1.SupportingDocument\x12\x62\n\x15\x61\x64\x64itional_references\x18\x07 \x03(\x0b\x32\x43.flexport.customs.declaration.eu.common.v1beta1.AdditionalReference\x12^\n\x13transport_documents\x18\x08 \x03(\x0b\x32\x41.flexport.customs.declaration.eu.common.v1beta1.TransportDocument\x12$\n\x1cunique_consignment_reference\x18\t \x01(\t\x12T\n\rauthorisation\x18\x0e \x01(\x0b\x32=.flexport.customs.declaration.eu.common.v1beta1.Authorisation\x12J\n\x08\x65xporter\x18\x0f \x01(\x0b\x32\x38.flexport.customs.declaration.eu.common.v1beta1.Exporter\x12J\n\x08importer\x18\x10 \x01(\x0b\x32\x38.flexport.customs.declaration.eu.common.v1beta1.Importer\x12\x46\n\x06seller\x18\x11 \x01(\x0b\x32\x36.flexport.customs.declaration.eu.common.v1beta1.Seller\x12\x44\n\x05\x62uyer\x18\x12 \x01(\x0b\x32\x35.flexport.customs.declaration.eu.common.v1beta1.Buyer\x12r\n\x1e\x61\x64\x64itional_supply_chain_actors\x18\x13 \x03(\x0b\x32J.flexport.customs.declaration.eu.common.v1beta1.AdditionalSupplyChainActor\x12o\n\x1c\x61\x64\x64itional_fiscal_references\x18\x14 \x03(\x0b\x32I.flexport.customs.declaration.eu.common.v1beta1.AdditionalFiscalReference\x12Q\n\x10\x64uties_and_taxes\x18\x15 \x03(\x0b\x32\x37.flexport.customs.declaration.eu.common.v1beta1.DutyTax\x12\x63\n\x18\x61\x64\x64itions_and_deductions\x18\x16 \x03(\x0b\x32\x41.flexport.customs.declaration.eu.common.v1beta1.AdditionDeduction\x12\x1b\n\x13valuation_indicator\x18\x17 \x01(\t\x12\x30\n\x14item_amount_invoiced\x18\x18 \x01(\x0b\x32\x12.google.type.Money\x12k\n\x10valuation_method\x18\x19 \x01(\x0e\x32Q.flexport.customs.declaration.eu.import.v1beta1.GoodsShipmentItem.ValuationMethod\x12\x12\n\npreference\x18\x1a \x01(\t\x12(\n\x0cpostal_value\x18\x1b \x01(\x0b\x32\x12.google.type.Money\x12+\n\x0fintrinsic_value\x18\x1c \x01(\x0b\x32\x12.google.type.Money\x12;\n\x1ftransport_insurance_destination\x18\x1d \x01(\x0b\x32\x12.google.type.Money\x12\x32\n\x16total_duties_and_taxes\x18\x1e \x01(\x0b\x32\x12.google.type.Money\x12-\n\x12\x64\x61te_of_acceptance\x18\x1f \x01(\x0b\x32\x11.google.type.Date\x12\x1e\n\x16\x63ountry_of_destination\x18  \x01(\t\x12\x1d\n\x15region_of_destination\x18! \x01(\t\x12\x1b\n\x13\x63ountry_of_dispatch\x18" \x01(\t\x12\x19\n\x11\x63ountry_of_origin\x18# \x01(\t\x12&\n\x1e\x63ountry_of_preferential_origin\x18$ \x01(\t\x12\x10\n\x08net_mass\x18\n \x01(\x01\x12\x1b\n\x13supplementary_units\x18\x0b \x01(\t\x12\x12\n\ngross_mass\x18\x0c \x01(\x01\x12\x1c\n\x14\x64\x65scription_of_goods\x18\r \x01(\t\x12L\n\tpackaging\x18% \x03(\x0b\x32\x39.flexport.customs.declaration.eu.common.v1beta1.Packaging\x12\x10\n\x08\x63us_code\x18& \x01(\t\x12U\n\x0e\x63ommodity_code\x18\' \x01(\x0b\x32=.flexport.customs.declaration.eu.common.v1beta1.CommodityCode\x12\x1a\n\x12quota_order_number\x18( \x01(\t\x12\x1d\n\x15nature_of_transaction\x18) \x01(\r\x12\x19\n\x11statistical_value\x18* \x01(\x01\x1a\x44\n\tProcedure\x12\x1b\n\x13requested_procedure\x18\x01 \x01(\t\x12\x1a\n\x12previous_procedure\x18\x02 \x01(\t"\xa9\x02\n\x0fValuationMethod\x12\x1c\n\x18VALUATION_METHOD_INVALID\x10\x00\x12&\n"VALUATION_METHOD_TRANSACTION_VALUE\x10\x01\x12\x36\n2VALUATION_METHOD_TRANSACTION_VALUE_IDENTICAL_GOODS\x10\x02\x12\x34\n0VALUATION_METHOD_TRANSACTION_VALUE_SIMILAR_GOODS\x10\x03\x12\x1e\n\x1aVALUATION_METHOD_DEDUCTIVE\x10\x04\x12#\n\x1fVALUATION_METHOD_COMPUTED_VALUE\x10\x05\x12\x1d\n\x19VALUATION_METHOD_FALLBACK\x10\x06\x42m\n3com.flexport.customs.declaration.eu.imports.v1beta1P\x01\xea\x02\x33\x46lexport::Customs::Declaration::EU::Import::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customs.declaration.eu.import.v1beta1.goods_shipment_item_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n3com.flexport.customs.declaration.eu.imports.v1beta1P\001\352\0023Flexport::Customs::Declaration::EU::Import::V1Beta1"
    _globals["_GOODSSHIPMENTITEM"]._serialized_start = 711
    _globals["_GOODSSHIPMENTITEM"]._serialized_end = 3543
    _globals["_GOODSSHIPMENTITEM_PROCEDURE"]._serialized_start = 3175
    _globals["_GOODSSHIPMENTITEM_PROCEDURE"]._serialized_end = 3243
    _globals["_GOODSSHIPMENTITEM_VALUATIONMETHOD"]._serialized_start = 3246
    _globals["_GOODSSHIPMENTITEM_VALUATIONMETHOD"]._serialized_end = 3543
# @@protoc_insertion_point(module_scope)