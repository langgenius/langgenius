# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customs/usadapter/entrysummaryrelease/v1/entry_duties.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nDflexport/customs/usadapter/entrysummaryrelease/v1/entry_duties.proto\x12\x31\x66lexport.customs.usadapter.entrysummaryrelease.v1\x1a>flexport/customs/usadapter/entrysummaryrelease/v1/tariff.proto\x1a\x16google/type/date.proto"\xb6\x01\n\x0b\x45ntryDuties\x12\x12\n\nfiler_code\x18\x01 \x01(\t\x12\x14\n\x0c\x65ntry_number\x18\x02 \x01(\t\x12\x11\n\tfiling_id\x18\x03 \x01(\t\x12\x11\n\treference\x18\x04 \x01(\t\x12W\n\x0eline_item_duty\x18\x05 \x03(\x0b\x32?.flexport.customs.usadapter.entrysummaryrelease.v1.LineItemDuty"\xdc\x01\n\x0cLineItemDuty\x12\x16\n\x0einvoice_number\x18\x01 \x01(\t\x12\x18\n\x10line_item_number\x18\x02 \x01(\t\x12I\n\x06tariff\x18\x03 \x01(\x0b\x32\x39.flexport.customs.usadapter.entrysummaryrelease.v1.Tariff\x12O\n\x04\x64uty\x18\x04 \x01(\x0b\x32\x41.flexport.customs.usadapter.entrysummaryrelease.v1.CalculatedDuty"\x8d\x02\n\x0e\x43\x61lculatedDuty\x12\x0c\n\x04\x64uty\x18\x01 \x01(\t\x12\x18\n\x10p1_specific_rate\x18\x02 \x01(\t\x12\x1a\n\x12p2_ad_valorem_rate\x18\x03 \x01(\t\x12\x15\n\rp3_other_rate\x18\x04 \x01(\t\x12\x65\n\x15\x64uty_computation_code\x18\x05 \x01(\x0e\x32\x46.flexport.customs.usadapter.entrysummaryrelease.v1.DutyComputationCode\x12\x39\n\x1e\x64uty_calculated_at_import_date\x18\x06 \x01(\x0b\x32\x11.google.type.Date*\x8e\x07\n\x13\x44utyComputationCode\x12!\n\x1d\x44UTY_COMPUTATION_CODE_INVALID\x10\x00\x12 \n\x1c\x44UTY_COMPUTATION_CODE_0_FREE\x10\x01\x12/\n+DUTY_COMPUTATION_CODE_1_SPECIFIC_QUANTITY_1\x10\x02\x12/\n+DUTY_COMPUTATION_CODE_2_SPECIFIC_QUANTITY_2\x10\x03\x12-\n)DUTY_COMPUTATION_CODE_3_MULTIPLE_SPECIFIC\x10\x04\x12/\n+DUTY_COMPUTATION_CODE_4_COMPOUND_QUANTITY_1\x10\x05\x12/\n+DUTY_COMPUTATION_CODE_5_COMPOUND_QUANTITY_2\x10\x06\x12+\n\'DUTY_COMPUTATION_CODE_6_SPEFIC_COMPOUND\x10\x07\x12&\n"DUTY_COMPUTATION_CODE_7_AD_VALOREM\x10\x08\x12#\n\x1f\x44UTY_COMPUTATION_CODE_9_DERIVED\x10\t\x12+\n\'DUTY_COMPUTATION_CODE_A_FUNC_AD_VALOREM\x10\n\x12\x32\n.DUTY_COMPUTATION_CODE_B_SPECIC_FUNC_AD_VALOREM\x10\x0b\x12)\n%DUTY_COMPUTATION_CODE_C_SPECIC_SPEFIC\x10\x0c\x12/\n+DUTY_COMPUTATION_CODE_D_COMPOUNT_QUANTITY_3\x10\r\x12\x38\n4DUTY_COMPUTATION_CODE_E_SPECIFIC_COMPOUND_QUANTITY_3\x10\x0e\x12\x31\n-DUTY_COMPUTATION_CODE_F_SPECIFIC_PYROTECHNICS\x10\x0f\x12\x37\n3DUTY_COMPUTATION_CODE_J_SPECIFIC_SUGAR_QUANTITY_3_2\x10\x10\x12\x37\n3DUTY_COMPUTATION_CODE_K_SPECIFIC_SUGAR_QUANTITY_2_1\x10\x11\x12)\n%DUTY_COMPUTATION_CODE_X_NOT_AVALIABLE\x10\x12\x42q\n5com.flexport.customs.usadapter.entrysummaryrelease.v1P\x01\xea\x02\x35\x46lexport::Customs::UsAdapter::EntrySummaryRelease::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customs.usadapter.entrysummaryrelease.v1.entry_duties_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n5com.flexport.customs.usadapter.entrysummaryrelease.v1P\001\352\0025Flexport::Customs::UsAdapter::EntrySummaryRelease::V1"
    _globals["_DUTYCOMPUTATIONCODE"]._serialized_start = 892
    _globals["_DUTYCOMPUTATIONCODE"]._serialized_end = 1802
    _globals["_ENTRYDUTIES"]._serialized_start = 212
    _globals["_ENTRYDUTIES"]._serialized_end = 394
    _globals["_LINEITEMDUTY"]._serialized_start = 397
    _globals["_LINEITEMDUTY"]._serialized_end = 617
    _globals["_CALCULATEDDUTY"]._serialized_start = 620
    _globals["_CALCULATEDDUTY"]._serialized_end = 889
# @@protoc_insertion_point(module_scope)