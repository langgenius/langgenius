# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.customsonlybooking.email.v1beta1 import (
    email_api_pb2 as flexport_dot_customsonlybooking_dot_email_dot_v1beta1_dot_email__api__pb2,
)


class EmailAPIStub:
    """The email service definition."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateOrUpdateEmail = channel.unary_unary(
            "/flexport.customsonlybooking.email.v1beta1.EmailAPI/CreateOrUpdateEmail",
            request_serializer=flexport_dot_customsonlybooking_dot_email_dot_v1beta1_dot_email__api__pb2.CreateOrUpdateEmailRequest.SerializeToString,
            response_deserializer=flexport_dot_customsonlybooking_dot_email_dot_v1beta1_dot_email__api__pb2.CreateOrUpdateEmailResponse.FromString,
        )


class EmailAPIServicer:
    """The email service definition."""

    def CreateOrUpdateEmail(self, request, context):
        """Creates or updates email object."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_EmailAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateOrUpdateEmail": grpc.unary_unary_rpc_method_handler(
            servicer.CreateOrUpdateEmail,
            request_deserializer=flexport_dot_customsonlybooking_dot_email_dot_v1beta1_dot_email__api__pb2.CreateOrUpdateEmailRequest.FromString,
            response_serializer=flexport_dot_customsonlybooking_dot_email_dot_v1beta1_dot_email__api__pb2.CreateOrUpdateEmailResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.customsonlybooking.email.v1beta1.EmailAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class EmailAPI:
    """The email service definition."""

    @staticmethod
    def CreateOrUpdateEmail(
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
            "/flexport.customsonlybooking.email.v1beta1.EmailAPI/CreateOrUpdateEmail",
            flexport_dot_customsonlybooking_dot_email_dot_v1beta1_dot_email__api__pb2.CreateOrUpdateEmailRequest.SerializeToString,
            flexport_dot_customsonlybooking_dot_email_dot_v1beta1_dot_email__api__pb2.CreateOrUpdateEmailResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )