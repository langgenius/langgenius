# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/originops/masterbillofladingchanged/v1/master_bill_of_lading_changed.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nSflexport/originops/masterbillofladingchanged/v1/master_bill_of_lading_changed.proto\x12/flexport.originops.masterbillofladingchanged.v1\x1a\x46\x66lexport/originops/billofladingchanged/v1/bill_of_lading_changed.proto\x1a>flexport/originops/dispositionevent/v1/disposition_event.proto\x1a?flexport/originops/eventrootcontext/v1/event_root_context.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd8\x03\n\x19MasterBillOfLadingChanged\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x02 \x01(\t\x12T\n\x12\x65vent_root_context\x18\x03 \x01(\x0b\x32\x38.flexport.originops.eventrootcontext.v1.EventRootContext\x12\x33\n\x0f\x63reated_at_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x62ill_number\x18\x06 \x01(\t\x12\\\n\x12parsed_house_bills\x18\x07 \x03(\x0b\x32@.flexport.originops.masterbillofladingchanged.v1.ParsedHouseBill\x12\x66\n\x11transmission_mode\x18\x08 \x01(\x0e\x32G.flexport.originops.billofladingchanged.v1.BillOfLadingTransmissionModeB\x02\x18\x01"|\n\x0fParsedHouseBill\x12\x13\n\x0b\x62ill_number\x18\x01 \x01(\t\x12T\n\x12\x64isposition_events\x18\x02 \x03(\x0b\x32\x38.flexport.originops.dispositionevent.v1.DispositionEventB\x8c\x01\n3com.flexport.originops.masterbillofladingchanged.v1B\x1eMasterBillOfLadingChangedProtoP\x01\xea\x02\x32\x46lexport::OriginOps::MasterBillOfLadingChanged::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.originops.masterbillofladingchanged.v1.master_bill_of_lading_changed_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n3com.flexport.originops.masterbillofladingchanged.v1B\036MasterBillOfLadingChangedProtoP\001\352\0022Flexport::OriginOps::MasterBillOfLadingChanged::V1"
    _globals["_MASTERBILLOFLADINGCHANGED"].fields_by_name["transmission_mode"]._options = None
    _globals["_MASTERBILLOFLADINGCHANGED"].fields_by_name["transmission_mode"]._serialized_options = b"\030\001"
    _globals["_MASTERBILLOFLADINGCHANGED"]._serialized_start = 371
    _globals["_MASTERBILLOFLADINGCHANGED"]._serialized_end = 843
    _globals["_PARSEDHOUSEBILL"]._serialized_start = 845
    _globals["_PARSEDHOUSEBILL"]._serialized_end = 969
# @@protoc_insertion_point(module_scope)