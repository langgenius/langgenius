# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/quoting/draftquote/v1beta1/draft_quote_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n9flexport/quoting/draftquote/v1beta1/draft_quote_api.proto\x12#flexport.quoting.draftquote.v1beta1\x1a.flexport/quoting/core_quote/v1/corequote.proto\x1a?flexport/quoting/quoteshare/v1beta1/service_item_template.proto\x1a!flexport/quoting/rfq/v2/rfq.proto"A\n\x16WriteDraftQuoteRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x62id\x18\x02 \x01(\x04\x12\x0c\n\x04name\x18\x03 \x01(\t"\x19\n\x17WriteDraftQuoteResponse"\xee\x01\n\x1a\x42\x61\x63kfillDraftQuotesRequest\x12\x38\n\x06quotes\x18\x01 \x03(\x0b\x32(.flexport.quoting.corequote.v1.CoreQuote\x12*\n\x04rfqs\x18\x02 \x03(\x0b\x32\x1c.flexport.quoting.rfq.v2.Rfq\x12X\n\x16service_item_templates\x18\x03 \x03(\x0b\x32\x38.flexport.quoting.quoteshare.v1beta1.ServiceItemTemplate\x12\x10\n\x08user_fid\x18\x04 \x01(\t"W\n\x1b\x42\x61\x63kfillDraftQuotesResponse\x12\x38\n\x06quotes\x18\x01 \x03(\x0b\x32(.flexport.quoting.corequote.v1.CoreQuote"%\n\x16ReadDraftQuotesRequest\x12\x0b\n\x03\x66id\x18\x01 \x03(\t"X\n\x17ReadDraftQuotesResponse\x12=\n\x0b\x63ore_quotes\x18\x01 \x03(\x0b\x32(.flexport.quoting.corequote.v1.CoreQuote2\xc8\x03\n\rDraftQuoteAPI\x12\x8c\x01\n\x0fWriteDraftQuote\x12;.flexport.quoting.draftquote.v1beta1.WriteDraftQuoteRequest\x1a<.flexport.quoting.draftquote.v1beta1.WriteDraftQuoteResponse\x12\x98\x01\n\x13\x42\x61\x63kfillDraftQuotes\x12?.flexport.quoting.draftquote.v1beta1.BackfillDraftQuotesRequest\x1a@.flexport.quoting.draftquote.v1beta1.BackfillDraftQuotesResponse\x12\x8c\x01\n\x0fReadDraftQuotes\x12;.flexport.quoting.draftquote.v1beta1.ReadDraftQuotesRequest\x1a<.flexport.quoting.draftquote.v1beta1.ReadDraftQuotesResponseBh\n\'com.flexport.quoting.draftquote.v1beta1B\x12\x44raftQuoteApiProtoP\x01\xea\x02&Flexport::Quoting::DraftQuote::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.quoting.draftquote.v1beta1.draft_quote_api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n'com.flexport.quoting.draftquote.v1beta1B\022DraftQuoteApiProtoP\001\352\002&Flexport::Quoting::DraftQuote::V1Beta1"
    _globals["_WRITEDRAFTQUOTEREQUEST"]._serialized_start = 246
    _globals["_WRITEDRAFTQUOTEREQUEST"]._serialized_end = 311
    _globals["_WRITEDRAFTQUOTERESPONSE"]._serialized_start = 313
    _globals["_WRITEDRAFTQUOTERESPONSE"]._serialized_end = 338
    _globals["_BACKFILLDRAFTQUOTESREQUEST"]._serialized_start = 341
    _globals["_BACKFILLDRAFTQUOTESREQUEST"]._serialized_end = 579
    _globals["_BACKFILLDRAFTQUOTESRESPONSE"]._serialized_start = 581
    _globals["_BACKFILLDRAFTQUOTESRESPONSE"]._serialized_end = 668
    _globals["_READDRAFTQUOTESREQUEST"]._serialized_start = 670
    _globals["_READDRAFTQUOTESREQUEST"]._serialized_end = 707
    _globals["_READDRAFTQUOTESRESPONSE"]._serialized_start = 709
    _globals["_READDRAFTQUOTESRESPONSE"]._serialized_end = 797
    _globals["_DRAFTQUOTEAPI"]._serialized_start = 800
    _globals["_DRAFTQUOTEAPI"]._serialized_end = 1256
# @@protoc_insertion_point(module_scope)