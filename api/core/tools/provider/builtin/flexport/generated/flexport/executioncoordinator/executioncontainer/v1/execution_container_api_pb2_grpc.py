# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.executioncoordinator.executioncontainer.v1 import (
    execution_container_api_pb2 as flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2,
)


class ExecutionContainerAPIStub:
    """An API for interacting with ExecutionContainer entities."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetShipmentContainer = channel.unary_unary(
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/GetShipmentContainer",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetShipmentContainerRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetShipmentContainerResponse.FromString,
        )
        self.ListShipmentContainers = channel.unary_unary(
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/ListShipmentContainers",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.ListShipmentContainersRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.ListShipmentContainersResponse.FromString,
        )
        self.GetContainerEvents = channel.unary_unary(
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/GetContainerEvents",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetContainerEventsRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetContainerEventsResponse.FromString,
        )
        self.UpdateShipmentContainers = channel.unary_unary(
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/UpdateShipmentContainers",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpdateShipmentContainersRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpdateShipmentContainersResponse.FromString,
        )
        self.BatchUpdateContainerAttributes = channel.unary_unary(
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/BatchUpdateContainerAttributes",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.BatchUpdateContainerAttributesRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.BatchUpdateContainerAttributesResponse.FromString,
        )
        self.UpsertContainerActivityPosts = channel.unary_unary(
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/UpsertContainerActivityPosts",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpsertContainerActivityPostsRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpsertContainerActivityPostsResponse.FromString,
        )
        self.AttachContainerToShipment = channel.unary_unary(
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/AttachContainerToShipment",
            request_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.AttachContainerToShipmentRequest.SerializeToString,
            response_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.AttachContainerToShipmentResponse.FromString,
        )


class ExecutionContainerAPIServicer:
    """An API for interacting with ExecutionContainer entities."""

    def GetShipmentContainer(self, request, context):
        """READS
        Gets an execution container.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListShipmentContainers(self, request, context):
        """Gets all a execution containers for a shipment_fid."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetContainerEvents(self, request, context):
        """Gets container events for a shipment_fid, container_number and execution_container_event_type"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateShipmentContainers(self, request, context):
        """WRITES
        Updates a given order's shipment containers to match those given in the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchUpdateContainerAttributes(self, request, context):
        """Batch updates container attributes"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpsertContainerActivityPosts(self, request, context):
        """Upsert activity posts for a given container"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AttachContainerToShipment(self, request, context):
        """Attach a container to a shipment"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ExecutionContainerAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetShipmentContainer": grpc.unary_unary_rpc_method_handler(
            servicer.GetShipmentContainer,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetShipmentContainerRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetShipmentContainerResponse.SerializeToString,
        ),
        "ListShipmentContainers": grpc.unary_unary_rpc_method_handler(
            servicer.ListShipmentContainers,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.ListShipmentContainersRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.ListShipmentContainersResponse.SerializeToString,
        ),
        "GetContainerEvents": grpc.unary_unary_rpc_method_handler(
            servicer.GetContainerEvents,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetContainerEventsRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetContainerEventsResponse.SerializeToString,
        ),
        "UpdateShipmentContainers": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateShipmentContainers,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpdateShipmentContainersRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpdateShipmentContainersResponse.SerializeToString,
        ),
        "BatchUpdateContainerAttributes": grpc.unary_unary_rpc_method_handler(
            servicer.BatchUpdateContainerAttributes,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.BatchUpdateContainerAttributesRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.BatchUpdateContainerAttributesResponse.SerializeToString,
        ),
        "UpsertContainerActivityPosts": grpc.unary_unary_rpc_method_handler(
            servicer.UpsertContainerActivityPosts,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpsertContainerActivityPostsRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpsertContainerActivityPostsResponse.SerializeToString,
        ),
        "AttachContainerToShipment": grpc.unary_unary_rpc_method_handler(
            servicer.AttachContainerToShipment,
            request_deserializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.AttachContainerToShipmentRequest.FromString,
            response_serializer=flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.AttachContainerToShipmentResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ExecutionContainerAPI:
    """An API for interacting with ExecutionContainer entities."""

    @staticmethod
    def GetShipmentContainer(
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
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/GetShipmentContainer",
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetShipmentContainerRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetShipmentContainerResponse.FromString,
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
    def ListShipmentContainers(
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
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/ListShipmentContainers",
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.ListShipmentContainersRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.ListShipmentContainersResponse.FromString,
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
    def GetContainerEvents(
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
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/GetContainerEvents",
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetContainerEventsRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.GetContainerEventsResponse.FromString,
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
    def UpdateShipmentContainers(
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
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/UpdateShipmentContainers",
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpdateShipmentContainersRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpdateShipmentContainersResponse.FromString,
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
    def BatchUpdateContainerAttributes(
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
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/BatchUpdateContainerAttributes",
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.BatchUpdateContainerAttributesRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.BatchUpdateContainerAttributesResponse.FromString,
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
    def UpsertContainerActivityPosts(
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
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/UpsertContainerActivityPosts",
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpsertContainerActivityPostsRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.UpsertContainerActivityPostsResponse.FromString,
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
    def AttachContainerToShipment(
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
            "/flexport.executioncoordinator.executioncontainer.v1.ExecutionContainerAPI/AttachContainerToShipment",
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.AttachContainerToShipmentRequest.SerializeToString,
            flexport_dot_executioncoordinator_dot_executioncontainer_dot_v1_dot_execution__container__api__pb2.AttachContainerToShipmentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )