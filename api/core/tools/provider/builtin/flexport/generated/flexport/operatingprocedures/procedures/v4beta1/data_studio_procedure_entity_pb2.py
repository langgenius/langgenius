# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/operatingprocedures/procedures/v4beta1/data_studio_procedure_entity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nRflexport/operatingprocedures/procedures/v4beta1/data_studio_procedure_entity.proto\x12/flexport.operatingprocedures.procedures.v4beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\xd5\x07\n\x19\x44\x61taStudioProcedureEntity\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x12\n\nclient_fid\x18\x03 \x01(\t\x12\x1a\n\x12\x63ompany_entity_fid\x18\x04 \x01(\t\x12\x11\n\tconsignee\x18\x05 \x01(\t\x12\x16\n\x0e\x63onsignee_fids\x18\x06 \x03(\t\x12\x16\n\x0e\x63reated_by_fid\x18\x07 \x01(\t\x12.\n\ndeleted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65stination\x18\t \x01(\t\x12\x1b\n\x13\x64\x65stination_country\x18\n \x01(\t\x12!\n\x19\x64\x65stination_country_codes\x18\x0b \x03(\t\x12\x1c\n\x14\x64\x65stination_original\x18\x0c \x01(\t\x12\x1d\n\x15\x64\x65stination_port_fids\x18\r \x03(\t\x12\x15\n\rexport_import\x18\x0e \x01(\x05\x12\x19\n\x11\x66lexport_standard\x18\x0f \x01(\t\x12\x0e\n\x06inland\x18\x10 \x01(\t\x12\x17\n\x0finland_original\x18\x11 \x01(\t\x12\x18\n\x10inland_port_fids\x18\x12 \x03(\t\x12\x0e\n\x06office\x18\x13 \x01(\t\x12\x0e\n\x06origin\x18\x14 \x01(\t\x12\x16\n\x0eorigin_country\x18\x15 \x01(\t\x12\x1c\n\x14origin_country_codes\x18\x16 \x03(\t\x12\x18\n\x10origin_port_fids\x18\x17 \x03(\t\x12\x1a\n\x12other_instructions\x18\x18 \x01(\t\x12!\n\x19other_instructions_prompt\x18\x19 \x01(\t\x12\x16\n\x0eprocedure_item\x18\x1a \x01(\t\x12\x15\n\rprocess_owner\x18\x1b \x01(\t\x12\x15\n\rservice_types\x18\x1c \x03(\x05\x12\x10\n\x08services\x18\x1d \x01(\t\x12\x0f\n\x07shipper\x18\x1e \x01(\t\x12\x14\n\x0cshipper_fids\x18\x1f \x03(\t\x12\r\n\x05squad\x18  \x01(\t\x12\x19\n\x11structured_option\x18! \x01(\t\x12 \n\x18structured_option_prompt\x18" \x01(\t\x12\x16\n\x0eupdated_by_fid\x18# \x01(\t\x12.\n\ncreated_at\x18$ \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18% \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x8c\x01\n3com.flexport.operatingprocedures.procedures.v4beta1B\x1e\x44\x61taStudioProcedureEntityProtoP\x01\xea\x02\x32\x46lexport::OperatingProcedures::Procedures::V4Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.operatingprocedures.procedures.v4beta1.data_studio_procedure_entity_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n3com.flexport.operatingprocedures.procedures.v4beta1B\036DataStudioProcedureEntityProtoP\001\352\0022Flexport::OperatingProcedures::Procedures::V4Beta1"
    _globals["_DATASTUDIOPROCEDUREENTITY"]._serialized_start = 169
    _globals["_DATASTUDIOPROCEDUREENTITY"]._serialized_end = 1150
# @@protoc_insertion_point(module_scope)