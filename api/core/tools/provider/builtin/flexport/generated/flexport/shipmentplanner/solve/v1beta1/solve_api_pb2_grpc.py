# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.shipmentplanner.solve.v1beta1 import (
    solve_api_pb2 as flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2,
)


class SolveAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLCLShipmentRouteOptions = channel.unary_unary(
            "/flexport.shipmentplanner.solve.v1beta1.SolveAPI/GetLCLShipmentRouteOptions",
            request_serializer=flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.GetLCLShipmentRouteOptionsRequest.SerializeToString,
            response_deserializer=flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.GetLCLShipmentRouteOptionsResponse.FromString,
        )
        self.PublishLCLShipmentRouteSolution = channel.unary_unary(
            "/flexport.shipmentplanner.solve.v1beta1.SolveAPI/PublishLCLShipmentRouteSolution",
            request_serializer=flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.PublishLCLShipmentRouteSolutionRequest.SerializeToString,
            response_deserializer=flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.PublishLCLShipmentRouteSolutionResponse.FromString,
        )


class SolveAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def GetLCLShipmentRouteOptions(self, request, context):
        """
        Gets the full list of all plan constraints at the time of calling including both shipment constraints and affinity
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PublishLCLShipmentRouteSolution(self, request, context):
        """
        Publish a solution
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SolveAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetLCLShipmentRouteOptions": grpc.unary_unary_rpc_method_handler(
            servicer.GetLCLShipmentRouteOptions,
            request_deserializer=flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.GetLCLShipmentRouteOptionsRequest.FromString,
            response_serializer=flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.GetLCLShipmentRouteOptionsResponse.SerializeToString,
        ),
        "PublishLCLShipmentRouteSolution": grpc.unary_unary_rpc_method_handler(
            servicer.PublishLCLShipmentRouteSolution,
            request_deserializer=flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.PublishLCLShipmentRouteSolutionRequest.FromString,
            response_serializer=flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.PublishLCLShipmentRouteSolutionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.shipmentplanner.solve.v1beta1.SolveAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class SolveAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLCLShipmentRouteOptions(
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
            "/flexport.shipmentplanner.solve.v1beta1.SolveAPI/GetLCLShipmentRouteOptions",
            flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.GetLCLShipmentRouteOptionsRequest.SerializeToString,
            flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.GetLCLShipmentRouteOptionsResponse.FromString,
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
    def PublishLCLShipmentRouteSolution(
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
            "/flexport.shipmentplanner.solve.v1beta1.SolveAPI/PublishLCLShipmentRouteSolution",
            flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.PublishLCLShipmentRouteSolutionRequest.SerializeToString,
            flexport_dot_shipmentplanner_dot_solve_dot_v1beta1_dot_solve__api__pb2.PublishLCLShipmentRouteSolutionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )