# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/rulesengine/decisiontable/v1/decision_table_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n>flexport/rulesengine/decisiontable/v1/decision_table_api.proto\x12%flexport.rulesengine.decisiontable.v1\x1a:flexport/rulesengine/decisiontable/v1/decision_table.proto"&\n\x17GetDecisionTableRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"h\n\x18GetDecisionTableResponse\x12L\n\x0e\x64\x65\x63ision_table\x18\x01 \x01(\x0b\x32\x34.flexport.rulesengine.decisiontable.v1.DecisionTable2\xa8\x01\n\x10\x44\x65\x63isionTableAPI\x12\x93\x01\n\x10GetDecisionTable\x12>.flexport.rulesengine.decisiontable.v1.GetDecisionTableRequest\x1a?.flexport.rulesengine.decisiontable.v1.GetDecisionTableResponseBo\n)com.flexport.rulesengine.decisiontable.v1B\x15\x44\x65\x63isionTableApiProtoP\x01\xea\x02(Flexport::RulesEngine::DecisionTable::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.rulesengine.decisiontable.v1.decision_table_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n)com.flexport.rulesengine.decisiontable.v1B\025DecisionTableApiProtoP\001\352\002(Flexport::RulesEngine::DecisionTable::V1"
    _globals["_GETDECISIONTABLEREQUEST"]._serialized_start = 165
    _globals["_GETDECISIONTABLEREQUEST"]._serialized_end = 203
    _globals["_GETDECISIONTABLERESPONSE"]._serialized_start = 205
    _globals["_GETDECISIONTABLERESPONSE"]._serialized_end = 309
    _globals["_DECISIONTABLEAPI"]._serialized_start = 312
    _globals["_DECISIONTABLEAPI"]._serialized_end = 480
# @@protoc_insertion_point(module_scope)