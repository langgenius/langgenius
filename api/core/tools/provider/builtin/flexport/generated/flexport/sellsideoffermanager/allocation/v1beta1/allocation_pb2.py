# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/sellsideoffermanager/allocation/v1beta1/allocation.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nAflexport/sellsideoffermanager/allocation/v1beta1/allocation.proto\x12\x30\x66lexport.sellsideoffermanager.allocation.v1beta1\x1a\x1egoogle/protobuf/wrappers.proto"\xeb\x01\n\nAllocation\x12\x39\n\x14\x61vailable_allocation\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x35\n\x10total_allocation\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12)\n\x04year\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12)\n\x04week\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x15\n\rallocation_id\x18\x05 \x01(\tB\x7f\n4com.flexport.sellsideoffermanager.allocation.v1beta1B\x0f\x41llocationProtoP\x01\xea\x02\x33\x46lexport::SellSideOfferManager::Allocation::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.sellsideoffermanager.allocation.v1beta1.allocation_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n4com.flexport.sellsideoffermanager.allocation.v1beta1B\017AllocationProtoP\001\352\0023Flexport::SellSideOfferManager::Allocation::V1Beta1"
    _globals["_ALLOCATION"]._serialized_start = 152
    _globals["_ALLOCATION"]._serialized_end = 387
# @@protoc_insertion_point(module_scope)