# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.transcription.transcriptionservice.v1beta1 import (
    transcription_service_api_pb2 as flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2,
)


class TranscriptionServiceAPIStub:
    """This is the API for the Transcription Service."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Transcribe = channel.unary_unary(
            "/flexport.transcription.transcriptionservice.v1beta1.TranscriptionServiceAPI/Transcribe",
            request_serializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.TranscribeRequest.SerializeToString,
            response_deserializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.TranscribeResponse.FromString,
        )
        self.ScaleAiCallback = channel.unary_unary(
            "/flexport.transcription.transcriptionservice.v1beta1.TranscriptionServiceAPI/ScaleAiCallback",
            request_serializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.ScaleAiCallbackRequest.SerializeToString,
            response_deserializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.ScaleAiCallbackResponse.FromString,
        )
        self.RossumCallback = channel.unary_unary(
            "/flexport.transcription.transcriptionservice.v1beta1.TranscriptionServiceAPI/RossumCallback",
            request_serializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.RossumCallbackRequest.SerializeToString,
            response_deserializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.RossumCallbackResponse.FromString,
        )


class TranscriptionServiceAPIServicer:
    """This is the API for the Transcription Service."""

    def Transcribe(self, request, context):
        """Transcribe a file given its location as a URL."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ScaleAiCallback(self, request, context):
        """Callback URL to give to Scale.ai."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RossumCallback(self, request, context):
        """Callback URL to give to Rossum."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TranscriptionServiceAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Transcribe": grpc.unary_unary_rpc_method_handler(
            servicer.Transcribe,
            request_deserializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.TranscribeRequest.FromString,
            response_serializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.TranscribeResponse.SerializeToString,
        ),
        "ScaleAiCallback": grpc.unary_unary_rpc_method_handler(
            servicer.ScaleAiCallback,
            request_deserializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.ScaleAiCallbackRequest.FromString,
            response_serializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.ScaleAiCallbackResponse.SerializeToString,
        ),
        "RossumCallback": grpc.unary_unary_rpc_method_handler(
            servicer.RossumCallback,
            request_deserializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.RossumCallbackRequest.FromString,
            response_serializer=flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.RossumCallbackResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.transcription.transcriptionservice.v1beta1.TranscriptionServiceAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class TranscriptionServiceAPI:
    """This is the API for the Transcription Service."""

    @staticmethod
    def Transcribe(
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
            "/flexport.transcription.transcriptionservice.v1beta1.TranscriptionServiceAPI/Transcribe",
            flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.TranscribeRequest.SerializeToString,
            flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.TranscribeResponse.FromString,
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
    def ScaleAiCallback(
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
            "/flexport.transcription.transcriptionservice.v1beta1.TranscriptionServiceAPI/ScaleAiCallback",
            flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.ScaleAiCallbackRequest.SerializeToString,
            flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.ScaleAiCallbackResponse.FromString,
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
    def RossumCallback(
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
            "/flexport.transcription.transcriptionservice.v1beta1.TranscriptionServiceAPI/RossumCallback",
            flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.RossumCallbackRequest.SerializeToString,
            flexport_dot_transcription_dot_transcriptionservice_dot_v1beta1_dot_transcription__service__api__pb2.RossumCallbackResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )