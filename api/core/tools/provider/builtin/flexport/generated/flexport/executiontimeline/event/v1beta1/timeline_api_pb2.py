# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executiontimeline/event/v1beta1/timeline_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n;flexport/executiontimeline/event/v1beta1/timeline_api.proto\x12(flexport.executiontimeline.event.v1beta1\x1a=flexport/executiontimeline/event/v1beta1/timeline_event.proto\x1aMflexport/executiontimeline/event/v1beta1/timeline_event_type_dependency.proto\x1aJflexport/executiontimeline/event/v1beta1/timeline_event_type_mapping.proto"i\n\x16\x43reateEventTypeRequest\x12O\n\nevent_type\x18\x01 \x01(\x0b\x32;.flexport.executiontimeline.event.v1beta1.TimelineEventType"j\n\x17\x43reateEventTypeResponse\x12O\n\nevent_type\x18\x01 \x01(\x0b\x32;.flexport.executiontimeline.event.v1beta1.TimelineEventType"%\n\x16\x44\x65leteEventTypeRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"j\n\x17\x44\x65leteEventTypeResponse\x12O\n\nevent_type\x18\x01 \x01(\x0b\x32;.flexport.executiontimeline.event.v1beta1.TimelineEventType"h\n\x13GetEventTypeRequest\x12Q\n\x04type\x18\x01 \x01(\x0e\x32\x43.flexport.executiontimeline.event.v1beta1.TimelineEventTypeCategory"g\n\x14GetEventTypeResponse\x12O\n\nevent_type\x18\x01 \x01(\x0b\x32;.flexport.executiontimeline.event.v1beta1.TimelineEventType"7\n\x1eGetEventTriggerMappingsRequest\x12\x15\n\rec_event_type\x18\x01 \x01(\t"\x82\x01\n\x1fGetEventTriggerMappingsResponse\x12_\n\x13\x65vent_type_mappings\x18\x01 \x03(\x0b\x32\x42.flexport.executiontimeline.event.v1beta1.TimelineEventTypeMapping"\x82\x01\n CreateEventTriggerMappingRequest\x12^\n\x12\x65vent_type_mapping\x18\x01 \x01(\x0b\x32\x42.flexport.executiontimeline.event.v1beta1.TimelineEventTypeMapping"\x83\x01\n!CreateEventTriggerMappingResponse\x12^\n\x12\x65vent_type_mapping\x18\x01 \x01(\x0b\x32\x42.flexport.executiontimeline.event.v1beta1.TimelineEventTypeMapping"/\n DeleteEventTriggerMappingRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"\x83\x01\n!DeleteEventTriggerMappingResponse\x12^\n\x12\x65vent_type_mapping\x18\x01 \x01(\x0b\x32\x42.flexport.executiontimeline.event.v1beta1.TimelineEventTypeMapping",\n\x1dGetEventTypeDependencyRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"\x8a\x01\n\x1eGetEventTypeDependencyResponse\x12h\n\x19timeline_event_dependency\x18\x01 \x01(\x0b\x32\x45.flexport.executiontimeline.event.v1beta1.TimelineEventTypeDependency"\x8c\x01\n CreateEventTypeDependencyRequest\x12h\n\x19timeline_event_dependency\x18\x01 \x01(\x0b\x32\x45.flexport.executiontimeline.event.v1beta1.TimelineEventTypeDependency"\x8d\x01\n!CreateEventTypeDependencyResponse\x12h\n\x19timeline_event_dependency\x18\x01 \x01(\x0b\x32\x45.flexport.executiontimeline.event.v1beta1.TimelineEventTypeDependency"/\n DeleteEventTypeDependencyRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"\x8d\x01\n!DeleteEventTypeDependencyResponse\x12h\n\x19timeline_event_dependency\x18\x01 \x01(\x0b\x32\x45.flexport.executiontimeline.event.v1beta1.TimelineEventTypeDependency2\x8a\x0c\n\x0bTimelineAPI\x12\x8d\x01\n\x0cGetEventType\x12=.flexport.executiontimeline.event.v1beta1.GetEventTypeRequest\x1a>.flexport.executiontimeline.event.v1beta1.GetEventTypeResponse\x12\x96\x01\n\x0f\x43reateEventType\x12@.flexport.executiontimeline.event.v1beta1.CreateEventTypeRequest\x1a\x41.flexport.executiontimeline.event.v1beta1.CreateEventTypeResponse\x12\x96\x01\n\x0f\x44\x65leteEventType\x12@.flexport.executiontimeline.event.v1beta1.DeleteEventTypeRequest\x1a\x41.flexport.executiontimeline.event.v1beta1.DeleteEventTypeResponse\x12\xae\x01\n\x17GetEventTriggerMappings\x12H.flexport.executiontimeline.event.v1beta1.GetEventTriggerMappingsRequest\x1aI.flexport.executiontimeline.event.v1beta1.GetEventTriggerMappingsResponse\x12\xb4\x01\n\x19\x43reateEventTriggerMapping\x12J.flexport.executiontimeline.event.v1beta1.CreateEventTriggerMappingRequest\x1aK.flexport.executiontimeline.event.v1beta1.CreateEventTriggerMappingResponse\x12\xb4\x01\n\x19\x44\x65leteEventTriggerMapping\x12J.flexport.executiontimeline.event.v1beta1.DeleteEventTriggerMappingRequest\x1aK.flexport.executiontimeline.event.v1beta1.DeleteEventTriggerMappingResponse\x12\xab\x01\n\x16GetEventTypeDependency\x12G.flexport.executiontimeline.event.v1beta1.GetEventTypeDependencyRequest\x1aH.flexport.executiontimeline.event.v1beta1.GetEventTypeDependencyResponse\x12\xb4\x01\n\x19\x43reateEventTypeDependency\x12J.flexport.executiontimeline.event.v1beta1.CreateEventTypeDependencyRequest\x1aK.flexport.executiontimeline.event.v1beta1.CreateEventTypeDependencyResponse\x12\xb4\x01\n\x19\x44\x65leteEventTypeDependency\x12J.flexport.executiontimeline.event.v1beta1.DeleteEventTypeDependencyRequest\x1aK.flexport.executiontimeline.event.v1beta1.DeleteEventTypeDependencyResponseBp\n,com.flexport.executiontimeline.event.v1beta1B\x10TimelineApiProtoP\x01\xea\x02+Flexport::ExecutionTimeline::Event::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executiontimeline.event.v1beta1.timeline_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n,com.flexport.executiontimeline.event.v1beta1B\020TimelineApiProtoP\001\352\002+Flexport::ExecutionTimeline::Event::V1Beta1"
    _globals["_CREATEEVENTTYPEREQUEST"]._serialized_start = 323
    _globals["_CREATEEVENTTYPEREQUEST"]._serialized_end = 428
    _globals["_CREATEEVENTTYPERESPONSE"]._serialized_start = 430
    _globals["_CREATEEVENTTYPERESPONSE"]._serialized_end = 536
    _globals["_DELETEEVENTTYPEREQUEST"]._serialized_start = 538
    _globals["_DELETEEVENTTYPEREQUEST"]._serialized_end = 575
    _globals["_DELETEEVENTTYPERESPONSE"]._serialized_start = 577
    _globals["_DELETEEVENTTYPERESPONSE"]._serialized_end = 683
    _globals["_GETEVENTTYPEREQUEST"]._serialized_start = 685
    _globals["_GETEVENTTYPEREQUEST"]._serialized_end = 789
    _globals["_GETEVENTTYPERESPONSE"]._serialized_start = 791
    _globals["_GETEVENTTYPERESPONSE"]._serialized_end = 894
    _globals["_GETEVENTTRIGGERMAPPINGSREQUEST"]._serialized_start = 896
    _globals["_GETEVENTTRIGGERMAPPINGSREQUEST"]._serialized_end = 951
    _globals["_GETEVENTTRIGGERMAPPINGSRESPONSE"]._serialized_start = 954
    _globals["_GETEVENTTRIGGERMAPPINGSRESPONSE"]._serialized_end = 1084
    _globals["_CREATEEVENTTRIGGERMAPPINGREQUEST"]._serialized_start = 1087
    _globals["_CREATEEVENTTRIGGERMAPPINGREQUEST"]._serialized_end = 1217
    _globals["_CREATEEVENTTRIGGERMAPPINGRESPONSE"]._serialized_start = 1220
    _globals["_CREATEEVENTTRIGGERMAPPINGRESPONSE"]._serialized_end = 1351
    _globals["_DELETEEVENTTRIGGERMAPPINGREQUEST"]._serialized_start = 1353
    _globals["_DELETEEVENTTRIGGERMAPPINGREQUEST"]._serialized_end = 1400
    _globals["_DELETEEVENTTRIGGERMAPPINGRESPONSE"]._serialized_start = 1403
    _globals["_DELETEEVENTTRIGGERMAPPINGRESPONSE"]._serialized_end = 1534
    _globals["_GETEVENTTYPEDEPENDENCYREQUEST"]._serialized_start = 1536
    _globals["_GETEVENTTYPEDEPENDENCYREQUEST"]._serialized_end = 1580
    _globals["_GETEVENTTYPEDEPENDENCYRESPONSE"]._serialized_start = 1583
    _globals["_GETEVENTTYPEDEPENDENCYRESPONSE"]._serialized_end = 1721
    _globals["_CREATEEVENTTYPEDEPENDENCYREQUEST"]._serialized_start = 1724
    _globals["_CREATEEVENTTYPEDEPENDENCYREQUEST"]._serialized_end = 1864
    _globals["_CREATEEVENTTYPEDEPENDENCYRESPONSE"]._serialized_start = 1867
    _globals["_CREATEEVENTTYPEDEPENDENCYRESPONSE"]._serialized_end = 2008
    _globals["_DELETEEVENTTYPEDEPENDENCYREQUEST"]._serialized_start = 2010
    _globals["_DELETEEVENTTYPEDEPENDENCYREQUEST"]._serialized_end = 2057
    _globals["_DELETEEVENTTYPEDEPENDENCYRESPONSE"]._serialized_start = 2060
    _globals["_DELETEEVENTTYPEDEPENDENCYRESPONSE"]._serialized_end = 2201
    _globals["_TIMELINEAPI"]._serialized_start = 2204
    _globals["_TIMELINEAPI"]._serialized_end = 3750
# @@protoc_insertion_point(module_scope)