# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customscargomanifestquery/entities/v1beta1/cargo_manifest_master_bill_of_lading.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n^flexport/customscargomanifestquery/entities/v1beta1/cargo_manifest_master_bill_of_lading.proto\x12\x33\x66lexport.customscargomanifestquery.entities.v1beta1\x1a\x63\x66lexport/customscargomanifestquery/entities/v1beta1/cargo_manifest_bill_of_lading_disposition.proto\x1a_flexport/customscargomanifestquery/entities/v1beta1/cargo_manifest_bill_of_lading_in_bond.proto\x1a]flexport/customscargomanifestquery/entities/v1beta1/cargo_manifest_house_bill_of_lading.proto\x1a\x61\x66lexport/customscargomanifestquery/enums/v1beta1/customs_cargo_manifest_bill_of_lading_type.proto\x1a\x64\x66lexport/customscargomanifestquery/enums/v1beta1/customs_cargo_manifest_mode_of_transportation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto"\xb9\n\n\x1f\x43\x61rgoManifestMasterBillOfLading\x12\x1a\n\x12master_bill_number\x18\x01 \x01(\t\x12\x13\n\x0bisf_on_file\x18\x02 \x01(\x08\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x14\n\x0c\x63\x61rrier_code\x18\x04 \x01(\t\x12*\n\x0f\x64\x61te_of_arrival\x18\x05 \x01(\x0b\x32\x11.google.type.Date\x12\x19\n\x11manifest_quantity\x18\x06 \x01(\x05\x12\x13\n\x0bissuer_code\x18\x07 \x01(\t\x12&\n\x1evoyage_or_trip_manifest_number\x18\x08 \x01(\t\x12:\n2importing_vessel_code_or_importing_conveyance_name\x18\t \x01(\t\x12\x30\n\x15vessel_departure_date\x18\n \x01(\x0b\x32\x11.google.type.Date\x12"\n\x1avessel_departure_port_code\x18\x0b \x01(\t\x12\x32\n*manifested_port_of_unlading_or_import_code\x18\x0c \x01(\t\x12\x1a\n\rport_of_entry\x18\r \x01(\x05H\x00\x88\x01\x01\x12\x12\n\nfirms_code\x18\x0e \x01(\t\x12\x19\n\x11\x66irms_trip_number\x18\x0f \x01(\t\x12.\n&actual_port_of_unlading_or_import_code\x18\x10 \x01(\t\x12\x1d\n\x10\x61mended_quantity\x18\x11 \x01(\x05H\x01\x88\x01\x01\x12\x1b\n\x13\x63ontainer_load_port\x18\x12 \x01(\t\x12.\n\x13\x63ontainer_load_date\x18\x13 \x01(\x0b\x32\x11.google.type.Date\x12s\n\x13\x62ill_of_lading_type\x18\x14 \x01(\x0e\x32V.flexport.customscargomanifestquery.enums.v1beta1.CustomsCargoManifestBillOfLadingType\x12z\n\x16mode_of_transportation\x18\x15 \x01(\x0e\x32Z.flexport.customscargomanifestquery.enums.v1beta1.CustomsCargoManifestModeOfTransportation\x12h\n\x0bhouse_bills\x18\x16 \x03(\x0b\x32S.flexport.customscargomanifestquery.entities.v1beta1.CargoManifestHouseBillOfLading\x12o\n\x0c\x64ispositions\x18\x17 \x03(\x0b\x32Y.flexport.customscargomanifestquery.entities.v1beta1.CargoManifestBillOfLadingDisposition\x12\x66\n\x08in_bonds\x18\x18 \x03(\x0b\x32T.flexport.customscargomanifestquery.entities.v1beta1.CargoManifestBillOfLadingInBond\x12\x35\n\x11last_retrieved_at\x18\x19 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x10\n\x0e_port_of_entryB\x13\n\x11_amended_quantityB\x9a\x01\n7com.flexport.customscargomanifestquery.entities.v1beta1B$CargoManifestMasterBillOfLadingProtoP\x01\xea\x02\x36\x46lexport::CustomsCargoManifestQuery::Entities::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customscargomanifestquery.entities.v1beta1.cargo_manifest_master_bill_of_lading_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n7com.flexport.customscargomanifestquery.entities.v1beta1B$CargoManifestMasterBillOfLadingProtoP\001\352\0026Flexport::CustomsCargoManifestQuery::Entities::V1Beta1"
    _globals["_CARGOMANIFESTMASTERBILLOFLADING"]._serialized_start = 703
    _globals["_CARGOMANIFESTMASTERBILLOFLADING"]._serialized_end = 2040
# @@protoc_insertion_point(module_scope)