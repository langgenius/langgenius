# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customsworkflowinstrumentation/enums/eventtype/v1beta1/event_type.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\nPflexport/customsworkflowinstrumentation/enums/eventtype/v1beta1/event_type.proto\x12?flexport.customsworkflowinstrumentation.enums.eventtype.v1beta1*\x81\x11\n\tEventType\x12\x16\n\x12\x45VENT_TYPE_INVALID\x10\x00\x12\x19\n\x15\x45VENT_TYPE_CI_CREATED\x10\x01\x12!\n\x1d\x45VENT_TYPE_CI_MARKED_COMPLETE\x10\x02\x12\x19\n\x15\x45VENT_TYPE_CI_UPDATED\x10\x03\x12*\n&EVENT_TYPE_CUSTOMS_DECLARATION_UPDATED\x10\x04\x12$\n EVENT_TYPE_CUSTOMS_ENTRY_CREATED\x10\x05\x12+\n'EVENT_TYPE_CUSTOMS_LINE_ITEMS_ALLOCATED\x10\x06\x12,\n(EVENT_TYPE_CUSTOMS_LINE_ITEMS_CLASSIFIED\x10\x07\x12\"\n\x1e\x45VENT_TYPE_DIGITIZE_CI_STARTED\x10\x08\x12-\n)EVENT_TYPE_DIRECT_CBP_TRANSMISSION_FAILED\x10\t\x12 \n\x1c\x45VENT_TYPE_DOCUMENT_ARCHIVED\x10\n\x12$\n EVENT_TYPE_DOCUMENT_TYPE_CHANGED\x10\x0b\x12\"\n\x1e\x45VENT_TYPE_DOCUMENT_UNARCHIVED\x10\x0c\x12 \n\x1c\x45VENT_TYPE_DOCUMENT_UPLOADED\x10\r\x12/\n+EVENT_TYPE_ENTRY_LINES_VALIDATION_COMPLETED\x10\x0e\x12.\n*EVENT_TYPE_ENTRY_LINES_VALIDATION_REVERTED\x10\x0f\x12+\n'EVENT_TYPE_ENTRY_MARKED_AS_NOT_PREPARED\x10\x10\x12'\n#EVENT_TYPE_ENTRY_MARKED_AS_PREPARED\x10\x11\x12\x30\n,EVENT_TYPE_ENTRY_TRANSMITTED_DIRECTLY_TO_CBP\x10\x12\x12*\n&EVENT_TYPE_ENTRY_TRANSMITTED_TO_NETCHB\x10\x13\x12\"\n\x1e\x45VENT_TYPE_EXCEPTION_CANCELLED\x10\x14\x12 \n\x1c\x45VENT_TYPE_EXCEPTION_CREATED\x10\x15\x12!\n\x1d\x45VENT_TYPE_EXCEPTION_REOPENED\x10\x16\x12!\n\x1d\x45VENT_TYPE_EXCEPTION_RESOLVED\x10\x17\x12\x35\n1EVENT_TYPE_INVOICE_CHARGES_VERIFICATION_CANCELLED\x10\x18\x12\x30\n,EVENT_TYPE_INVOICE_CHARGES_VERIFICATION_DONE\x10\x19\x12#\n\x1f\x45VENT_TYPE_ISF_AMENDED_MANUALLY\x10\x1a\x12+\n'EVENT_TYPE_ISF_CREATED_FROM_SHIPPER_ISF\x10\x1b\x12#\n\x1f\x45VENT_TYPE_ISF_CREATED_MANUALLY\x10\x1c\x12\x1a\n\x16\x45VENT_TYPE_ISF_DELETED\x10\x1d\x12$\n EVENT_TYPE_ISF_RECEIPT_GENERATED\x10\x1e\x12\x37\n3EVENT_TYPE_ISF_STATUS_UPDATED_PER_RESPONSE_FROM_CBP\x10\x1f\x12*\n&EVENT_TYPE_ISF_SUBMITTED_AUTOMATICALLY\x10 \x12%\n!EVENT_TYPE_ISF_SUBMITTED_MANUALLY\x10!\x12\x31\n-EVENT_TYPE_MANIFEST_INFO_VALIDATION_COMPLETED\x10\"\x12\x30\n,EVENT_TYPE_MANIFEST_INFO_VALIDATION_REVERTED\x10#\x12(\n$EVENT_TYPE_MODE_OF_TRANSPORT_UPDATED\x10$\x12(\n$EVENT_TYPE_NETCHB_ENTRY_LOG_RECEIVED\x10%\x12)\n%EVENT_TYPE_NETCHB_TRANSMISSION_FAILED\x10&\x12 \n\x1c\x45VENT_TYPE_OCEAN_HBL_DELETED\x10'\x12\"\n\x1e\x45VENT_TYPE_OCEAN_HBL_GENERATED\x10(\x12!\n\x1d\x45VENT_TYPE_OCEAN_MBL_RECEIVED\x10)\x12#\n\x1f\x45VENT_TYPE_PGA_PROFILES_UPDATED\x10*\x12-\n)EVENT_TYPE_REPLY_MADE_IN_EXCEPTION_THREAD\x10+\x12.\n*EVENT_TYPE_ROUTE_INFO_VALIDATION_COMPLETED\x10,\x12-\n)EVENT_TYPE_ROUTE_INFO_VALIDATION_REVERTED\x10-\x12\"\n\x1e\x45VENT_TYPE_ROUTE_SHAPE_UPDATED\x10.\x12+\n'EVENT_TYPE_SET_SHIPMENT_CUSTOMS_CLEARED\x10/\x12\x1f\n\x1b\x45VENT_TYPE_SHIPMENT_CREATED\x10\x30\x12-\n)EVENT_TYPE_UNSET_SHIPMENT_CUSTOMS_CLEARED\x10\x31\x12,\n(EVENT_TYPE_ISF_FILING_PARTY_TYPE_UPDATED\x10\x32\x12'\n#EVENT_TYPE_ISF_CREATED_FROM_EDI_ISF\x10\x33\x12.\n*EVENT_TYPE_CUSTOMS_LINE_ITEMS_UNCLASSIFIED\x10\x34\x42\x9d\x01\nCcom.flexport.customsworkflowinstrumentation.enums.eventtype.v1beta1B\x0e\x45ventTypeProtoP\x01\xea\x02\x43\x46lexport::CustomsWorkflowInstrumentation::Enums::EventType::V1Beta1b\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customsworkflowinstrumentation.enums.eventtype.v1beta1.event_type_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\nCcom.flexport.customsworkflowinstrumentation.enums.eventtype.v1beta1B\016EventTypeProtoP\001\352\002CFlexport::CustomsWorkflowInstrumentation::Enums::EventType::V1Beta1"
    _globals["_EVENTTYPE"]._serialized_start = 150
    _globals["_EVENTTYPE"]._serialized_end = 2327
# @@protoc_insertion_point(module_scope)