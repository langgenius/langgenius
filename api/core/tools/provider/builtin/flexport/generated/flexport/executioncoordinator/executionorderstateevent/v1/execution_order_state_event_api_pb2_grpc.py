# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.executioncoordinator.executionorderstateevent.v1 import (
    execution_order_state_event_api_pb2 as flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2,
)


class ExecutionOrderStateEventAPIStub:
    """An API for reading ExecutionOrderStateEvent."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetExecutionOrderStateEvent = channel.unary_unary(
            "/flexport.executioncoordinator.executionorderstateevent.v1.ExecutionOrderStateEventAPI/GetExecutionOrderStateEvent",
            request_serializer=flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.GetExecutionOrderStateEventRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.GetExecutionOrderStateEventResponse.FromString,
        )
        self.BackfillExecutionOrderStateEvent = channel.unary_unary(
            "/flexport.executioncoordinator.executionorderstateevent.v1.ExecutionOrderStateEventAPI/BackfillExecutionOrderStateEvent",
            request_serializer=flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.BackfillExecutionOrderStateEventRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.BackfillExecutionOrderStateEventResponse.FromString,
        )


class ExecutionOrderStateEventAPIServicer:
    """An API for reading ExecutionOrderStateEvent."""

    def GetExecutionOrderStateEvent(self, request, context):
        """Retrieves an ExecutionOrderStateEvent."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BackfillExecutionOrderStateEvent(self, request, context):
        """Backfills an ExecutionOrderStateEvent."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ExecutionOrderStateEventAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetExecutionOrderStateEvent": grpc.unary_unary_rpc_method_handler(
            servicer.GetExecutionOrderStateEvent,
            request_deserializer=flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.GetExecutionOrderStateEventRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.GetExecutionOrderStateEventResponse.SerializeToString,
        ),
        "BackfillExecutionOrderStateEvent": grpc.unary_unary_rpc_method_handler(
            servicer.BackfillExecutionOrderStateEvent,
            request_deserializer=flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.BackfillExecutionOrderStateEventRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.BackfillExecutionOrderStateEventResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.executioncoordinator.executionorderstateevent.v1.ExecutionOrderStateEventAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ExecutionOrderStateEventAPI:
    """An API for reading ExecutionOrderStateEvent."""

    @staticmethod
    def GetExecutionOrderStateEvent(
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
            "/flexport.executioncoordinator.executionorderstateevent.v1.ExecutionOrderStateEventAPI/GetExecutionOrderStateEvent",
            flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.GetExecutionOrderStateEventRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.GetExecutionOrderStateEventResponse.FromString,
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
    def BackfillExecutionOrderStateEvent(
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
            "/flexport.executioncoordinator.executionorderstateevent.v1.ExecutionOrderStateEventAPI/BackfillExecutionOrderStateEvent",
            flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.BackfillExecutionOrderStateEventRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executionorderstateevent_dot_v1_dot_execution__order__state__event__api__pb2.BackfillExecutionOrderStateEventResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )