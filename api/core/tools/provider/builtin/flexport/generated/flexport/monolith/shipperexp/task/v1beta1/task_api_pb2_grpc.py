# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.monolith.shipperexp.task.v1beta1 import (
    task_api_pb2 as flexport_dot_monolith_dot_shipperexp_dot_task_dot_v1beta1_dot_task__api__pb2,
)


class TaskAPIStub:
    """Shipper_exp document task service.
    https://docs.google.com/document/d/1Z352tx59bmBchQRqHD4SGQlBR2uG4_NOh4akQmKqsmg
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MarkTaskStatus = channel.unary_unary(
            "/flexport.monolith.shipperexp.task.v1beta1.TaskAPI/MarkTaskStatus",
            request_serializer=flexport_dot_monolith_dot_shipperexp_dot_task_dot_v1beta1_dot_task__api__pb2.MarkTaskStatusRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_shipperexp_dot_task_dot_v1beta1_dot_task__api__pb2.MarkTaskStatusResponse.FromString,
        )


class TaskAPIServicer:
    """Shipper_exp document task service.
    https://docs.google.com/document/d/1Z352tx59bmBchQRqHD4SGQlBR2uG4_NOh4akQmKqsmg
    """

    def MarkTaskStatus(self, request, context):
        """Mark task status."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TaskAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "MarkTaskStatus": grpc.unary_unary_rpc_method_handler(
            servicer.MarkTaskStatus,
            request_deserializer=flexport_dot_monolith_dot_shipperexp_dot_task_dot_v1beta1_dot_task__api__pb2.MarkTaskStatusRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_shipperexp_dot_task_dot_v1beta1_dot_task__api__pb2.MarkTaskStatusResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.monolith.shipperexp.task.v1beta1.TaskAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class TaskAPI:
    """Shipper_exp document task service.
    https://docs.google.com/document/d/1Z352tx59bmBchQRqHD4SGQlBR2uG4_NOh4akQmKqsmg
    """

    @staticmethod
    def MarkTaskStatus(
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
            "/flexport.monolith.shipperexp.task.v1beta1.TaskAPI/MarkTaskStatus",
            flexport_dot_monolith_dot_shipperexp_dot_task_dot_v1beta1_dot_task__api__pb2.MarkTaskStatusRequest.SerializeToString,
            flexport_dot_monolith_dot_shipperexp_dot_task_dot_v1beta1_dot_task__api__pb2.MarkTaskStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )