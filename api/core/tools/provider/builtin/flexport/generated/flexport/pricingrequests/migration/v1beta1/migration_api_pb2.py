# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/pricingrequests/migration/v1beta1/migration_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n>flexport/pricingrequests/migration/v1beta1/migration_api.proto\x12*flexport.pricingrequests.migration.v1beta1"\x1d\n\x0eSyncBidRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"2\n\x0fSyncBidResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t2\x93\x01\n\x0cMigrationAPI\x12\x82\x01\n\x07SyncBid\x12:.flexport.pricingrequests.migration.v1beta1.SyncBidRequest\x1a;.flexport.pricingrequests.migration.v1beta1.SyncBidResponseBu\n.com.flexport.pricingrequests.migration.v1beta1B\x11MigrationApiProtoP\x01\xea\x02-Flexport::PricingRequests::Migration::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.pricingrequests.migration.v1beta1.migration_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n.com.flexport.pricingrequests.migration.v1beta1B\021MigrationApiProtoP\001\352\002-Flexport::PricingRequests::Migration::V1Beta1"
    _globals["_SYNCBIDREQUEST"]._serialized_start = 110
    _globals["_SYNCBIDREQUEST"]._serialized_end = 139
    _globals["_SYNCBIDRESPONSE"]._serialized_start = 141
    _globals["_SYNCBIDRESPONSE"]._serialized_end = 191
    _globals["_MIGRATIONAPI"]._serialized_start = 194
    _globals["_MIGRATIONAPI"]._serialized_end = 341
# @@protoc_insertion_point(module_scope)