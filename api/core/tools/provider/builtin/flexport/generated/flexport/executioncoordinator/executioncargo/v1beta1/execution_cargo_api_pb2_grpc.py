# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.executioncoordinator.executioncargo.v1beta1 import (
    execution_cargo_api_pb2 as flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2,
)


class ExecutionCargoAPIStub:
    """An API for interacting with ExecutionCargo entities."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateExecutionCargo = channel.unary_unary(
            "/flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI/CreateExecutionCargo",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.CreateExecutionCargoRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.CreateExecutionCargoResponse.FromString,
        )
        self.GetExecutionCargo = channel.unary_unary(
            "/flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI/GetExecutionCargo",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.GetExecutionCargoRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.GetExecutionCargoResponse.FromString,
        )
        self.ListExecutionCargoRevisions = channel.unary_unary(
            "/flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI/ListExecutionCargoRevisions",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoRevisionsRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoRevisionsResponse.FromString,
        )
        self.ListExecutionCargo = channel.unary_unary(
            "/flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI/ListExecutionCargo",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoResponse.FromString,
        )
        self.UpdateExecutionCargo = channel.unary_unary(
            "/flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI/UpdateExecutionCargo",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.UpdateExecutionCargoRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.UpdateExecutionCargoResponse.FromString,
        )


class ExecutionCargoAPIServicer:
    """An API for interacting with ExecutionCargo entities."""

    def CreateExecutionCargo(self, request, context):
        """Creates an ExecutionCargo entity."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetExecutionCargo(self, request, context):
        """Retrieves an ExecutionCargo entity."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListExecutionCargoRevisions(self, request, context):
        """Retrieves all revisions of an ExecutionCargo, sorted in chronological order (earliest revision first)."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListExecutionCargo(self, request, context):
        """Retrieves a List of ExecutionCargo entity."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateExecutionCargo(self, request, context):
        """Updates an ExecutionCargo entity. If there are no changes, the current revision is returned."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ExecutionCargoAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateExecutionCargo": grpc.unary_unary_rpc_method_handler(
            servicer.CreateExecutionCargo,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.CreateExecutionCargoRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.CreateExecutionCargoResponse.SerializeToString,
        ),
        "GetExecutionCargo": grpc.unary_unary_rpc_method_handler(
            servicer.GetExecutionCargo,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.GetExecutionCargoRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.GetExecutionCargoResponse.SerializeToString,
        ),
        "ListExecutionCargoRevisions": grpc.unary_unary_rpc_method_handler(
            servicer.ListExecutionCargoRevisions,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoRevisionsRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoRevisionsResponse.SerializeToString,
        ),
        "ListExecutionCargo": grpc.unary_unary_rpc_method_handler(
            servicer.ListExecutionCargo,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoResponse.SerializeToString,
        ),
        "UpdateExecutionCargo": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateExecutionCargo,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.UpdateExecutionCargoRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.UpdateExecutionCargoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ExecutionCargoAPI:
    """An API for interacting with ExecutionCargo entities."""

    @staticmethod
    def CreateExecutionCargo(
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
            "/flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI/CreateExecutionCargo",
            flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.CreateExecutionCargoRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.CreateExecutionCargoResponse.FromString,
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
    def GetExecutionCargo(
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
            "/flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI/GetExecutionCargo",
            flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.GetExecutionCargoRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.GetExecutionCargoResponse.FromString,
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
    def ListExecutionCargoRevisions(
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
            "/flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI/ListExecutionCargoRevisions",
            flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoRevisionsRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoRevisionsResponse.FromString,
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
    def ListExecutionCargo(
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
            "/flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI/ListExecutionCargo",
            flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.ListExecutionCargoResponse.FromString,
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
    def UpdateExecutionCargo(
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
            "/flexport.executioncoordinator.executioncargo.v1beta1.ExecutionCargoAPI/UpdateExecutionCargo",
            flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.UpdateExecutionCargoRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncargo_dot_v1beta1_dot_execution__cargo__api__pb2.UpdateExecutionCargoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )