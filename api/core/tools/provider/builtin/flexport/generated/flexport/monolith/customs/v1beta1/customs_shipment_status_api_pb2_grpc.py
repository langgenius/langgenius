# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.monolith.customs.v1beta1 import (
    customs_shipment_status_api_pb2 as flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2,
)


class CustomsShipmentStatusAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CustomsShipmentReleased = channel.unary_unary(
            "/flexport.monolith.customs.v1beta1.CustomsShipmentStatusAPI/CustomsShipmentReleased",
            request_serializer=flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentReleasedRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentReleasedResponse.FromString,
        )
        self.CustomsShipmentCleared = channel.unary_unary(
            "/flexport.monolith.customs.v1beta1.CustomsShipmentStatusAPI/CustomsShipmentCleared",
            request_serializer=flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentClearedRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentClearedResponse.FromString,
        )


class CustomsShipmentStatusAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def CustomsShipmentReleased(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CustomsShipmentCleared(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CustomsShipmentStatusAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CustomsShipmentReleased": grpc.unary_unary_rpc_method_handler(
            servicer.CustomsShipmentReleased,
            request_deserializer=flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentReleasedRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentReleasedResponse.SerializeToString,
        ),
        "CustomsShipmentCleared": grpc.unary_unary_rpc_method_handler(
            servicer.CustomsShipmentCleared,
            request_deserializer=flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentClearedRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentClearedResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.monolith.customs.v1beta1.CustomsShipmentStatusAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class CustomsShipmentStatusAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CustomsShipmentReleased(
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
            "/flexport.monolith.customs.v1beta1.CustomsShipmentStatusAPI/CustomsShipmentReleased",
            flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentReleasedRequest.SerializeToString,
            flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentReleasedResponse.FromString,
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
    def CustomsShipmentCleared(
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
            "/flexport.monolith.customs.v1beta1.CustomsShipmentStatusAPI/CustomsShipmentCleared",
            flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentClearedRequest.SerializeToString,
            flexport_dot_monolith_dot_customs_dot_v1beta1_dot_customs__shipment__status__api__pb2.CustomsShipmentClearedResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )