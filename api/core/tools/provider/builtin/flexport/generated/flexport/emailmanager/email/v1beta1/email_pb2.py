# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/emailmanager/email/v1beta1/email.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n/flexport/emailmanager/email/v1beta1/email.proto\x12#flexport.emailmanager.email.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xe5\x07\n\x05\x45mail\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x30\n\x0c\x63reated_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tsent_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nemail_type\x18\x04 \x01(\t\x12\x0f\n\x07subject\x18\x05 \x01(\t\x12*\n\x04\x62ody\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12G\n\x0c\x66rom_contact\x18\x07 \x01(\x0b\x32\x31.flexport.emailmanager.email.v1beta1.EmailContact\x12K\n\x10reply_to_contact\x18\x08 \x01(\x0b\x32\x31.flexport.emailmanager.email.v1beta1.EmailContact\x12\x46\n\x0bto_contacts\x18\t \x03(\x0b\x32\x31.flexport.emailmanager.email.v1beta1.EmailContact\x12\x46\n\x0b\x63\x63_contacts\x18\n \x03(\x0b\x32\x31.flexport.emailmanager.email.v1beta1.EmailContact\x12G\n\x0c\x62\x63\x63_contacts\x18\x0b \x03(\x0b\x32\x31.flexport.emailmanager.email.v1beta1.EmailContact\x12\x13\n\x0bis_outbound\x18\x0c \x01(\x08\x12\x46\n\x06labels\x18\r \x03(\x0b\x32\x36.flexport.emailmanager.email.v1beta1.Email.LabelsEntry\x12\x44\n\x0b\x61ttachments\x18\x0e \x03(\x0b\x32/.flexport.emailmanager.email.v1beta1.Attachment\x12\x0f\n\x07\x63ontext\x18\x0f \x01(\t\x12\x16\n\x0e\x63reated_by_fid\x18\x10 \x01(\t\x12K\n\x0ftracking_events\x18\x11 \x03(\x0b\x32\x32.flexport.emailmanager.email.v1beta1.TrackingEvent\x12\x35\n\x0fplain_text_body\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a^\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12>\n\x05value\x18\x02 \x01(\x0b\x32/.flexport.emailmanager.email.v1beta1.LabelValue:\x02\x38\x01",\n\nLabelValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x42\x06\n\x04kind"I\n\nAttachment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0f\x66ile_object_fid\x18\x02 \x01(\t\x12\x14\n\x0c\x64ocument_fid\x18\x03 \x01(\t"E\n\x0c\x45mailContact\x12\x15\n\remail_address\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08user_fid\x18\x03 \x01(\t"\xbf\x01\n\rTrackingEvent\x12\x11\n\temail_fid\x18\x01 \x01(\t\x12\x1f\n\x17recipient_email_address\x18\x02 \x01(\t\x12J\n\nevent_type\x18\x03 \x01(\x0e\x32\x36.flexport.emailmanager.email.v1beta1.TrackingEventType\x12.\n\nevent_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\x9f\x02\n\x11TrackingEventType\x12\x1f\n\x1bTRACKING_EVENT_TYPE_INVALID\x10\x00\x12!\n\x1dTRACKING_EVENT_TYPE_PROCESSED\x10\x01\x12\x1f\n\x1bTRACKING_EVENT_TYPE_DROPPED\x10\x02\x12!\n\x1dTRACKING_EVENT_TYPE_DELIVERED\x10\x03\x12\x1f\n\x1bTRACKING_EVENT_TYPE_BOUNCED\x10\x04\x12\x1f\n\x1bTRACKING_EVENT_TYPE_BLOCKED\x10\x05\x12 \n\x1cTRACKING_EVENT_TYPE_DEFERRED\x10\x06\x12\x1e\n\x1aTRACKING_EVENT_TYPE_OPENED\x10\x07*q\n\rRecipientRole\x12\x1a\n\x16RECIPIENT_ROLE_INVALID\x10\x00\x12\x15\n\x11RECIPIENT_ROLE_TO\x10\x01\x12\x15\n\x11RECIPIENT_ROLE_CC\x10\x02\x12\x16\n\x12RECIPIENT_ROLE_BCC\x10\x03\x42`\n\'com.flexport.emailmanager.email.v1beta1B\nEmailProtoP\x01\xea\x02&Flexport::EmailManager::Email::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.emailmanager.email.v1beta1.email_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n'com.flexport.emailmanager.email.v1beta1B\nEmailProtoP\001\352\002&Flexport::EmailManager::Email::V1Beta1"
    )
    _globals["_EMAIL_LABELSENTRY"]._options = None
    _globals["_EMAIL_LABELSENTRY"]._serialized_options = b"8\001"
    _globals["_TRACKINGEVENTTYPE"]._serialized_start = 1540
    _globals["_TRACKINGEVENTTYPE"]._serialized_end = 1827
    _globals["_RECIPIENTROLE"]._serialized_start = 1829
    _globals["_RECIPIENTROLE"]._serialized_end = 1942
    _globals["_EMAIL"]._serialized_start = 154
    _globals["_EMAIL"]._serialized_end = 1151
    _globals["_EMAIL_LABELSENTRY"]._serialized_start = 1057
    _globals["_EMAIL_LABELSENTRY"]._serialized_end = 1151
    _globals["_LABELVALUE"]._serialized_start = 1153
    _globals["_LABELVALUE"]._serialized_end = 1197
    _globals["_ATTACHMENT"]._serialized_start = 1199
    _globals["_ATTACHMENT"]._serialized_end = 1272
    _globals["_EMAILCONTACT"]._serialized_start = 1274
    _globals["_EMAILCONTACT"]._serialized_end = 1343
    _globals["_TRACKINGEVENT"]._serialized_start = 1346
    _globals["_TRACKINGEVENT"]._serialized_end = 1537
# @@protoc_insertion_point(module_scope)