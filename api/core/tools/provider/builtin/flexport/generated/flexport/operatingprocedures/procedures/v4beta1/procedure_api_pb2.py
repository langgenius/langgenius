# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/operatingprocedures/procedures/v4beta1/procedure_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nCflexport/operatingprocedures/procedures/v4beta1/procedure_api.proto\x12/flexport.operatingprocedures.procedures.v4beta1\x1a?flexport/operatingprocedures/procedures/v4beta1/procedure.proto"\x82\x01\n\x19\x43reateSSDProcedureRequest\x12M\n\tprocedure\x18\x01 \x01(\x0b\x32:.flexport.operatingprocedures.procedures.v4beta1.Procedure\x12\x16\n\x0e\x63reated_by_fid\x18\x02 \x01(\t"T\n\x1a\x43reateSSDProcedureResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rprocedure_fid\x18\x02 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x03 \x03(\t"\x99\x01\n\x19UpdateSSDProcedureRequest\x12\x15\n\rprocedure_fid\x18\x01 \x01(\t\x12\x16\n\x0eupdated_by_fid\x18\x02 \x01(\t\x12M\n\tprocedure\x18\x03 \x01(\x0b\x32:.flexport.operatingprocedures.procedures.v4beta1.Procedure"T\n\x1aUpdateSSDProcedureResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rprocedure_fid\x18\x02 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x03 \x03(\t"K\n\x1a\x44\x65stroySSDProcedureRequest\x12\x15\n\rprocedure_fid\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65leted_by_fid\x18\x02 \x01(\t"U\n\x1b\x44\x65stroySSDProcedureResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rprocedure_fid\x18\x02 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x03 \x03(\t"\x8a\x01\n$GetSSDProcedureByProcedureFIDRequest\x12\x15\n\rprocedure_fid\x18\x01 \x01(\t\x12K\n\x06\x63\x61ller\x18\x02 \x01(\x0e\x32;.flexport.operatingprocedures.procedures.v4beta1.CallerName"v\n%GetSSDProcedureByProcedureFIDResponse\x12M\n\tprocedure\x18\x01 \x01(\x0b\x32:.flexport.operatingprocedures.procedures.v4beta1.Procedure"\xa0\x01\n$GetSSDProcedureOfTypeForTopicRequest\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12S\n\ntopic_type\x18\x02 \x01(\x0e\x32?.flexport.operatingprocedures.procedures.v4beta1.SupportedTopic\x12\x11\n\ttopic_fid\x18\x03 \x01(\t"\x86\x01\n%GetSSDProcedureOfTypeForTopicResponse\x12M\n\tprocedure\x18\x01 \x01(\x0b\x32:.flexport.operatingprocedures.procedures.v4beta1.Procedure\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t"I\n\x1fGetMatchingConfigurationRequest\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x02 \x01(\t"<\n GetMatchingConfigurationResponse\x12\x18\n\x10output_body_json\x18\x01 \x01(\t*o\n\x0eSupportedTopic\x12\x1b\n\x17SUPPORTED_TOPIC_INVALID\x10\x00\x12\x1c\n\x18SUPPORTED_TOPIC_SHIPMENT\x10\x01\x12"\n\x1eSUPPORTED_TOPIC_DELIVERY_ORDER\x10\x02*\x94\x01\n\nCallerName\x12\x17\n\x13\x43\x41LLER_NAME_INVALID\x10\x00\x12%\n!CALLER_NAME_WORK_ITEMS_AUTOMATION\x10\x01\x12\x1f\n\x1b\x43\x41LLER_NAME_EMAIL_GENERATOR\x10\x02\x12%\n!CALLER_NAME_CUSTOMS_CLIENT_ENGINE\x10\x03\x32\x85\t\n\x0cProcedureAPI\x12\xce\x01\n\x1dGetSSDProcedureByProcedureFID\x12U.flexport.operatingprocedures.procedures.v4beta1.GetSSDProcedureByProcedureFIDRequest\x1aV.flexport.operatingprocedures.procedures.v4beta1.GetSSDProcedureByProcedureFIDResponse\x12\xce\x01\n\x1dGetSSDProcedureOfTypeForTopic\x12U.flexport.operatingprocedures.procedures.v4beta1.GetSSDProcedureOfTypeForTopicRequest\x1aV.flexport.operatingprocedures.procedures.v4beta1.GetSSDProcedureOfTypeForTopicResponse\x12\xad\x01\n\x12\x43reateSSDProcedure\x12J.flexport.operatingprocedures.procedures.v4beta1.CreateSSDProcedureRequest\x1aK.flexport.operatingprocedures.procedures.v4beta1.CreateSSDProcedureResponse\x12\xb0\x01\n\x13\x44\x65stroySSDProcedure\x12K.flexport.operatingprocedures.procedures.v4beta1.DestroySSDProcedureRequest\x1aL.flexport.operatingprocedures.procedures.v4beta1.DestroySSDProcedureResponse\x12\xad\x01\n\x12UpdateSSDProcedure\x12J.flexport.operatingprocedures.procedures.v4beta1.UpdateSSDProcedureRequest\x1aK.flexport.operatingprocedures.procedures.v4beta1.UpdateSSDProcedureResponse\x12\xbf\x01\n\x18GetMatchingConfiguration\x12P.flexport.operatingprocedures.procedures.v4beta1.GetMatchingConfigurationRequest\x1aQ.flexport.operatingprocedures.procedures.v4beta1.GetMatchingConfigurationResponseB\x7f\n3com.flexport.operatingprocedures.procedures.v4beta1B\x11ProcedureApiProtoP\x01\xea\x02\x32\x46lexport::OperatingProcedures::Procedures::V4Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.operatingprocedures.procedures.v4beta1.procedure_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n3com.flexport.operatingprocedures.procedures.v4beta1B\021ProcedureApiProtoP\001\352\0022Flexport::OperatingProcedures::Procedures::V4Beta1"
    _globals["_SUPPORTEDTOPIC"]._serialized_start = 1508
    _globals["_SUPPORTEDTOPIC"]._serialized_end = 1619
    _globals["_CALLERNAME"]._serialized_start = 1622
    _globals["_CALLERNAME"]._serialized_end = 1770
    _globals["_CREATESSDPROCEDUREREQUEST"]._serialized_start = 186
    _globals["_CREATESSDPROCEDUREREQUEST"]._serialized_end = 316
    _globals["_CREATESSDPROCEDURERESPONSE"]._serialized_start = 318
    _globals["_CREATESSDPROCEDURERESPONSE"]._serialized_end = 402
    _globals["_UPDATESSDPROCEDUREREQUEST"]._serialized_start = 405
    _globals["_UPDATESSDPROCEDUREREQUEST"]._serialized_end = 558
    _globals["_UPDATESSDPROCEDURERESPONSE"]._serialized_start = 560
    _globals["_UPDATESSDPROCEDURERESPONSE"]._serialized_end = 644
    _globals["_DESTROYSSDPROCEDUREREQUEST"]._serialized_start = 646
    _globals["_DESTROYSSDPROCEDUREREQUEST"]._serialized_end = 721
    _globals["_DESTROYSSDPROCEDURERESPONSE"]._serialized_start = 723
    _globals["_DESTROYSSDPROCEDURERESPONSE"]._serialized_end = 808
    _globals["_GETSSDPROCEDUREBYPROCEDUREFIDREQUEST"]._serialized_start = 811
    _globals["_GETSSDPROCEDUREBYPROCEDUREFIDREQUEST"]._serialized_end = 949
    _globals["_GETSSDPROCEDUREBYPROCEDUREFIDRESPONSE"]._serialized_start = 951
    _globals["_GETSSDPROCEDUREBYPROCEDUREFIDRESPONSE"]._serialized_end = 1069
    _globals["_GETSSDPROCEDUREOFTYPEFORTOPICREQUEST"]._serialized_start = 1072
    _globals["_GETSSDPROCEDUREOFTYPEFORTOPICREQUEST"]._serialized_end = 1232
    _globals["_GETSSDPROCEDUREOFTYPEFORTOPICRESPONSE"]._serialized_start = 1235
    _globals["_GETSSDPROCEDUREOFTYPEFORTOPICRESPONSE"]._serialized_end = 1369
    _globals["_GETMATCHINGCONFIGURATIONREQUEST"]._serialized_start = 1371
    _globals["_GETMATCHINGCONFIGURATIONREQUEST"]._serialized_end = 1444
    _globals["_GETMATCHINGCONFIGURATIONRESPONSE"]._serialized_start = 1446
    _globals["_GETMATCHINGCONFIGURATIONRESPONSE"]._serialized_end = 1506
    _globals["_PROCEDUREAPI"]._serialized_start = 1773
    _globals["_PROCEDUREAPI"]._serialized_end = 2930
# @@protoc_insertion_point(module_scope)