# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.airprocurement.surchargesprovider.v1beta1 import (
    surcharges_provider_api_pb2 as flexport_dot_airprocurement_dot_surchargesprovider_dot_v1beta1_dot_surcharges__provider__api__pb2,
)


class SurchargesProviderAPIStub:
    """This service is used to retrieve surcharges."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindODCharges = channel.unary_unary(
            "/flexport.airprocurement.surchargesprovider.v1beta1.SurchargesProviderAPI/FindODCharges",
            request_serializer=flexport_dot_airprocurement_dot_surchargesprovider_dot_v1beta1_dot_surcharges__provider__api__pb2.FindODChargesRequest.SerializeToString,
            response_deserializer=flexport_dot_airprocurement_dot_surchargesprovider_dot_v1beta1_dot_surcharges__provider__api__pb2.FindODChargesResponse.FromString,
        )


class SurchargesProviderAPIServicer:
    """This service is used to retrieve surcharges."""

    def FindODCharges(self, request, context):
        """Find origin and destination charges matching a given request."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SurchargesProviderAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "FindODCharges": grpc.unary_unary_rpc_method_handler(
            servicer.FindODCharges,
            request_deserializer=flexport_dot_airprocurement_dot_surchargesprovider_dot_v1beta1_dot_surcharges__provider__api__pb2.FindODChargesRequest.FromString,
            response_serializer=flexport_dot_airprocurement_dot_surchargesprovider_dot_v1beta1_dot_surcharges__provider__api__pb2.FindODChargesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.airprocurement.surchargesprovider.v1beta1.SurchargesProviderAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class SurchargesProviderAPI:
    """This service is used to retrieve surcharges."""

    @staticmethod
    def FindODCharges(
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
            "/flexport.airprocurement.surchargesprovider.v1beta1.SurchargesProviderAPI/FindODCharges",
            flexport_dot_airprocurement_dot_surchargesprovider_dot_v1beta1_dot_surcharges__provider__api__pb2.FindODChargesRequest.SerializeToString,
            flexport_dot_airprocurement_dot_surchargesprovider_dot_v1beta1_dot_surcharges__provider__api__pb2.FindODChargesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )