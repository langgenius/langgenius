# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/catalog/offering/cartage/v1/cartage.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n2flexport/catalog/offering/cartage/v1/cartage.proto\x12$flexport.catalog.offering.cartage.v1\x1a+flexport/catalog/location/v1/location.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x89\x03\n\x14\x43\x61rtageAttributesDto\x12/\n\ncarrier_id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12/\n\tdirection\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\naddress_id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x34\n\x0fservice_area_id\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x30\n\x0b\x66\x61\x63ility_id\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\x15transit_time_min_days\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12:\n\x15transit_time_max_days\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int32Value"\x8e\x03\n\x19\x43\x61rtageQueryAttributesDto\x12\x13\n\x0b\x63\x61rrier_ids\x18\x01 \x03(\x03\x12/\n\tdirection\x18\x02 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x12\x10\n\x08port_ids\x18\x03 \x03(\x03\x12\x18\n\x10service_area_ids\x18\x04 \x03(\x03\x12\x14\n\x0cgeobound_ids\x18\x05 \x03(\x03\x12;\n\x08location\x18\x06 \x01(\x0b\x32).flexport.catalog.location.v1.LocationDto\x12\x14\n\x0c\x66\x61\x63ility_ids\x18\x07 \x03(\x03\x12.\n\tweight_kg\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x32\n\x0e\x61llow_seaports\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0e\x61llow_airports\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValueBe\n(com.flexport.catalog.offering.cartage.v1B\x0c\x43\x61rtageProtoP\x01\xea\x02(Flexport::Catalog::Offering::Cartage::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.catalog.offering.cartage.v1.cartage_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n(com.flexport.catalog.offering.cartage.v1B\014CartageProtoP\001\352\002(Flexport::Catalog::Offering::Cartage::V1"
    _globals["_CARTAGEATTRIBUTESDTO"]._serialized_start = 170
    _globals["_CARTAGEATTRIBUTESDTO"]._serialized_end = 563
    _globals["_CARTAGEQUERYATTRIBUTESDTO"]._serialized_start = 566
    _globals["_CARTAGEQUERYATTRIBUTESDTO"]._serialized_end = 964
# @@protoc_insertion_point(module_scope)