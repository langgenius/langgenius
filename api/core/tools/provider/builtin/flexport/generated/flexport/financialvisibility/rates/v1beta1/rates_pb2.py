# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/financialvisibility/rates/v1beta1/rates.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n6flexport/financialvisibility/rates/v1beta1/rates.proto\x12&flexport.financialledger.rates.v1beta1\x1a\x36\x66lexport/financialvisibility/utils/v1beta1/utils.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xaa\x01\n\x0bRateItemDto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12=\n\x04rate\x18\x02 \x01(\x0b\x32/.flexport.financialledger.rates.v1beta1.RateDto\x12N\n\x12\x63ontext_attributes\x18\x03 \x01(\x0b\x32\x32.flexport.financialvisibility.v1beta1.JSONValueDto"F\n\x0fMinimumPriceDto\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x15\n\rcurrency_code\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\t"\x9c\x02\n\x07RateDto\x12\x15\n\rcurrency_code\x18\x01 \x01(\t\x12N\n\rminimum_price\x18\x02 \x01(\x0b\x32\x37.flexport.financialledger.rates.v1beta1.MinimumPriceDto\x12O\n\rformula_value\x18\x03 \x01(\x0b\x32\x36.flexport.financialledger.rates.v1beta1.FormulaRateDtoH\x00\x12P\n\x10\x62reak_rate_value\x18\x04 \x01(\x0b\x32\x34.flexport.financialledger.rates.v1beta1.BreakRateDtoH\x00\x42\x07\n\x05value"\xe7\x01\n\x0e\x46ormulaRateDto\x12\x0f\n\x07\x66ormula\x18\x01 \x01(\t\x12X\n\tconstants\x18\x02 \x03(\x0b\x32\x45.flexport.financialledger.rates.v1beta1.FormulaRateDto.ConstantsEntry\x1aj\n\x0e\x43onstantsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x38.flexport.financialledger.rates.v1beta1.ConstantValueDto:\x02\x38\x01"\xa9\x01\n\x10\x43onstantValueDto\x12V\n\x0cnumber_value\x18\x01 \x01(\x0b\x32>.flexport.financialledger.rates.v1beta1.NumberConstantValueDtoH\x00\x12\x34\n\x0cstring_value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x42\x07\n\x05value"h\n\x16NumberConstantValueDto\x12\x0e\n\x06\x61mount\x18\x01 \x01(\t\x12>\n\x05units\x18\x02 \x03(\x0b\x32/.flexport.financialledger.rates.v1beta1.UnitDto"&\n\x07UnitDto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05power\x18\x02 \x01(\x11"h\n\x0c\x42reakRateDto\x12X\n\x13\x62reak_rate_sections\x18\x01 \x03(\x0b\x32;.flexport.financialledger.rates.v1beta1.BreakRateSectionDto"\xa1\x01\n\x13\x42reakRateSectionDto\x12K\n\x0c\x62reak_ranges\x18\x01 \x03(\x0b\x32\x35.flexport.financialledger.rates.v1beta1.BreakRangeDto\x12=\n\x04rate\x18\x02 \x01(\x0b\x32/.flexport.financialledger.rates.v1beta1.RateDto"\x82\x01\n\rBreakRangeDto\x12\r\n\x05\x62\x61sis\x18\x01 \x01(\t\x12)\n\x03min\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x03max\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0c\n\x04unit\x18\x04 \x01(\tBf\n*com.flexport.financialledger.rates.v1beta1B\nRatesProtoP\x01\xea\x02)Flexport::FinancialLedger::Rates::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.financialvisibility.rates.v1beta1.rates_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n*com.flexport.financialledger.rates.v1beta1B\nRatesProtoP\001\352\002)Flexport::FinancialLedger::Rates::V1Beta1"
    _globals["_FORMULARATEDTO_CONSTANTSENTRY"]._options = None
    _globals["_FORMULARATEDTO_CONSTANTSENTRY"]._serialized_options = b"8\001"
    _globals["_RATEITEMDTO"]._serialized_start = 187
    _globals["_RATEITEMDTO"]._serialized_end = 357
    _globals["_MINIMUMPRICEDTO"]._serialized_start = 359
    _globals["_MINIMUMPRICEDTO"]._serialized_end = 429
    _globals["_RATEDTO"]._serialized_start = 432
    _globals["_RATEDTO"]._serialized_end = 716
    _globals["_FORMULARATEDTO"]._serialized_start = 719
    _globals["_FORMULARATEDTO"]._serialized_end = 950
    _globals["_FORMULARATEDTO_CONSTANTSENTRY"]._serialized_start = 844
    _globals["_FORMULARATEDTO_CONSTANTSENTRY"]._serialized_end = 950
    _globals["_CONSTANTVALUEDTO"]._serialized_start = 953
    _globals["_CONSTANTVALUEDTO"]._serialized_end = 1122
    _globals["_NUMBERCONSTANTVALUEDTO"]._serialized_start = 1124
    _globals["_NUMBERCONSTANTVALUEDTO"]._serialized_end = 1228
    _globals["_UNITDTO"]._serialized_start = 1230
    _globals["_UNITDTO"]._serialized_end = 1268
    _globals["_BREAKRATEDTO"]._serialized_start = 1270
    _globals["_BREAKRATEDTO"]._serialized_end = 1374
    _globals["_BREAKRATESECTIONDTO"]._serialized_start = 1377
    _globals["_BREAKRATESECTIONDTO"]._serialized_end = 1538
    _globals["_BREAKRANGEDTO"]._serialized_start = 1541
    _globals["_BREAKRANGEDTO"]._serialized_end = 1671
# @@protoc_insertion_point(module_scope)