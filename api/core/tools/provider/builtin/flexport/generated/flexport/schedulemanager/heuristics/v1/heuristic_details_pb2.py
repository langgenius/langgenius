# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/schedulemanager/heuristics/v1/heuristic_details.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n>flexport/schedulemanager/heuristics/v1/heuristic_details.proto\x12&flexport.schedulemanager.heuristics.v1\x1a?flexport/schedulemanager/types/enums/v1/prediction_source.proto"\x95\x01\n\x10HeuristicDetails\x12\x16\n\x0eheuristic_name\x18\x01 \x01(\t\x12Q\n\x0bsuggestions\x18\x02 \x03(\x0b\x32<.flexport.schedulemanager.heuristics.v1.TravelTimeSuggestion\x12\x16\n\x0e\x65rror_messages\x18\x03 \x03(\t"\xea\x01\n\x14TravelTimeSuggestion\x12O\n\x0fsuggestion_type\x18\x01 \x01(\x0e\x32\x36.flexport.schedulemanager.heuristics.v1.SuggestionType\x12\x17\n\x0fsuggestion_days\x18\x02 \x01(\x05\x12\x12\n\nentity_fid\x18\x03 \x01(\t\x12T\n\x11prediction_source\x18\x04 \x01(\x0e\x32\x39.flexport.schedulemanager.types.enums.v1.PredictionSource*\x80\x01\n\x0eSuggestionType\x12\x1b\n\x17SUGGESTION_TYPE_INVALID\x10\x00\x12\x19\n\x15SUGGESTION_TYPE_DWELL\x10\x01\x12\x19\n\x15SUGGESTION_TYPE_DEVAN\x10\x02\x12\x1b\n\x17SUGGESTION_TYPE_TRANSIT\x10\x03\x42q\n*com.flexport.schedulemanager.heuristics.v1B\x15HeuristicDetailsProtoP\x01\xea\x02)Flexport::ScheduleManager::Heuristics::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.schedulemanager.heuristics.v1.heuristic_details_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n*com.flexport.schedulemanager.heuristics.v1B\025HeuristicDetailsProtoP\001\352\002)Flexport::ScheduleManager::Heuristics::V1"
    _globals["_SUGGESTIONTYPE"]._serialized_start = 561
    _globals["_SUGGESTIONTYPE"]._serialized_end = 689
    _globals["_HEURISTICDETAILS"]._serialized_start = 172
    _globals["_HEURISTICDETAILS"]._serialized_end = 321
    _globals["_TRAVELTIMESUGGESTION"]._serialized_start = 324
    _globals["_TRAVELTIMESUGGESTION"]._serialized_end = 558
# @@protoc_insertion_point(module_scope)