# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/monolith/airexecution/hawb/v1beta1/house_air_waybill_engine_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nNflexport/monolith/airexecution/hawb/v1beta1/house_air_waybill_engine_api.proto\x12+flexport.monolith.airexecution.hawb.v1beta1\x1aGflexport/airshippingdoc/houseairwaybill/v1beta1/house_air_waybill.proto"8\n!ListEngineHouseAirWaybillsRequest\x12\x13\n\x0bshipment_id\x18\x01 \x01(\x05"\x92\x01\n"ListEngineHouseAirWaybillsResponse\x12\\\n\x12house_air_waybills\x18\x01 \x03(\x0b\x32@.flexport.airshippingdoc.houseairwaybill.v1beta1.HouseAirWaybill\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t"\x91\x01\n SaveEngineHouseAirWaybillRequest\x12[\n\x11house_air_waybill\x18\x01 \x01(\x0b\x32@.flexport.airshippingdoc.houseairwaybill.v1beta1.HouseAirWaybill\x12\x10\n\x08user_fid\x18\x02 \x01(\t"H\n!SaveEngineHouseAirWaybillResponse\x12\x13\n\x0bshipment_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t"d\n&UpdateEngineBillOfLadingAndMiscRequest\x12\x13\n\x0bshipment_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x62ill_number\x18\x02 \x01(\t\x12\x10\n\x08user_fid\x18\x03 \x01(\t"T\n\'UpdateEngineBillOfLadingAndMiscResponse\x12\x19\n\x11\x62ill_of_lading_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t2\xe0\x04\n\x12HouseAirWaybillAPI\x12\xbd\x01\n\x1aListEngineHouseAirWaybills\x12N.flexport.monolith.airexecution.hawb.v1beta1.ListEngineHouseAirWaybillsRequest\x1aO.flexport.monolith.airexecution.hawb.v1beta1.ListEngineHouseAirWaybillsResponse\x12\xba\x01\n\x19SaveEngineHouseAirWaybill\x12M.flexport.monolith.airexecution.hawb.v1beta1.SaveEngineHouseAirWaybillRequest\x1aN.flexport.monolith.airexecution.hawb.v1beta1.SaveEngineHouseAirWaybillResponse\x12\xcc\x01\n\x1fUpdateEngineBillOfLadingAndMisc\x12S.flexport.monolith.airexecution.hawb.v1beta1.UpdateEngineBillOfLadingAndMiscRequest\x1aT.flexport.monolith.airexecution.hawb.v1beta1.UpdateEngineBillOfLadingAndMiscResponseB\x84\x01\n/com.flexport.monolith.airexecution.hawb.v1beta1B\x1dHouseAirWaybillEngineApiProtoP\x01\xea\x02/Flexport::Monolith::AirExecution::HAWB::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.monolith.airexecution.hawb.v1beta1.house_air_waybill_engine_api_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n/com.flexport.monolith.airexecution.hawb.v1beta1B\035HouseAirWaybillEngineApiProtoP\001\352\002/Flexport::Monolith::AirExecution::HAWB::V1Beta1"
    _globals["_LISTENGINEHOUSEAIRWAYBILLSREQUEST"]._serialized_start = 200
    _globals["_LISTENGINEHOUSEAIRWAYBILLSREQUEST"]._serialized_end = 256
    _globals["_LISTENGINEHOUSEAIRWAYBILLSRESPONSE"]._serialized_start = 259
    _globals["_LISTENGINEHOUSEAIRWAYBILLSRESPONSE"]._serialized_end = 405
    _globals["_SAVEENGINEHOUSEAIRWAYBILLREQUEST"]._serialized_start = 408
    _globals["_SAVEENGINEHOUSEAIRWAYBILLREQUEST"]._serialized_end = 553
    _globals["_SAVEENGINEHOUSEAIRWAYBILLRESPONSE"]._serialized_start = 555
    _globals["_SAVEENGINEHOUSEAIRWAYBILLRESPONSE"]._serialized_end = 627
    _globals["_UPDATEENGINEBILLOFLADINGANDMISCREQUEST"]._serialized_start = 629
    _globals["_UPDATEENGINEBILLOFLADINGANDMISCREQUEST"]._serialized_end = 729
    _globals["_UPDATEENGINEBILLOFLADINGANDMISCRESPONSE"]._serialized_start = 731
    _globals["_UPDATEENGINEBILLOFLADINGANDMISCRESPONSE"]._serialized_end = 815
    _globals["_HOUSEAIRWAYBILLAPI"]._serialized_start = 818
    _globals["_HOUSEAIRWAYBILLAPI"]._serialized_end = 1426
# @@protoc_insertion_point(module_scope)