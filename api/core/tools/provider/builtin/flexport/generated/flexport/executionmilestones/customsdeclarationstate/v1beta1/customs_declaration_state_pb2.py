# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/executionmilestones/customsdeclarationstate/v1beta1/customs_declaration_state.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\\flexport/executionmilestones/customsdeclarationstate/v1beta1/customs_declaration_state.proto\x12<flexport.executionmilestones.customsdeclarationstate.v1beta1\x1a\x65\x66lexport/executioncoordinator/executionoffering/v1/valueadded/import_customs_execution_offering.proto\x1agflexport/forwardingcustomsmanager/export/customsdeclaration/enums/v1beta1/automated_export_system.proto\x1a:flexport/monolith/customs/v1beta1/customs_status_api.proto\x1aJflexport/monolith/customs/v1beta1/declaration_filing_process_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xce\x08\n\x17\x43ustomsDeclarationState\x12_\n\x1a\x64\x65\x63laration_filing_process\x18\x01 \x03(\x0b\x32;.flexport.monolith.customs.v1beta1.DeclarationFilingProcess\x12\x14\n\x0cshipment_fid\x18\x02 \x01(\t\x12W\n\x08isf_info\x18\x03 \x01(\x0b\x32\x45.flexport.executionmilestones.customsdeclarationstate.v1beta1.IsfInfo\x12W\n\x08\x61ms_info\x18\x04 \x01(\x0b\x32\x45.flexport.executionmilestones.customsdeclarationstate.v1beta1.AmsInfo\x12[\n\x08\x61\x65s_info\x18\x05 \x01(\x0b\x32\x45.flexport.executionmilestones.customsdeclarationstate.v1beta1.AesInfoB\x02\x18\x01\x12\x65\n\x10\x61\x65s_filing_infos\x18\x06 \x03(\x0b\x32K.flexport.executionmilestones.customsdeclarationstate.v1beta1.AesFilingInfo\x12\x63\n\x0e\x63ustoms_status\x18\x07 \x03(\x0b\x32K.flexport.executionmilestones.customsdeclarationstate.v1beta1.CustomsStatus\x12t\n\x17sli_digitization_status\x18\x08 \x03(\x0b\x32S.flexport.executionmilestones.customsdeclarationstate.v1beta1.SliDigitizationStatus\x12\x87\x01\n\x12manual_work_status\x18\t \x03(\x0b\x32k.flexport.executionmilestones.customsdeclarationstate.v1beta1.CustomsDeclarationState.ManualWorkStatusEntry\x12W\n\x08\x65ns_info\x18\n \x01(\x0b\x32\x45.flexport.executionmilestones.customsdeclarationstate.v1beta1.EnsInfo\x1a\x87\x01\n\x15ManualWorkStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12]\n\x05value\x18\x02 \x01(\x0b\x32N.flexport.executionmilestones.customsdeclarationstate.v1beta1.ManualWorkStatus:\x02\x38\x01"v\n\x10ManualWorkStatus\x12\x14\n\x0cis_completed\x18\x01 \x01(\x08\x12\x17\n\x0flast_updated_by\x18\x02 \x01(\t\x12\x33\n\x0flast_updated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"\xc2\x02\n\rCustomsStatus\x12\x19\n\x11origin_address_id\x18\x01 \x01(\x05\x12\x1e\n\x16\x64\x65stination_address_id\x18\x02 \x01(\x05\x12\x12\n\ncarrier_id\x18\x04 \x01(\x05\x12\x35\n\x11status_updated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12R\n\x10top_level_status\x18\x06 \x01(\x0e\x32\x38.flexport.monolith.customs.v1beta1.CustomsTopLevelStatus\x12W\n\x10sub_level_status\x18\x07 \x03(\x0b\x32=.flexport.monolith.customs.v1beta1.CustomsSubLevelStatusEntry"\x92\x02\n\rAesFilingInfo\x12\x12\n\nitn_number\x18\x01 \x01(\t\x12\x0b\n\x03\x66id\x18\x02 \x01(\t\x12\x16\n\x0e\x62roker_comment\x18\x03 \x01(\t\x12.\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13updated_by_user_fid\x18\x16 \x01(\t\x12u\n\x11\x61\x65s_filing_status\x18\x17 \x01(\x0e\x32Z.flexport.forwardingcustomsmanager.export.customsdeclaration.enums.v1beta1.AesFilingStatusJ\x04\x08\x04\x10\x15"\xc4\x01\n\x15SliDigitizationStatus\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\x03\x12\x14\n\x0cis_confirmed\x18\x0b \x01(\x08\x12\x19\n\x0c\x63onfirmed_by\x18\x0c \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x0bis_archived\x18\x15 \x01(\x08\x12.\n\nupdated_at\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07version\x18\x17 \x01(\x05\x42\x0f\n\r_confirmed_by"g\n\x07\x41\x65sInfo\x12X\n\titn_infos\x18\x01 \x03(\x0b\x32\x45.flexport.executionmilestones.customsdeclarationstate.v1beta1.ItnInfo:\x02\x18\x01":\n\x07ItnInfo\x12\x12\n\nitn_number\x18\x01 \x01(\t\x12\x17\n\x0flast_updated_by\x18\x02 \x01(\t:\x02\x18\x01"\xa1\x03\n\x07IsfInfo\x12\\\n\risf_file_type\x18\x01 \x01(\x0e\x32\x45.flexport.executionmilestones.customsdeclarationstate.v1beta1.IsfType\x12\x30\n\x0cisf_due_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x64\n\x08isf_role\x18\x03 \x01(\x0e\x32N.flexport.executioncoordinator.executionoffering.v1.ImporterSecurityFilingRoleB\x02\x18\x01\x12\x19\n\x11mark_as_completed\x18\x04 \x01(\x08\x12\x1b\n\x13last_updated_by_fid\x18\x05 \x01(\t\x12h\n\x11isf_filing_status\x18\x06 \x01(\x0e\x32M.flexport.executionmilestones.customsdeclarationstate.v1beta1.IsfFilingStatus"\xf0\x02\n\x07\x41msInfo\x12\x64\n\x0fport_of_calling\x18\x01 \x01(\x0e\x32K.flexport.executionmilestones.customsdeclarationstate.v1beta1.PortOfCalling\x12q\n\x10\x61ms_filing_types\x18\x02 \x01(\x0e\x32W.flexport.executionmilestones.customsdeclarationstate.v1beta1.AmsFilingTypesCombination\x12o\n\x15hbl_level_filing_data\x18\x03 \x03(\x0b\x32P.flexport.executionmilestones.customsdeclarationstate.v1beta1.HblLevelFilingData\x12\x1b\n\x13last_updated_by_fid\x18\x04 \x01(\t"\xca\x01\n\x12HblLevelFilingData\x12\x12\n\nhbl_number\x18\x01 \x01(\t\x12k\n\x14latest_filing_status\x18\x02 \x01(\x0e\x32M.flexport.executionmilestones.customsdeclarationstate.v1beta1.AmsFilingStatus\x12\x33\n\x0flast_updated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"\xcd\x01\n\x15HblLevelEnsFilingData\x12\x12\n\nhbl_number\x18\x01 \x01(\t\x12k\n\x14latest_filing_status\x18\x02 \x01(\x0e\x32M.flexport.executionmilestones.customsdeclarationstate.v1beta1.EnsFilingStatus\x12\x33\n\x0flast_updated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"\x9a\x01\n\x07\x45nsInfo\x12r\n\x15hbl_level_filing_data\x18\x01 \x03(\x0b\x32S.flexport.executionmilestones.customsdeclarationstate.v1beta1.HblLevelEnsFilingData\x12\x1b\n\x13last_updated_by_fid\x18\x02 \x01(\t*c\n\x0eManualWorkType\x12\x1c\n\x18MANUAL_WORK_TYPE_INVALID\x10\x00\x12\x33\n/MANUAL_WORK_TYPE_PACKING_DECLARATION_VALIDATION\x10\x01*Y\n\x07IsfType\x12\x14\n\x10ISF_TYPE_INVALID\x10\x00\x12\x17\n\x13ISF_TYPE_NOT_NEEDED\x10\x01\x12\x0f\n\x0bISF_TYPE_10\x10\x02\x12\x0e\n\nISF_TYPE_5\x10\x03*\x9f\x01\n\x0fIsfFilingStatus\x12\x1d\n\x19ISF_FILING_STATUS_INVALID\x10\x00\x12"\n\x1eISF_FILING_STATUS_FILED_ONLINE\x10\x01\x12%\n!ISF_FILING_STATUS_ACCEPTED_ONLINE\x10\x02\x12"\n\x1eISF_FILING_STATUS_OTHER_ONLINE\x10\x03*w\n\rPortOfCalling\x12\x1b\n\x17PORT_OF_CALLING_INVALID\x10\x00\x12\x16\n\x12PORT_OF_CALLING_US\x10\x01\x12\x16\n\x12PORT_OF_CALLING_CA\x10\x02\x12\x19\n\x15PORT_OF_CALLING_OTHER\x10\x03*\xd1\x02\n\x19\x41msFilingTypesCombination\x12(\n$AMS_FILING_TYPES_COMBINATION_INVALID\x10\x00\x12)\n%AMS_FILING_TYPES_COMBINATION_AMS_ONLY\x10\x01\x12)\n%AMS_FILING_TYPES_COMBINATION_ACI_ONLY\x10\x02\x12/\n+AMS_FILING_TYPES_COMBINATION_EMANIFEST_ONLY\x10\x03\x12)\n%AMS_FILING_TYPES_COMBINATION_AFR_ONLY\x10\x04\x12(\n$AMS_FILING_TYPES_COMBINATION_AMS_ACI\x10\x05\x12.\n*AMS_FILING_TYPES_COMBINATION_AMS_EMANIFEST\x10\x06*\xe2\x02\n\x0f\x41msFilingStatus\x12\x1d\n\x19\x41MS_FILING_STATUS_INVALID\x10\x00\x12"\n\x1e\x41MS_FILING_STATUS_FILED_ONLINE\x10\x01\x12$\n AMS_FILING_STATUS_MATCHED_ONLINE\x10\x02\x12"\n\x1e\x41MS_FILING_STATUS_ERROR_ONLINE\x10\x03\x12#\n\x1f\x41MS_FILING_STATUS_FILED_OFFLINE\x10\x04\x12%\n!AMS_FILING_STATUS_MATCHED_OFFLINE\x10\x05\x12\x1f\n\x1b\x41MS_FILING_STATUS_NOT_FILED\x10\x06\x12-\n)AMS_FILING_STATUS_SENT_TRADE_TECH_OFFLINE\x10\x07\x12&\n"AMS_FILING_STATUS_UNDEFINED_ONLINE\x10\x08*\x9d\x01\n\x0f\x45nsFilingStatus\x12\x1d\n\x19\x45NS_FILING_STATUS_INVALID\x10\x00\x12#\n\x1f\x45NS_FILING_STATUS_FILED_OFFLINE\x10\x01\x12%\n!ENS_FILING_STATUS_MATCHED_OFFLINE\x10\x02\x12\x1f\n\x1b\x45NS_FILING_STATUS_NOT_FILED\x10\x03\x42\xa4\x01\n@com.flexport.executionmilestones.customsdeclarationstate.v1beta1B\x1c\x43ustomsDeclarationStateProtoP\x01\xea\x02?Flexport::ExecutionMilestones::CustomsDeclarationState::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.executionmilestones.customsdeclarationstate.v1beta1.customs_declaration_state_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n@com.flexport.executionmilestones.customsdeclarationstate.v1beta1B\034CustomsDeclarationStateProtoP\001\352\002?Flexport::ExecutionMilestones::CustomsDeclarationState::V1Beta1"
    _globals["_CUSTOMSDECLARATIONSTATE_MANUALWORKSTATUSENTRY"]._options = None
    _globals["_CUSTOMSDECLARATIONSTATE_MANUALWORKSTATUSENTRY"]._serialized_options = b"8\001"
    _globals["_CUSTOMSDECLARATIONSTATE"].fields_by_name["aes_info"]._options = None
    _globals["_CUSTOMSDECLARATIONSTATE"].fields_by_name["aes_info"]._serialized_options = b"\030\001"
    _globals["_AESINFO"]._options = None
    _globals["_AESINFO"]._serialized_options = b"\030\001"
    _globals["_ITNINFO"]._options = None
    _globals["_ITNINFO"]._serialized_options = b"\030\001"
    _globals["_ISFINFO"].fields_by_name["isf_role"]._options = None
    _globals["_ISFINFO"].fields_by_name["isf_role"]._serialized_options = b"\030\001"
    _globals["_MANUALWORKTYPE"]._serialized_start = 4087
    _globals["_MANUALWORKTYPE"]._serialized_end = 4186
    _globals["_ISFTYPE"]._serialized_start = 4188
    _globals["_ISFTYPE"]._serialized_end = 4277
    _globals["_ISFFILINGSTATUS"]._serialized_start = 4280
    _globals["_ISFFILINGSTATUS"]._serialized_end = 4439
    _globals["_PORTOFCALLING"]._serialized_start = 4441
    _globals["_PORTOFCALLING"]._serialized_end = 4560
    _globals["_AMSFILINGTYPESCOMBINATION"]._serialized_start = 4563
    _globals["_AMSFILINGTYPESCOMBINATION"]._serialized_end = 4900
    _globals["_AMSFILINGSTATUS"]._serialized_start = 4903
    _globals["_AMSFILINGSTATUS"]._serialized_end = 5257
    _globals["_ENSFILINGSTATUS"]._serialized_start = 5260
    _globals["_ENSFILINGSTATUS"]._serialized_end = 5417
    _globals["_CUSTOMSDECLARATIONSTATE"]._serialized_start = 536
    _globals["_CUSTOMSDECLARATIONSTATE"]._serialized_end = 1638
    _globals["_CUSTOMSDECLARATIONSTATE_MANUALWORKSTATUSENTRY"]._serialized_start = 1503
    _globals["_CUSTOMSDECLARATIONSTATE_MANUALWORKSTATUSENTRY"]._serialized_end = 1638
    _globals["_MANUALWORKSTATUS"]._serialized_start = 1640
    _globals["_MANUALWORKSTATUS"]._serialized_end = 1758
    _globals["_CUSTOMSSTATUS"]._serialized_start = 1761
    _globals["_CUSTOMSSTATUS"]._serialized_end = 2083
    _globals["_AESFILINGINFO"]._serialized_start = 2086
    _globals["_AESFILINGINFO"]._serialized_end = 2360
    _globals["_SLIDIGITIZATIONSTATUS"]._serialized_start = 2363
    _globals["_SLIDIGITIZATIONSTATUS"]._serialized_end = 2559
    _globals["_AESINFO"]._serialized_start = 2561
    _globals["_AESINFO"]._serialized_end = 2664
    _globals["_ITNINFO"]._serialized_start = 2666
    _globals["_ITNINFO"]._serialized_end = 2724
    _globals["_ISFINFO"]._serialized_start = 2727
    _globals["_ISFINFO"]._serialized_end = 3144
    _globals["_AMSINFO"]._serialized_start = 3147
    _globals["_AMSINFO"]._serialized_end = 3515
    _globals["_HBLLEVELFILINGDATA"]._serialized_start = 3518
    _globals["_HBLLEVELFILINGDATA"]._serialized_end = 3720
    _globals["_HBLLEVELENSFILINGDATA"]._serialized_start = 3723
    _globals["_HBLLEVELENSFILINGDATA"]._serialized_end = 3928
    _globals["_ENSINFO"]._serialized_start = 3931
    _globals["_ENSINFO"]._serialized_end = 4085
# @@protoc_insertion_point(module_scope)