# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.airsupply.allotmentscheduleinstance.v1beta1 import (
    allotment_schedule_instance_api_pb2 as flexport_dot_airsupply_dot_allotmentscheduleinstance_dot_v1beta1_dot_allotment__schedule__instance__api__pb2,
)


class AllotmentScheduleInstanceAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAllotmentScheduleInstances = channel.unary_unary(
            "/flexport.airsupply.allotmentscheduleinstance.v1beta1.AllotmentScheduleInstanceAPI/ListAllotmentScheduleInstances",
            request_serializer=flexport_dot_airsupply_dot_allotmentscheduleinstance_dot_v1beta1_dot_allotment__schedule__instance__api__pb2.ListAllotmentScheduleInstancesRequest.SerializeToString,
            response_deserializer=flexport_dot_airsupply_dot_allotmentscheduleinstance_dot_v1beta1_dot_allotment__schedule__instance__api__pb2.ListAllotmentScheduleInstancesResponse.FromString,
        )


class AllotmentScheduleInstanceAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def ListAllotmentScheduleInstances(self, request, context):
        """Returns allotment schedule instances for given condition"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AllotmentScheduleInstanceAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListAllotmentScheduleInstances": grpc.unary_unary_rpc_method_handler(
            servicer.ListAllotmentScheduleInstances,
            request_deserializer=flexport_dot_airsupply_dot_allotmentscheduleinstance_dot_v1beta1_dot_allotment__schedule__instance__api__pb2.ListAllotmentScheduleInstancesRequest.FromString,
            response_serializer=flexport_dot_airsupply_dot_allotmentscheduleinstance_dot_v1beta1_dot_allotment__schedule__instance__api__pb2.ListAllotmentScheduleInstancesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.airsupply.allotmentscheduleinstance.v1beta1.AllotmentScheduleInstanceAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class AllotmentScheduleInstanceAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListAllotmentScheduleInstances(
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
            "/flexport.airsupply.allotmentscheduleinstance.v1beta1.AllotmentScheduleInstanceAPI/ListAllotmentScheduleInstances",
            flexport_dot_airsupply_dot_allotmentscheduleinstance_dot_v1beta1_dot_allotment__schedule__instance__api__pb2.ListAllotmentScheduleInstancesRequest.SerializeToString,
            flexport_dot_airsupply_dot_allotmentscheduleinstance_dot_v1beta1_dot_allotment__schedule__instance__api__pb2.ListAllotmentScheduleInstancesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )