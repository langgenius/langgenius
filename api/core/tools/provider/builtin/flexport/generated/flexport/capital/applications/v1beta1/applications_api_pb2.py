# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/capital/applications/v1beta1/applications_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n<flexport/capital/applications/v1beta1/applications_api.proto\x12%flexport.capital.applications.v1beta1\x1a\x37\x66lexport/capital/applications/v1beta1/application.proto"j\n\x18\x43reateApplicationRequest\x12N\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32\x39.flexport.capital.applications.v1beta1.ApplicationDetails"3\n\x19\x43reateApplicationResponse\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t"/\n\x15GetApplicationRequest\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t"x\n\x16GetApplicationsRequest\x12J\n\x08statuses\x18\x01 \x03(\x0e\x32\x38.flexport.capital.applications.v1beta1.ApplicationStatus\x12\x12\n\ncreated_at\x18\x02 \x01(\t"a\n\x16GetApplicationResponse\x12G\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32\x32.flexport.capital.applications.v1beta1.Application"c\n\x17GetApplicationsResponse\x12H\n\x0c\x61pplications\x18\x01 \x03(\x0b\x32\x32.flexport.capital.applications.v1beta1.Application"2\n\x18SubmitApplicationRequest\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t"d\n\x19SubmitApplicationResponse\x12G\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32\x32.flexport.capital.applications.v1beta1.Application"\x82\x01\n\x18UpdateApplicationRequest\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t\x12N\n\x0b\x61pplication\x18\x02 \x01(\x0b\x32\x39.flexport.capital.applications.v1beta1.ApplicationDetails"d\n\x19UpdateApplicationResponse\x12G\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32\x32.flexport.capital.applications.v1beta1.Application"\xf2\x01\n\x19ProcessApplicationRequest\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t\x12W\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32G.flexport.capital.applications.v1beta1.ProcessApplicationRequest.Action\x12\x0e\n\x06reason\x18\x03 \x01(\t"T\n\x06\x41\x63tion\x12\x12\n\x0e\x41\x43TION_INVALID\x10\x00\x12\x12\n\x0e\x41\x43TION_APPROVE\x10\x01\x12\x0f\n\x0b\x41\x43TION_DENY\x10\x02\x12\x11\n\rACTION_CANCEL\x10\x03"\x8d\x03\n\x1aProcessApplicationResponse\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t\x12X\n\x06result\x18\x02 \x01(\x0e\x32H.flexport.capital.applications.v1beta1.ProcessApplicationResponse.Result\x12\x0f\n\x07message\x18\x03 \x01(\t"\xeb\x01\n\x06Result\x12\x12\n\x0eRESULT_INVALID\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x1b\n\x17RESULT_ALREADY_APPROVED\x10\x02\x12\x1b\n\x17RESULT_ALREADY_REJECTED\x10\x03\x12\x1b\n\x17RESULT_ALREADY_CANCELED\x10\x04\x12 \n\x1cRESULT_APPLICATION_NOT_FOUND\x10\x05\x12&\n"RESULT_APPLICATION_IN_DRAFT_STATUS\x10\x06\x12\x18\n\x14RESULT_UNKNOWN_ERROR\x10\x07\x32\x9b\x07\n\x0f\x41pplicationsAPI\x12\x96\x01\n\x11\x43reateApplication\x12?.flexport.capital.applications.v1beta1.CreateApplicationRequest\x1a@.flexport.capital.applications.v1beta1.CreateApplicationResponse\x12\x8d\x01\n\x0eGetApplication\x12<.flexport.capital.applications.v1beta1.GetApplicationRequest\x1a=.flexport.capital.applications.v1beta1.GetApplicationResponse\x12\x90\x01\n\x0fGetApplications\x12=.flexport.capital.applications.v1beta1.GetApplicationsRequest\x1a>.flexport.capital.applications.v1beta1.GetApplicationsResponse\x12\x96\x01\n\x11SubmitApplication\x12?.flexport.capital.applications.v1beta1.SubmitApplicationRequest\x1a@.flexport.capital.applications.v1beta1.SubmitApplicationResponse\x12\x96\x01\n\x11UpdateApplication\x12?.flexport.capital.applications.v1beta1.UpdateApplicationRequest\x1a@.flexport.capital.applications.v1beta1.UpdateApplicationResponse\x12\x99\x01\n\x12ProcessApplication\x12@.flexport.capital.applications.v1beta1.ProcessApplicationRequest\x1a\x41.flexport.capital.applications.v1beta1.ProcessApplicationResponseBn\n)com.flexport.capital.applications.v1beta1B\x14\x41pplicationsApiProtoP\x01\xea\x02(Flexport::Capital::Applications::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.capital.applications.v1beta1.applications_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n)com.flexport.capital.applications.v1beta1B\024ApplicationsApiProtoP\001\352\002(Flexport::Capital::Applications::V1Beta1"
    _globals["_CREATEAPPLICATIONREQUEST"]._serialized_start = 160
    _globals["_CREATEAPPLICATIONREQUEST"]._serialized_end = 266
    _globals["_CREATEAPPLICATIONRESPONSE"]._serialized_start = 268
    _globals["_CREATEAPPLICATIONRESPONSE"]._serialized_end = 319
    _globals["_GETAPPLICATIONREQUEST"]._serialized_start = 321
    _globals["_GETAPPLICATIONREQUEST"]._serialized_end = 368
    _globals["_GETAPPLICATIONSREQUEST"]._serialized_start = 370
    _globals["_GETAPPLICATIONSREQUEST"]._serialized_end = 490
    _globals["_GETAPPLICATIONRESPONSE"]._serialized_start = 492
    _globals["_GETAPPLICATIONRESPONSE"]._serialized_end = 589
    _globals["_GETAPPLICATIONSRESPONSE"]._serialized_start = 591
    _globals["_GETAPPLICATIONSRESPONSE"]._serialized_end = 690
    _globals["_SUBMITAPPLICATIONREQUEST"]._serialized_start = 692
    _globals["_SUBMITAPPLICATIONREQUEST"]._serialized_end = 742
    _globals["_SUBMITAPPLICATIONRESPONSE"]._serialized_start = 744
    _globals["_SUBMITAPPLICATIONRESPONSE"]._serialized_end = 844
    _globals["_UPDATEAPPLICATIONREQUEST"]._serialized_start = 847
    _globals["_UPDATEAPPLICATIONREQUEST"]._serialized_end = 977
    _globals["_UPDATEAPPLICATIONRESPONSE"]._serialized_start = 979
    _globals["_UPDATEAPPLICATIONRESPONSE"]._serialized_end = 1079
    _globals["_PROCESSAPPLICATIONREQUEST"]._serialized_start = 1082
    _globals["_PROCESSAPPLICATIONREQUEST"]._serialized_end = 1324
    _globals["_PROCESSAPPLICATIONREQUEST_ACTION"]._serialized_start = 1240
    _globals["_PROCESSAPPLICATIONREQUEST_ACTION"]._serialized_end = 1324
    _globals["_PROCESSAPPLICATIONRESPONSE"]._serialized_start = 1327
    _globals["_PROCESSAPPLICATIONRESPONSE"]._serialized_end = 1724
    _globals["_PROCESSAPPLICATIONRESPONSE_RESULT"]._serialized_start = 1489
    _globals["_PROCESSAPPLICATIONRESPONSE_RESULT"]._serialized_end = 1724
    _globals["_APPLICATIONSAPI"]._serialized_start = 1727
    _globals["_APPLICATIONSAPI"]._serialized_end = 2650
# @@protoc_insertion_point(module_scope)