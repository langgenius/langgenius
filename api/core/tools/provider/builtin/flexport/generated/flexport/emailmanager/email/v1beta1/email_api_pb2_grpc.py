# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.emailmanager.email.v1beta1 import (
    email_api_pb2 as flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2,
)


class EmailAPIStub:
    """Main API for interacting with Email entities.
    Please read API developer guide https://flexport.atlassian.net/wiki/spaces/EN/pages/2678981182/Email+Manager+API+Developer+Guide
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEmail = channel.unary_unary(
            "/flexport.emailmanager.email.v1beta1.EmailAPI/GetEmail",
            request_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailRequest.SerializeToString,
            response_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailResponse.FromString,
        )
        self.ListEmails = channel.unary_unary(
            "/flexport.emailmanager.email.v1beta1.EmailAPI/ListEmails",
            request_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.ListEmailsRequest.SerializeToString,
            response_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.ListEmailsResponse.FromString,
        )
        self.SendEmail = channel.unary_unary(
            "/flexport.emailmanager.email.v1beta1.EmailAPI/SendEmail",
            request_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.SendEmailRequest.SerializeToString,
            response_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.SendEmailResponse.FromString,
        )
        self.LogEmail = channel.unary_unary(
            "/flexport.emailmanager.email.v1beta1.EmailAPI/LogEmail",
            request_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.LogEmailRequest.SerializeToString,
            response_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.LogEmailResponse.FromString,
        )
        self.GetTemplatePlaceholders = channel.unary_unary(
            "/flexport.emailmanager.email.v1beta1.EmailAPI/GetTemplatePlaceholders",
            request_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetTemplatePlaceholdersRequest.SerializeToString,
            response_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetTemplatePlaceholdersResponse.FromString,
        )
        self.GetInterpolatedEmail = channel.unary_unary(
            "/flexport.emailmanager.email.v1beta1.EmailAPI/GetInterpolatedEmail",
            request_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetInterpolatedEmailRequest.SerializeToString,
            response_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetInterpolatedEmailResponse.FromString,
        )
        self.CreateEmailTemplate = channel.unary_unary(
            "/flexport.emailmanager.email.v1beta1.EmailAPI/CreateEmailTemplate",
            request_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.CreateEmailTemplateRequest.SerializeToString,
            response_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.CreateEmailTemplateResponse.FromString,
        )
        self.GetEmailTemplate = channel.unary_unary(
            "/flexport.emailmanager.email.v1beta1.EmailAPI/GetEmailTemplate",
            request_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailTemplateRequest.SerializeToString,
            response_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailTemplateResponse.FromString,
        )


class EmailAPIServicer:
    """Main API for interacting with Email entities.
    Please read API developer guide https://flexport.atlassian.net/wiki/spaces/EN/pages/2678981182/Email+Manager+API+Developer+Guide
    """

    def GetEmail(self, request, context):
        """Find a specific email by fid."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListEmails(self, request, context):
        """Search emails by filter criteria."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SendEmail(self, request, context):
        """Send an email based on input"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LogEmail(self, request, context):
        """Log an email from core (internal-only API, do not use)."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTemplatePlaceholders(self, request, context):
        """given templateFid or emailType, get the template by fid or default template by emailType. extract required variable names from subject&htmlBody&plainBody."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetInterpolatedEmail(self, request, context):
        """given templateFid or emailType along with variables, get the interpolated email subject&html_body&plain_body."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateEmailTemplate(self, request, context):
        """Create an email template"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetEmailTemplate(self, request, context):
        """Retrieve an email, get the template by fid or default template by emailType"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_EmailAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetEmail": grpc.unary_unary_rpc_method_handler(
            servicer.GetEmail,
            request_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailRequest.FromString,
            response_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailResponse.SerializeToString,
        ),
        "ListEmails": grpc.unary_unary_rpc_method_handler(
            servicer.ListEmails,
            request_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.ListEmailsRequest.FromString,
            response_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.ListEmailsResponse.SerializeToString,
        ),
        "SendEmail": grpc.unary_unary_rpc_method_handler(
            servicer.SendEmail,
            request_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.SendEmailRequest.FromString,
            response_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.SendEmailResponse.SerializeToString,
        ),
        "LogEmail": grpc.unary_unary_rpc_method_handler(
            servicer.LogEmail,
            request_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.LogEmailRequest.FromString,
            response_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.LogEmailResponse.SerializeToString,
        ),
        "GetTemplatePlaceholders": grpc.unary_unary_rpc_method_handler(
            servicer.GetTemplatePlaceholders,
            request_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetTemplatePlaceholdersRequest.FromString,
            response_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetTemplatePlaceholdersResponse.SerializeToString,
        ),
        "GetInterpolatedEmail": grpc.unary_unary_rpc_method_handler(
            servicer.GetInterpolatedEmail,
            request_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetInterpolatedEmailRequest.FromString,
            response_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetInterpolatedEmailResponse.SerializeToString,
        ),
        "CreateEmailTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.CreateEmailTemplate,
            request_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.CreateEmailTemplateRequest.FromString,
            response_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.CreateEmailTemplateResponse.SerializeToString,
        ),
        "GetEmailTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.GetEmailTemplate,
            request_deserializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailTemplateRequest.FromString,
            response_serializer=flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailTemplateResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.emailmanager.email.v1beta1.EmailAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class EmailAPI:
    """Main API for interacting with Email entities.
    Please read API developer guide https://flexport.atlassian.net/wiki/spaces/EN/pages/2678981182/Email+Manager+API+Developer+Guide
    """

    @staticmethod
    def GetEmail(
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
            "/flexport.emailmanager.email.v1beta1.EmailAPI/GetEmail",
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailRequest.SerializeToString,
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailResponse.FromString,
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
    def ListEmails(
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
            "/flexport.emailmanager.email.v1beta1.EmailAPI/ListEmails",
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.ListEmailsRequest.SerializeToString,
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.ListEmailsResponse.FromString,
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
    def SendEmail(
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
            "/flexport.emailmanager.email.v1beta1.EmailAPI/SendEmail",
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.SendEmailRequest.SerializeToString,
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.SendEmailResponse.FromString,
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
    def LogEmail(
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
            "/flexport.emailmanager.email.v1beta1.EmailAPI/LogEmail",
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.LogEmailRequest.SerializeToString,
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.LogEmailResponse.FromString,
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
    def GetTemplatePlaceholders(
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
            "/flexport.emailmanager.email.v1beta1.EmailAPI/GetTemplatePlaceholders",
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetTemplatePlaceholdersRequest.SerializeToString,
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetTemplatePlaceholdersResponse.FromString,
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
    def GetInterpolatedEmail(
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
            "/flexport.emailmanager.email.v1beta1.EmailAPI/GetInterpolatedEmail",
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetInterpolatedEmailRequest.SerializeToString,
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetInterpolatedEmailResponse.FromString,
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
    def CreateEmailTemplate(
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
            "/flexport.emailmanager.email.v1beta1.EmailAPI/CreateEmailTemplate",
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.CreateEmailTemplateRequest.SerializeToString,
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.CreateEmailTemplateResponse.FromString,
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
    def GetEmailTemplate(
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
            "/flexport.emailmanager.email.v1beta1.EmailAPI/GetEmailTemplate",
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailTemplateRequest.SerializeToString,
            flexport_dot_emailmanager_dot_email_dot_v1beta1_dot_email__api__pb2.GetEmailTemplateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )