# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.carriershippingdoc.kinesiseventpublisher.v1beta1 import (
    kinesis_event_publisher_api_pb2 as flexport_dot_carriershippingdoc_dot_kinesiseventpublisher_dot_v1beta1_dot_kinesis__event__publisher__api__pb2,
)


class KinesisEventPublisherAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PublishOceanFreightReleaseReceivedEtse = channel.unary_unary(
            "/flexport.carriershippingdoc.kinesiseventpublisher.v1beta1.KinesisEventPublisherAPI/PublishOceanFreightReleaseReceivedEtse",
            request_serializer=flexport_dot_carriershippingdoc_dot_kinesiseventpublisher_dot_v1beta1_dot_kinesis__event__publisher__api__pb2.PublishOceanFreightReleaseReceivedEtseRequest.SerializeToString,
            response_deserializer=flexport_dot_carriershippingdoc_dot_kinesiseventpublisher_dot_v1beta1_dot_kinesis__event__publisher__api__pb2.PublishOceanFreightReleaseReceivedEtseResponse.FromString,
        )


class KinesisEventPublisherAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def PublishOceanFreightReleaseReceivedEtse(self, request, context):
        """This gRPC API should only be used by PublishEtseLambda in carrier_shipping_doc_automation. DO NOT use it anywhere else."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_KinesisEventPublisherAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "PublishOceanFreightReleaseReceivedEtse": grpc.unary_unary_rpc_method_handler(
            servicer.PublishOceanFreightReleaseReceivedEtse,
            request_deserializer=flexport_dot_carriershippingdoc_dot_kinesiseventpublisher_dot_v1beta1_dot_kinesis__event__publisher__api__pb2.PublishOceanFreightReleaseReceivedEtseRequest.FromString,
            response_serializer=flexport_dot_carriershippingdoc_dot_kinesiseventpublisher_dot_v1beta1_dot_kinesis__event__publisher__api__pb2.PublishOceanFreightReleaseReceivedEtseResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.carriershippingdoc.kinesiseventpublisher.v1beta1.KinesisEventPublisherAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class KinesisEventPublisherAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PublishOceanFreightReleaseReceivedEtse(
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
            "/flexport.carriershippingdoc.kinesiseventpublisher.v1beta1.KinesisEventPublisherAPI/PublishOceanFreightReleaseReceivedEtse",
            flexport_dot_carriershippingdoc_dot_kinesiseventpublisher_dot_v1beta1_dot_kinesis__event__publisher__api__pb2.PublishOceanFreightReleaseReceivedEtseRequest.SerializeToString,
            flexport_dot_carriershippingdoc_dot_kinesiseventpublisher_dot_v1beta1_dot_kinesis__event__publisher__api__pb2.PublishOceanFreightReleaseReceivedEtseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )