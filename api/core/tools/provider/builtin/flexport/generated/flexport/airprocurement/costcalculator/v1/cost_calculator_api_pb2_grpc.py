# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.airprocurement.costcalculator.v1 import (
    cost_calculator_api_pb2 as flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2,
)


class CostCalculatorAPIStub:
    """Cost Calculator API compatible with Procurement Rates."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CalculateCost = channel.unary_unary(
            "/flexport.airprocurement.costcalculator.v1.CostCalculatorAPI/CalculateCost",
            request_serializer=flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.CalculateCostRequest.SerializeToString,
            response_deserializer=flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.CalculateCostResponse.FromString,
        )
        self.FindCost = channel.unary_unary(
            "/flexport.airprocurement.costcalculator.v1.CostCalculatorAPI/FindCost",
            request_serializer=flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.FindCostRequest.SerializeToString,
            response_deserializer=flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.FindCostResponse.FromString,
        )


class CostCalculatorAPIServicer:
    """Cost Calculator API compatible with Procurement Rates."""

    def CalculateCost(self, request, context):
        """Calculates the cost for a given Procurement Rate and set of PricingVariables."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FindCost(self, request, context):
        """Find cost for a batch of shipments given a set of rate search criteria and cargo information"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CostCalculatorAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CalculateCost": grpc.unary_unary_rpc_method_handler(
            servicer.CalculateCost,
            request_deserializer=flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.CalculateCostRequest.FromString,
            response_serializer=flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.CalculateCostResponse.SerializeToString,
        ),
        "FindCost": grpc.unary_unary_rpc_method_handler(
            servicer.FindCost,
            request_deserializer=flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.FindCostRequest.FromString,
            response_serializer=flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.FindCostResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.airprocurement.costcalculator.v1.CostCalculatorAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class CostCalculatorAPI:
    """Cost Calculator API compatible with Procurement Rates."""

    @staticmethod
    def CalculateCost(
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
            "/flexport.airprocurement.costcalculator.v1.CostCalculatorAPI/CalculateCost",
            flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.CalculateCostRequest.SerializeToString,
            flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.CalculateCostResponse.FromString,
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
    def FindCost(
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
            "/flexport.airprocurement.costcalculator.v1.CostCalculatorAPI/FindCost",
            flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.FindCostRequest.SerializeToString,
            flexport_dot_airprocurement_dot_costcalculator_dot_v1_dot_cost__calculator__api__pb2.FindCostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )