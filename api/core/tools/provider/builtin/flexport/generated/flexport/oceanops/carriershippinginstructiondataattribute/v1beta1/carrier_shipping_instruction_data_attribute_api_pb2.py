# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/oceanops/carriershippinginstructiondataattribute/v1beta1/carrier_shipping_instruction_data_attribute_api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nwflexport/oceanops/carriershippinginstructiondataattribute/v1beta1/carrier_shipping_instruction_data_attribute_api.proto\x12\x41\x66lexport.oceanops.carriershippinginstructiondataattribute.v1beta1\x1a)flexport/oceanops/port/v1beta1/port.proto\x1a-flexport/rulesengine/options/v1/options.proto"\x84\x05\n\x19RateGroupAndRemarkRequest\x12\x1e\n\x11\x63\x61rrier_scac_code\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x0f\x63ontract_number\x18\x02 \x01(\tH\x01\x88\x01\x01\x12%\n\x18port_of_loading_loc_code\x18\x03 \x01(\tH\x02\x88\x01\x01\x12)\n\x1cport_of_loading_country_code\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\'\n\x1aport_of_discharge_loc_code\x18\x05 \x01(\tH\x04\x88\x01\x01\x12+\n\x1eport_of_discharge_country_code\x18\x06 \x01(\tH\x05\x88\x01\x01\x12/\n"interior_point_intermodal_loc_code\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x33\n&interior_point_intermodal_country_code\x18\x08 \x01(\tH\x07\x88\x01\x01:\x1f\x82\xf7\x02\x1bRate Group & Remark RequestB\x14\n\x12_carrier_scac_codeB\x12\n\x10_contract_numberB\x1b\n\x19_port_of_loading_loc_codeB\x1f\n\x1d_port_of_loading_country_codeB\x1d\n\x1b_port_of_discharge_loc_codeB!\n\x1f_port_of_discharge_country_codeB%\n#_interior_point_intermodal_loc_codeB)\n\'_interior_point_intermodal_country_code"\xd2\x01\n\x1aRateGroupAndRemarkResponse\x12\x1a\n\rservice_level\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nrate_group\x18\x02 \x01(\tH\x01\x88\x01\x01\x12"\n\x15\x62ill_of_lading_remark\x18\x03 \x01(\tH\x02\x88\x01\x01: \x82\xf7\x02\x1cRate Group & Remark ResponseB\x10\n\x0e_service_levelB\r\n\x0b_rate_groupB\x18\n\x16_bill_of_lading_remark"\xcb\x02\n CargoDescriptionAndRemarkRequest\x12\x1c\n\x0f\x63ontract_number\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tclient_id\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12+\n\x1eplace_of_delivery_country_code\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0cpremium_type\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1e\n\x11\x63\x61rrier_scac_code\x18\x05 \x01(\tH\x04\x88\x01\x01:\x1d\x82\xf7\x02\x19\x43\x61rgoDescription & RemarkB\x12\n\x10_contract_numberB\x0c\n\n_client_idB!\n\x1f_place_of_delivery_country_codeB\x0f\n\r_premium_typeB\x14\n\x12_carrier_scac_code"\xb9\x01\n!CargoDescriptionAndRemarkResponse\x12#\n\x11\x63\x61rgo_description\x18\x01 \x01(\tB\x08\xaa\xf7\x02\x04\n\x02\x10\x05\x12\x18\n\x06remark\x18\x02 \x01(\tB\x08\xaa\xf7\x02\x04\n\x02\x10\x05:U\x82\xf7\x02QBoth responses are nullable and may be templates for further string interpolation"\x9a\x02\n&CargoDescriptionAndRemarkVerTwoRequest\x12\x1e\n\x11\x63\x61rrier_scac_code\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x0f\x63ontract_number\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tclient_id\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x13\n\x06is_nac\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x13\n\x06is_fak\x18\x05 \x01(\x08H\x04\x88\x01\x01:"\x82\xf7\x02\x1e\x43\x61rgoDescription & Remark (V2)B\x14\n\x12_carrier_scac_codeB\x12\n\x10_contract_numberB\x0c\n\n_client_idB\t\n\x07_is_nacB\t\n\x07_is_fak"\xbf\x01\n\'CargoDescriptionAndRemarkVerTwoResponse\x12#\n\x11\x63\x61rgo_description\x18\x01 \x01(\tB\x08\xaa\xf7\x02\x04\n\x02\x10\x05\x12\x18\n\x06remark\x18\x02 \x01(\tB\x08\xaa\xf7\x02\x04\n\x02\x10\x05:U\x82\xf7\x02QBoth responses are nullable and may be templates for further string interpolation"\xb7\x01\n\x16\x43ontractNacInfoRequest\x12\x1c\n\x0f\x63ontract_number\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tclient_id\x18\x02 \x01(\x04H\x01\x88\x01\x01:E\x82\xf7\x02\x41Needs ContractNumber and ClientId to determine the mapped NacInfoB\x12\n\x10_contract_numberB\x0c\n\n_client_id"e\n\x17\x43ontractNacInfoResponse\x12\x10\n\x08nac_info\x18\x01 \x01(\t:8\x82\xf7\x02\x34Nac info: client name, and optionally commodity name"\x8e\x03\n\x1e\x46ixedAccountBookingInfoRequest\x12\x1c\n\x0f\x63ontract_number\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tclient_id\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x13\n\x06string\x18\x03 \x01(\tH\x02\x88\x01\x01\x12%\n\x18port_of_receipt_loc_code\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\'\n\x1aport_of_discharge_loc_code\x18\x05 \x01(\tH\x04\x88\x01\x01\x12(\n\x1bport_of_intermodal_loc_code\x18\x06 \x01(\tH\x05\x88\x01\x01:\x1e\x82\xf7\x02\x1a\x46ixed account booking infoB\x12\n\x10_contract_numberB\x0c\n\n_client_idB\t\n\x07_stringB\x1b\n\x19_port_of_receipt_loc_codeB\x1d\n\x1b_port_of_discharge_loc_codeB\x1e\n\x1c_port_of_intermodal_loc_code"|\n\x1f\x46ixedAccountBookingInfoResponse\x12\x14\n\x0c\x62ooking_code\x18\x01 \x01(\t\x12\x13\n\x0b\x63lient_name\x18\x02 \x01(\t:.\x82\xf7\x02*Fixed account booking code and client_name"\xb3\x03\n\x17\x43\x61rrierRateGroupRequest\x12\x1c\n\x0f\x63ontract_number\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\x18port_of_loading_loc_code\x18\x02 \x01(\t\x12$\n\x1cport_of_loading_country_code\x18\x03 \x01(\t\x12"\n\x1aport_of_discharge_loc_code\x18\x04 \x01(\t\x12&\n\x1eport_of_discharge_country_code\x18\x05 \x01(\t\x12*\n"interior_point_intermodal_loc_code\x18\x06 \x01(\t\x12.\n&interior_point_intermodal_country_code\x18\x07 \x01(\t\x12\x11\n\tclient_id\x18\x08 \x01(\x04\x12\x0e\n\x06string\x18\t \x01(\t\x12\x13\n\x0bvessel_name\x18\n \x01(\t\x12&\n\x1eplace_of_delivery_country_code\x18\x0b \x01(\t:\x16\x82\xf7\x02\x12\x43\x61rrier rate groupB\x12\n\x10_contract_number"F\n\x18\x43\x61rrierRateGroupResponse\x12\x12\n\nrate_group\x18\x01 \x01(\t:\x16\x82\xf7\x02\x12\x43\x61rrier rate group"\xa5\x03\n%BillOfLadingCommentsOtherNotesRequest\x12\x19\n\x0c\x63\x61rrier_scac\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x0f\x63ontract_number\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\rservice_level\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x17\n\nrate_group\x18\x04 \x01(\tH\x03\x88\x01\x01\x12"\n\x15\x62ill_of_lading_remark\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1a\n\rorigin_region\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x1f\n\x12\x64\x65stination_region\x18\x07 \x01(\tH\x06\x88\x01\x01:$\x82\xf7\x02 B/L Comments Other Notes RequestB\x0f\n\r_carrier_scacB\x12\n\x10_contract_numberB\x10\n\x0e_service_levelB\r\n\x0b_rate_groupB\x18\n\x16_bill_of_lading_remarkB\x10\n\x0e_origin_regionB\x15\n\x13_destination_region"e\n&BillOfLadingCommentsOtherNotesResponse\x12\x14\n\x06output\x18\x01 \x01(\tB\x04\xb8\xf7\x02\x01:%\x82\xf7\x02!B/L Comments Other Notes Response"\xb1\x10\n$CargoDescriptionAndRemarkRuleRequest\x12\x1c\n\x0f\x63ontract_number\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10\x66\x65\x65\x64\x65r_vessel_id\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12)\n\x1cmaster_bill_of_lading_number\x18\x03 \x01(\tH\x02\x88\x01\x01\x12,\n\x1fmultiple_shipping_order_numbers\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x42\n\x0fport_of_loading\x18\x05 \x01(\x0b\x32$.flexport.oceanops.port.v1beta1.PortH\x04\x88\x01\x01\x12\x44\n\x11port_of_discharge\x18\x06 \x01(\x0b\x32$.flexport.oceanops.port.v1beta1.PortH\x05\x88\x01\x01\x12\x44\n\x11place_of_delivery\x18\x07 \x01(\x0b\x32$.flexport.oceanops.port.v1beta1.PortH\x06\x88\x01\x01\x12\x90\x01\n\rorigin_region\x18\x08 \x01(\x0e\x32t.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CargoDescriptionAndRemarkRuleRequest.OriginRegionH\x07\x88\x01\x01\x12\x9a\x01\n\x12\x64\x65stination_region\x18\t \x01(\x0e\x32y.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CargoDescriptionAndRemarkRuleRequest.DestinationRegionH\x08\x88\x01\x01\x12\x1e\n\x11\x63\x61rrier_scac_code\x18\n \x01(\tH\t\x88\x01\x01\x12\x1c\n\x0f\x63ontainer_count\x18\x0b \x01(\x04H\n\x88\x01\x01\x12\x8e\x01\n\x0c\x66reight_term\x18\x0c \x01(\x0e\x32s.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CargoDescriptionAndRemarkRuleRequest.FreightTermH\x0b\x88\x01\x01\x12(\n\x1bhouse_bill_of_lading_number\x18\r \x01(\tH\x0c\x88\x01\x01\x12\x17\n\npay_office\x18\x0e \x01(\tH\r\x88\x01\x01\x12\x10\n\x08\x63urrency\x18\x0f \x01(\t\x12\x13\n\x06is_fak\x18\x10 \x01(\x08H\x0e\x88\x01\x01\x12\x13\n\x06is_nac\x18\x11 \x01(\x08H\x0f\x88\x01\x01\x12\x96\x01\n\x10payment_location\x18\x12 \x01(\x0e\x32w.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CargoDescriptionAndRemarkRuleRequest.PaymentLocationH\x10\x88\x01\x01"\x80\x01\n\x0cOriginRegion\x12\x19\n\x15ORIGIN_REGION_INVALID\x10\x00\x12\x1b\n\x17ORIGIN_REGION_SHEN_ZHEN\x10\x01\x12\x1b\n\x17ORIGIN_REGION_SHANG_HAI\x10\x02\x12\x1b\n\x17ORIGIN_REGION_HONG_KONG\x10\x03"\x84\x01\n\x11\x44\x65stinationRegion\x12\x1e\n\x1a\x44\x45STINATION_REGION_INVALID\x10\x00\x12\x19\n\x15\x44\x45STINATION_REGION_CA\x10\x01\x12\x19\n\x15\x44\x45STINATION_REGION_US\x10\x02\x12\x19\n\x15\x44\x45STINATION_REGION_EU\x10\x03"\x7f\n\x0b\x46reightTerm\x12\x18\n\x14\x46REIGHT_TERM_INVALID\x10\x00\x12\x18\n\x14\x46REIGHT_TERM_PREPAID\x10\x01\x12\x18\n\x14\x46REIGHT_TERM_COLLECT\x10\x02\x12"\n\x1e\x46REIGHT_TERM_PAYABLE_ELSEWHERE\x10\x03"i\n\x0fPaymentLocation\x12\x1c\n\x18PAYMENT_LOCATION_INVALID\x10\x00\x12\x18\n\x14PAYMENT_LOCATION_POD\x10\x01\x12\x1e\n\x1aPAYMENT_LOCATION_ROTTERDAM\x10\x02:*\x82\xf7\x02&CargoDescription & Remark (rule-based)B\x12\n\x10_contract_numberB\x13\n\x11_feeder_vessel_idB\x1f\n\x1d_master_bill_of_lading_numberB"\n _multiple_shipping_order_numbersB\x12\n\x10_port_of_loadingB\x14\n\x12_port_of_dischargeB\x14\n\x12_place_of_deliveryB\x10\n\x0e_origin_regionB\x15\n\x13_destination_regionB\x14\n\x12_carrier_scac_codeB\x12\n\x10_container_countB\x0f\n\r_freight_termB\x1e\n\x1c_house_bill_of_lading_numberB\r\n\x0b_pay_officeB\t\n\x07_is_fakB\t\n\x07_is_nacB\x13\n\x11_payment_location"\xa2\x01\n%CargoDescriptionAndRemarkRuleResponse\x12+\n\x11\x63\x61rgo_description\x18\x01 \x01(\tB\x10\x98\xf7\x02\x01\xaa\xf7\x02\x04\n\x02\x10\x05\xb8\xf7\x02\x01\x12 \n\x06remark\x18\x02 \x01(\tB\x10\x98\xf7\x02\x01\xaa\xf7\x02\x04\n\x02\x10\x05\xb8\xf7\x02\x01:*\x82\xf7\x02&CargoDescription & Remark (rule-based)"n\n\x19\x43ontractAttributesRequest\x12\x1c\n\x0f\x63ontract_number\x18\x01 \x01(\tH\x00\x88\x01\x01:\x1f\x82\xf7\x02\x1b\x43ontract Attributes RequestB\x12\n\x10_contract_number"r\n\x1a\x43ontractAttributesResponse\x12\x0e\n\x06is_fak\x18\x01 \x01(\x08\x12\x0e\n\x06is_nac\x18\x02 \x01(\x08\x12\x12\n\nis_premium\x18\x03 \x01(\x08: \x82\xf7\x02\x1c\x43ontract Attributes Response"\xaa\x02\n$FreightChargesPaymentLocationRequest\x12\x1e\n\x11\x63\x61rrier_scac_code\x18\x01 \x01(\tH\x00\x88\x01\x01\x12+\n\x1eport_of_discharge_country_code\x18\x02 \x01(\tH\x01\x88\x01\x01\x12+\n\x1eplace_of_delivery_country_code\x18\x03 \x01(\tH\x02\x88\x01\x01:,\x82\xf7\x02(Freight Charges Payment Location RequestB\x14\n\x12_carrier_scac_codeB!\n\x1f_port_of_discharge_country_codeB!\n\x1f_place_of_delivery_country_code"\xd6\x02\n%FreightChargesPaymentLocationResponse\x12\x92\x01\n\x10payment_location\x18\x01 \x01(\x0e\x32x.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.FreightChargesPaymentLocationResponse.PaymentLocation"i\n\x0fPaymentLocation\x12\x1c\n\x18PAYMENT_LOCATION_INVALID\x10\x00\x12\x18\n\x14PAYMENT_LOCATION_POD\x10\x01\x12\x1e\n\x1aPAYMENT_LOCATION_ROTTERDAM\x10\x02:-\x82\xf7\x02)Freight Charges Payment Location Response2\x9f\x1f\n*CarrierShippingInstructionDataAttributeAPI\x12\xf0\x02\n\x12RateGroupAndRemark\x12\\.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.RateGroupAndRemarkRequest\x1a].flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.RateGroupAndRemarkResponse"\x9c\x01\x8a\xf7\x02\x91\x01\x12Pcom.flexport.oceanops.carriershippinginstructiondataattribute.rategroupandremark\x1a\x32Rate group & remark from carrier & contract number"\tocean_ops\x92\xf7\x02\x02\x18\x01\x12\xa7\x03\n\x19\x43\x61rgoDescriptionAndRemark\x12\x63.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CargoDescriptionAndRemarkRequest\x1a\x64.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CargoDescriptionAndRemarkResponse"\xbe\x01\x8a\xf7\x02\xad\x01\x12Wcom.flexport.oceanops.carriershippinginstructiondataattribute.cargodescriptionandremark\x1aGCargoDescription & Remark, may return a template for further population"\tocean_ops\x92\xf7\x02\x02\x18\x01\x9a\xf7\x02\x02\x08\x01\x12\xbb\x03\n\x1f\x43\x61rgoDescriptionAndRemarkVerTwo\x12i.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CargoDescriptionAndRemarkVerTwoRequest\x1aj.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CargoDescriptionAndRemarkVerTwoResponse"\xc0\x01\x8a\xf7\x02\xaf\x01\x12Ycom.flexport.oceanops.carriershippinginstructiondataattribute.cargodescriptionandremarkv2\x1aGCargoDescription & Remark, may return a template for further population"\tocean_ops\x92\xf7\x02\x02\x18\x01\x9a\xf7\x02\x02\x08\x01\x12\xfd\x02\n\x0f\x43ontractNacInfo\x12Y.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.ContractNacInfoRequest\x1aZ.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.ContractNacInfoResponse"\xb2\x01\x8a\xf7\x02\xa1\x01\x12Mcom.flexport.oceanops.carriershippinginstructiondataattribute.contractnacinfo\x1a\x45\x43\x61rrier contract nac info: client name, and optionally commodity name"\tocean_ops\x92\xf7\x02\x02\x18\x01\x9a\xf7\x02\x02\x08\x01\x12\xf1\x02\n\x17\x46ixedAccountBookingInfo\x12\x61.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.FixedAccountBookingInfoRequest\x1a\x62.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.FixedAccountBookingInfoResponse"\x8e\x01\x8a\xf7\x02~\x12Ucom.flexport.oceanops.carriershippinginstructiondataattribute.fixedaccountbookinginfo\x1a\x1a\x46ixed account booking info"\tocean_ops\x92\xf7\x02\x02\x18\x01\x9a\xf7\x02\x02\x08\x01\x12\xcc\x02\n\x10\x43\x61rrierRateGroup\x12Z.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CarrierRateGroupRequest\x1a[.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CarrierRateGroupResponse"\x7f\x8a\xf7\x02o\x12Ncom.flexport.oceanops.carriershippinginstructiondataattribute.carrierrategroup\x1a\x12\x43\x61rrier rate group"\tocean_ops\x92\xf7\x02\x02\x18\x01\x9a\xf7\x02\x02\x08\x01\x12\xa3\x03\n\x1e\x42illOfLadingCommentsOtherNotes\x12h.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.BillOfLadingCommentsOtherNotesRequest\x1ai.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.BillOfLadingCommentsOtherNotesResponse"\xab\x01\x8a\xf7\x02\xa0\x01\x12\\com.flexport.oceanops.carriershippinginstructiondataattribute.billofladingcommentsothernotes\x1a\x35\x43\x61rrier Shipping Instruction B/L Comments Other Notes"\tocean_ops\x92\xf7\x02\x02\x18\x01\x12\x90\x03\n\x1d\x43\x61rgoDescriptionAndRemarkRule\x12g.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CargoDescriptionAndRemarkRuleRequest\x1ah.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.CargoDescriptionAndRemarkRuleResponse"\x9b\x01\x8a\xf7\x02\x90\x01\x12[com.flexport.oceanops.carriershippinginstructiondataattribute.cargodescriptionandremarkrule\x1a&CargoDescription & Remark (rule-based)"\tocean_ops\x92\xf7\x02\x02\x18\x01\x12\xe7\x02\n\x12\x43ontractAttributes\x12\\.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.ContractAttributesRequest\x1a].flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.ContractAttributesResponse"\x93\x01\x8a\xf7\x02\x88\x01\x12Pcom.flexport.oceanops.carriershippinginstructiondataattribute.contractattributes\x1a)contract attributes (fak/nac/premium/...)"\tocean_ops\x9a\xf7\x02\x02\x08\x01\x12\x9e\x03\n\x1d\x46reightChargesPaymentLocation\x12g.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.FreightChargesPaymentLocationRequest\x1ah.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.FreightChargesPaymentLocationResponse"\xa9\x01\x8a\xf7\x02\x9e\x01\x12[com.flexport.oceanops.carriershippinginstructiondataattribute.freightchargespaymentlocation\x1a\x34\x46reight Charges Payment Location (rule-based) (FEWB)"\tocean_ops\x92\xf7\x02\x02\x18\x01\x1a\x0f\x8a\xf7\x02\x0b\n\tocean_opsB\xc1\x01\nEcom.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1B/CarrierShippingInstructionDataAttributeApiProtoP\x01\xea\x02\x44\x46lexport::OceanOps::CarrierShippingInstructionDataAttribute::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "flexport.oceanops.carriershippinginstructiondataattribute.v1beta1.carrier_shipping_instruction_data_attribute_api_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\nEcom.flexport.oceanops.carriershippinginstructiondataattribute.v1beta1B/CarrierShippingInstructionDataAttributeApiProtoP\001\352\002DFlexport::OceanOps::CarrierShippingInstructionDataAttribute::V1Beta1"
    _globals["_RATEGROUPANDREMARKREQUEST"]._options = None
    _globals["_RATEGROUPANDREMARKREQUEST"]._serialized_options = b"\202\367\002\033Rate Group & Remark Request"
    _globals["_RATEGROUPANDREMARKRESPONSE"]._options = None
    _globals["_RATEGROUPANDREMARKRESPONSE"]._serialized_options = b"\202\367\002\034Rate Group & Remark Response"
    _globals["_CARGODESCRIPTIONANDREMARKREQUEST"]._options = None
    _globals["_CARGODESCRIPTIONANDREMARKREQUEST"]._serialized_options = b"\202\367\002\031CargoDescription & Remark"
    _globals["_CARGODESCRIPTIONANDREMARKRESPONSE"].fields_by_name["cargo_description"]._options = None
    _globals["_CARGODESCRIPTIONANDREMARKRESPONSE"].fields_by_name[
        "cargo_description"
    ]._serialized_options = b"\252\367\002\004\n\002\020\005"
    _globals["_CARGODESCRIPTIONANDREMARKRESPONSE"].fields_by_name["remark"]._options = None
    _globals["_CARGODESCRIPTIONANDREMARKRESPONSE"].fields_by_name[
        "remark"
    ]._serialized_options = b"\252\367\002\004\n\002\020\005"
    _globals["_CARGODESCRIPTIONANDREMARKRESPONSE"]._options = None
    _globals[
        "_CARGODESCRIPTIONANDREMARKRESPONSE"
    ]._serialized_options = (
        b"\202\367\002QBoth responses are nullable and may be templates for further string interpolation"
    )
    _globals["_CARGODESCRIPTIONANDREMARKVERTWOREQUEST"]._options = None
    _globals[
        "_CARGODESCRIPTIONANDREMARKVERTWOREQUEST"
    ]._serialized_options = b"\202\367\002\036CargoDescription & Remark (V2)"
    _globals["_CARGODESCRIPTIONANDREMARKVERTWORESPONSE"].fields_by_name["cargo_description"]._options = None
    _globals["_CARGODESCRIPTIONANDREMARKVERTWORESPONSE"].fields_by_name[
        "cargo_description"
    ]._serialized_options = b"\252\367\002\004\n\002\020\005"
    _globals["_CARGODESCRIPTIONANDREMARKVERTWORESPONSE"].fields_by_name["remark"]._options = None
    _globals["_CARGODESCRIPTIONANDREMARKVERTWORESPONSE"].fields_by_name[
        "remark"
    ]._serialized_options = b"\252\367\002\004\n\002\020\005"
    _globals["_CARGODESCRIPTIONANDREMARKVERTWORESPONSE"]._options = None
    _globals[
        "_CARGODESCRIPTIONANDREMARKVERTWORESPONSE"
    ]._serialized_options = (
        b"\202\367\002QBoth responses are nullable and may be templates for further string interpolation"
    )
    _globals["_CONTRACTNACINFOREQUEST"]._options = None
    _globals[
        "_CONTRACTNACINFOREQUEST"
    ]._serialized_options = b"\202\367\002ANeeds ContractNumber and ClientId to determine the mapped NacInfo"
    _globals["_CONTRACTNACINFORESPONSE"]._options = None
    _globals[
        "_CONTRACTNACINFORESPONSE"
    ]._serialized_options = b"\202\367\0024Nac info: client name, and optionally commodity name"
    _globals["_FIXEDACCOUNTBOOKINGINFOREQUEST"]._options = None
    _globals["_FIXEDACCOUNTBOOKINGINFOREQUEST"]._serialized_options = b"\202\367\002\032Fixed account booking info"
    _globals["_FIXEDACCOUNTBOOKINGINFORESPONSE"]._options = None
    _globals[
        "_FIXEDACCOUNTBOOKINGINFORESPONSE"
    ]._serialized_options = b"\202\367\002*Fixed account booking code and client_name"
    _globals["_CARRIERRATEGROUPREQUEST"]._options = None
    _globals["_CARRIERRATEGROUPREQUEST"]._serialized_options = b"\202\367\002\022Carrier rate group"
    _globals["_CARRIERRATEGROUPRESPONSE"]._options = None
    _globals["_CARRIERRATEGROUPRESPONSE"]._serialized_options = b"\202\367\002\022Carrier rate group"
    _globals["_BILLOFLADINGCOMMENTSOTHERNOTESREQUEST"]._options = None
    _globals[
        "_BILLOFLADINGCOMMENTSOTHERNOTESREQUEST"
    ]._serialized_options = b"\202\367\002 B/L Comments Other Notes Request"
    _globals["_BILLOFLADINGCOMMENTSOTHERNOTESRESPONSE"].fields_by_name["output"]._options = None
    _globals["_BILLOFLADINGCOMMENTSOTHERNOTESRESPONSE"].fields_by_name[
        "output"
    ]._serialized_options = b"\270\367\002\001"
    _globals["_BILLOFLADINGCOMMENTSOTHERNOTESRESPONSE"]._options = None
    _globals[
        "_BILLOFLADINGCOMMENTSOTHERNOTESRESPONSE"
    ]._serialized_options = b"\202\367\002!B/L Comments Other Notes Response"
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST"]._options = None
    _globals[
        "_CARGODESCRIPTIONANDREMARKRULEREQUEST"
    ]._serialized_options = b"\202\367\002&CargoDescription & Remark (rule-based)"
    _globals["_CARGODESCRIPTIONANDREMARKRULERESPONSE"].fields_by_name["cargo_description"]._options = None
    _globals["_CARGODESCRIPTIONANDREMARKRULERESPONSE"].fields_by_name[
        "cargo_description"
    ]._serialized_options = b"\230\367\002\001\252\367\002\004\n\002\020\005\270\367\002\001"
    _globals["_CARGODESCRIPTIONANDREMARKRULERESPONSE"].fields_by_name["remark"]._options = None
    _globals["_CARGODESCRIPTIONANDREMARKRULERESPONSE"].fields_by_name[
        "remark"
    ]._serialized_options = b"\230\367\002\001\252\367\002\004\n\002\020\005\270\367\002\001"
    _globals["_CARGODESCRIPTIONANDREMARKRULERESPONSE"]._options = None
    _globals[
        "_CARGODESCRIPTIONANDREMARKRULERESPONSE"
    ]._serialized_options = b"\202\367\002&CargoDescription & Remark (rule-based)"
    _globals["_CONTRACTATTRIBUTESREQUEST"]._options = None
    _globals["_CONTRACTATTRIBUTESREQUEST"]._serialized_options = b"\202\367\002\033Contract Attributes Request"
    _globals["_CONTRACTATTRIBUTESRESPONSE"]._options = None
    _globals["_CONTRACTATTRIBUTESRESPONSE"]._serialized_options = b"\202\367\002\034Contract Attributes Response"
    _globals["_FREIGHTCHARGESPAYMENTLOCATIONREQUEST"]._options = None
    _globals[
        "_FREIGHTCHARGESPAYMENTLOCATIONREQUEST"
    ]._serialized_options = b"\202\367\002(Freight Charges Payment Location Request"
    _globals["_FREIGHTCHARGESPAYMENTLOCATIONRESPONSE"]._options = None
    _globals[
        "_FREIGHTCHARGESPAYMENTLOCATIONRESPONSE"
    ]._serialized_options = b"\202\367\002)Freight Charges Payment Location Response"
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"]._serialized_options = b"\212\367\002\013\n\tocean_ops"
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name["RateGroupAndRemark"]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "RateGroupAndRemark"
    ]._serialized_options = b'\212\367\002\221\001\022Pcom.flexport.oceanops.carriershippinginstructiondataattribute.rategroupandremark\0322Rate group & remark from carrier & contract number"\tocean_ops\222\367\002\002\030\001'
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name["CargoDescriptionAndRemark"]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "CargoDescriptionAndRemark"
    ]._serialized_options = b'\212\367\002\255\001\022Wcom.flexport.oceanops.carriershippinginstructiondataattribute.cargodescriptionandremark\032GCargoDescription & Remark, may return a template for further population"\tocean_ops\222\367\002\002\030\001\232\367\002\002\010\001'
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "CargoDescriptionAndRemarkVerTwo"
    ]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "CargoDescriptionAndRemarkVerTwo"
    ]._serialized_options = b'\212\367\002\257\001\022Ycom.flexport.oceanops.carriershippinginstructiondataattribute.cargodescriptionandremarkv2\032GCargoDescription & Remark, may return a template for further population"\tocean_ops\222\367\002\002\030\001\232\367\002\002\010\001'
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name["ContractNacInfo"]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "ContractNacInfo"
    ]._serialized_options = b'\212\367\002\241\001\022Mcom.flexport.oceanops.carriershippinginstructiondataattribute.contractnacinfo\032ECarrier contract nac info: client name, and optionally commodity name"\tocean_ops\222\367\002\002\030\001\232\367\002\002\010\001'
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name["FixedAccountBookingInfo"]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "FixedAccountBookingInfo"
    ]._serialized_options = b'\212\367\002~\022Ucom.flexport.oceanops.carriershippinginstructiondataattribute.fixedaccountbookinginfo\032\032Fixed account booking info"\tocean_ops\222\367\002\002\030\001\232\367\002\002\010\001'
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name["CarrierRateGroup"]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "CarrierRateGroup"
    ]._serialized_options = b'\212\367\002o\022Ncom.flexport.oceanops.carriershippinginstructiondataattribute.carrierrategroup\032\022Carrier rate group"\tocean_ops\222\367\002\002\030\001\232\367\002\002\010\001'
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "BillOfLadingCommentsOtherNotes"
    ]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "BillOfLadingCommentsOtherNotes"
    ]._serialized_options = b'\212\367\002\240\001\022\\com.flexport.oceanops.carriershippinginstructiondataattribute.billofladingcommentsothernotes\0325Carrier Shipping Instruction B/L Comments Other Notes"\tocean_ops\222\367\002\002\030\001'
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "CargoDescriptionAndRemarkRule"
    ]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "CargoDescriptionAndRemarkRule"
    ]._serialized_options = b'\212\367\002\220\001\022[com.flexport.oceanops.carriershippinginstructiondataattribute.cargodescriptionandremarkrule\032&CargoDescription & Remark (rule-based)"\tocean_ops\222\367\002\002\030\001'
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name["ContractAttributes"]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "ContractAttributes"
    ]._serialized_options = b'\212\367\002\210\001\022Pcom.flexport.oceanops.carriershippinginstructiondataattribute.contractattributes\032)contract attributes (fak/nac/premium/...)"\tocean_ops\232\367\002\002\010\001'
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "FreightChargesPaymentLocation"
    ]._options = None
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"].methods_by_name[
        "FreightChargesPaymentLocation"
    ]._serialized_options = b'\212\367\002\236\001\022[com.flexport.oceanops.carriershippinginstructiondataattribute.freightchargespaymentlocation\0324Freight Charges Payment Location (rule-based) (FEWB)"\tocean_ops\222\367\002\002\030\001'
    _globals["_RATEGROUPANDREMARKREQUEST"]._serialized_start = 281
    _globals["_RATEGROUPANDREMARKREQUEST"]._serialized_end = 925
    _globals["_RATEGROUPANDREMARKRESPONSE"]._serialized_start = 928
    _globals["_RATEGROUPANDREMARKRESPONSE"]._serialized_end = 1138
    _globals["_CARGODESCRIPTIONANDREMARKREQUEST"]._serialized_start = 1141
    _globals["_CARGODESCRIPTIONANDREMARKREQUEST"]._serialized_end = 1472
    _globals["_CARGODESCRIPTIONANDREMARKRESPONSE"]._serialized_start = 1475
    _globals["_CARGODESCRIPTIONANDREMARKRESPONSE"]._serialized_end = 1660
    _globals["_CARGODESCRIPTIONANDREMARKVERTWOREQUEST"]._serialized_start = 1663
    _globals["_CARGODESCRIPTIONANDREMARKVERTWOREQUEST"]._serialized_end = 1945
    _globals["_CARGODESCRIPTIONANDREMARKVERTWORESPONSE"]._serialized_start = 1948
    _globals["_CARGODESCRIPTIONANDREMARKVERTWORESPONSE"]._serialized_end = 2139
    _globals["_CONTRACTNACINFOREQUEST"]._serialized_start = 2142
    _globals["_CONTRACTNACINFOREQUEST"]._serialized_end = 2325
    _globals["_CONTRACTNACINFORESPONSE"]._serialized_start = 2327
    _globals["_CONTRACTNACINFORESPONSE"]._serialized_end = 2428
    _globals["_FIXEDACCOUNTBOOKINGINFOREQUEST"]._serialized_start = 2431
    _globals["_FIXEDACCOUNTBOOKINGINFOREQUEST"]._serialized_end = 2829
    _globals["_FIXEDACCOUNTBOOKINGINFORESPONSE"]._serialized_start = 2831
    _globals["_FIXEDACCOUNTBOOKINGINFORESPONSE"]._serialized_end = 2955
    _globals["_CARRIERRATEGROUPREQUEST"]._serialized_start = 2958
    _globals["_CARRIERRATEGROUPREQUEST"]._serialized_end = 3393
    _globals["_CARRIERRATEGROUPRESPONSE"]._serialized_start = 3395
    _globals["_CARRIERRATEGROUPRESPONSE"]._serialized_end = 3465
    _globals["_BILLOFLADINGCOMMENTSOTHERNOTESREQUEST"]._serialized_start = 3468
    _globals["_BILLOFLADINGCOMMENTSOTHERNOTESREQUEST"]._serialized_end = 3889
    _globals["_BILLOFLADINGCOMMENTSOTHERNOTESRESPONSE"]._serialized_start = 3891
    _globals["_BILLOFLADINGCOMMENTSOTHERNOTESRESPONSE"]._serialized_end = 3992
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST"]._serialized_start = 3995
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST"]._serialized_end = 6092
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST_ORIGINREGION"]._serialized_start = 5185
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST_ORIGINREGION"]._serialized_end = 5313
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST_DESTINATIONREGION"]._serialized_start = 5316
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST_DESTINATIONREGION"]._serialized_end = 5448
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST_FREIGHTTERM"]._serialized_start = 5450
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST_FREIGHTTERM"]._serialized_end = 5577
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST_PAYMENTLOCATION"]._serialized_start = 5579
    _globals["_CARGODESCRIPTIONANDREMARKRULEREQUEST_PAYMENTLOCATION"]._serialized_end = 5684
    _globals["_CARGODESCRIPTIONANDREMARKRULERESPONSE"]._serialized_start = 6095
    _globals["_CARGODESCRIPTIONANDREMARKRULERESPONSE"]._serialized_end = 6257
    _globals["_CONTRACTATTRIBUTESREQUEST"]._serialized_start = 6259
    _globals["_CONTRACTATTRIBUTESREQUEST"]._serialized_end = 6369
    _globals["_CONTRACTATTRIBUTESRESPONSE"]._serialized_start = 6371
    _globals["_CONTRACTATTRIBUTESRESPONSE"]._serialized_end = 6485
    _globals["_FREIGHTCHARGESPAYMENTLOCATIONREQUEST"]._serialized_start = 6488
    _globals["_FREIGHTCHARGESPAYMENTLOCATIONREQUEST"]._serialized_end = 6786
    _globals["_FREIGHTCHARGESPAYMENTLOCATIONRESPONSE"]._serialized_start = 6789
    _globals["_FREIGHTCHARGESPAYMENTLOCATIONRESPONSE"]._serialized_end = 7131
    _globals["_FREIGHTCHARGESPAYMENTLOCATIONRESPONSE_PAYMENTLOCATION"]._serialized_start = 5579
    _globals["_FREIGHTCHARGESPAYMENTLOCATIONRESPONSE_PAYMENTLOCATION"]._serialized_end = 5684
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"]._serialized_start = 7134
    _globals["_CARRIERSHIPPINGINSTRUCTIONDATAATTRIBUTEAPI"]._serialized_end = 11133
# @@protoc_insertion_point(module_scope)