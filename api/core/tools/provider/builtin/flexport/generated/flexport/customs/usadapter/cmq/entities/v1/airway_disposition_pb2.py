# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customs/usadapter/cmq/entities/v1/airway_disposition.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nCflexport/customs/usadapter/cmq/entities/v1/airway_disposition.proto\x12*flexport.customs.usadapter.cmq.entities.v1\x1a\x16google/type/date.proto\x1a\x1bgoogle/type/timeofday.proto"\xa8\x01\n\x11\x41irwayDisposition\x12+\n\x0b\x61\x63tion_time\x18\x01 \x01(\x0b\x32\x16.google.type.TimeOfDay\x12&\n\x0b\x61\x63tion_date\x18\x02 \x01(\x0b\x32\x11.google.type.Date\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x1f\n\x17in_bond_or_entry_number\x18\x05 \x01(\tBZ\n.com.flexport.customs.usadapter.cmq.entities.v1P\x01\xea\x02%Flexport::Customs::UsAdapter::Cmq::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customs.usadapter.cmq.entities.v1.airway_disposition_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n.com.flexport.customs.usadapter.cmq.entities.v1P\001\352\002%Flexport::Customs::UsAdapter::Cmq::V1"
    )
    _globals["_AIRWAYDISPOSITION"]._serialized_start = 169
    _globals["_AIRWAYDISPOSITION"]._serialized_end = 337
# @@protoc_insertion_point(module_scope)