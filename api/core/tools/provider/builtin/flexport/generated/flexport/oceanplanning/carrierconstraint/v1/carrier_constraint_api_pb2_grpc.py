# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.oceanplanning.carrierconstraint.v1 import (
    carrier_constraint_api_pb2 as flexport_dot_oceanplanning_dot_carrierconstraint_dot_v1_dot_carrier__constraint__api__pb2,
)


class CarrierConstraintAPIStub:
    """The carrier constraint service grpc API end point."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCarrierConstraintByRegion = channel.unary_unary(
            "/flexport.oceanplanning.carrierconstraint.v1.CarrierConstraintAPI/GetCarrierConstraintByRegion",
            request_serializer=flexport_dot_oceanplanning_dot_carrierconstraint_dot_v1_dot_carrier__constraint__api__pb2.GetCarrierConstraintByRegionRequest.SerializeToString,
            response_deserializer=flexport_dot_oceanplanning_dot_carrierconstraint_dot_v1_dot_carrier__constraint__api__pb2.GetCarrierConstraintByRegionResponse.FromString,
        )


class CarrierConstraintAPIServicer:
    """The carrier constraint service grpc API end point."""

    def GetCarrierConstraintByRegion(self, request, context):
        """Get the carrier constraint mapping by the given region name."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CarrierConstraintAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetCarrierConstraintByRegion": grpc.unary_unary_rpc_method_handler(
            servicer.GetCarrierConstraintByRegion,
            request_deserializer=flexport_dot_oceanplanning_dot_carrierconstraint_dot_v1_dot_carrier__constraint__api__pb2.GetCarrierConstraintByRegionRequest.FromString,
            response_serializer=flexport_dot_oceanplanning_dot_carrierconstraint_dot_v1_dot_carrier__constraint__api__pb2.GetCarrierConstraintByRegionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.oceanplanning.carrierconstraint.v1.CarrierConstraintAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class CarrierConstraintAPI:
    """The carrier constraint service grpc API end point."""

    @staticmethod
    def GetCarrierConstraintByRegion(
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
            "/flexport.oceanplanning.carrierconstraint.v1.CarrierConstraintAPI/GetCarrierConstraintByRegion",
            flexport_dot_oceanplanning_dot_carrierconstraint_dot_v1_dot_carrier__constraint__api__pb2.GetCarrierConstraintByRegionRequest.SerializeToString,
            flexport_dot_oceanplanning_dot_carrierconstraint_dot_v1_dot_carrier__constraint__api__pb2.GetCarrierConstraintByRegionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )