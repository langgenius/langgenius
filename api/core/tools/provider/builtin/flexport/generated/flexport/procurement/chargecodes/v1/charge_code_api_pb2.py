# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/procurement/chargecodes/v1/charge_code_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n9flexport/procurement/chargecodes/v1/charge_code_api.proto\x12#flexport.procurement.chargecodes.v1\x1a\x33\x66lexport/procurement/rates/v1/universal_rates.proto\x1a/flexport/procurement/rates/write/v1/rates.proto"i\n\x15\x46indChargeCodeRequest\x12;\n\x06source\x18\x01 \x01(\x0e\x32+.flexport.procurement.rates.write.v1.Source\x12\x13\n\x0b\x63harge_name\x18\x02 \x01(\t"X\n\x16\x46indChargeCodeResponse\x12>\n\x0b\x63harge_code\x18\x01 \x01(\x0b\x32).flexport.procurement.rates.v1.ChargeCode"U\n\x16\x46indChargeCodesRequest\x12;\n\x06source\x18\x01 \x01(\x0e\x32+.flexport.procurement.rates.write.v1.Source"Z\n\x17\x46indChargeCodesResponse\x12?\n\x0c\x63harge_codes\x18\x01 \x03(\x0b\x32).flexport.procurement.rates.v1.ChargeCode2\xaa\x02\n\rChargeCodeAPI\x12\x89\x01\n\x0e\x46indChargeCode\x12:.flexport.procurement.chargecodes.v1.FindChargeCodeRequest\x1a;.flexport.procurement.chargecodes.v1.FindChargeCodeResponse\x12\x8c\x01\n\x0f\x46indChargeCodes\x12;.flexport.procurement.chargecodes.v1.FindChargeCodesRequest\x1a<.flexport.procurement.chargecodes.v1.FindChargeCodesResponseB?\n\'com.flexport.procurement.chargecodes.v1B\x12\x43hargeCodeApiProtoP\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.procurement.chargecodes.v1.charge_code_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n'com.flexport.procurement.chargecodes.v1B\022ChargeCodeApiProtoP\001"
    _globals["_FINDCHARGECODEREQUEST"]._serialized_start = 200
    _globals["_FINDCHARGECODEREQUEST"]._serialized_end = 305
    _globals["_FINDCHARGECODERESPONSE"]._serialized_start = 307
    _globals["_FINDCHARGECODERESPONSE"]._serialized_end = 395
    _globals["_FINDCHARGECODESREQUEST"]._serialized_start = 397
    _globals["_FINDCHARGECODESREQUEST"]._serialized_end = 482
    _globals["_FINDCHARGECODESRESPONSE"]._serialized_start = 484
    _globals["_FINDCHARGECODESRESPONSE"]._serialized_end = 574
    _globals["_CHARGECODEAPI"]._serialized_start = 577
    _globals["_CHARGECODEAPI"]._serialized_end = 875
# @@protoc_insertion_point(module_scope)