# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/compliance/entityevent/v1beta1/status_change.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n;flexport/compliance/entityevent/v1beta1/status_change.proto\x12'flexport.compliance.entityevent.v1beta1\x1a\x37\x66lexport/compliance/entityevent/v1beta1/id_detail.proto\x1a:flexport/compliance/entityevent/v1beta1/party_status.proto\"\x9a\x01\n\x0cStatusChange\x12>\n\x03ids\x18\x01 \x03(\x0b\x32\x31.flexport.compliance.entityevent.v1beta1.IdDetail\x12J\n\x0cparty_status\x18\x02 \x01(\x0e\x32\x34.flexport.compliance.entityevent.v1beta1.PartyStatusBo\n+com.flexport.compliance.entityevent.v1beta1B\x11StatusChangeProtoP\x01\xea\x02*Flexport::Compliance::EntityEvent::V1Beta1b\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.compliance.entityevent.v1beta1.status_change_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n+com.flexport.compliance.entityevent.v1beta1B\021StatusChangeProtoP\001\352\002*Flexport::Compliance::EntityEvent::V1Beta1"
    _globals["_STATUSCHANGE"]._serialized_start = 222
    _globals["_STATUSCHANGE"]._serialized_end = 376
# @@protoc_insertion_point(module_scope)