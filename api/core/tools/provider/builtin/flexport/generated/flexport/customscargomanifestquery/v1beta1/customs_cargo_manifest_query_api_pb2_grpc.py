# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.customscargomanifestquery.v1beta1 import (
    customs_cargo_manifest_query_api_pb2 as flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2,
)


class CustomsCargoManifestQueryAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterMasterBillNumbers = channel.unary_unary(
            "/flexport.customscargomanifestquery.v1beta1.CustomsCargoManifestQueryAPI/RegisterMasterBillNumbers",
            request_serializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RegisterMasterBillNumbersRequest.SerializeToString,
            response_deserializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RegisterMasterBillNumbersResponse.FromString,
        )
        self.GetCargoManifest = channel.unary_unary(
            "/flexport.customscargomanifestquery.v1beta1.CustomsCargoManifestQueryAPI/GetCargoManifest",
            request_serializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.GetCargoManifestRequest.SerializeToString,
            response_deserializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.GetCargoManifestResponse.FromString,
        )
        self.RefreshAndGetCargoManifest = channel.unary_unary(
            "/flexport.customscargomanifestquery.v1beta1.CustomsCargoManifestQueryAPI/RefreshAndGetCargoManifest",
            request_serializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RefreshAndGetCargoManifestRequest.SerializeToString,
            response_deserializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RefreshAndGetCargoManifestResponse.FromString,
        )


class CustomsCargoManifestQueryAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def RegisterMasterBillNumbers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetCargoManifest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RefreshAndGetCargoManifest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CustomsCargoManifestQueryAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "RegisterMasterBillNumbers": grpc.unary_unary_rpc_method_handler(
            servicer.RegisterMasterBillNumbers,
            request_deserializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RegisterMasterBillNumbersRequest.FromString,
            response_serializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RegisterMasterBillNumbersResponse.SerializeToString,
        ),
        "GetCargoManifest": grpc.unary_unary_rpc_method_handler(
            servicer.GetCargoManifest,
            request_deserializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.GetCargoManifestRequest.FromString,
            response_serializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.GetCargoManifestResponse.SerializeToString,
        ),
        "RefreshAndGetCargoManifest": grpc.unary_unary_rpc_method_handler(
            servicer.RefreshAndGetCargoManifest,
            request_deserializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RefreshAndGetCargoManifestRequest.FromString,
            response_serializer=flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RefreshAndGetCargoManifestResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.customscargomanifestquery.v1beta1.CustomsCargoManifestQueryAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class CustomsCargoManifestQueryAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterMasterBillNumbers(
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
            "/flexport.customscargomanifestquery.v1beta1.CustomsCargoManifestQueryAPI/RegisterMasterBillNumbers",
            flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RegisterMasterBillNumbersRequest.SerializeToString,
            flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RegisterMasterBillNumbersResponse.FromString,
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
    def GetCargoManifest(
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
            "/flexport.customscargomanifestquery.v1beta1.CustomsCargoManifestQueryAPI/GetCargoManifest",
            flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.GetCargoManifestRequest.SerializeToString,
            flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.GetCargoManifestResponse.FromString,
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
    def RefreshAndGetCargoManifest(
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
            "/flexport.customscargomanifestquery.v1beta1.CustomsCargoManifestQueryAPI/RefreshAndGetCargoManifest",
            flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RefreshAndGetCargoManifestRequest.SerializeToString,
            flexport_dot_customscargomanifestquery_dot_v1beta1_dot_customs__cargo__manifest__query__api__pb2.RefreshAndGetCargoManifestResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )