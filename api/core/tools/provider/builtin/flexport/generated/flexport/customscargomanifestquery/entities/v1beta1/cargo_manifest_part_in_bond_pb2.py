# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customscargomanifestquery/entities/v1beta1/cargo_manifest_part_in_bond.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nUflexport/customscargomanifestquery/entities/v1beta1/cargo_manifest_part_in_bond.proto\x12\x33\x66lexport.customscargomanifestquery.entities.v1beta1"\x99\x02\n\x17\x43\x61rgoManifestPartInBond\x12\x16\n\x0ein_bond_number\x18\x01 \x01(\t\x12\x1d\n\x15originating_port_code\x18\x02 \x01(\t\x12(\n manifested_destination_port_code\x18\x03 \x01(\t\x12\x35\n-actual_destination_port_code_manual_diversion\x18\x04 \x01(\t\x12\x32\n*actual_destination_port_code_edi_diversion\x18\x05 \x01(\t\x12\x16\n\x0ein_bond_status\x18\x06 \x01(\t\x12\x1a\n\x12in_bond_entry_type\x18\x07 \x01(\tB\x92\x01\n7com.flexport.customscargomanifestquery.entities.v1beta1B\x1c\x43\x61rgoManifestPartInBondProtoP\x01\xea\x02\x36\x46lexport::CustomsCargoManifestQuery::Entities::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customscargomanifestquery.entities.v1beta1.cargo_manifest_part_in_bond_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n7com.flexport.customscargomanifestquery.entities.v1beta1B\034CargoManifestPartInBondProtoP\001\352\0026Flexport::CustomsCargoManifestQuery::Entities::V1Beta1"
    _globals["_CARGOMANIFESTPARTINBOND"]._serialized_start = 143
    _globals["_CARGOMANIFESTPARTINBOND"]._serialized_end = 424
# @@protoc_insertion_point(module_scope)