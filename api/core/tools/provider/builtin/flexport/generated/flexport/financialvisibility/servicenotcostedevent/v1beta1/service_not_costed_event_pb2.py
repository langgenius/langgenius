# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/financialvisibility/servicenotcostedevent/v1beta1/service_not_costed_event.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nYflexport/financialvisibility/servicenotcostedevent/v1beta1/service_not_costed_event.proto\x12:flexport.financialvisibility.servicenotcostedevent.v1beta1\x1a\x38\x66lexport/financialvisibility/common/v1beta1/common.proto\x1aGflexport/financialvisibility/supplyservice/v1beta1/supply_service.proto"\xa7\x03\n\x15ServiceNotCostedEvent\x12V\n\nidentifier\x18\x01 \x01(\x0b\x32\x42.flexport.financialledger.supplyservice.v1beta1.ExternalIdentifier\x12H\n\x04mode\x18\x02 \x01(\x0e\x32:.flexport.financialledger.supplyservice.v1beta1.SupplyMode\x12I\n\tmilestone\x18\x03 \x01(\x0e\x32\x36.flexport.financialvisibility.common.v1beta1.Milestone\x12\x19\n\x11vendor_entity_fid\x18\x04 \x01(\t\x12k\n\x13\x65xternal_references\x18\x05 \x03(\x0b\x32N.flexport.financialledger.supplyservice.v1beta1.ExternalReferenceParametersDto\x12\x19\n\x11purchase_order_id\x18\x06 \x01(\tB\x96\x01\n:com.flexport.financialledger.servicenotcostedevent.v1beta1B\x1aServiceNotCostedEventProtoP\x01\xea\x02\x39\x46lexport::FinancialLedger::ServiceNotCostedEvent::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.financialvisibility.servicenotcostedevent.v1beta1.service_not_costed_event_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n:com.flexport.financialledger.servicenotcostedevent.v1beta1B\032ServiceNotCostedEventProtoP\001\352\0029Flexport::FinancialLedger::ServiceNotCostedEvent::V1Beta1"
    _globals["_SERVICENOTCOSTEDEVENT"]._serialized_start = 285
    _globals["_SERVICENOTCOSTEDEVENT"]._serialized_end = 708
# @@protoc_insertion_point(module_scope)