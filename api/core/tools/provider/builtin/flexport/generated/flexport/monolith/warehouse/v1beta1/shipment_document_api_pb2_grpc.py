# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.monolith.warehouse.v1beta1 import (
    shipment_document_api_pb2 as flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2,
)


class ShipmentDocumentAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchDocuments = channel.unary_unary(
            "/flexport.monolith.warehouse.v1beta1.ShipmentDocumentAPI/SearchDocuments",
            request_serializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.SearchDocumentsRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.SearchDocumentsResponse.FromString,
        )
        self.DownloadDocument = channel.unary_unary(
            "/flexport.monolith.warehouse.v1beta1.ShipmentDocumentAPI/DownloadDocument",
            request_serializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.DownloadDocumentRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.DownloadDocumentResponse.FromString,
        )
        self.PreSignedUploadUrl = channel.unary_unary(
            "/flexport.monolith.warehouse.v1beta1.ShipmentDocumentAPI/PreSignedUploadUrl",
            request_serializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.PreSignedUploadUrlRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.PreSignedUploadUrlResponse.FromString,
        )
        self.UploadDocuments = channel.unary_unary(
            "/flexport.monolith.warehouse.v1beta1.ShipmentDocumentAPI/UploadDocuments",
            request_serializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.UploadDocumentsRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.UploadDocumentsResponse.FromString,
        )


class ShipmentDocumentAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def SearchDocuments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DownloadDocument(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PreSignedUploadUrl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UploadDocuments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ShipmentDocumentAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SearchDocuments": grpc.unary_unary_rpc_method_handler(
            servicer.SearchDocuments,
            request_deserializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.SearchDocumentsRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.SearchDocumentsResponse.SerializeToString,
        ),
        "DownloadDocument": grpc.unary_unary_rpc_method_handler(
            servicer.DownloadDocument,
            request_deserializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.DownloadDocumentRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.DownloadDocumentResponse.SerializeToString,
        ),
        "PreSignedUploadUrl": grpc.unary_unary_rpc_method_handler(
            servicer.PreSignedUploadUrl,
            request_deserializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.PreSignedUploadUrlRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.PreSignedUploadUrlResponse.SerializeToString,
        ),
        "UploadDocuments": grpc.unary_unary_rpc_method_handler(
            servicer.UploadDocuments,
            request_deserializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.UploadDocumentsRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.UploadDocumentsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.monolith.warehouse.v1beta1.ShipmentDocumentAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ShipmentDocumentAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SearchDocuments(
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
            "/flexport.monolith.warehouse.v1beta1.ShipmentDocumentAPI/SearchDocuments",
            flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.SearchDocumentsRequest.SerializeToString,
            flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.SearchDocumentsResponse.FromString,
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
    def DownloadDocument(
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
            "/flexport.monolith.warehouse.v1beta1.ShipmentDocumentAPI/DownloadDocument",
            flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.DownloadDocumentRequest.SerializeToString,
            flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.DownloadDocumentResponse.FromString,
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
    def PreSignedUploadUrl(
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
            "/flexport.monolith.warehouse.v1beta1.ShipmentDocumentAPI/PreSignedUploadUrl",
            flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.PreSignedUploadUrlRequest.SerializeToString,
            flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.PreSignedUploadUrlResponse.FromString,
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
    def UploadDocuments(
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
            "/flexport.monolith.warehouse.v1beta1.ShipmentDocumentAPI/UploadDocuments",
            flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.UploadDocumentsRequest.SerializeToString,
            flexport_dot_monolith_dot_warehouse_dot_v1beta1_dot_shipment__document__api__pb2.UploadDocumentsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )