# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.monolith.compliance.dangerousgoods.rpc.v1beta1 import (
    document_scraper_shipment_details_api_pb2 as flexport_dot_monolith_dot_compliance_dot_dangerousgoods_dot_rpc_dot_v1beta1_dot_document__scraper__shipment__details__api__pb2,
)


class DocumentScraperShipmentDetailsAPIStub:
    """API for fetching shipment data needed for DocumentScraper screening decisions."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDocumentScraperShipmentDetails = channel.unary_unary(
            "/flexport.monolith.compliance.dangerousgoods.rpc.v1beta1.DocumentScraperShipmentDetailsAPI/GetDocumentScraperShipmentDetails",
            request_serializer=flexport_dot_monolith_dot_compliance_dot_dangerousgoods_dot_rpc_dot_v1beta1_dot_document__scraper__shipment__details__api__pb2.GetDocumentScraperShipmentDetailsRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_compliance_dot_dangerousgoods_dot_rpc_dot_v1beta1_dot_document__scraper__shipment__details__api__pb2.GetDocumentScraperShipmentDetailsResponse.FromString,
        )


class DocumentScraperShipmentDetailsAPIServicer:
    """API for fetching shipment data needed for DocumentScraper screening decisions."""

    def GetDocumentScraperShipmentDetails(self, request, context):
        """Fetch shipment data for a given shipmentFid."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DocumentScraperShipmentDetailsAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetDocumentScraperShipmentDetails": grpc.unary_unary_rpc_method_handler(
            servicer.GetDocumentScraperShipmentDetails,
            request_deserializer=flexport_dot_monolith_dot_compliance_dot_dangerousgoods_dot_rpc_dot_v1beta1_dot_document__scraper__shipment__details__api__pb2.GetDocumentScraperShipmentDetailsRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_compliance_dot_dangerousgoods_dot_rpc_dot_v1beta1_dot_document__scraper__shipment__details__api__pb2.GetDocumentScraperShipmentDetailsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.monolith.compliance.dangerousgoods.rpc.v1beta1.DocumentScraperShipmentDetailsAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class DocumentScraperShipmentDetailsAPI:
    """API for fetching shipment data needed for DocumentScraper screening decisions."""

    @staticmethod
    def GetDocumentScraperShipmentDetails(
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
            "/flexport.monolith.compliance.dangerousgoods.rpc.v1beta1.DocumentScraperShipmentDetailsAPI/GetDocumentScraperShipmentDetails",
            flexport_dot_monolith_dot_compliance_dot_dangerousgoods_dot_rpc_dot_v1beta1_dot_document__scraper__shipment__details__api__pb2.GetDocumentScraperShipmentDetailsRequest.SerializeToString,
            flexport_dot_monolith_dot_compliance_dot_dangerousgoods_dot_rpc_dot_v1beta1_dot_document__scraper__shipment__details__api__pb2.GetDocumentScraperShipmentDetailsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )