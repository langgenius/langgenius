# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/oex/carrierbookingbundle/v1beta1/carrier_booking_bundle_internal_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nSflexport/oex/carrierbookingbundle/v1beta1/carrier_booking_bundle_internal_api.proto\x12)flexport.oex.carrierbookingbundle.v1beta1\x1a\x46\x66lexport/oex/carrierbookingbundle/v1beta1/carrier_booking_bundle.proto"\xe7\x01\n\x1ePutCarrierBookingBundleRequest\x12\x63\n\x16\x63\x61rrier_booking_bundle\x18\x01 \x01(\x0b\x32?.flexport.oex.carrierbookingbundle.v1beta1.CarrierBookingBundleB\x02\x18\x01\x12`\n\x17\x63\x61rrier_booking_bundles\x18\x02 \x03(\x0b\x32?.flexport.oex.carrierbookingbundle.v1beta1.CarrierBookingBundle"`\n\x1fPutCarrierBookingBundleResponse\x12\x1f\n\x13\x63\x61rrier_booking_fid\x18\x01 \x01(\tB\x02\x18\x01\x12\x1c\n\x14\x63\x61rrier_booking_fids\x18\x02 \x03(\t2\xd9\x01\n\x1f\x43\x61rrierBookingBundleInternalAPI\x12\xb5\x01\n\x17PutCarrierBookingBundle\x12I.flexport.oex.carrierbookingbundle.v1beta1.PutCarrierBookingBundleRequest\x1aJ.flexport.oex.carrierbookingbundle.v1beta1.PutCarrierBookingBundleResponse"\x03\x90\x02\x02\x42\x86\x01\n-com.flexport.oex.carrierbookingbundle.v1beta1B$CarrierBookingBundleInternalApiProtoP\x01\xea\x02,Flexport::OEX::CarrierBookingBundle::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.oex.carrierbookingbundle.v1beta1.carrier_booking_bundle_internal_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n-com.flexport.oex.carrierbookingbundle.v1beta1B$CarrierBookingBundleInternalApiProtoP\001\352\002,Flexport::OEX::CarrierBookingBundle::V1Beta1"
    _globals["_PUTCARRIERBOOKINGBUNDLEREQUEST"].fields_by_name["carrier_booking_bundle"]._options = None
    _globals["_PUTCARRIERBOOKINGBUNDLEREQUEST"].fields_by_name[
        "carrier_booking_bundle"
    ]._serialized_options = b"\030\001"
    _globals["_PUTCARRIERBOOKINGBUNDLERESPONSE"].fields_by_name["carrier_booking_fid"]._options = None
    _globals["_PUTCARRIERBOOKINGBUNDLERESPONSE"].fields_by_name["carrier_booking_fid"]._serialized_options = b"\030\001"
    _globals["_CARRIERBOOKINGBUNDLEINTERNALAPI"].methods_by_name["PutCarrierBookingBundle"]._options = None
    _globals["_CARRIERBOOKINGBUNDLEINTERNALAPI"].methods_by_name[
        "PutCarrierBookingBundle"
    ]._serialized_options = b"\220\002\002"
    _globals["_PUTCARRIERBOOKINGBUNDLEREQUEST"]._serialized_start = 203
    _globals["_PUTCARRIERBOOKINGBUNDLEREQUEST"]._serialized_end = 434
    _globals["_PUTCARRIERBOOKINGBUNDLERESPONSE"]._serialized_start = 436
    _globals["_PUTCARRIERBOOKINGBUNDLERESPONSE"]._serialized_end = 532
    _globals["_CARRIERBOOKINGBUNDLEINTERNALAPI"]._serialized_start = 535
    _globals["_CARRIERBOOKINGBUNDLEINTERNALAPI"]._serialized_end = 752
# @@protoc_insertion_point(module_scope)