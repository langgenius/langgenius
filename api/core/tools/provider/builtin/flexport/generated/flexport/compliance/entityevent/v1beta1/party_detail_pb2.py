# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/compliance/entityevent/v1beta1/party_detail.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n:flexport/compliance/entityevent/v1beta1/party_detail.proto\x12'flexport.compliance.entityevent.v1beta1\x1a<flexport/compliance/entityevent/v1beta1/company_detail.proto\x1a\x37\x66lexport/compliance/entityevent/v1beta1/id_detail.proto\x1a\x39\x66lexport/compliance/entityevent/v1beta1/user_detail.proto\"\xfc\x01\n\x0bPartyDetail\x12>\n\x03ids\x18\x01 \x03(\x0b\x32\x31.flexport.compliance.entityevent.v1beta1.IdDetail\x12J\n\x0buser_detail\x18\x02 \x01(\x0b\x32\x33.flexport.compliance.entityevent.v1beta1.UserDetailH\x00\x12P\n\x0e\x63ompany_detail\x18\x03 \x01(\x0b\x32\x36.flexport.compliance.entityevent.v1beta1.CompanyDetailH\x00\x42\x0f\n\rentity_detailBn\n+com.flexport.compliance.entityevent.v1beta1B\x10PartyDetailProtoP\x01\xea\x02*Flexport::Compliance::EntityEvent::V1Beta1b\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.compliance.entityevent.v1beta1.party_detail_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n+com.flexport.compliance.entityevent.v1beta1B\020PartyDetailProtoP\001\352\002*Flexport::Compliance::EntityEvent::V1Beta1"
    _globals["_PARTYDETAIL"]._serialized_start = 282
    _globals["_PARTYDETAIL"]._serialized_end = 534
# @@protoc_insertion_point(module_scope)