# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/dataoutreachcampaigns/emailoutreachoutcome/v1beta1/email_outreach_outcome.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\naflexport/monolith/dataoutreachcampaigns/emailoutreachoutcome/v1beta1/email_outreach_outcome.proto\x12\x44\x66lexport.monolith.dataoutreachcampaigns.emailoutreachoutcome.v1beta1"\xaa\x01\n\x14\x45mailOutreachOutcome\x12\x13\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\x05\x12\x14\n\x0c\x63\x61mpaign_fid\x18\x02 \x01(\t\x12g\n\x08statuses\x18\x03 \x03(\x0b\x32U.flexport.monolith.dataoutreachcampaigns.emailoutreachoutcome.v1beta1.RecipientStatus"\x87\x01\n\x0fRecipientStatus\x12\x11\n\trecipient\x18\x01 \x01(\t\x12\x61\n\x06status\x18\x02 \x01(\x0e\x32Q.flexport.monolith.dataoutreachcampaigns.emailoutreachoutcome.v1beta1.EmailStatus*\x7f\n\x0b\x45mailStatus\x12\x18\n\x14\x45MAIL_STATUS_INVALID\x10\x00\x12\x1a\n\x16\x45MAIL_STATUS_PROCESSED\x10\x01\x12\x1a\n\x16\x45MAIL_STATUS_DELIVERED\x10\x02\x12\x1e\n\x1a\x45MAIL_STATUS_NOT_DELIVERED\x10\x03\x42\xb2\x01\nHcom.flexport.monolith.dataoutreachcampaigns.emailoutreachoutcome.v1beta1B\x19\x45mailOutreachOutcomeProtoP\x01\xea\x02HFlexport::Monolith::DataOutreachCampaigns::EmailOutreachOutcome::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.monolith.dataoutreachcampaigns.emailoutreachoutcome.v1beta1.email_outreach_outcome_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\nHcom.flexport.monolith.dataoutreachcampaigns.emailoutreachoutcome.v1beta1B\031EmailOutreachOutcomeProtoP\001\352\002HFlexport::Monolith::DataOutreachCampaigns::EmailOutreachOutcome::V1Beta1"
    _globals["_EMAILSTATUS"]._serialized_start = 482
    _globals["_EMAILSTATUS"]._serialized_end = 609
    _globals["_EMAILOUTREACHOUTCOME"]._serialized_start = 172
    _globals["_EMAILOUTREACHOUTCOME"]._serialized_end = 342
    _globals["_RECIPIENTSTATUS"]._serialized_start = 345
    _globals["_RECIPIENTSTATUS"]._serialized_end = 480
# @@protoc_insertion_point(module_scope)