# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/catalog/offering/v2beta1/offering.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n0flexport/catalog/offering/v2beta1/offering.proto\x12!flexport.catalog.offering.v2beta1\x1a,flexport/catalog/charge/v2beta1/charge.proto\x1a#flexport/catalog/date/v1/date.proto\x1a/flexport/catalog/offering/air/v2beta1/air.proto\x1a=flexport/catalog/offering/carbonoffset/v1/carbon_offset.proto\x1a\x37\x66lexport/catalog/offering/cartage/v2beta1/cartage.proto\x1a:flexport/catalog/offering/destination/v1/destination.proto\x1a\x37\x66lexport/catalog/offering/drayage/v2beta1/drayage.proto\x1a?flexport/catalog/offering/exportcustoms/v1/export_customs.proto\x1a*flexport/catalog/offering/ftl/v1/ftl.proto\x1aLflexport/catalog/offering/global_conveyor_belt/v1/global_conveyor_belt.proto\x1a?flexport/catalog/offering/importcustoms/v1/import_customs.proto\x1a\x36\x66lexport/catalog/offering/insurance/v1/insurance.proto\x1a\x35\x66lexport/catalog/offering/linehaul/v1/line_haul.proto\x1a\x35\x66lexport/catalog/offering/oceanfcl/v1/ocean_fcl.proto\x1a:flexport/catalog/offering/oceanfcl/v2beta1/ocean_fcl.proto\x1a\x35\x66lexport/catalog/offering/oceanlcl/v1/ocean_lcl.proto\x1a\x30\x66lexport/catalog/offering/origin/v1/origin.proto\x1a\x33\x66lexport/catalog/restrictions/v1/restrictions.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xbb\x0f\n\x11\x43lientOfferingDto\x12)\n\x03\x66id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nclient_fid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x0f\x61\x63tivation_date\x18\x03 \x01(\x0b\x32!.flexport.catalog.date.v1.DateDto\x12:\n\x0f\x65xpiration_date\x18\x04 \x01(\x0b\x32!.flexport.catalog.date.v1.DateDto\x12\x39\n\x13\x66reight_partner_fid\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tfree_text\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0e\x63reated_by_fid\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0f\x63reated_at_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\x07\x63harges\x18\t \x03(\x0b\x32\x30.flexport.catalog.charge.v2beta1.ClientChargeDto\x12\x45\n\ntotal_cost\x18\n \x01(\x0b\x32\x31.flexport.catalog.charge.v2beta1.EvaluatedRateDto\x12\x45\n\ntotal_sell\x18\x0b \x01(\x0b\x32\x31.flexport.catalog.charge.v2beta1.EvaluatedRateDto\x12G\n\x0crestrictions\x18\x0c \x01(\x0b\x32\x31.flexport.catalog.restrictions.v1.RestrictionsDto\x12\x0e\n\x06is_nac\x18\r \x01(\x08\x12\x46\n\x03\x61ir\x18\x65 \x01(\x0b\x32\x37.flexport.catalog.offering.air.v2beta1.AirAttributesDtoH\x00\x12]\n\rcarbon_offset\x18\x66 \x01(\x0b\x32\x44.flexport.catalog.offering.carbonoffset.v1.CarbonOffsetAttributesDtoH\x00\x12R\n\x07\x63\x61rtage\x18g \x01(\x0b\x32?.flexport.catalog.offering.cartage.v2beta1.CartageAttributesDtoH\x00\x12Y\n\x0b\x64\x65stination\x18h \x01(\x0b\x32\x42.flexport.catalog.offering.destination.v1.DestinationAttributesDtoH\x00\x12R\n\x07\x64rayage\x18i \x01(\x0b\x32?.flexport.catalog.offering.drayage.v2beta1.DrayageAttributesDtoH\x00\x12`\n\x0e\x65xport_customs\x18j \x01(\x0b\x32\x46.flexport.catalog.offering.exportcustoms.v1.ExportCustomsAttributesDtoH\x00\x12`\n\x0eimport_customs\x18k \x01(\x0b\x32\x46.flexport.catalog.offering.importcustoms.v1.ImportCustomsAttributesDtoH\x00\x12S\n\tinsurance\x18l \x01(\x0b\x32>.flexport.catalog.offering.insurance.v1.InsuranceAttributesDtoH\x00\x12Q\n\tline_haul\x18m \x01(\x0b\x32<.flexport.catalog.offering.linehaul.v1.LineHaulAttributesDtoH\x00\x12Q\n\tocean_fcl\x18n \x01(\x0b\x32<.flexport.catalog.offering.oceanfcl.v1.OceanFclAttributesDtoH\x00\x12Q\n\tocean_lcl\x18o \x01(\x0b\x32<.flexport.catalog.offering.oceanlcl.v1.OceanLclAttributesDtoH\x00\x12J\n\x06origin\x18p \x01(\x0b\x32\x38.flexport.catalog.offering.origin.v1.OriginAttributesDtoH\x00\x12\x41\n\x03\x66tl\x18q \x01(\x0b\x32\x32.flexport.catalog.offering.ftl.v1.FtlAttributesDtoH\x00\x12r\n\x14global_conveyor_belt\x18r \x01(\x0b\x32R.flexport.catalog.offering.global_conveyor_belt.v1.GlobalConveyorBeltAttributesDtoH\x00\x42\x11\n\x0ftype_attributes"\xb6\n\n ClientOfferingQueryAttributesDto\x12\x30\n\nclient_fid\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x07on_date\x18\x02 \x01(\x0b\x32!.flexport.catalog.date.v1.DateDto\x12\x1c\n\x14\x66reight_partner_fids\x18\x03 \x03(\t\x12\x32\n\x0cshipment_fid\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12K\n\x03\x61ir\x18\x65 \x01(\x0b\x32<.flexport.catalog.offering.air.v2beta1.AirQueryAttributesDtoH\x00\x12\x62\n\rcarbon_offset\x18\x66 \x01(\x0b\x32I.flexport.catalog.offering.carbonoffset.v1.CarbonOffsetQueryAttributesDtoH\x00\x12W\n\x07\x63\x61rtage\x18g \x01(\x0b\x32\x44.flexport.catalog.offering.cartage.v2beta1.CartageQueryAttributesDtoH\x00\x12^\n\x0b\x64\x65stination\x18h \x01(\x0b\x32G.flexport.catalog.offering.destination.v1.DestinationQueryAttributesDtoH\x00\x12W\n\x07\x64rayage\x18i \x01(\x0b\x32\x44.flexport.catalog.offering.drayage.v2beta1.DrayageQueryAttributesDtoH\x00\x12\x65\n\x0e\x65xport_customs\x18j \x01(\x0b\x32K.flexport.catalog.offering.exportcustoms.v1.ExportCustomsQueryAttributesDtoH\x00\x12\x65\n\x0eimport_customs\x18k \x01(\x0b\x32K.flexport.catalog.offering.importcustoms.v1.ImportCustomsQueryAttributesDtoH\x00\x12X\n\tinsurance\x18l \x01(\x0b\x32\x43.flexport.catalog.offering.insurance.v1.InsuranceQueryAttributesDtoH\x00\x12V\n\tline_haul\x18m \x01(\x0b\x32\x41.flexport.catalog.offering.linehaul.v1.LineHaulQueryAttributesDtoH\x00\x12[\n\tocean_fcl\x18n \x01(\x0b\x32\x46.flexport.catalog.offering.oceanfcl.v2beta1.OceanFclQueryAttributesDtoH\x00\x12V\n\tocean_lcl\x18o \x01(\x0b\x32\x41.flexport.catalog.offering.oceanlcl.v1.OceanLclQueryAttributesDtoH\x00\x12O\n\x06origin\x18p \x01(\x0b\x32=.flexport.catalog.offering.origin.v1.OriginQueryAttributesDtoH\x00\x42\x11\n\x0ftype_attributes*\x88\x01\n\tSortByDto\x12\x17\n\x13SORT_BY_DTO_INVALID\x10\x00\x12\x14\n\x10SORT_BY_DTO_SELL\x10\x01\x12\x1c\n\x18SORT_BY_DTO_TRANSIT_TIME\x10\x02\x12\x18\n\x14SORT_BY_DTO_DISTANCE\x10\x03\x12\x14\n\x10SORT_BY_DTO_COST\x10\x04\x42_\n%com.flexport.catalog.offering.v2beta1B\rOfferingProtoP\x01\xea\x02$Flexport::Catalog::Offering::V2Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.catalog.offering.v2beta1.offering_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n%com.flexport.catalog.offering.v2beta1B\rOfferingProtoP\001\352\002$Flexport::Catalog::Offering::V2Beta1"
    )
    _globals["_SORTBYDTO"]._serialized_start = 4477
    _globals["_SORTBYDTO"]._serialized_end = 4613
    _globals["_CLIENTOFFERINGDTO"]._serialized_start = 1158
    _globals["_CLIENTOFFERINGDTO"]._serialized_end = 3137
    _globals["_CLIENTOFFERINGQUERYATTRIBUTESDTO"]._serialized_start = 3140
    _globals["_CLIENTOFFERINGQUERYATTRIBUTESDTO"]._serialized_end = 4474
# @@protoc_insertion_point(module_scope)