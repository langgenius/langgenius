# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.originops.grpcserver.shipmentstatus.v1 import (
    shipment_status_api_pb2 as flexport_dot_originops_dot_grpcserver_dot_shipmentstatus_dot_v1_dot_shipment__status__api__pb2,
)


class ShipmentStatusAPIStub:
    """An API for rendering/mutating queues status of a shipment in origin ops service."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetShipmentStatus = channel.unary_unary(
            "/flexport.originops.grpcserver.shipmentstatus.v1.ShipmentStatusAPI/GetShipmentStatus",
            request_serializer=flexport_dot_originops_dot_grpcserver_dot_shipmentstatus_dot_v1_dot_shipment__status__api__pb2.GetShipmentStatusRequest.SerializeToString,
            response_deserializer=flexport_dot_originops_dot_grpcserver_dot_shipmentstatus_dot_v1_dot_shipment__status__api__pb2.GetShipmentStatusResponse.FromString,
        )


class ShipmentStatusAPIServicer:
    """An API for rendering/mutating queues status of a shipment in origin ops service."""

    def GetShipmentStatus(self, request, context):
        """Get all status of a shipment."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ShipmentStatusAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetShipmentStatus": grpc.unary_unary_rpc_method_handler(
            servicer.GetShipmentStatus,
            request_deserializer=flexport_dot_originops_dot_grpcserver_dot_shipmentstatus_dot_v1_dot_shipment__status__api__pb2.GetShipmentStatusRequest.FromString,
            response_serializer=flexport_dot_originops_dot_grpcserver_dot_shipmentstatus_dot_v1_dot_shipment__status__api__pb2.GetShipmentStatusResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.originops.grpcserver.shipmentstatus.v1.ShipmentStatusAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ShipmentStatusAPI:
    """An API for rendering/mutating queues status of a shipment in origin ops service."""

    @staticmethod
    def GetShipmentStatus(
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
            "/flexport.originops.grpcserver.shipmentstatus.v1.ShipmentStatusAPI/GetShipmentStatus",
            flexport_dot_originops_dot_grpcserver_dot_shipmentstatus_dot_v1_dot_shipment__status__api__pb2.GetShipmentStatusRequest.SerializeToString,
            flexport_dot_originops_dot_grpcserver_dot_shipmentstatus_dot_v1_dot_shipment__status__api__pb2.GetShipmentStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )