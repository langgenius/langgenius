# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/documentprocessor/documentschema/v1beta1/arrival_notice.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nFflexport/documentprocessor/documentschema/v1beta1/arrival_notice.proto\x12\x31\x66lexport.documentprocessor.documentschema.v1beta1\x1a\x46\x66lexport/documentprocessor/documentschema/v1beta1/document_field.proto"\xf0\x05\n\x16\x41rrivalNoticeContainer\x12Z\n\x10\x63ontainer_number\x18\x01 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12U\n\x0bseal_number\x18\x02 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12X\n\x0e\x63ontainer_type\x18\x03 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12\x61\n\x17total_container_cartons\x18\x04 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12V\n\x0cgross_weight\x18\x05 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12`\n\x16gross_weight_unit_type\x18\x06 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12P\n\x06volume\x18\x07 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12Z\n\x10volume_unit_type\x18\x08 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField"\xd2\x13\n\rArrivalNotice\x12U\n\x0b\x66irms_codes\x18P \x03(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12V\n\x0cgross_weight\x18\x13 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12W\n\rtotal_cartons\x18. \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12\x61\n\x17total_container_cartons\x18/ \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12T\n\nmbl_number\x18\x38 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12[\n\x11\x63ontainer_numbers\x18O \x03(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12V\n\x0c\x63\x61rrier_scac\x18: \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12_\n\x15\x63ommodity_description\x18; \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12k\n!consignee_master_name_and_address\x18< \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12[\n\x11\x64\x65stination_agent\x18= \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12_\n\x15\x65ta_place_of_delivery\x18> \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12_\n\x15\x65ta_port_of_discharge\x18? \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12S\n\tit_number\x18@ \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12T\n\nissue_date\x18\x41 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12W\n\rmother_vessel\x18\x42 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12V\n\x0cnotify_party\x18\x43 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12Y\n\x0fpickup_location\x18\x44 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12U\n\x0bpiece_count\x18\x45 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12Z\n\x10place_of_receipt\x18\x46 \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12[\n\x11port_of_discharge\x18G \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12Y\n\x0fport_of_loading\x18H \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12i\n\x1fshipper_master_name_and_address\x18I \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12S\n\tunit_type\x18J \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12Y\n\x0fvendor_wordmark\x18K \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12W\n\rvoyage_number\x18L \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12Q\n\x07waybill\x18M \x01(\x0b\x32@.flexport.documentprocessor.documentschema.v1beta1.DocumentField\x12]\n\ncontainers\x18N \x03(\x0b\x32I.flexport.documentprocessor.documentschema.v1beta1.ArrivalNoticeContainerJ\x04\x08\x01\x10\x13J\x04\x08\x14\x10.J\x04\x08\x30\x10\x38J\x04\x08\x39\x10:B\x84\x01\n5com.flexport.documentprocessor.documentschema.v1beta1B\x12\x41rrivalNoticeProtoP\x01\xea\x02\x34\x46lexport::DocumentProcessor::DocumentSchema::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.documentprocessor.documentschema.v1beta1.arrival_notice_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n5com.flexport.documentprocessor.documentschema.v1beta1B\022ArrivalNoticeProtoP\001\352\0024Flexport::DocumentProcessor::DocumentSchema::V1Beta1"
    _globals["_ARRIVALNOTICECONTAINER"]._serialized_start = 198
    _globals["_ARRIVALNOTICECONTAINER"]._serialized_end = 950
    _globals["_ARRIVALNOTICE"]._serialized_start = 953
    _globals["_ARRIVALNOTICE"]._serialized_end = 3467
# @@protoc_insertion_point(module_scope)