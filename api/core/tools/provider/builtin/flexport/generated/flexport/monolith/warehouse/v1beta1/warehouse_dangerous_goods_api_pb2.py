# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/warehouse/v1beta1/warehouse_dangerous_goods_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\nGflexport/monolith/warehouse/v1beta1/warehouse_dangerous_goods_api.proto\x12#flexport.monolith.warehouse.v1beta1\"W\n'CheckDangerousGoodsLabelMismatchRequest\x12\x13\n\x0bshipment_id\x18\x01 \x01(\t\x12\x17\n\x0f\x64g_label_groups\x18\x02 \x03(\t\"z\n(CheckDangerousGoodsLabelMismatchResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x13\n\x0bis_mismatch\x18\x02 \x01(\x08\x12\x18\n\x10mismatch_message\x18\x03 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x04 \x03(\t2\xde\x01\n\x1aWarehouseDangerousGoodsAPI\x12\xbf\x01\n CheckDangerousGoodsLabelMismatch\x12L.flexport.monolith.warehouse.v1beta1.CheckDangerousGoodsLabelMismatchRequest\x1aM.flexport.monolith.warehouse.v1beta1.CheckDangerousGoodsLabelMismatchResponseBu\n'com.flexport.monolith.warehouse.v1beta1B\x1fWarehouseDangerousGoodsApiProtoP\x01\xea\x02&Flexport::Monolith::Warehouse::V1Beta1b\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.warehouse.v1beta1.warehouse_dangerous_goods_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n'com.flexport.monolith.warehouse.v1beta1B\037WarehouseDangerousGoodsApiProtoP\001\352\002&Flexport::Monolith::Warehouse::V1Beta1"
    _globals["_CHECKDANGEROUSGOODSLABELMISMATCHREQUEST"]._serialized_start = 112
    _globals["_CHECKDANGEROUSGOODSLABELMISMATCHREQUEST"]._serialized_end = 199
    _globals["_CHECKDANGEROUSGOODSLABELMISMATCHRESPONSE"]._serialized_start = 201
    _globals["_CHECKDANGEROUSGOODSLABELMISMATCHRESPONSE"]._serialized_end = 323
    _globals["_WAREHOUSEDANGEROUSGOODSAPI"]._serialized_start = 326
    _globals["_WAREHOUSEDANGEROUSGOODSAPI"]._serialized_end = 548
# @@protoc_insertion_point(module_scope)