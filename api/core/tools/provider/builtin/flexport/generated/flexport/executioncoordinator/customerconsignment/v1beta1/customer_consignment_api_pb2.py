# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executioncoordinator/customerconsignment/v1beta1/customer_consignment_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nXflexport/executioncoordinator/customerconsignment/v1beta1/customer_consignment_api.proto\x12\x39\x66lexport.executioncoordinator.customerconsignment.v1beta1\x1aTflexport/executioncoordinator/customerconsignment/v1beta1/customer_consignment.proto\x1a`flexport/executioncoordinator/customerconsignment/v1beta1/customer_consignment_measurement.proto"c\n\x1dGetCustomerConsignmentRequest\x12\x1d\n\x15\x65xternal_reference_id\x18\x01 \x01(\t\x12#\n\x1b\x65xternal_company_entity_fid\x18\x02 \x01(\t"\x95\x02\n\x1eGetCustomerConsignmentResponse\x12l\n\x14\x63ustomer_consignment\x18\x01 \x01(\x0b\x32N.flexport.executioncoordinator.customerconsignment.v1beta1.CustomerConsignment\x12\x84\x01\n!customer_consignment_measurements\x18\x02 \x03(\x0b\x32Y.flexport.executioncoordinator.customerconsignment.v1beta1.CustomerConsignmentMeasurement".\n\x1eGetCustomerConsignmentsRequest\x12\x0c\n\x04\x66ids\x18\x01 \x03(\t"\x82\x02\n\x1fGetCustomerConsignmentsResponse\x12q\n\x15\x63ustomer_consignments\x18\x01 \x03(\x0b\x32N.flexport.executioncoordinator.customerconsignment.v1beta1.CustomerConsignmentB\x02\x18\x01\x12l\n\tresponses\x18\x02 \x03(\x0b\x32Y.flexport.executioncoordinator.customerconsignment.v1beta1.GetCustomerConsignmentResponse"\x90\x01\n CreateCustomerConsignmentRequest\x12l\n\x14\x63ustomer_consignment\x18\x01 \x01(\x0b\x32N.flexport.executioncoordinator.customerconsignment.v1beta1.CustomerConsignment"\x91\x01\n!CreateCustomerConsignmentResponse\x12l\n\x14\x63ustomer_consignment\x18\x01 \x01(\x0b\x32N.flexport.executioncoordinator.customerconsignment.v1beta1.CustomerConsignment2\x94\x05\n\x16\x43ustomerConsignmentAPI\x12\xcd\x01\n\x16GetCustomerConsignment\x12X.flexport.executioncoordinator.customerconsignment.v1beta1.GetCustomerConsignmentRequest\x1aY.flexport.executioncoordinator.customerconsignment.v1beta1.GetCustomerConsignmentResponse\x12\xd0\x01\n\x17GetCustomerConsignments\x12Y.flexport.executioncoordinator.customerconsignment.v1beta1.GetCustomerConsignmentsRequest\x1aZ.flexport.executioncoordinator.customerconsignment.v1beta1.GetCustomerConsignmentsResponse\x12\xd6\x01\n\x19\x43reateCustomerConsignment\x12[.flexport.executioncoordinator.customerconsignment.v1beta1.CreateCustomerConsignmentRequest\x1a\\.flexport.executioncoordinator.customerconsignment.v1beta1.CreateCustomerConsignmentResponseB\x9d\x01\n=com.flexport.executioncoordinator.customerconsignment.v1beta1B\x1b\x43ustomerConsignmentApiProtoP\x01\xea\x02<Flexport::ExecutionCoordinator::CustomerConsignment::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executioncoordinator.customerconsignment.v1beta1.customer_consignment_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n=com.flexport.executioncoordinator.customerconsignment.v1beta1B\033CustomerConsignmentApiProtoP\001\352\002<Flexport::ExecutionCoordinator::CustomerConsignment::V1Beta1"
    _globals["_GETCUSTOMERCONSIGNMENTSRESPONSE"].fields_by_name["customer_consignments"]._options = None
    _globals["_GETCUSTOMERCONSIGNMENTSRESPONSE"].fields_by_name[
        "customer_consignments"
    ]._serialized_options = b"\030\001"
    _globals["_GETCUSTOMERCONSIGNMENTREQUEST"]._serialized_start = 335
    _globals["_GETCUSTOMERCONSIGNMENTREQUEST"]._serialized_end = 434
    _globals["_GETCUSTOMERCONSIGNMENTRESPONSE"]._serialized_start = 437
    _globals["_GETCUSTOMERCONSIGNMENTRESPONSE"]._serialized_end = 714
    _globals["_GETCUSTOMERCONSIGNMENTSREQUEST"]._serialized_start = 716
    _globals["_GETCUSTOMERCONSIGNMENTSREQUEST"]._serialized_end = 762
    _globals["_GETCUSTOMERCONSIGNMENTSRESPONSE"]._serialized_start = 765
    _globals["_GETCUSTOMERCONSIGNMENTSRESPONSE"]._serialized_end = 1023
    _globals["_CREATECUSTOMERCONSIGNMENTREQUEST"]._serialized_start = 1026
    _globals["_CREATECUSTOMERCONSIGNMENTREQUEST"]._serialized_end = 1170
    _globals["_CREATECUSTOMERCONSIGNMENTRESPONSE"]._serialized_start = 1173
    _globals["_CREATECUSTOMERCONSIGNMENTRESPONSE"]._serialized_end = 1318
    _globals["_CUSTOMERCONSIGNMENTAPI"]._serialized_start = 1321
    _globals["_CUSTOMERCONSIGNMENTAPI"]._serialized_end = 1981
# @@protoc_insertion_point(module_scope)