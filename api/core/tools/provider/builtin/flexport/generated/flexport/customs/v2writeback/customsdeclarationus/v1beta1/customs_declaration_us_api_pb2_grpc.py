# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.customs.v2writeback.customsdeclarationus.v1beta1 import (
    customs_declaration_us_api_pb2 as flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2,
)


class CustomsV2CustomsDeclarationUsWritebackAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WritebackCustomsEntries = channel.unary_unary(
            "/flexport.customs.v2writeback.customsdeclarationus.v1beta1.CustomsV2CustomsDeclarationUsWritebackAPI/WritebackCustomsEntries",
            request_serializer=flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.WritebackCustomsEntriesRequest.SerializeToString,
            response_deserializer=flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.WritebackCustomsEntriesResponse.FromString,
        )
        self.UnenrollCustomsEntries = channel.unary_unary(
            "/flexport.customs.v2writeback.customsdeclarationus.v1beta1.CustomsV2CustomsDeclarationUsWritebackAPI/UnenrollCustomsEntries",
            request_serializer=flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.UnenrollCustomsEntriesRequest.SerializeToString,
            response_deserializer=flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.UnenrollCustomsEntriesResponse.FromString,
        )


class CustomsV2CustomsDeclarationUsWritebackAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def WritebackCustomsEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UnenrollCustomsEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CustomsV2CustomsDeclarationUsWritebackAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "WritebackCustomsEntries": grpc.unary_unary_rpc_method_handler(
            servicer.WritebackCustomsEntries,
            request_deserializer=flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.WritebackCustomsEntriesRequest.FromString,
            response_serializer=flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.WritebackCustomsEntriesResponse.SerializeToString,
        ),
        "UnenrollCustomsEntries": grpc.unary_unary_rpc_method_handler(
            servicer.UnenrollCustomsEntries,
            request_deserializer=flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.UnenrollCustomsEntriesRequest.FromString,
            response_serializer=flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.UnenrollCustomsEntriesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.customs.v2writeback.customsdeclarationus.v1beta1.CustomsV2CustomsDeclarationUsWritebackAPI",
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class CustomsV2CustomsDeclarationUsWritebackAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WritebackCustomsEntries(
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
            "/flexport.customs.v2writeback.customsdeclarationus.v1beta1.CustomsV2CustomsDeclarationUsWritebackAPI/WritebackCustomsEntries",
            flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.WritebackCustomsEntriesRequest.SerializeToString,
            flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.WritebackCustomsEntriesResponse.FromString,
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
    def UnenrollCustomsEntries(
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
            "/flexport.customs.v2writeback.customsdeclarationus.v1beta1.CustomsV2CustomsDeclarationUsWritebackAPI/UnenrollCustomsEntries",
            flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.UnenrollCustomsEntriesRequest.SerializeToString,
            flexport_dot_customs_dot_v2writeback_dot_customsdeclarationus_dot_v1beta1_dot_customs__declaration__us__api__pb2.UnenrollCustomsEntriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )