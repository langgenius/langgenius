# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/customs/productlibrary/products/v1beta1/product.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n>flexport/customs/productlibrary/products/v1beta1/product.proto\x12\x30\x66lexport.customs.productlibrary.products.v1beta1\x1a\x41\x66lexport/customs/productlibrary/common/v1beta1/country_code.proto\x1a\x64\x66lexport/customs/productlibrary/products/productcountryspecific/us/v1beta1/product_us_specific.proto\x1a=flexport/customs/productlibrary/products/v1beta1/tariff.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xb3\x01\n\x12ProductWithContext\x12Q\n\x07\x63ontext\x18\x01 \x01(\x0b\x32@.flexport.customs.productlibrary.products.v1beta1.ProductContext\x12J\n\x07product\x18\x02 \x01(\x0b\x32\x39.flexport.customs.productlibrary.products.v1beta1.Product"\x9e\x02\n\x0eProductContext\x12V\n\x11\x63ountry_of_import\x18\x01 \x01(\x0e\x32;.flexport.customs.productlibrary.common.v1beta1.CountryCode\x12V\n\x11\x63ountry_of_origin\x18\x02 \x01(\x0e\x32;.flexport.customs.productlibrary.common.v1beta1.CountryCode\x12V\n\x11\x63ountry_of_export\x18\x03 \x01(\x0e\x32;.flexport.customs.productlibrary.common.v1beta1.CountryCodeJ\x04\x08\x04\x10\x05"\xb8\x12\n\x07Product\x12\x13\n\x0bproduct_fid\x18\x01 \x01(\t\x12\x0b\n\x03sku\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\nclient_fid\x18\x04 \x01(\t\x12U\n\nproperties\x18\x07 \x03(\x0b\x32\x41.flexport.customs.productlibrary.products.v1beta1.ProductProperty\x12M\n\x0btariff_info\x18\x05 \x03(\x0b\x32\x38.flexport.customs.productlibrary.products.v1beta1.Tariff\x12p\n\x16\x63ountry_specific_infos\x18\x08 \x03(\x0b\x32P.flexport.customs.productlibrary.products.v1beta1.Product.ProductCountrySpecific\x12\x0c\n\x04name\x18\t \x01(\t\x12^\n\nconditions\x18\x06 \x03(\x0b\x32J.flexport.customs.productlibrary.products.v1beta1.Product.ProductCondition\x1a\x96\x01\n\x16ProductCountrySpecific\x12t\n\x0bus_specific\x18\x01 \x01(\x0b\x32].flexport.customs.productlibrary.products.productcountryspecific.us.v1beta1.ProductUsSpecificH\x00\x42\x06\n\x04info\x1a\xc2\r\n\x10ProductCondition\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12w\n\x0e\x63ondition_type\x18\x02 \x01(\x0e\x32_.flexport.customs.productlibrary.products.v1beta1.Product.ProductCondition.ProductConditionType\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x14\n\x07message\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x32\n\x0elast_evaluated\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x91\x01\n\x1e\x63lassification_missing_context\x18\x65 \x01(\x0b\x32g.flexport.customs.productlibrary.products.v1beta1.Product.ProductCondition.ClassificationMissingContextH\x00\x12\x8e\x01\n\x1d\x63otton_fee_incomplete_context\x18\x66 \x01(\x0b\x32\x65.flexport.customs.productlibrary.products.v1beta1.Product.ProductCondition.CottonFeeIncompleteContextH\x00\x1a\x9c\x03\n\x1c\x43lassificationMissingContext\x12V\n\x11\x63ountry_of_import\x18\x01 \x01(\x0e\x32;.flexport.customs.productlibrary.common.v1beta1.CountryCode\x12V\n\x11\x63ountry_of_origin\x18\x02 \x01(\x0e\x32;.flexport.customs.productlibrary.common.v1beta1.CountryCode\x12v\n\x06reason\x18\x03 \x01(\x0e\x32\x66.flexport.customs.productlibrary.products.v1beta1.Product.ProductCondition.ClassificationMissingReason\x12T\n\x05\x61\x63tor\x18\x04 \x01(\x0e\x32\x45.flexport.customs.productlibrary.products.v1beta1.ClassificationActor\x1at\n\x1a\x43ottonFeeIncompleteContext\x12V\n\x11\x63ountry_of_import\x18\x01 \x01(\x0e\x32;.flexport.customs.productlibrary.common.v1beta1.CountryCode"\xd2\x02\n\x14ProductConditionType\x12"\n\x1ePRODUCT_CONDITION_TYPE_INVALID\x10\x00\x12\x31\n-PRODUCT_CONDITION_TYPE_CLASSIFICATION_MISSING\x10\x08\x12\x30\n,PRODUCT_CONDITION_TYPE_COTTON_FEE_INCOMPLETE\x10\x03\x12\x39\n5PRODUCT_CONDITION_TYPE_SPECIAL_TARIFFS_301_INCOMPLETE\x10\x02\x12\x31\n-PRODUCT_CONDITION_TYPE_FDA_PROFILE_INCOMPLETE\x10\x04\x12\x31\n-PRODUCT_CONDITION_TYPE_EPA_PROFILE_INCOMPLETE\x10\x05"\x04\x08\x01\x10\x01"\x04\x08\x06\x10\x06"\x04\x08\x07\x10\x07"\x88\x02\n\x1b\x43lassificationMissingReason\x12)\n%CLASSIFICATION_MISSING_REASON_INVALID\x10\x00\x12;\n7CLASSIFICATION_MISSING_REASON_CLASSIFICATION_INCOMPLETE\x10\x01\x12\x41\n=CLASSIFICATION_MISSING_REASON_CLASSIFICATION_MORE_INFO_NEEDED\x10\x02\x12>\n:CLASSIFICATION_MISSING_REASON_CLASSIFICATION_PENDING_AUDIT\x10\x03\x42\t\n\x07\x63ontextB\n\n\x08_message".\n\x0fProductProperty\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t*\x85\x01\n\x13\x43lassificationActor\x12 \n\x1c\x43LASSIFICATION_ACTOR_INVALID\x10\x00\x12*\n&CLASSIFICATION_ACTOR_FLEXPORT_INTERNAL\x10\x01\x12 \n\x1c\x43LASSIFICATION_ACTOR_AVALARA\x10\x02\x42}\n4com.flexport.customs.productlibrary.products.v1beta1B\x0cProductProtoP\x01\xea\x02\x34\x46lexport::Customs::ProductLibrary::Products::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "flexport.customs.productlibrary.products.v1beta1.product_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n4com.flexport.customs.productlibrary.products.v1beta1B\014ProductProtoP\001\352\0024Flexport::Customs::ProductLibrary::Products::V1Beta1"
    _globals["_CLASSIFICATIONACTOR"]._serialized_start = 3296
    _globals["_CLASSIFICATIONACTOR"]._serialized_end = 3429
    _globals["_PRODUCTWITHCONTEXT"]._serialized_start = 414
    _globals["_PRODUCTWITHCONTEXT"]._serialized_end = 593
    _globals["_PRODUCTCONTEXT"]._serialized_start = 596
    _globals["_PRODUCTCONTEXT"]._serialized_end = 882
    _globals["_PRODUCT"]._serialized_start = 885
    _globals["_PRODUCT"]._serialized_end = 3245
    _globals["_PRODUCT_PRODUCTCOUNTRYSPECIFIC"]._serialized_start = 1362
    _globals["_PRODUCT_PRODUCTCOUNTRYSPECIFIC"]._serialized_end = 1512
    _globals["_PRODUCT_PRODUCTCONDITION"]._serialized_start = 1515
    _globals["_PRODUCT_PRODUCTCONDITION"]._serialized_end = 3245
    _globals["_PRODUCT_PRODUCTCONDITION_CLASSIFICATIONMISSINGCONTEXT"]._serialized_start = 2084
    _globals["_PRODUCT_PRODUCTCONDITION_CLASSIFICATIONMISSINGCONTEXT"]._serialized_end = 2496
    _globals["_PRODUCT_PRODUCTCONDITION_COTTONFEEINCOMPLETECONTEXT"]._serialized_start = 2498
    _globals["_PRODUCT_PRODUCTCONDITION_COTTONFEEINCOMPLETECONTEXT"]._serialized_end = 2614
    _globals["_PRODUCT_PRODUCTCONDITION_PRODUCTCONDITIONTYPE"]._serialized_start = 2617
    _globals["_PRODUCT_PRODUCTCONDITION_PRODUCTCONDITIONTYPE"]._serialized_end = 2955
    _globals["_PRODUCT_PRODUCTCONDITION_CLASSIFICATIONMISSINGREASON"]._serialized_start = 2958
    _globals["_PRODUCT_PRODUCTCONDITION_CLASSIFICATIONMISSINGREASON"]._serialized_end = 3222
    _globals["_PRODUCTPROPERTY"]._serialized_start = 3247
    _globals["_PRODUCTPROPERTY"]._serialized_end = 3293
# @@protoc_insertion_point(module_scope)