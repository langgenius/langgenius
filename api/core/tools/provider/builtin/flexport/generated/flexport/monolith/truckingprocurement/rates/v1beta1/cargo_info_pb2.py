# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/truckingprocurement/rates/v1beta1/cargo_info.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nDflexport/monolith/truckingprocurement/rates/v1beta1/cargo_info.proto\x12\x33\x66lexport.monolith.truckingprocurement.rates.v1beta1"\x9d\x01\n\x0f\x43\x61rgoDimensions\x12[\n\x04unit\x18\x01 \x01(\x0e\x32M.flexport.monolith.truckingprocurement.rates.v1beta1.TruckingRateUnitDistance\x12\x0e\n\x06length\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r"x\n\x0b\x43\x61rgoWeight\x12Y\n\x04unit\x18\x01 \x01(\x0e\x32K.flexport.monolith.truckingprocurement.rates.v1beta1.TruckingRateUnitWeight\x12\x0e\n\x06weight\x18\x02 \x01(\r"\xc8\x02\n\x13\x43\x61rgoInfoCollection\x12P\n\x06weight\x18\x01 \x01(\x0b\x32@.flexport.monolith.truckingprocurement.rates.v1beta1.CargoWeight\x12X\n\ndimensions\x18\x02 \x01(\x0b\x32\x44.flexport.monolith.truckingprocurement.rates.v1beta1.CargoDimensions\x12h\n\rcargo_element\x18\x03 \x01(\x0e\x32Q.flexport.monolith.truckingprocurement.rates.v1beta1.TruckingRateUnitCargoElement\x12\x1b\n\x13\x63\x61rgo_element_count\x18\x04 \x01(\r"u\n\tCargoInfo\x12h\n\x16\x63\x61rgo_info_collections\x18\x01 \x03(\x0b\x32H.flexport.monolith.truckingprocurement.rates.v1beta1.CargoInfoCollection*\x95\x01\n\x18TruckingRateUnitDistance\x12\'\n#TRUCKING_RATE_UNIT_DISTANCE_INVALID\x10\x00\x12*\n&TRUCKING_RATE_UNIT_DISTANCE_CENTIMETER\x10\x01\x12$\n TRUCKING_RATE_UNIT_DISTANCE_INCH\x10\x02*\x83\x01\n\x16TruckingRateUnitWeight\x12%\n!TRUCKING_RATE_UNIT_WEIGHT_INVALID\x10\x00\x12 \n\x1cTRUCKING_RATE_UNIT_WEIGHT_LB\x10\x01\x12 \n\x1cTRUCKING_RATE_UNIT_WEIGHT_KG\x10\x02*\xd6\x01\n\x1cTruckingRateUnitCargoElement\x12,\n(TRUCKING_RATE_UNIT_CARGO_ELEMENT_INVALID\x10\x00\x12+\n\'TRUCKING_RATE_UNIT_CARGO_ELEMENT_CARTON\x10\x01\x12.\n*TRUCKING_RATE_UNIT_CARGO_ELEMENT_CONTAINER\x10\x02\x12+\n\'TRUCKING_RATE_UNIT_CARGO_ELEMENT_PALLET\x10\x03\x42\x87\x01\n7com.flexport.monolith.truckingprocurement.rates.v1beta1B\x10RateRequestCargoP\x01\xea\x02\x37\x46lexport::Monolith::TruckingProcurement::Rates::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.truckingprocurement.rates.v1beta1.cargo_info_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n7com.flexport.monolith.truckingprocurement.rates.v1beta1B\020RateRequestCargoP\001\352\0027Flexport::Monolith::TruckingProcurement::Rates::V1Beta1"
    _globals["_TRUCKINGRATEUNITDISTANCE"]._serialized_start = 858
    _globals["_TRUCKINGRATEUNITDISTANCE"]._serialized_end = 1007
    _globals["_TRUCKINGRATEUNITWEIGHT"]._serialized_start = 1010
    _globals["_TRUCKINGRATEUNITWEIGHT"]._serialized_end = 1141
    _globals["_TRUCKINGRATEUNITCARGOELEMENT"]._serialized_start = 1144
    _globals["_TRUCKINGRATEUNITCARGOELEMENT"]._serialized_end = 1358
    _globals["_CARGODIMENSIONS"]._serialized_start = 126
    _globals["_CARGODIMENSIONS"]._serialized_end = 283
    _globals["_CARGOWEIGHT"]._serialized_start = 285
    _globals["_CARGOWEIGHT"]._serialized_end = 405
    _globals["_CARGOINFOCOLLECTION"]._serialized_start = 408
    _globals["_CARGOINFOCOLLECTION"]._serialized_end = 736
    _globals["_CARGOINFO"]._serialized_start = 738
    _globals["_CARGOINFO"]._serialized_end = 855
# @@protoc_insertion_point(module_scope)