# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.monolith.oceanconsol.lcltransittimes.v1beta1 import (
    lcl_transit_times_api_pb2 as flexport_dot_monolith_dot_oceanconsol_dot_lcltransittimes_dot_v1beta1_dot_lcl__transit__times__api__pb2,
)


class LclTransitTimesAPIStub:
    """This is the API for ocean consolidation services to retrieve ocean LCL transit times."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListLclTransitTimes = channel.unary_unary(
            "/flexport.monolith.oceanconsol.lcltransittimes.v1beta1.LclTransitTimesAPI/ListLclTransitTimes",
            request_serializer=flexport_dot_monolith_dot_oceanconsol_dot_lcltransittimes_dot_v1beta1_dot_lcl__transit__times__api__pb2.ListLclTransitTimesRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_oceanconsol_dot_lcltransittimes_dot_v1beta1_dot_lcl__transit__times__api__pb2.ListLclTransitTimesResponse.FromString,
        )


class LclTransitTimesAPIServicer:
    """This is the API for ocean consolidation services to retrieve ocean LCL transit times."""

    def ListLclTransitTimes(self, request, context):
        """List LCL transit times."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_LclTransitTimesAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListLclTransitTimes": grpc.unary_unary_rpc_method_handler(
            servicer.ListLclTransitTimes,
            request_deserializer=flexport_dot_monolith_dot_oceanconsol_dot_lcltransittimes_dot_v1beta1_dot_lcl__transit__times__api__pb2.ListLclTransitTimesRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_oceanconsol_dot_lcltransittimes_dot_v1beta1_dot_lcl__transit__times__api__pb2.ListLclTransitTimesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.monolith.oceanconsol.lcltransittimes.v1beta1.LclTransitTimesAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class LclTransitTimesAPI:
    """This is the API for ocean consolidation services to retrieve ocean LCL transit times."""

    @staticmethod
    def ListLclTransitTimes(
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
            "/flexport.monolith.oceanconsol.lcltransittimes.v1beta1.LclTransitTimesAPI/ListLclTransitTimes",
            flexport_dot_monolith_dot_oceanconsol_dot_lcltransittimes_dot_v1beta1_dot_lcl__transit__times__api__pb2.ListLclTransitTimesRequest.SerializeToString,
            flexport_dot_monolith_dot_oceanconsol_dot_lcltransittimes_dot_v1beta1_dot_lcl__transit__times__api__pb2.ListLclTransitTimesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )