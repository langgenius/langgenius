# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executionperformance/v1beta1/execution_performance_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nEflexport/executionperformance/v1beta1/execution_performance_api.proto\x12%flexport.executionperformance.v1beta1\x1a$flexport/otp/v1beta1/milestone.proto\x1a\x1f\x66lexport/otp/v1beta1/span.proto\x1a\x1f\x66lexport/otp/v1beta1/time.proto\x1a#flexport/otp/v1beta1/timeline.proto"h\n\x12GetTimelineRequest\x12\r\n\x03\x66id\x18\x01 \x01(\tH\x00\x12\x1d\n\x13\x65xecution_order_fid\x18\x02 \x01(\tH\x00\x12\x16\n\x0cshipment_fid\x18\x03 \x01(\tH\x00\x42\x0c\n\nidentifier"G\n\x13GetTimelineResponse\x12\x30\n\x08timeline\x18\x01 \x01(\x0b\x32\x1e.flexport.otp.v1beta1.Timeline"%\n\x14ListTimelinesRequest\x12\r\n\x05limit\x18\x01 \x01(\r"J\n\x15ListTimelinesResponse\x12\x31\n\ttimelines\x18\x01 \x03(\x0b\x32\x1e.flexport.otp.v1beta1.Timeline""\n\x13GetMilestoneRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"J\n\x14GetMilestoneResponse\x12\x32\n\tmilestone\x18\x01 \x01(\x0b\x32\x1f.flexport.otp.v1beta1.Milestone"\xbe\x01\n\x15ListMilestonesRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x16\n\x0ctimeline_fid\x18\x02 \x01(\tH\x00\x12\x1d\n\x13\x65xecution_order_fid\x18\x03 \x01(\tH\x00\x12\x16\n\x0cshipment_fid\x18\x04 \x01(\tH\x00\x12\x1c\n\x12\x65xecution_task_fid\x18\x05 \x01(\tH\x00\x12\x1d\n\x13\x65xecution_cargo_fid\x18\x06 \x01(\tH\x00\x42\n\n\x08\x63riteria"M\n\x16ListMilestonesResponse\x12\x33\n\nmilestones\x18\x01 \x03(\x0b\x32\x1f.flexport.otp.v1beta1.Milestone"\x1d\n\x0eGetTimeRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t";\n\x0fGetTimeResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.flexport.otp.v1beta1.Time"8\n\x10ListTimesRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x15\n\rmilestone_fid\x18\x02 \x01(\t">\n\x11ListTimesResponse\x12)\n\x05times\x18\x01 \x03(\x0b\x32\x1a.flexport.otp.v1beta1.Time"v\n\x19\x43\x61lculateIntervalsRequest\x12\x16\n\x0ctimeline_fid\x18\x01 \x01(\tH\x00\x12\x1d\n\x13\x65xecution_order_fid\x18\x02 \x01(\tH\x00\x12\x16\n\x0cshipment_fid\x18\x03 \x01(\tH\x00\x42\n\n\x08\x63riteria"O\n\x1a\x43\x61lculateIntervalsResponse\x12\x31\n\tintervals\x18\x01 \x03(\x0b\x32\x1e.flexport.otp.v1beta1.Interval"w\n\x1a\x43\x61lculateViolationsRequest\x12\x16\n\x0ctimeline_fid\x18\x01 \x01(\tH\x00\x12\x1d\n\x13\x65xecution_order_fid\x18\x02 \x01(\tH\x00\x12\x16\n\x0cshipment_fid\x18\x03 \x01(\tH\x00\x42\n\n\x08\x63riteria"R\n\x1b\x43\x61lculateViolationsResponse\x12\x33\n\nviolations\x18\x01 \x03(\x0b\x32\x1f.flexport.otp.v1beta1.Violation2\xfc\x08\n\x17\x45xecutionPerformanceAPI\x12\x84\x01\n\x0bGetTimeline\x12\x39.flexport.executionperformance.v1beta1.GetTimelineRequest\x1a:.flexport.executionperformance.v1beta1.GetTimelineResponse\x12\x8a\x01\n\rListTimelines\x12;.flexport.executionperformance.v1beta1.ListTimelinesRequest\x1a<.flexport.executionperformance.v1beta1.ListTimelinesResponse\x12\x87\x01\n\x0cGetMilestone\x12:.flexport.executionperformance.v1beta1.GetMilestoneRequest\x1a;.flexport.executionperformance.v1beta1.GetMilestoneResponse\x12\x8d\x01\n\x0eListMilestones\x12<.flexport.executionperformance.v1beta1.ListMilestonesRequest\x1a=.flexport.executionperformance.v1beta1.ListMilestonesResponse\x12x\n\x07GetTime\x12\x35.flexport.executionperformance.v1beta1.GetTimeRequest\x1a\x36.flexport.executionperformance.v1beta1.GetTimeResponse\x12~\n\tListTimes\x12\x37.flexport.executionperformance.v1beta1.ListTimesRequest\x1a\x38.flexport.executionperformance.v1beta1.ListTimesResponse\x12\x99\x01\n\x12\x43\x61lculateIntervals\x12@.flexport.executionperformance.v1beta1.CalculateIntervalsRequest\x1a\x41.flexport.executionperformance.v1beta1.CalculateIntervalsResponse\x12\x9c\x01\n\x13\x43\x61lculateViolations\x12\x41.flexport.executionperformance.v1beta1.CalculateViolationsRequest\x1a\x42.flexport.executionperformance.v1beta1.CalculateViolationsResponseBu\n)com.flexport.executionperformance.v1beta1B\x1c\x45xecutionPerformanceApiProtoP\x01\xea\x02\'Flexport::ExecutionPerformance::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executionperformance.v1beta1.execution_performance_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n)com.flexport.executionperformance.v1beta1B\034ExecutionPerformanceApiProtoP\001\352\002'Flexport::ExecutionPerformance::V1Beta1"
    _globals["_GETTIMELINEREQUEST"]._serialized_start = 253
    _globals["_GETTIMELINEREQUEST"]._serialized_end = 357
    _globals["_GETTIMELINERESPONSE"]._serialized_start = 359
    _globals["_GETTIMELINERESPONSE"]._serialized_end = 430
    _globals["_LISTTIMELINESREQUEST"]._serialized_start = 432
    _globals["_LISTTIMELINESREQUEST"]._serialized_end = 469
    _globals["_LISTTIMELINESRESPONSE"]._serialized_start = 471
    _globals["_LISTTIMELINESRESPONSE"]._serialized_end = 545
    _globals["_GETMILESTONEREQUEST"]._serialized_start = 547
    _globals["_GETMILESTONEREQUEST"]._serialized_end = 581
    _globals["_GETMILESTONERESPONSE"]._serialized_start = 583
    _globals["_GETMILESTONERESPONSE"]._serialized_end = 657
    _globals["_LISTMILESTONESREQUEST"]._serialized_start = 660
    _globals["_LISTMILESTONESREQUEST"]._serialized_end = 850
    _globals["_LISTMILESTONESRESPONSE"]._serialized_start = 852
    _globals["_LISTMILESTONESRESPONSE"]._serialized_end = 929
    _globals["_GETTIMEREQUEST"]._serialized_start = 931
    _globals["_GETTIMEREQUEST"]._serialized_end = 960
    _globals["_GETTIMERESPONSE"]._serialized_start = 962
    _globals["_GETTIMERESPONSE"]._serialized_end = 1021
    _globals["_LISTTIMESREQUEST"]._serialized_start = 1023
    _globals["_LISTTIMESREQUEST"]._serialized_end = 1079
    _globals["_LISTTIMESRESPONSE"]._serialized_start = 1081
    _globals["_LISTTIMESRESPONSE"]._serialized_end = 1143
    _globals["_CALCULATEINTERVALSREQUEST"]._serialized_start = 1145
    _globals["_CALCULATEINTERVALSREQUEST"]._serialized_end = 1263
    _globals["_CALCULATEINTERVALSRESPONSE"]._serialized_start = 1265
    _globals["_CALCULATEINTERVALSRESPONSE"]._serialized_end = 1344
    _globals["_CALCULATEVIOLATIONSREQUEST"]._serialized_start = 1346
    _globals["_CALCULATEVIOLATIONSREQUEST"]._serialized_end = 1465
    _globals["_CALCULATEVIOLATIONSRESPONSE"]._serialized_start = 1467
    _globals["_CALCULATEVIOLATIONSRESPONSE"]._serialized_end = 1549
    _globals["_EXECUTIONPERFORMANCEAPI"]._serialized_start = 1552
    _globals["_EXECUTIONPERFORMANCEAPI"]._serialized_end = 2700
# @@protoc_insertion_point(module_scope)