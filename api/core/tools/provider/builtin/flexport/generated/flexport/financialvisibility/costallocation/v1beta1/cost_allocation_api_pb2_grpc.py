# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.financialvisibility.costallocation.v1beta1 import (
    cost_allocation_api_pb2 as flexport_dot_financialvisibility_dot_costallocation_dot_v1beta1_dot_cost__allocation__api__pb2,
)


class CostAllocationAPIStub:
    """The CostAllocation definition."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
            "/flexport.financialledger.costallocation.v1beta1.CostAllocationAPI/Register",
            request_serializer=flexport_dot_financialvisibility_dot_costallocation_dot_v1beta1_dot_cost__allocation__api__pb2.RegisterRequest.SerializeToString,
            response_deserializer=flexport_dot_financialvisibility_dot_costallocation_dot_v1beta1_dot_cost__allocation__api__pb2.RegisterResponse.FromString,
        )


class CostAllocationAPIServicer:
    """The CostAllocation definition."""

    def Register(self, request, context):
        """Register CostAllocation with FinancialLedger."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CostAllocationAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Register": grpc.unary_unary_rpc_method_handler(
            servicer.Register,
            request_deserializer=flexport_dot_financialvisibility_dot_costallocation_dot_v1beta1_dot_cost__allocation__api__pb2.RegisterRequest.FromString,
            response_serializer=flexport_dot_financialvisibility_dot_costallocation_dot_v1beta1_dot_cost__allocation__api__pb2.RegisterResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.financialledger.costallocation.v1beta1.CostAllocationAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class CostAllocationAPI:
    """The CostAllocation definition."""

    @staticmethod
    def Register(
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
            "/flexport.financialledger.costallocation.v1beta1.CostAllocationAPI/Register",
            flexport_dot_financialvisibility_dot_costallocation_dot_v1beta1_dot_cost__allocation__api__pb2.RegisterRequest.SerializeToString,
            flexport_dot_financialvisibility_dot_costallocation_dot_v1beta1_dot_cost__allocation__api__pb2.RegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )