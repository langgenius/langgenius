# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/dumboindexing/derivedshipment/v1beta1/filter_shipments_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nIflexport/dumboindexing/derivedshipment/v1beta1/filter_shipments_api.proto\x12.flexport.dumboindexing.derivedshipment.v1beta1\x1aJflexport/dumboindexing/derivedshipment/v1beta1/shipment_filter_input.proto"\xe1\x01\n\'ListShipmentIdentifiersByFiltersRequest\x12\x63\n\x15shipment_filter_input\x18\x01 \x01(\x0b\x32\x44.flexport.dumboindexing.derivedshipment.v1beta1.ShipmentFilterDetail\x12Q\n\x0cpage_request\x18\x02 \x01(\x0b\x32;.flexport.dumboindexing.derivedshipment.v1beta1.PageRequest"\xae\x01\n(ListShipmentIdentifiersByFiltersResponse\x12\x81\x01\n%shipment_identifier_pagination_detail\x18\x01 \x03(\x0b\x32R.flexport.dumboindexing.derivedshipment.v1beta1.ShipmentIdentifierPaginationDetail"z\n"ShipmentIdentifierPaginationDetail\x12\x1e\n\x14\x64\x65rived_shipment_fid\x18\x01 \x01(\tH\x00\x12\x16\n\x0cshipment_fid\x18\x02 \x01(\tH\x00\x12\x0e\n\x06\x63ursor\x18\x04 \x01(\tB\x0c\n\nidentifier"W\n\x0bPageRequest\x12\r\n\x05\x66irst\x18\x01 \x01(\r\x12\x0c\n\x04last\x18\x02 \x01(\r\x12\x14\n\x0c\x61\x66ter_cursor\x18\x03 \x01(\t\x12\x15\n\rbefore_cursor\x18\x04 \x01(\t2\xec\x01\n\x12\x46ilterShipmentsAPI\x12\xd5\x01\n ListShipmentIdentifiersByFilters\x12W.flexport.dumboindexing.derivedshipment.v1beta1.ListShipmentIdentifiersByFiltersRequest\x1aX.flexport.dumboindexing.derivedshipment.v1beta1.ListShipmentIdentifiersByFiltersResponseB\x83\x01\n2com.flexport.dumboindexing.derivedshipment.v1beta1B\x17\x46ilterShipmentsApiProtoP\x01\xea\x02\x31\x46lexport::DumboIndexing::DerivedShipment::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.dumboindexing.derivedshipment.v1beta1.filter_shipments_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n2com.flexport.dumboindexing.derivedshipment.v1beta1B\027FilterShipmentsApiProtoP\001\352\0021Flexport::DumboIndexing::DerivedShipment::V1Beta1"
    _globals["_LISTSHIPMENTIDENTIFIERSBYFILTERSREQUEST"]._serialized_start = 202
    _globals["_LISTSHIPMENTIDENTIFIERSBYFILTERSREQUEST"]._serialized_end = 427
    _globals["_LISTSHIPMENTIDENTIFIERSBYFILTERSRESPONSE"]._serialized_start = 430
    _globals["_LISTSHIPMENTIDENTIFIERSBYFILTERSRESPONSE"]._serialized_end = 604
    _globals["_SHIPMENTIDENTIFIERPAGINATIONDETAIL"]._serialized_start = 606
    _globals["_SHIPMENTIDENTIFIERPAGINATIONDETAIL"]._serialized_end = 728
    _globals["_PAGEREQUEST"]._serialized_start = 730
    _globals["_PAGEREQUEST"]._serialized_end = 817
    _globals["_FILTERSHIPMENTSAPI"]._serialized_start = 820
    _globals["_FILTERSHIPMENTSAPI"]._serialized_end = 1056
# @@protoc_insertion_point(module_scope)