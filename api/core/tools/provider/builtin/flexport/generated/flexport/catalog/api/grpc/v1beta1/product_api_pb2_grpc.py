# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.catalog.api.grpc.v1beta1 import (
    product_api_pb2 as flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2,
)


class ProductEntryAPIStub:
    """Document based product entry based on predefined product schema"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateProductEntry = channel.unary_unary(
            "/flexport.catalog.api.grpc.v1beta1.ProductEntryAPI/CreateProductEntry",
            request_serializer=flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.CreateProductEntryRequest.SerializeToString,
            response_deserializer=flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.CreateProductEntryResponse.FromString,
        )
        self.SearchProductEntries = channel.unary_unary(
            "/flexport.catalog.api.grpc.v1beta1.ProductEntryAPI/SearchProductEntries",
            request_serializer=flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.SearchProductEntriesRequest.SerializeToString,
            response_deserializer=flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.SearchProductEntriesResponse.FromString,
        )


class ProductEntryAPIServicer:
    """Document based product entry based on predefined product schema"""

    def CreateProductEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SearchProductEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ProductEntryAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateProductEntry": grpc.unary_unary_rpc_method_handler(
            servicer.CreateProductEntry,
            request_deserializer=flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.CreateProductEntryRequest.FromString,
            response_serializer=flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.CreateProductEntryResponse.SerializeToString,
        ),
        "SearchProductEntries": grpc.unary_unary_rpc_method_handler(
            servicer.SearchProductEntries,
            request_deserializer=flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.SearchProductEntriesRequest.FromString,
            response_serializer=flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.SearchProductEntriesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.catalog.api.grpc.v1beta1.ProductEntryAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ProductEntryAPI:
    """Document based product entry based on predefined product schema"""

    @staticmethod
    def CreateProductEntry(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/flexport.catalog.api.grpc.v1beta1.ProductEntryAPI/CreateProductEntry",
            flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.CreateProductEntryRequest.SerializeToString,
            flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.CreateProductEntryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SearchProductEntries(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/flexport.catalog.api.grpc.v1beta1.ProductEntryAPI/SearchProductEntries",
            flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.SearchProductEntriesRequest.SerializeToString,
            flexport_dot_catalog_dot_api_dot_grpc_dot_v1beta1_dot_product__api__pb2.SearchProductEntriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )