# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.dumboindexing.derivedshipment.v1beta1 import (
    filter_shipments_api_pb2 as flexport_dot_dumboindexing_dot_derivedshipment_dot_v1beta1_dot_filter__shipments__api__pb2,
)


class FilterShipmentsAPIStub:
    """An API for interacting with DerivedShipment entities."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListShipmentIdentifiersByFilters = channel.unary_unary(
            "/flexport.dumboindexing.derivedshipment.v1beta1.FilterShipmentsAPI/ListShipmentIdentifiersByFilters",
            request_serializer=flexport_dot_dumboindexing_dot_derivedshipment_dot_v1beta1_dot_filter__shipments__api__pb2.ListShipmentIdentifiersByFiltersRequest.SerializeToString,
            response_deserializer=flexport_dot_dumboindexing_dot_derivedshipment_dot_v1beta1_dot_filter__shipments__api__pb2.ListShipmentIdentifiersByFiltersResponse.FromString,
        )


class FilterShipmentsAPIServicer:
    """An API for interacting with DerivedShipment entities."""

    def ListShipmentIdentifiersByFilters(self, request, context):
        """Lists identifiers for filtered shipments."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FilterShipmentsAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListShipmentIdentifiersByFilters": grpc.unary_unary_rpc_method_handler(
            servicer.ListShipmentIdentifiersByFilters,
            request_deserializer=flexport_dot_dumboindexing_dot_derivedshipment_dot_v1beta1_dot_filter__shipments__api__pb2.ListShipmentIdentifiersByFiltersRequest.FromString,
            response_serializer=flexport_dot_dumboindexing_dot_derivedshipment_dot_v1beta1_dot_filter__shipments__api__pb2.ListShipmentIdentifiersByFiltersResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.dumboindexing.derivedshipment.v1beta1.FilterShipmentsAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class FilterShipmentsAPI:
    """An API for interacting with DerivedShipment entities."""

    @staticmethod
    def ListShipmentIdentifiersByFilters(
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
            "/flexport.dumboindexing.derivedshipment.v1beta1.FilterShipmentsAPI/ListShipmentIdentifiersByFilters",
            flexport_dot_dumboindexing_dot_derivedshipment_dot_v1beta1_dot_filter__shipments__api__pb2.ListShipmentIdentifiersByFiltersRequest.SerializeToString,
            flexport_dot_dumboindexing_dot_derivedshipment_dot_v1beta1_dot_filter__shipments__api__pb2.ListShipmentIdentifiersByFiltersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )