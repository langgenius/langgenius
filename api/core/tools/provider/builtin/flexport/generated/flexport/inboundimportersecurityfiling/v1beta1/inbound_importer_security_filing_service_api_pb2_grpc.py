# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.inboundimportersecurityfiling.v1beta1 import (
    inbound_importer_security_filing_service_api_pb2 as flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2,
)


class InboundImporterSecurityFilingServiceAPIStub:
    """The API for the Inbound Importer Security Filing Engine."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpsertInboundImporterSecurityFiling = channel.unary_unary(
            "/flexport.inboundimportersecurityfiling.v1beta1.InboundImporterSecurityFilingServiceAPI/UpsertInboundImporterSecurityFiling",
            request_serializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.UpsertInboundImporterSecurityFilingRequest.SerializeToString,
            response_deserializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.UpsertInboundImporterSecurityFilingResponse.FromString,
        )
        self.GetInboundImporterSecurityFilings = channel.unary_unary(
            "/flexport.inboundimportersecurityfiling.v1beta1.InboundImporterSecurityFilingServiceAPI/GetInboundImporterSecurityFilings",
            request_serializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundImporterSecurityFilingsRequest.SerializeToString,
            response_deserializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundImporterSecurityFilingsResponse.FromString,
        )
        self.AttachInboundIsfToEo = channel.unary_unary(
            "/flexport.inboundimportersecurityfiling.v1beta1.InboundImporterSecurityFilingServiceAPI/AttachInboundIsfToEo",
            request_serializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.AttachInboundIsfToEoRequest.SerializeToString,
            response_deserializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.AttachInboundIsfToEoResponse.FromString,
        )
        self.GetInboundIsfByStableId = channel.unary_unary(
            "/flexport.inboundimportersecurityfiling.v1beta1.InboundImporterSecurityFilingServiceAPI/GetInboundIsfByStableId",
            request_serializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundIsfByStableIdRequest.SerializeToString,
            response_deserializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundIsfByStableIdResponse.FromString,
        )


class InboundImporterSecurityFilingServiceAPIServicer:
    """The API for the Inbound Importer Security Filing Engine."""

    def UpsertInboundImporterSecurityFiling(self, request, context):
        """Upsert an inbound importer security filing."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetInboundImporterSecurityFilings(self, request, context):
        """Get all importer security filings given an execution order fid."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AttachInboundIsfToEo(self, request, context):
        """Attach an importer security filing to an execution order"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetInboundIsfByStableId(self, request, context):
        """Get an importer security filing given a stable id"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_InboundImporterSecurityFilingServiceAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "UpsertInboundImporterSecurityFiling": grpc.unary_unary_rpc_method_handler(
            servicer.UpsertInboundImporterSecurityFiling,
            request_deserializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.UpsertInboundImporterSecurityFilingRequest.FromString,
            response_serializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.UpsertInboundImporterSecurityFilingResponse.SerializeToString,
        ),
        "GetInboundImporterSecurityFilings": grpc.unary_unary_rpc_method_handler(
            servicer.GetInboundImporterSecurityFilings,
            request_deserializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundImporterSecurityFilingsRequest.FromString,
            response_serializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundImporterSecurityFilingsResponse.SerializeToString,
        ),
        "AttachInboundIsfToEo": grpc.unary_unary_rpc_method_handler(
            servicer.AttachInboundIsfToEo,
            request_deserializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.AttachInboundIsfToEoRequest.FromString,
            response_serializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.AttachInboundIsfToEoResponse.SerializeToString,
        ),
        "GetInboundIsfByStableId": grpc.unary_unary_rpc_method_handler(
            servicer.GetInboundIsfByStableId,
            request_deserializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundIsfByStableIdRequest.FromString,
            response_serializer=flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundIsfByStableIdResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.inboundimportersecurityfiling.v1beta1.InboundImporterSecurityFilingServiceAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class InboundImporterSecurityFilingServiceAPI:
    """The API for the Inbound Importer Security Filing Engine."""

    @staticmethod
    def UpsertInboundImporterSecurityFiling(
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
            "/flexport.inboundimportersecurityfiling.v1beta1.InboundImporterSecurityFilingServiceAPI/UpsertInboundImporterSecurityFiling",
            flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.UpsertInboundImporterSecurityFilingRequest.SerializeToString,
            flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.UpsertInboundImporterSecurityFilingResponse.FromString,
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
    def GetInboundImporterSecurityFilings(
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
            "/flexport.inboundimportersecurityfiling.v1beta1.InboundImporterSecurityFilingServiceAPI/GetInboundImporterSecurityFilings",
            flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundImporterSecurityFilingsRequest.SerializeToString,
            flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundImporterSecurityFilingsResponse.FromString,
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
    def AttachInboundIsfToEo(
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
            "/flexport.inboundimportersecurityfiling.v1beta1.InboundImporterSecurityFilingServiceAPI/AttachInboundIsfToEo",
            flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.AttachInboundIsfToEoRequest.SerializeToString,
            flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.AttachInboundIsfToEoResponse.FromString,
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
    def GetInboundIsfByStableId(
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
            "/flexport.inboundimportersecurityfiling.v1beta1.InboundImporterSecurityFilingServiceAPI/GetInboundIsfByStableId",
            flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundIsfByStableIdRequest.SerializeToString,
            flexport_dot_inboundimportersecurityfiling_dot_v1beta1_dot_inbound__importer__security__filing__service__api__pb2.GetInboundIsfByStableIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )