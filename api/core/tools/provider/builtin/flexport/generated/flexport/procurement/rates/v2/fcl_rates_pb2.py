# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/procurement/rates/v2/fcl_rates.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n-flexport/procurement/rates/v2/fcl_rates.proto\x12\x1d\x66lexport.procurement.rates.v2"I\n\x07\x46\x63lRate\x12>\n\nrate_items\x18\x01 \x03(\x0b\x32*.flexport.procurement.rates.v2.FclRateItem"\xcc\x02\n\x0b\x46\x63lRateItem\x12\x1c\n\x14\x66lexport_charge_name\x18\x01 \x01(\t\x12\x1a\n\x12source_charge_name\x18\x02 \x01(\t\x12\x18\n\x10\x63harge_group_fid\x18\x03 \x01(\t\x12\x45\n\x12included_structure\x18\x04 \x01(\x0b\x32\'.flexport.procurement.rates.v2.IncludedH\x00\x12=\n\x0e\x66lat_structure\x18\x05 \x01(\x0b\x32#.flexport.procurement.rates.v2.FlatH\x00\x12N\n\x17per_container_structure\x18\x06 \x01(\x0b\x32+.flexport.procurement.rates.v2.PerContainerH\x00\x42\x13\n\x11pricing_structure"\n\n\x08Included"=\n\x04\x46lat\x12\x35\n\x06\x61mount\x18\x01 \x01(\x0b\x32%.flexport.procurement.rates.v2.Amount"\x94\x01\n\x0cPerContainer\x12\x35\n\x06\x61mount\x18\x01 \x01(\x0b\x32%.flexport.procurement.rates.v2.Amount\x12M\n\x0e\x63ontainer_type\x18\x02 \x01(\x0e\x32\x35.flexport.procurement.rates.v2.SupportedContainerType"/\n\x06\x41mount\x12\x0e\n\x06micros\x18\x01 \x01(\x03\x12\x15\n\rcurrency_code\x18\x02 \x01(\t*\xd2\x01\n\x07Variant\x12\x13\n\x0fVARIANT_INVALID\x10\x00\x12 \n\x1cVARIANT_NON_ARB_BASE_FREIGHT\x10\x01\x12\x1c\n\x18VARIANT_ARB_BASE_FREIGHT\x10\x02\x12%\n!VARIANT_PART_OF_FREIGHT_SURCHARGE\x10\x03\x12"\n\x1eVARIANT_ORIGIN_LOCAL_SURCHARGE\x10\x04\x12\'\n#VARIANT_DESTINATION_LOCAL_SURCHARGE\x10\x05*\xc8\x01\n\x16SupportedContainerType\x12$\n SUPPORTED_CONTAINER_TYPE_INVALID\x10\x00\x12\x1f\n\x1bSUPPORTED_CONTAINER_TYPE_20\x10\x01\x12\x1f\n\x1bSUPPORTED_CONTAINER_TYPE_40\x10\x02\x12"\n\x1eSUPPORTED_CONTAINER_TYPE_40_HC\x10\x03\x12"\n\x1eSUPPORTED_CONTAINER_TYPE_45_HC\x10\x04\x42R\n!com.flexport.procurement.rates.v2B\x08\x46\x63lRatesP\x01\xea\x02 Flexport::Procurement::Rates::V2b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.procurement.rates.v2.fcl_rates_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n!com.flexport.procurement.rates.v2B\010FclRatesP\001\352\002 Flexport::Procurement::Rates::V2"
    )
    _globals["_VARIANT"]._serialized_start = 766
    _globals["_VARIANT"]._serialized_end = 976
    _globals["_SUPPORTEDCONTAINERTYPE"]._serialized_start = 979
    _globals["_SUPPORTEDCONTAINERTYPE"]._serialized_end = 1179
    _globals["_FCLRATE"]._serialized_start = 80
    _globals["_FCLRATE"]._serialized_end = 153
    _globals["_FCLRATEITEM"]._serialized_start = 156
    _globals["_FCLRATEITEM"]._serialized_end = 488
    _globals["_INCLUDED"]._serialized_start = 490
    _globals["_INCLUDED"]._serialized_end = 500
    _globals["_FLAT"]._serialized_start = 502
    _globals["_FLAT"]._serialized_end = 563
    _globals["_PERCONTAINER"]._serialized_start = 566
    _globals["_PERCONTAINER"]._serialized_end = 714
    _globals["_AMOUNT"]._serialized_start = 716
    _globals["_AMOUNT"]._serialized_end = 763
# @@protoc_insertion_point(module_scope)