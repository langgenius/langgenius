# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/assignment/grpc/shipmentinfofetcher/v1beta1/shipment_info_fetcher_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nTflexport/assignment/grpc/shipmentinfofetcher/v1beta1/shipment_info_fetcher_api.proto\x12\x34\x66lexport.assignment.grpc.shipmentinfofetcher.v1beta1\x1a[flexport/assignment/grpc/shipmentinfofetcher/v1beta1/shipment_first_quote_accepted_at.proto\x1aPflexport/assignment/grpc/shipmentinfofetcher/v1beta1/shipment_quote_status.proto"8\n\x1fListFirstQuoteAcceptedAtRequest\x12\x15\n\rshipment_fids\x18\x01 \x03(\t"\x87\x01\n ListFirstQuoteAcceptedAtResponse\x12\x63\n\x07results\x18\x01 \x03(\x0b\x32R.flexport.assignment.grpc.shipmentinfofetcher.v1beta1.ShipmentFirstQuoteAcceptedAt"/\n\x16ListQuoteStatusRequest\x12\x15\n\rshipment_fids\x18\x01 \x03(\t"u\n\x17ListQuoteStatusResponse\x12Z\n\x07results\x18\x01 \x03(\x0b\x32I.flexport.assignment.grpc.shipmentinfofetcher.v1beta1.ShipmentQuoteStatus2\x95\x03\n\x16ShipmentInfoFetcherAPI\x12\xc9\x01\n\x18ListFirstQuoteAcceptedAt\x12U.flexport.assignment.grpc.shipmentinfofetcher.v1beta1.ListFirstQuoteAcceptedAtRequest\x1aV.flexport.assignment.grpc.shipmentinfofetcher.v1beta1.ListFirstQuoteAcceptedAtResponse\x12\xae\x01\n\x0fListQuoteStatus\x12L.flexport.assignment.grpc.shipmentinfofetcher.v1beta1.ListQuoteStatusRequest\x1aM.flexport.assignment.grpc.shipmentinfofetcher.v1beta1.ListQuoteStatusResponseB\x94\x01\n8com.flexport.assignment.grpc.shipmentinfofetcher.v1beta1B\x1bShipmentInfoFetcherApiProtoP\x01\xea\x02\x38\x46lexport::Assignment::Grpc::ShipmentInfoFetcher::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.assignment.grpc.shipmentinfofetcher.v1beta1.shipment_info_fetcher_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n8com.flexport.assignment.grpc.shipmentinfofetcher.v1beta1B\033ShipmentInfoFetcherApiProtoP\001\352\0028Flexport::Assignment::Grpc::ShipmentInfoFetcher::V1Beta1"
    _globals["_LISTFIRSTQUOTEACCEPTEDATREQUEST"]._serialized_start = 317
    _globals["_LISTFIRSTQUOTEACCEPTEDATREQUEST"]._serialized_end = 373
    _globals["_LISTFIRSTQUOTEACCEPTEDATRESPONSE"]._serialized_start = 376
    _globals["_LISTFIRSTQUOTEACCEPTEDATRESPONSE"]._serialized_end = 511
    _globals["_LISTQUOTESTATUSREQUEST"]._serialized_start = 513
    _globals["_LISTQUOTESTATUSREQUEST"]._serialized_end = 560
    _globals["_LISTQUOTESTATUSRESPONSE"]._serialized_start = 562
    _globals["_LISTQUOTESTATUSRESPONSE"]._serialized_end = 679
    _globals["_SHIPMENTINFOFETCHERAPI"]._serialized_start = 682
    _globals["_SHIPMENTINFOFETCHERAPI"]._serialized_end = 1087
# @@protoc_insertion_point(module_scope)