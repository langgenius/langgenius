# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.pricingrequests.hello.v1beta1 import (
    hello_api_pb2 as flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2,
)


class HelloAPIStub:
    """TODO: All services require a comment that contains at least one complete sentence."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Hello = channel.unary_unary(
            "/flexport.pricingrequests.hello.v1beta1.HelloAPI/Hello",
            request_serializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloRequest.SerializeToString,
            response_deserializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloResponse.FromString,
        )
        self.HelloCore = channel.unary_unary(
            "/flexport.pricingrequests.hello.v1beta1.HelloAPI/HelloCore",
            request_serializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloCoreRequest.SerializeToString,
            response_deserializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloCoreResponse.FromString,
        )
        self.BigYikes = channel.unary_unary(
            "/flexport.pricingrequests.hello.v1beta1.HelloAPI/BigYikes",
            request_serializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.BigYikesRequest.SerializeToString,
            response_deserializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.BigYikesResponse.FromString,
        )


class HelloAPIServicer:
    """TODO: All services require a comment that contains at least one complete sentence."""

    def Hello(self, request, context):
        """Here we'll make sure everything is nice and hooked up. We'll also add some logging statements, and some DataDog incrementing so we can validate all that is working"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def HelloCore(self, request, context):
        """Here we'll test the call out to the monolith gRPC service from this service."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BigYikes(self, request, context):
        """We'll always raise an exception inside here, we want to make sure Sentries are being raised and routed to the correct places. Also test error logging"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_HelloAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Hello": grpc.unary_unary_rpc_method_handler(
            servicer.Hello,
            request_deserializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloRequest.FromString,
            response_serializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloResponse.SerializeToString,
        ),
        "HelloCore": grpc.unary_unary_rpc_method_handler(
            servicer.HelloCore,
            request_deserializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloCoreRequest.FromString,
            response_serializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloCoreResponse.SerializeToString,
        ),
        "BigYikes": grpc.unary_unary_rpc_method_handler(
            servicer.BigYikes,
            request_deserializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.BigYikesRequest.FromString,
            response_serializer=flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.BigYikesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.pricingrequests.hello.v1beta1.HelloAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class HelloAPI:
    """TODO: All services require a comment that contains at least one complete sentence."""

    @staticmethod
    def Hello(
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
            "/flexport.pricingrequests.hello.v1beta1.HelloAPI/Hello",
            flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloRequest.SerializeToString,
            flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloResponse.FromString,
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
    def HelloCore(
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
            "/flexport.pricingrequests.hello.v1beta1.HelloAPI/HelloCore",
            flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloCoreRequest.SerializeToString,
            flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.HelloCoreResponse.FromString,
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
    def BigYikes(
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
            "/flexport.pricingrequests.hello.v1beta1.HelloAPI/BigYikes",
            flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.BigYikesRequest.SerializeToString,
            flexport_dot_pricingrequests_dot_hello_dot_v1beta1_dot_hello__api__pb2.BigYikesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )