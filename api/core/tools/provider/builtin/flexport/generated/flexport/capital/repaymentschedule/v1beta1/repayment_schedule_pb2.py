# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/capital/repaymentschedule/v1beta1/repayment_schedule.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nCflexport/capital/repaymentschedule/v1beta1/repayment_schedule.proto\x12*flexport.capital.repaymentschedule.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x19google/type/decimal.proto"\xa5\x05\n\x11RepaymentSchedule\x12\x0f\n\x07loan_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x12\x15\n\rcurrency_code\x18\x04 \x01(\t\x12\x10\n\x08\x64ue_date\x18\x05 \x01(\t\x12\x13\n\x0bpaid_amount\x18\x06 \x01(\x03\x12K\n\x06status\x18\x07 \x01(\x0e\x32;.flexport.capital.repaymentschedule.v1beta1.RepaymentStatus\x12\x1a\n\x12\x63\x61pital_invoice_id\x18\x08 \x01(\t\x12\x11\n\tprinciple\x18\t \x01(\x03\x12\x0b\n\x03\x66\x65\x65\x18\n \x01(\x03\x12\x13\n\x0bschedule_id\x18\x0b \x01(\t\x12\x12\n\ninvoice_id\x18\x0c \x01(\t\x12\x12\n\namount_usd\x18\r \x01(\x03\x12\x17\n\x0fpaid_amount_usd\x18\x0e \x01(\x03\x12\x1c\n\x14principal_amount_usd\x18\x0f \x01(\x03\x12\x16\n\x0e\x66\x65\x65_amount_usd\x18\x10 \x01(\x03\x12+\n\rexchange_rate\x18\x11 \x01(\x0b\x32\x14.google.type.Decimal\x12\x37\n\x11\x65xchange_rate_fid\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x39\n\x13\x63\x61pital_invoice_fid\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0f\x63reated_at_time\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"i\n\x1aRepaymentStatusFilterValue\x12K\n\x06values\x18\x02 \x03(\x0e\x32;.flexport.capital.repaymentschedule.v1beta1.RepaymentStatus"\xcf\x02\n\x18RepaymentScheduleFilters\x12/\n\tclient_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12V\n\x06status\x18\x02 \x01(\x0b\x32\x46.flexport.capital.repaymentschedule.v1beta1.RepaymentStatusFilterValue\x12\x37\n\x13\x64ue_date_after_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14\x64ue_date_before_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x11search_parameters\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue"\x92\x03\n\x07Payment\x12\x13\n\x0bpayment_fid\x18\x01 \x01(\t\x12\x1e\n\x16repayment_schedule_fid\x18\x02 \x01(\t\x12\x15\n\rcurrency_code\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\x12\x12\n\namount_usd\x18\x05 \x01(\x03\x12;\n\x15payment_line_item_fid\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x11\x65\x66\x66\x65\x63tive_at_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x13\x63\x61nopy_line_item_id\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0f\x63reated_at_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp"\xa4\x03\n\x06Refund\x12\x12\n\nrefund_fid\x18\x01 \x01(\t\x12\x1e\n\x16repayment_schedule_fid\x18\x02 \x01(\t\x12\x13\n\x0bpayment_fid\x18\x03 \x01(\t\x12\x15\n\rcurrency_code\x18\x04 \x01(\t\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x03\x12\x12\n\namount_usd\x18\x06 \x01(\x03\x12:\n\x14refund_line_item_fid\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x11\x65\x66\x66\x65\x63tive_at_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x13\x63\x61nopy_line_item_id\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0f\x63reated_at_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fupdated_at_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\xa3\x01\n\x0fRepaymentStatus\x12\x1c\n\x18REPAYMENT_STATUS_INVALID\x10\x00\x12\x1b\n\x17REPAYMENT_STATUS_UNPAID\x10\x01\x12\x19\n\x15REPAYMENT_STATUS_PAID\x10\x02\x12\x1c\n\x18REPAYMENT_STATUS_PARTIAL\x10\x03\x12\x1c\n\x18REPAYMENT_STATUS_OVERDUE\x10\x04\x42z\n.com.flexport.capital.repaymentschedule.v1beta1B\x16RepaymentScheduleProtoP\x01\xea\x02-Flexport::Capital::RepaymentSchedule::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.capital.repaymentschedule.v1beta1.repayment_schedule_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n.com.flexport.capital.repaymentschedule.v1beta1B\026RepaymentScheduleProtoP\001\352\002-Flexport::Capital::RepaymentSchedule::V1Beta1"
    _globals["_REPAYMENTSTATUS"]._serialized_start = 2161
    _globals["_REPAYMENTSTATUS"]._serialized_end = 2324
    _globals["_REPAYMENTSCHEDULE"]._serialized_start = 208
    _globals["_REPAYMENTSCHEDULE"]._serialized_end = 885
    _globals["_REPAYMENTSTATUSFILTERVALUE"]._serialized_start = 887
    _globals["_REPAYMENTSTATUSFILTERVALUE"]._serialized_end = 992
    _globals["_REPAYMENTSCHEDULEFILTERS"]._serialized_start = 995
    _globals["_REPAYMENTSCHEDULEFILTERS"]._serialized_end = 1330
    _globals["_PAYMENT"]._serialized_start = 1333
    _globals["_PAYMENT"]._serialized_end = 1735
    _globals["_REFUND"]._serialized_start = 1738
    _globals["_REFUND"]._serialized_end = 2158
# @@protoc_insertion_point(module_scope)