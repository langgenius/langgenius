# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/workitems/workitemservice/v1beta1/work_item.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n:flexport/workitems/workitemservice/v1beta1/work_item.proto\x12*flexport.workitems.workitemservice.v1beta1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xcf\x0f\n\x08WorkItem\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x12\n\nupsert_key\x18\x02 \x01(\t\x12\x16\n\x0ework_item_type\x18\x03 \x01(\t\x12-\n\x0cwork_context\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\x15 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\ntopic_fids\x18\x05 \x03(\t\x12/\n\x0b\x64ue_at_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12L\n\x07\x64\x65tails\x18\x07 \x01(\x0b\x32;.flexport.workitems.workitemservice.v1beta1.WorkItemDetails\x12M\n\x08warnings\x18\x08 \x03(\x0b\x32;.flexport.workitems.workitemservice.v1beta1.WorkItemWarning\x12V\n\rblock_reasons\x18\t \x03(\x0b\x32?.flexport.workitems.workitemservice.v1beta1.WorkItemBlockReason\x12\x35\n\x11\x63ompleted_at_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x12snoozed_until_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\napplicable\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x15\n\rassignee_fids\x18\r \x03(\t\x12\x36\n\x12\x61pplicable_at_time\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x10\x63ompleted_by_fid\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0eupdated_by_fid\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x10\n\x08revision\x18\x11 \x01(\x04\x12+\n\x05state\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x11is_for_automation\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12S\n\x0f\x61utomation_type\x18\x14 \x01(\x0e\x32:.flexport.workitems.workitemservice.v1beta1.AutomationType\x12\x1b\n\x13optimistic_revision\x18\x16 \x01(\x04\x12\x33\n\x0fupdated_at_time\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12X\n\x11\x65xception_context\x18\x18 \x03(\x0b\x32=.flexport.workitems.workitemservice.v1beta1.WorkItemException\x12\x1d\n\x15\x61pplicable_at_reasons\x18\x19 \x03(\t\x12?\n\x19\x61pplicable_at_description\x18\x1a \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0f\x63reated_at_time\x18\x1b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12k\n\x17\x61utomation_availability\x18\x1c \x01(\x0b\x32J.flexport.workitems.workitemservice.v1beta1.WorkItemAutomationAvailability\x12_\n\x11\x61utomation_result\x18\x1d \x01(\x0b\x32\x44.flexport.workitems.workitemservice.v1beta1.WorkItemAutomationResult\x12;\n\x17last_applicable_at_time\x18\x1e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0esnoozed_by_fid\x18\x1f \x01(\t\x12\x18\n\x10unsnoozed_by_fid\x18  \x01(\t\x12.\n\nstate_lock\x18! \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x37\n\x11state_lock_reason\x18" \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x17\x66irst_completed_at_time\x18# \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x12\x66irst_completed_by\x18$ \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x11\x66irst_due_at_time\x18% \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16\x61utomation_due_at_time\x18& \x01(\x0b\x32\x1a.google.protobuf.Timestamp""\n\x0fWorkItemDetails\x12\x0f\n\x07\x64\x65tails\x18\x01 \x01(\t""\n\x0fWorkItemWarning\x12\x0f\n\x07warning\x18\x01 \x01(\t"+\n\x13WorkItemBlockReason\x12\x14\n\x0c\x62lock_reason\x18\x01 \x01(\t"]\n\x11WorkItemException\x12\x15\n\rexception_fid\x18\x01 \x01(\t\x12\x31\n\rdue_date_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"@\n\x12WorkItemIdentifier\x12\x12\n\nupsert_key\x18\x01 \x01(\t\x12\x16\n\x0ework_item_type\x18\x02 \x01(\t"O\n\x1eWorkItemAutomationAvailability\x12-\n\tavailable\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue"\xab\x01\n\x18WorkItemAutomationResult\x12*\n\x06result\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\rfailed_reason\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\xc8\x06\n\x0fUpstreamService\x12\x1c\n\x18UPSTREAM_SERVICE_INVALID\x10\x00\x12 \n\x1cUPSTREAM_SERVICE_UNSPECIFIED\x10\x01\x12\x1f\n\x1bUPSTREAM_SERVICE_COMPLIANCE\x10\x02\x12 \n\x1cUPSTREAM_SERVICE_CUSTOMS_ISF\x10\x03\x12)\n%UPSTREAM_SERVICE_EXECUTION_MILESTONES\x10\x04\x12\x1d\n\x19UPSTREAM_SERVICE_MONORAIL\x10\x05\x12)\n%UPSTREAM_SERVICE_OCEAN_FMT_ASSIGNMENT\x10\x06\x12\x1e\n\x1aUPSTREAM_SERVICE_OCEAN_OPS\x10\x07\x12#\n\x1fUPSTREAM_SERVICE_OCEAN_PLANNING\x10\x08\x12!\n\x1dUPSTREAM_SERVICE_OCEAN_SUPPLY\x10\t\x12\x1c\n\x18UPSTREAM_SERVICE_QUOTING\x10\n\x12\x1f\n\x1bUPSTREAM_SERVICE_WORK_ITEMS\x10\x0b\x12)\n%UPSTREAM_SERVICE_EXCEPTION_MANAGEMENT\x10\x0c\x12"\n\x1eUPSTREAM_SERVICE_DOCUMENT_FLOW\x10\r\x12\x19\n\x15UPSTREAM_SERVICE_TEST\x10\x0e\x12.\n*UPSTREAM_SERVICE_COMMERCIAL_INVOICE_ENGINE\x10\x0f\x12\x1f\n\x1bUPSTREAM_SERVICE_VISIBILITY\x10\x10\x12)\n%UPSTREAM_SERVICE_CUSTOMS_DECLARATIONS\x10\x11\x12\x1c\n\x18UPSTREAM_SERVICE_BILLING\x10\x12\x12\x1e\n\x1aUPSTREAM_SERVICE_LOAD_PLAN\x10\x13\x12%\n!UPSTREAM_SERVICE_SCHEDULE_MANAGER\x10\x14\x12\x18\n\x14UPSTREAM_SERVICE_OEX\x10\x15\x12\x31\n-UPSTREAM_SERVICE_LAMBDA_WORK_ITEMS_AUTOMATION\x10\x16*\x86\x01\n\x0e\x41utomationType\x12\x1b\n\x17\x41UTOMATION_TYPE_INVALID\x10\x00\x12\x1a\n\x16\x41UTOMATION_TYPE_MANUAL\x10\x01\x12\x1f\n\x1b\x41UTOMATION_TYPE_AUTOMATABLE\x10\x02\x12\x1a\n\x16\x41UTOMATION_TYPE_HYBRID\x10\x03\x42q\n.com.flexport.workitems.workitemservice.v1beta1B\rWorkItemProtoP\x01\xea\x02-Flexport::WorkItems::WorkItemService::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.workitems.workitemservice.v1beta1.work_item_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n.com.flexport.workitems.workitemservice.v1beta1B\rWorkItemProtoP\001\352\002-Flexport::WorkItems::WorkItemService::V1Beta1"
    _globals["_UPSTREAMSERVICE"]._serialized_start = 2737
    _globals["_UPSTREAMSERVICE"]._serialized_end = 3577
    _globals["_AUTOMATIONTYPE"]._serialized_start = 3580
    _globals["_AUTOMATIONTYPE"]._serialized_end = 3714
    _globals["_WORKITEM"]._serialized_start = 202
    _globals["_WORKITEM"]._serialized_end = 2201
    _globals["_WORKITEMDETAILS"]._serialized_start = 2203
    _globals["_WORKITEMDETAILS"]._serialized_end = 2237
    _globals["_WORKITEMWARNING"]._serialized_start = 2239
    _globals["_WORKITEMWARNING"]._serialized_end = 2273
    _globals["_WORKITEMBLOCKREASON"]._serialized_start = 2275
    _globals["_WORKITEMBLOCKREASON"]._serialized_end = 2318
    _globals["_WORKITEMEXCEPTION"]._serialized_start = 2320
    _globals["_WORKITEMEXCEPTION"]._serialized_end = 2413
    _globals["_WORKITEMIDENTIFIER"]._serialized_start = 2415
    _globals["_WORKITEMIDENTIFIER"]._serialized_end = 2479
    _globals["_WORKITEMAUTOMATIONAVAILABILITY"]._serialized_start = 2481
    _globals["_WORKITEMAUTOMATIONAVAILABILITY"]._serialized_end = 2560
    _globals["_WORKITEMAUTOMATIONRESULT"]._serialized_start = 2563
    _globals["_WORKITEMAUTOMATIONRESULT"]._serialized_end = 2734
# @@protoc_insertion_point(module_scope)