# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/airprocurement/rates/v1/rate_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n/flexport/airprocurement/rates/v1/rate_api.proto\x12 flexport.airprocurement.rates.v1\x1a\x42\x66lexport/airprocurement/rates/v1/rate_search_term_parameters.proto\x1a\x36\x66lexport/airprocurement/rates/v1/universal_rates.proto"\xa2\x01\n\x10\x46indRatesRequest\x12I\n\x0fterm_parameters\x18\x01 \x01(\x0b\x32\x30.flexport.airprocurement.rates.v1.TermParameters\x12\x1e\n\x16\x65xclude_origin_charges\x18\x02 \x01(\x08\x12#\n\x1b\x65xclude_destination_charges\x18\x03 \x01(\x08"J\n\x11\x46indRatesResponse\x12\x35\n\x05rates\x18\x01 \x03(\x0b\x32&.flexport.airprocurement.rates.v1.Rate"\xa1\x01\n\x0f\x46indRateRequest\x12I\n\x0fterm_parameters\x18\x01 \x01(\x0b\x32\x30.flexport.airprocurement.rates.v1.TermParameters\x12\x1e\n\x16\x65xclude_origin_charges\x18\x02 \x01(\x08\x12#\n\x1b\x65xclude_destination_charges\x18\x03 \x01(\x08"H\n\x10\x46indRateResponse\x12\x34\n\x04rate\x18\x01 \x01(\x0b\x32&.flexport.airprocurement.rates.v1.Rate2\xf2\x01\n\x07RateAPI\x12t\n\tFindRates\x12\x32.flexport.airprocurement.rates.v1.FindRatesRequest\x1a\x33.flexport.airprocurement.rates.v1.FindRatesResponse\x12q\n\x08\x46indRate\x12\x31.flexport.airprocurement.rates.v1.FindRateRequest\x1a\x32.flexport.airprocurement.rates.v1.FindRateResponseB\\\n$com.flexport.airprocurement.rates.v1B\x0cRateApiProtoP\x01\xea\x02#Flexport::AirProcurement::Rates::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.airprocurement.rates.v1.rate_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n$com.flexport.airprocurement.rates.v1B\014RateApiProtoP\001\352\002#Flexport::AirProcurement::Rates::V1"
    )
    _globals["_FINDRATESREQUEST"]._serialized_start = 210
    _globals["_FINDRATESREQUEST"]._serialized_end = 372
    _globals["_FINDRATESRESPONSE"]._serialized_start = 374
    _globals["_FINDRATESRESPONSE"]._serialized_end = 448
    _globals["_FINDRATEREQUEST"]._serialized_start = 451
    _globals["_FINDRATEREQUEST"]._serialized_end = 612
    _globals["_FINDRATERESPONSE"]._serialized_start = 614
    _globals["_FINDRATERESPONSE"]._serialized_end = 686
    _globals["_RATEAPI"]._serialized_start = 689
    _globals["_RATEAPI"]._serialized_end = 931
# @@protoc_insertion_point(module_scope)