# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/schedulemanager/heuristics/v1beta1/heuristic_violation.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nEflexport/schedulemanager/heuristics/v1beta1/heuristic_violation.proto\x12+flexport.schedulemanager.heuristics.v1beta1\x1a>flexport/executioncoordinator/types/enums/v1/entry_point.proto\x1a\x37\x66lexport/schedulemanager/datechanges/v1/date_type.proto\x1a?flexport/schedulemanager/types/enums/v1/prediction_source.proto\x1a=flexport/schedulemanager/types/enums/v1/suggestion_type.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x9d\x06\n\x12HeuristicViolation\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x02 \x01(\t\x12\x1b\n\x13itinerary_revisions\x18\x03 \x03(\t\x12\x16\n\x0eheuristic_name\x18\n \x01(\t\x12\x19\n\x11\x64\x61te_transit_type\x18\x0b \x01(\t\x12\x44\n\tdate_type\x18\x0c \x01(\x0e\x32\x31.flexport.schedulemanager.datechanges.v1.DateType\x12\x10\n\x08user_fid\x18\x10 \x01(\t\x12M\n\x0b\x65ntry_point\x18\x11 \x01(\x0e\x32\x38.flexport.executioncoordinator.types.enums.v1.EntryPoint\x12\x1b\n\x13violated_entity_fid\x18\x14 \x01(\t\x12\x1c\n\x14violated_entity_type\x18\x15 \x01(\t\x12\x16\n\x0eviolation_days\x18\x16 \x01(\x05\x12\x18\n\x10violated_by_days\x18\x17 \x01(\x05\x12\x1d\n\x15suggestion_entity_fid\x18\x1e \x01(\t\x12P\n\x0fsuggestion_type\x18\x1f \x01(\x0e\x32\x37.flexport.schedulemanager.types.enums.v1.SuggestionType\x12\x17\n\x0fsuggestion_days\x18  \x01(\x03\x12_\n\x1csuggestion_prediction_source\x18! \x01(\x0e\x32\x39.flexport.schedulemanager.types.enums.v1.PredictionSource\x12\x35\n\x11is_flexport_owned\x18- \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12.\n\ncreated_at\x18\x32 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x33 \x01(\x0b\x32\x1a.google.protobuf.TimestampB}\n/com.flexport.schedulemanager.heuristics.v1beta1B\x17HeuristicViolationProtoP\x01\xea\x02.Flexport::ScheduleManager::Heuristics::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.schedulemanager.heuristics.v1beta1.heuristic_violation_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n/com.flexport.schedulemanager.heuristics.v1beta1B\027HeuristicViolationProtoP\001\352\002.Flexport::ScheduleManager::Heuristics::V1Beta1"
    _globals["_HEURISTICVIOLATION"]._serialized_start = 433
    _globals["_HEURISTICVIOLATION"]._serialized_end = 1230
# @@protoc_insertion_point(module_scope)