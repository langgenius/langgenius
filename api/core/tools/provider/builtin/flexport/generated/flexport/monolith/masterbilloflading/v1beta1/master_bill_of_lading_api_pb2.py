# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/masterbilloflading/v1beta1/master_bill_of_lading_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nLflexport/monolith/masterbilloflading/v1beta1/master_bill_of_lading_api.proto\x12,flexport.monolith.masterbilloflading.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\xd9\x04\n GetMasterBillOfLadingListRequest\x12w\n\x12\x65xecution_plan_fid\x18\x01 \x01(\x0b\x32Y.flexport.monolith.masterbilloflading.v1beta1.GetMasterBillOfLadingListRequest.StringListH\x00\x12q\n\x0cshipment_fid\x18\x02 \x01(\x0b\x32Y.flexport.monolith.masterbilloflading.v1beta1.GetMasterBillOfLadingListRequest.StringListH\x00\x12\x81\x01\n\x1cmaster_bill_of_lading_number\x18\x03 \x01(\x0b\x32Y.flexport.monolith.masterbilloflading.v1beta1.GetMasterBillOfLadingListRequest.StringListH\x00\x12|\n\x18master_bill_of_lading_id\x18\x04 \x01(\x0b\x32X.flexport.monolith.masterbilloflading.v1beta1.GetMasterBillOfLadingListRequest.Int32ListH\x00\x1a\x1c\n\nStringList\x12\x0e\n\x06values\x18\x01 \x03(\t\x1a\x1b\n\tInt32List\x12\x0e\n\x06values\x18\x01 \x03(\x05\x42\x0c\n\nidentifier"\x85\x01\n!GetMasterBillOfLadingListResponse\x12`\n\x16master_bill_of_ladings\x18\x01 \x03(\x0b\x32@.flexport.monolith.masterbilloflading.v1beta1.MasterBillOfLading"\x9a\x02\n!GenerateMasterBillOfLadingRequest\x12\x14\n\x0cshipment_fid\x18\x01 \x01(\t\x12\x13\n\x0b\x62ill_number\x18\x02 \x01(\t\x12Y\n\x11transmission_mode\x18\x03 \x01(\x0e\x32>.flexport.monolith.masterbilloflading.v1beta1.TransmissionMode\x12S\n\x0erelease_method\x18\x04 \x01(\x0e\x32;.flexport.monolith.masterbilloflading.v1beta1.ReleaseMethod\x12\x1a\n\x12\x62ill_number_source\x18\x05 \x01(\t"4\n"GenerateMasterBillOfLadingResponse\x12\x0e\n\x06\x65rrors\x18\x01 \x03(\t"\xb0\x06\n\x12MasterBillOfLading\x12\n\n\x02id\x18\x01 \x01(\x05\x12$\n\x1cmaster_bill_of_lading_number\x18\x02 \x01(\t\x12\x1a\n\x12\x65xecution_task_fid\x18\x03 \x01(\t\x12Y\n\x11transmission_mode\x18\x04 \x01(\x0e\x32>.flexport.monolith.masterbilloflading.v1beta1.TransmissionMode\x12S\n\x0erelease_method\x18\x05 \x01(\x0e\x32;.flexport.monolith.masterbilloflading.v1beta1.ReleaseMethod\x12\x13\n\x0b\x63\x61rrier_fid\x18\x06 \x01(\t\x12\x14\n\x0cshipment_fid\x18\x07 \x01(\t\x12\x1d\n\x15place_of_delivery_fid\x18\x08 \x01(\t\x12\x1c\n\x14place_of_receipt_fid\x18\t \x01(\t\x12\x1b\n\x13port_of_loading_fid\x18\n \x01(\t\x12\x1d\n\x15port_of_unloading_fid\x18\x0b \x01(\t\x12\x1d\n\x15\x64raft_approved_by_fid\x18\x0c \x01(\t\x12\x16\n\x0e\x63reated_by_fid\x18\r \x01(\t\x12\x16\n\x0eupdated_by_fid\x18\x0e \x01(\t\x12\x13\n\x0b\x64ocument_id\x18\x0f \x01(\x05\x12\x1b\n\x13release_document_id\x18\x10 \x01(\x05\x12/\n\x0b\x61rchived_at\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11\x64raft_approved_at\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0breleased_at\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ncreated_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\x8f\x01\n\x10TransmissionMode\x12\x1d\n\x19TRANSMISSION_MODE_INVALID\x10\x00\x12\x1d\n\x19TRANSMISSION_MODE_UNKNOWN\x10\x01\x12\x1e\n\x1aTRANSMISSION_MODE_ORIGINAL\x10\x02\x12\x1d\n\x19TRANSMISSION_MODE_EXPRESS\x10\x03*\x8c\x01\n\rReleaseMethod\x12\x1a\n\x16RELEASE_METHOD_INVALID\x10\x00\x12\x1e\n\x1aRELEASE_METHOD_UNSPECIFIED\x10\x01\x12\x1c\n\x18RELEASE_METHOD_MAIL_COPY\x10\x02\x12!\n\x1dRELEASE_METHOD_HOLD_FOR_TELEX\x10\x03\x32\x98\x03\n\x15MasterBillOfLadingAPI\x12\xbc\x01\n\x19GetMasterBillOfLadingList\x12N.flexport.monolith.masterbilloflading.v1beta1.GetMasterBillOfLadingListRequest\x1aO.flexport.monolith.masterbilloflading.v1beta1.GetMasterBillOfLadingListResponse\x12\xbf\x01\n\x1aGenerateMasterBillOfLading\x12O.flexport.monolith.masterbilloflading.v1beta1.GenerateMasterBillOfLadingRequest\x1aP.flexport.monolith.masterbilloflading.v1beta1.GenerateMasterBillOfLadingResponseB\x82\x01\n0com.flexport.monolith.masterbilloflading.v1beta1B\x1aMasterBillOfLadingApiProtoP\x01\xea\x02/Flexport::Monolith::MasterBillOfLading::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.masterbilloflading.v1beta1.master_bill_of_lading_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n0com.flexport.monolith.masterbilloflading.v1beta1B\032MasterBillOfLadingApiProtoP\001\352\002/Flexport::Monolith::MasterBillOfLading::V1Beta1"
    _globals["_TRANSMISSIONMODE"]._serialized_start = 2058
    _globals["_TRANSMISSIONMODE"]._serialized_end = 2201
    _globals["_RELEASEMETHOD"]._serialized_start = 2204
    _globals["_RELEASEMETHOD"]._serialized_end = 2344
    _globals["_GETMASTERBILLOFLADINGLISTREQUEST"]._serialized_start = 160
    _globals["_GETMASTERBILLOFLADINGLISTREQUEST"]._serialized_end = 761
    _globals["_GETMASTERBILLOFLADINGLISTREQUEST_STRINGLIST"]._serialized_start = 690
    _globals["_GETMASTERBILLOFLADINGLISTREQUEST_STRINGLIST"]._serialized_end = 718
    _globals["_GETMASTERBILLOFLADINGLISTREQUEST_INT32LIST"]._serialized_start = 720
    _globals["_GETMASTERBILLOFLADINGLISTREQUEST_INT32LIST"]._serialized_end = 747
    _globals["_GETMASTERBILLOFLADINGLISTRESPONSE"]._serialized_start = 764
    _globals["_GETMASTERBILLOFLADINGLISTRESPONSE"]._serialized_end = 897
    _globals["_GENERATEMASTERBILLOFLADINGREQUEST"]._serialized_start = 900
    _globals["_GENERATEMASTERBILLOFLADINGREQUEST"]._serialized_end = 1182
    _globals["_GENERATEMASTERBILLOFLADINGRESPONSE"]._serialized_start = 1184
    _globals["_GENERATEMASTERBILLOFLADINGRESPONSE"]._serialized_end = 1236
    _globals["_MASTERBILLOFLADING"]._serialized_start = 1239
    _globals["_MASTERBILLOFLADING"]._serialized_end = 2055
    _globals["_MASTERBILLOFLADINGAPI"]._serialized_start = 2347
    _globals["_MASTERBILLOFLADINGAPI"]._serialized_end = 2755
# @@protoc_insertion_point(module_scope)