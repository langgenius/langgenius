# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/airprocurement/v1beta1/core_service_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n?flexport/monolith/airprocurement/v1beta1/core_service_api.proto\x12(flexport.monolith.airprocurement.v1beta1"f\n\x18UploadMainFreightRequest\x12\x1b\n\x13storage_service_fid\x18\x01 \x01(\t\x12\x10\n\x08user_fid\x18\x02 \x01(\t\x12\x1b\n\x13partner_company_fid\x18\x03 \x01(\t"D\n\x19UploadMainFreightResponse\x12\x17\n\x0fsuccess_message\x18\x01 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t2\xaf\x01\n\x0e\x43oreServiceAPI\x12\x9c\x01\n\x11UploadMainFreight\x12\x42.flexport.monolith.airprocurement.v1beta1.UploadMainFreightRequest\x1a\x43.flexport.monolith.airprocurement.v1beta1.UploadMainFreightResponseBs\n,com.flexport.monolith.airprocurement.v1beta1B\x13\x43oreServiceApiProtoP\x01\xea\x02+Flexport::Monolith::AirProcurement::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.airprocurement.v1beta1.core_service_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n,com.flexport.monolith.airprocurement.v1beta1B\023CoreServiceApiProtoP\001\352\002+Flexport::Monolith::AirProcurement::V1Beta1"
    _globals["_UPLOADMAINFREIGHTREQUEST"]._serialized_start = 109
    _globals["_UPLOADMAINFREIGHTREQUEST"]._serialized_end = 211
    _globals["_UPLOADMAINFREIGHTRESPONSE"]._serialized_start = 213
    _globals["_UPLOADMAINFREIGHTRESPONSE"]._serialized_end = 281
    _globals["_CORESERVICEAPI"]._serialized_start = 284
    _globals["_CORESERVICEAPI"]._serialized_end = 459
# @@protoc_insertion_point(module_scope)