# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/commerce/facts/testrepository/v1beta1/out_example_message.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nHflexport/commerce/facts/testrepository/v1beta1/out_example_message.proto\x12.flexport.commerce.facts.testrepository.v1beta1\x1a\x38\x66lexport/commerce/facts/codegen/options/v1/options.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x83\x06\n\x11OutExampleMessage\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\t\x12O\n\x07message\x18\x02 \x01(\x0b\x32>.flexport.commerce.facts.testrepository.v1beta1.NestedMessage1\x12K\n\x05\x65num1\x18\x03 \x03(\x0e\x32<.flexport.commerce.facts.testrepository.v1beta1.ExampleEnum1\x12P\n\x05\x65num2\x18\x04 \x01(\x0e\x32<.flexport.commerce.facts.testrepository.v1beta1.ExampleEnum2H\x00\x88\x01\x01\x12)\n\x03str\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12(\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x66\n\x0bmap_strings\x18\x08 \x03(\x0b\x32Q.flexport.commerce.facts.testrepository.v1beta1.OutExampleMessage.MapStringsEntry\x12h\n\x0cmap_messages\x18\t \x03(\x0b\x32R.flexport.commerce.facts.testrepository.v1beta1.OutExampleMessage.MapMessagesEntry\x1a\x31\n\x0fMapStringsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1ar\n\x10MapMessagesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12M\n\x05value\x18\x02 \x01(\x0b\x32>.flexport.commerce.facts.testrepository.v1beta1.NestedMessage1:\x02\x38\x01:\x19\x18\x01\xc2\x80\x04\x13\n\x11OutExampleMessageB\x08\n\x06_enum2"\'\n\x13OneOfExampleMessage\x12\x0c\n\x04name\x18\x01 \x01(\t:\x02\x18\x01"a\n\x0eNestedMessage1\x12O\n\x07message\x18\x01 \x01(\x0b\x32>.flexport.commerce.facts.testrepository.v1beta1.NestedMessage2"d\n\x0eNestedMessage2\x12R\n\x07message\x18\x01 \x01(\x0b\x32\x41.flexport.commerce.facts.testrepository.v1beta1.OutExampleMessage*\x84\x01\n\x0c\x45xampleEnum1\x12\x19\n\x15\x45XAMPLE_ENUM1_INVALID\x10\x00\x12\x15\n\x11\x45XAMPLE_ENUM1_FOO\x10\x01\x12\x15\n\x11\x45XAMPLE_ENUM1_BAR\x10\x02\x12\x15\n\x11\x45XAMPLE_ENUM1_BAZ\x10\x03\x1a\x14\x18\x01\xc2\x80\x04\x0e\n\x0c\x45xampleEnum1*v\n\x0c\x45xampleEnum2\x12\x19\n\x15\x45XAMPLE_ENUM2_INVALID\x10\x00\x12\x19\n\x11\x45XAMPLE_ENUM2_FOO\x10\x01\x1a\x02\x08\x01\x12\x15\n\x11\x45XAMPLE_ENUM2_BAR\x10\x02\x12\x15\n\x11\x45XAMPLE_ENUM2_BAZ\x10\x03\x1a\x02\x18\x01\x42\x83\x01\n2com.flexport.commerce.facts.testrepository.v1beta1B\x16OutExampleMessageProtoP\x01\xea\x02\x32\x46lexport::Commerce::Facts::TestRepository::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.commerce.facts.testrepository.v1beta1.out_example_message_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n2com.flexport.commerce.facts.testrepository.v1beta1B\026OutExampleMessageProtoP\001\352\0022Flexport::Commerce::Facts::TestRepository::V1Beta1"
    _globals["_EXAMPLEENUM1"]._options = None
    _globals["_EXAMPLEENUM1"]._serialized_options = b"\030\001\302\200\004\016\n\014ExampleEnum1"
    _globals["_EXAMPLEENUM2"]._options = None
    _globals["_EXAMPLEENUM2"]._serialized_options = b"\030\001"
    _globals["_EXAMPLEENUM2"].values_by_name["EXAMPLE_ENUM2_FOO"]._options = None
    _globals["_EXAMPLEENUM2"].values_by_name["EXAMPLE_ENUM2_FOO"]._serialized_options = b"\010\001"
    _globals["_OUTEXAMPLEMESSAGE_MAPSTRINGSENTRY"]._options = None
    _globals["_OUTEXAMPLEMESSAGE_MAPSTRINGSENTRY"]._serialized_options = b"8\001"
    _globals["_OUTEXAMPLEMESSAGE_MAPMESSAGESENTRY"]._options = None
    _globals["_OUTEXAMPLEMESSAGE_MAPMESSAGESENTRY"]._serialized_options = b"8\001"
    _globals["_OUTEXAMPLEMESSAGE"]._options = None
    _globals["_OUTEXAMPLEMESSAGE"]._serialized_options = b"\030\001\302\200\004\023\n\021OutExampleMessage"
    _globals["_ONEOFEXAMPLEMESSAGE"]._options = None
    _globals["_ONEOFEXAMPLEMESSAGE"]._serialized_options = b"\030\001"
    _globals["_EXAMPLEENUM1"]._serialized_start = 1264
    _globals["_EXAMPLEENUM1"]._serialized_end = 1396
    _globals["_EXAMPLEENUM2"]._serialized_start = 1398
    _globals["_EXAMPLEENUM2"]._serialized_end = 1516
    _globals["_OUTEXAMPLEMESSAGE"]._serialized_start = 248
    _globals["_OUTEXAMPLEMESSAGE"]._serialized_end = 1019
    _globals["_OUTEXAMPLEMESSAGE_MAPSTRINGSENTRY"]._serialized_start = 817
    _globals["_OUTEXAMPLEMESSAGE_MAPSTRINGSENTRY"]._serialized_end = 866
    _globals["_OUTEXAMPLEMESSAGE_MAPMESSAGESENTRY"]._serialized_start = 868
    _globals["_OUTEXAMPLEMESSAGE_MAPMESSAGESENTRY"]._serialized_end = 982
    _globals["_ONEOFEXAMPLEMESSAGE"]._serialized_start = 1021
    _globals["_ONEOFEXAMPLEMESSAGE"]._serialized_end = 1060
    _globals["_NESTEDMESSAGE1"]._serialized_start = 1062
    _globals["_NESTEDMESSAGE1"]._serialized_end = 1159
    _globals["_NESTEDMESSAGE2"]._serialized_start = 1161
    _globals["_NESTEDMESSAGE2"]._serialized_end = 1261
# @@protoc_insertion_point(module_scope)