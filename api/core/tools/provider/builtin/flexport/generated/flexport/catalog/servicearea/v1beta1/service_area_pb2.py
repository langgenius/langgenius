# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/catalog/servicearea/v1beta1/service_area.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n7flexport/catalog/servicearea/v1beta1/service_area.proto\x12$flexport.catalog.servicearea.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xe3\x01\n\x0eServiceAreaDto\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0f\x63reated_at_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\ncompany_id\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x15\n\rgeo_bound_ids\x18\x05 \x03(\x03"t\n\x16ServiceAreaDistanceDto\x12,\n\x06min_km\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12,\n\x06max_km\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue"x\n\x0f\x43reatedResponse\x12J\n\x0cservice_area\x18\x01 \x01(\x0b\x32\x34.flexport.catalog.servicearea.v1beta1.ServiceAreaDto\x12\x19\n\x11validation_errors\x18\x02 \x03(\t"\x8e\x01\n\x08Location\x12)\n\x03lat\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x03lng\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06radius\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueBh\n(com.flexport.catalog.servicearea.v1beta1B\x10ServiceAreaProtoP\x01\xea\x02\'Flexport::Catalog::ServiceArea::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.catalog.servicearea.v1beta1.service_area_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n(com.flexport.catalog.servicearea.v1beta1B\020ServiceAreaProtoP\001\352\002'Flexport::Catalog::ServiceArea::V1Beta1"
    _globals["_SERVICEAREADTO"]._serialized_start = 163
    _globals["_SERVICEAREADTO"]._serialized_end = 390
    _globals["_SERVICEAREADISTANCEDTO"]._serialized_start = 392
    _globals["_SERVICEAREADISTANCEDTO"]._serialized_end = 508
    _globals["_CREATEDRESPONSE"]._serialized_start = 510
    _globals["_CREATEDRESPONSE"]._serialized_end = 630
    _globals["_LOCATION"]._serialized_start = 633
    _globals["_LOCATION"]._serialized_end = 775
# @@protoc_insertion_point(module_scope)