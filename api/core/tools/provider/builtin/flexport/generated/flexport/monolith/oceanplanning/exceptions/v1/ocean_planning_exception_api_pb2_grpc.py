# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.monolith.oceanplanning.exceptions.v1 import (
    ocean_planning_exception_api_pb2 as flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2,
)


class OceanPlanningExceptionAPIStub:
    """APIs for accessing and managing exceptions."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ResolveShipmentCancelledException = channel.unary_unary(
            "/flexport.monolith.oceanplanning.exceptions.v1.OceanPlanningExceptionAPI/ResolveShipmentCancelledException",
            request_serializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveShipmentCancelledExceptionRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveShipmentCancelledExceptionResponse.FromString,
        )
        self.FindActiveExceptionsForShipmentFidWithExceptionCategory = channel.unary_unary(
            "/flexport.monolith.oceanplanning.exceptions.v1.OceanPlanningExceptionAPI/FindActiveExceptionsForShipmentFidWithExceptionCategory",
            request_serializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindActiveExceptionsForShipmentFidWithExceptionCategoryRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindActiveExceptionsForShipmentFidWithExceptionCategoryResponse.FromString,
        )
        self.FindExceptionsForShipmentFidWithExceptionCategory = channel.unary_unary(
            "/flexport.monolith.oceanplanning.exceptions.v1.OceanPlanningExceptionAPI/FindExceptionsForShipmentFidWithExceptionCategory",
            request_serializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindExceptionsForShipmentFidWithExceptionCategoryRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindExceptionsForShipmentFidWithExceptionCategoryResponse.FromString,
        )
        self.ResolveException = channel.unary_unary(
            "/flexport.monolith.oceanplanning.exceptions.v1.OceanPlanningExceptionAPI/ResolveException",
            request_serializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveExceptionRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveExceptionResponse.FromString,
        )


class OceanPlanningExceptionAPIServicer:
    """APIs for accessing and managing exceptions."""

    def ResolveShipmentCancelledException(self, request, context):
        """Resolve shipment cancelled."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FindActiveExceptionsForShipmentFidWithExceptionCategory(self, request, context):
        """Find active exceptions."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FindExceptionsForShipmentFidWithExceptionCategory(self, request, context):
        """Find all filed exceptions."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ResolveException(self, request, context):
        """Resolve an exception."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_OceanPlanningExceptionAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ResolveShipmentCancelledException": grpc.unary_unary_rpc_method_handler(
            servicer.ResolveShipmentCancelledException,
            request_deserializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveShipmentCancelledExceptionRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveShipmentCancelledExceptionResponse.SerializeToString,
        ),
        "FindActiveExceptionsForShipmentFidWithExceptionCategory": grpc.unary_unary_rpc_method_handler(
            servicer.FindActiveExceptionsForShipmentFidWithExceptionCategory,
            request_deserializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindActiveExceptionsForShipmentFidWithExceptionCategoryRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindActiveExceptionsForShipmentFidWithExceptionCategoryResponse.SerializeToString,
        ),
        "FindExceptionsForShipmentFidWithExceptionCategory": grpc.unary_unary_rpc_method_handler(
            servicer.FindExceptionsForShipmentFidWithExceptionCategory,
            request_deserializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindExceptionsForShipmentFidWithExceptionCategoryRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindExceptionsForShipmentFidWithExceptionCategoryResponse.SerializeToString,
        ),
        "ResolveException": grpc.unary_unary_rpc_method_handler(
            servicer.ResolveException,
            request_deserializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveExceptionRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveExceptionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.monolith.oceanplanning.exceptions.v1.OceanPlanningExceptionAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class OceanPlanningExceptionAPI:
    """APIs for accessing and managing exceptions."""

    @staticmethod
    def ResolveShipmentCancelledException(
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
            "/flexport.monolith.oceanplanning.exceptions.v1.OceanPlanningExceptionAPI/ResolveShipmentCancelledException",
            flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveShipmentCancelledExceptionRequest.SerializeToString,
            flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveShipmentCancelledExceptionResponse.FromString,
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
    def FindActiveExceptionsForShipmentFidWithExceptionCategory(
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
            "/flexport.monolith.oceanplanning.exceptions.v1.OceanPlanningExceptionAPI/FindActiveExceptionsForShipmentFidWithExceptionCategory",
            flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindActiveExceptionsForShipmentFidWithExceptionCategoryRequest.SerializeToString,
            flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindActiveExceptionsForShipmentFidWithExceptionCategoryResponse.FromString,
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
    def FindExceptionsForShipmentFidWithExceptionCategory(
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
            "/flexport.monolith.oceanplanning.exceptions.v1.OceanPlanningExceptionAPI/FindExceptionsForShipmentFidWithExceptionCategory",
            flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindExceptionsForShipmentFidWithExceptionCategoryRequest.SerializeToString,
            flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.FindExceptionsForShipmentFidWithExceptionCategoryResponse.FromString,
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
    def ResolveException(
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
            "/flexport.monolith.oceanplanning.exceptions.v1.OceanPlanningExceptionAPI/ResolveException",
            flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveExceptionRequest.SerializeToString,
            flexport_dot_monolith_dot_oceanplanning_dot_exceptions_dot_v1_dot_ocean__planning__exception__api__pb2.ResolveExceptionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )