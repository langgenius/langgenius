# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/workflow/autoasn/models/shipment/v1beta1/shipment.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n@flexport/workflow/autoasn/models/shipment/v1beta1/shipment.proto\x12\x31\x66lexport.workflow.autoasn.models.shipment.v1beta1\x1a\x32\x66lexport/workflow/prelude/options/v1/options.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8e\x05\n\x08Shipment\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12L\n\x08shippers\x18\x02 \x03(\x0b\x32:.flexport.workflow.autoasn.models.shipment.v1beta1.Company\x12N\n\nconsignees\x18\x03 \x03(\x0b\x32:.flexport.workflow.autoasn.models.shipment.v1beta1.Company\x12G\n\x05graph\x18\x04 \x01(\x0b\x32\x38.flexport.workflow.autoasn.models.shipment.v1beta1.Graph\x12\x61\n\x13\x63ommercial_invoices\x18\x05 \x03(\x0b\x32\x44.flexport.workflow.autoasn.models.shipment.v1beta1.CommercialInvoice\x12\x10\n\x08priority\x18\x06 \x01(\t\x12\x14\n\x0c\x62ooking_mode\x18\x07 \x01(\t\x12_\n\x12\x63hecklist_send_asn\x18\x08 \x01(\x0b\x32\x43.flexport.workflow.autoasn.models.shipment.v1beta1.ChecklistSendAsn\x12N\n\tdocuments\x18\t \x03(\x0b\x32;.flexport.workflow.autoasn.models.shipment.v1beta1.Document\x12I\n\x06\x63lient\x18\n \x01(\x0b\x32\x39.flexport.workflow.autoasn.models.shipment.v1beta1.Client:\x07\x82\xf1\x04\x03\x66id"\x15\n\x06\x43lient\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"0\n\x07\x43ompany\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\x12\x0c\n\x04name\x18\x03 \x01(\t"n\n\x11\x43ommercialInvoice\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12L\n\x08products\x18\x02 \x03(\x0b\x32:.flexport.workflow.autoasn.models.shipment.v1beta1.Product"\x16\n\x07Product\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"\x88\x02\n\x05Graph\x12N\n\x05nodes\x18\x0b \x03(\x0b\x32?.flexport.workflow.autoasn.models.shipment.v1beta1.ShipmentNode\x12T\n\x10origin_addresses\x18\x0f \x03(\x0b\x32:.flexport.workflow.autoasn.models.shipment.v1beta1.Address\x12Y\n\x15\x64\x65stination_addresses\x18\x10 \x03(\x0b\x32:.flexport.workflow.autoasn.models.shipment.v1beta1.Address"e\n\x0cShipmentNode\x12\n\n\x02id\x18\x01 \x01(\x03\x12I\n\x05place\x18\x02 \x01(\x0b\x32:.flexport.workflow.autoasn.models.shipment.v1beta1.Address"{\n\x07\x41\x64\x64ress\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12M\n\x08location\x18\x02 \x01(\x0b\x32;.flexport.workflow.autoasn.models.shipment.v1beta1.Location\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t"\x17\n\x08Location\x12\x0b\n\x03\x66id\x18\x01 \x01(\t"\x85\x01\n\x10\x43hecklistSendAsn\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x15\n\rstatus_reason\x18\x04 \x01(\t\x12\x30\n\x0cupdated_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"\xa9\x03\n\x08\x44ocument\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x1f\n\x17\x61ttachment_content_type\x18\x02 \x01(\t\x12\x1b\n\x13\x61ttachment_filename\x18\x03 \x01(\t\x12;\n\x17\x61ttachment_updated_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x18\n\x10\x64ocument_type_id\x18\x06 \x01(\x03\x12V\n\rdocument_type\x18\x07 \x01(\x0b\x32?.flexport.workflow.autoasn.models.shipment.v1beta1.DocumentType\x12\x30\n\x0cupdated_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rarchived_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x65xpires_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp"7\n\x0c\x44ocumentType\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04slug\x18\x03 \x01(\tB\x81\x01\n5com.flexport.workflow.autoasn.models.shipment.v1beta1B\rShipmentProtoP\x01\xea\x02\x36\x46lexport::Workflow::AutoAsn::Models::Shipment::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.workflow.autoasn.models.shipment.v1beta1.shipment_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n5com.flexport.workflow.autoasn.models.shipment.v1beta1B\rShipmentProtoP\001\352\0026Flexport::Workflow::AutoAsn::Models::Shipment::V1Beta1"
    _globals["_SHIPMENT"]._options = None
    _globals["_SHIPMENT"]._serialized_options = b"\202\361\004\003fid"
    _globals["_SHIPMENT"]._serialized_start = 205
    _globals["_SHIPMENT"]._serialized_end = 859
    _globals["_CLIENT"]._serialized_start = 861
    _globals["_CLIENT"]._serialized_end = 882
    _globals["_COMPANY"]._serialized_start = 884
    _globals["_COMPANY"]._serialized_end = 932
    _globals["_COMMERCIALINVOICE"]._serialized_start = 934
    _globals["_COMMERCIALINVOICE"]._serialized_end = 1044
    _globals["_PRODUCT"]._serialized_start = 1046
    _globals["_PRODUCT"]._serialized_end = 1068
    _globals["_GRAPH"]._serialized_start = 1071
    _globals["_GRAPH"]._serialized_end = 1335
    _globals["_SHIPMENTNODE"]._serialized_start = 1337
    _globals["_SHIPMENTNODE"]._serialized_end = 1438
    _globals["_ADDRESS"]._serialized_start = 1440
    _globals["_ADDRESS"]._serialized_end = 1563
    _globals["_LOCATION"]._serialized_start = 1565
    _globals["_LOCATION"]._serialized_end = 1588
    _globals["_CHECKLISTSENDASN"]._serialized_start = 1591
    _globals["_CHECKLISTSENDASN"]._serialized_end = 1724
    _globals["_DOCUMENT"]._serialized_start = 1727
    _globals["_DOCUMENT"]._serialized_end = 2152
    _globals["_DOCUMENTTYPE"]._serialized_start = 2154
    _globals["_DOCUMENTTYPE"]._serialized_end = 2209
# @@protoc_insertion_point(module_scope)