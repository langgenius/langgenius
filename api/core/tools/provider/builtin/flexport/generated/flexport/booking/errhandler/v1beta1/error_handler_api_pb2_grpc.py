# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.booking.errhandler.v1beta1 import (
    error_handler_api_pb2 as flexport_dot_booking_dot_errhandler_dot_v1beta1_dot_error__handler__api__pb2,
)


class ErrorHandlerAPIStub:
    """We need to expose a http endpoint for the frontend of kotlin error handler to get data."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListBlockedEvents = channel.unary_unary(
            "/flexport.booking.errhandler.v1beta1.ErrorHandlerAPI/ListBlockedEvents",
            request_serializer=flexport_dot_booking_dot_errhandler_dot_v1beta1_dot_error__handler__api__pb2.ListBlockedEventsRequest.SerializeToString,
            response_deserializer=flexport_dot_booking_dot_errhandler_dot_v1beta1_dot_error__handler__api__pb2.ListBlockedEventsResponse.FromString,
        )


class ErrorHandlerAPIServicer:
    """We need to expose a http endpoint for the frontend of kotlin error handler to get data."""

    def ListBlockedEvents(self, request, context):
        """This Http endpoint is used for the frontend to get a list of blocked events."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ErrorHandlerAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListBlockedEvents": grpc.unary_unary_rpc_method_handler(
            servicer.ListBlockedEvents,
            request_deserializer=flexport_dot_booking_dot_errhandler_dot_v1beta1_dot_error__handler__api__pb2.ListBlockedEventsRequest.FromString,
            response_serializer=flexport_dot_booking_dot_errhandler_dot_v1beta1_dot_error__handler__api__pb2.ListBlockedEventsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.booking.errhandler.v1beta1.ErrorHandlerAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ErrorHandlerAPI:
    """We need to expose a http endpoint for the frontend of kotlin error handler to get data."""

    @staticmethod
    def ListBlockedEvents(
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
            "/flexport.booking.errhandler.v1beta1.ErrorHandlerAPI/ListBlockedEvents",
            flexport_dot_booking_dot_errhandler_dot_v1beta1_dot_error__handler__api__pb2.ListBlockedEventsRequest.SerializeToString,
            flexport_dot_booking_dot_errhandler_dot_v1beta1_dot_error__handler__api__pb2.ListBlockedEventsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )