# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/commerce/search/query/v1beta1/charge_management_context.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nFflexport/commerce/search/query/v1beta1/charge_management_context.proto\x12&flexport.commerce.search.query.v1beta1\x1a\x1egoogle/protobuf/wrappers.proto"\xa9\x03\n\x17\x43hargeManagementContext\x12;\n\x15isf_filing_party_type\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0cpricing_tier\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12:\n\x16wants_delivery_service\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x41\n\x1dwants_flexport_import_customs\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x41\n\x1dwants_flexport_export_customs\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12:\n\x16wants_flexport_freight\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x18\x64\x65stination_address_fids\x18\x07 \x03(\tBy\n*com.flexport.commerce.search.query.v1beta1B\x1c\x43hargeManagementContextProtoP\x01\xea\x02*Flexport::Commerce::Search::Query::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.commerce.search.query.v1beta1.charge_management_context_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n*com.flexport.commerce.search.query.v1beta1B\034ChargeManagementContextProtoP\001\352\002*Flexport::Commerce::Search::Query::V1Beta1"
    _globals["_CHARGEMANAGEMENTCONTEXT"]._serialized_start = 147
    _globals["_CHARGEMANAGEMENTCONTEXT"]._serialized_end = 572
# @@protoc_insertion_point(module_scope)