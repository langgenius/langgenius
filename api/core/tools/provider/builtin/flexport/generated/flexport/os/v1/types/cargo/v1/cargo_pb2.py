# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/os/v1/types/cargo/v1/cargo.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n)flexport/os/v1/types/cargo/v1/cargo.proto\x12\x1d\x66lexport.os.v1.types.cargo.v1*\x9f\x04\n\tCargoUnit\x12\x16\n\x12\x43\x41RGO_UNIT_INVALID\x10\x00\x12\x15\n\x11\x43\x41RGO_UNIT_PALLET\x10\x01\x12\x15\n\x11\x43\x41RGO_UNIT_CARTON\x10\x02\x12\x12\n\x0e\x43\x41RGO_UNIT_BAG\x10\x03\x12\x13\n\x0f\x43\x41RGO_UNIT_BALE\x10\x04\x12\x15\n\x11\x43\x41RGO_UNIT_BARREL\x10\x05\x12\x14\n\x10\x43\x41RGO_UNIT_CRATE\x10\x06\x12\x13\n\x0f\x43\x41RGO_UNIT_ROLL\x10\x07\x12!\n\x1d\x43\x41RGO_UNIT_ISO_6346_CONTAINER\x10\x08\x12\x12\n\x0e\x43\x41RGO_UNIT_ULD\x10\t\x12\x16\n\x12\x43\x41RGO_UNIT_PRODUCT\x10\n\x12\x16\n\x12\x43\x41RGO_UNIT_PACKAGE\x10\x0b\x12\x12\n\x0e\x43\x41RGO_UNIT_BOX\x10\x0c\x12\x13\n\x0f\x43\x41RGO_UNIT_DRUM\x10\r\x12\x15\n\x11\x43\x41RGO_UNIT_BUNDLE\x10\x0e\x12\x13\n\x0f\x43\x41RGO_UNIT_BULK\x10\x0f\x12\x13\n\x0f\x43\x41RGO_UNIT_TOTE\x10\x10\x12\x13\n\x0f\x43\x41RGO_UNIT_SKID\x10\x11\x12\x14\n\x10\x43\x41RGO_UNIT_PIECE\x10\x12\x12\x13\n\x0f\x43\x41RGO_UNIT_CASE\x10\x13\x12\x13\n\x0f\x43\x41RGO_UNIT_PAIL\x10\x14\x12\x12\n\x0e\x43\x41RGO_UNIT_SET\x10\x15\x12\x12\n\x0e\x43\x41RGO_UNIT_BIN\x10\x16\x12\x13\n\x0f\x43\x41RGO_UNIT_SACK\x10\x17*\x8b\x02\n\x0f\x43\x61rgoWeightUnit\x12\x1d\n\x19\x43\x41RGO_WEIGHT_UNIT_INVALID\x10\x00\x12\x1e\n\x1a\x43\x41RGO_WEIGHT_UNIT_KILOGRAM\x10\x01\x12\x1a\n\x16\x43\x41RGO_WEIGHT_UNIT_GRAM\x10\x02\x12\x1b\n\x17\x43\x41RGO_WEIGHT_UNIT_POUND\x10\x03\x12\x1b\n\x17\x43\x41RGO_WEIGHT_UNIT_OUNCE\x10\x04\x12\x1f\n\x1b\x43\x41RGO_WEIGHT_UNIT_SHORT_TON\x10\x05\x12\x1e\n\x1a\x43\x41RGO_WEIGHT_UNIT_LONG_TON\x10\x06\x12"\n\x1e\x43\x41RGO_WEIGHT_UNIT_METRIC_TONNE\x10\x07*\xbf\x01\n\x13\x43\x61rgoDimensionsUnit\x12!\n\x1d\x43\x41RGO_DIMENSIONS_UNIT_INVALID\x10\x00\x12\x1f\n\x1b\x43\x41RGO_DIMENSIONS_UNIT_METER\x10\x01\x12$\n CARGO_DIMENSIONS_UNIT_CENTIMETER\x10\x02\x12\x1e\n\x1a\x43\x41RGO_DIMENSIONS_UNIT_INCH\x10\x03\x12\x1e\n\x1a\x43\x41RGO_DIMENSIONS_UNIT_FOOT\x10\x04*u\n\x0f\x43\x61rgoVolumeUnit\x12\x1d\n\x19\x43\x41RGO_VOLUME_UNIT_INVALID\x10\x00\x12!\n\x1d\x43\x41RGO_VOLUME_UNIT_CUBIC_METER\x10\x01\x12 \n\x1c\x43\x41RGO_VOLUME_UNIT_CUBIC_FOOT\x10\x02*\xdc\x02\n\x14Iso6346ContainerSize\x12"\n\x1eISO6346_CONTAINER_SIZE_INVALID\x10\x00\x12$\n ISO6346_CONTAINER_SIZE_TWENTY_FT\x10\x01\x12\'\n#ISO6346_CONTAINER_SIZE_TWENTY_FT_HC\x10\x02\x12#\n\x1fISO6346_CONTAINER_SIZE_FORTY_FT\x10\x03\x12&\n"ISO6346_CONTAINER_SIZE_FORTY_FT_HC\x10\x04\x12+\n\'ISO6346_CONTAINER_SIZE_FORTY_FIVE_FT_HC\x10\x05\x12)\n%ISO6346_CONTAINER_SIZE_FIFTY_THREE_FT\x10\x06\x12,\n(ISO6346_CONTAINER_SIZE_FIFTY_THREE_FT_HC\x10\x07*\xf6\x02\n\x14Iso6346ContainerType\x12"\n\x1eISO6346_CONTAINER_TYPE_INVALID\x10\x00\x12\x1e\n\x1aISO6346_CONTAINER_TYPE_DRY\x10\x01\x12$\n ISO6346_CONTAINER_TYPE_FLAT_RACK\x10\x02\x12#\n\x1fISO6346_CONTAINER_TYPE_HEADLOAD\x10\x03\x12\x1f\n\x1bISO6346_CONTAINER_TYPE_OPEN\x10\x04\x12!\n\x1dISO6346_CONTAINER_TYPE_REEFER\x10\x05\x12\x1f\n\x1bISO6346_CONTAINER_TYPE_TANK\x10\x06\x12%\n!ISO6346_CONTAINER_TYPE_VENTILATED\x10\x07\x12\x1f\n\x1bISO6346_CONTAINER_TYPE_BULK\x10\x08\x12"\n\x1eISO6346_CONTAINER_TYPE_SPECIAL\x10\tBV\n!com.flexport.os.v1.types.cargo.v1B\nCargoProtoP\x01\xea\x02"Flexport::OS::V1::Types::Cargo::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.os.v1.types.cargo.v1.cargo_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b'\n!com.flexport.os.v1.types.cargo.v1B\nCargoProtoP\001\352\002"Flexport::OS::V1::Types::Cargo::V1'
    )
    _globals["_CARGOUNIT"]._serialized_start = 77
    _globals["_CARGOUNIT"]._serialized_end = 620
    _globals["_CARGOWEIGHTUNIT"]._serialized_start = 623
    _globals["_CARGOWEIGHTUNIT"]._serialized_end = 890
    _globals["_CARGODIMENSIONSUNIT"]._serialized_start = 893
    _globals["_CARGODIMENSIONSUNIT"]._serialized_end = 1084
    _globals["_CARGOVOLUMEUNIT"]._serialized_start = 1086
    _globals["_CARGOVOLUMEUNIT"]._serialized_end = 1203
    _globals["_ISO6346CONTAINERSIZE"]._serialized_start = 1206
    _globals["_ISO6346CONTAINERSIZE"]._serialized_end = 1554
    _globals["_ISO6346CONTAINERTYPE"]._serialized_start = 1557
    _globals["_ISO6346CONTAINERTYPE"]._serialized_end = 1931
# @@protoc_insertion_point(module_scope)