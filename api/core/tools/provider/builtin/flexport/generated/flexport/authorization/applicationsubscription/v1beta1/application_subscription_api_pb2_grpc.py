# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.authorization.applicationsubscription.v1beta1 import (
    application_subscription_api_pb2 as flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2,
)


class ApplicationSubscriptionAPIStub:
    """These APIs will be exposed as json over Http."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateApplicationSubscription = channel.unary_unary(
            "/flexport.authorization.applicationsubscription.v1beta1.ApplicationSubscriptionAPI/CreateApplicationSubscription",
            request_serializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.CreateApplicationSubscriptionRequest.SerializeToString,
            response_deserializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.CreateApplicationSubscriptionResponse.FromString,
        )
        self.UpdateApplicationSubscriptionStatus = channel.unary_unary(
            "/flexport.authorization.applicationsubscription.v1beta1.ApplicationSubscriptionAPI/UpdateApplicationSubscriptionStatus",
            request_serializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.UpdateApplicationSubscriptionStatusRequest.SerializeToString,
            response_deserializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.UpdateApplicationSubscriptionStatusResponse.FromString,
        )
        self.GetApplicationSubscriptionStatus = channel.unary_unary(
            "/flexport.authorization.applicationsubscription.v1beta1.ApplicationSubscriptionAPI/GetApplicationSubscriptionStatus",
            request_serializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.GetApplicationSubscriptionStatusRequest.SerializeToString,
            response_deserializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.GetApplicationSubscriptionStatusResponse.FromString,
        )


class ApplicationSubscriptionAPIServicer:
    """These APIs will be exposed as json over Http."""

    def CreateApplicationSubscription(self, request, context):
        """Create an Application Subscription. This API will be called from Auth0. The User will not have createApplication
        Subscription permission but client_Admin role. we should provide createApplicationSubscription to Auth0
        clientId/ClientSecret to have a proper auth check
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateApplicationSubscriptionStatus(self, request, context):
        """Third party will will not have store application_id/ApplicationSubscription. We need to drive application/
        ApplicationSubscription information from clientCredential and user_id from JWT.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetApplicationSubscriptionStatus(self, request, context):
        """Get the applicationSubscription status. True means active, False means inactive or unsubscribe."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ApplicationSubscriptionAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateApplicationSubscription": grpc.unary_unary_rpc_method_handler(
            servicer.CreateApplicationSubscription,
            request_deserializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.CreateApplicationSubscriptionRequest.FromString,
            response_serializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.CreateApplicationSubscriptionResponse.SerializeToString,
        ),
        "UpdateApplicationSubscriptionStatus": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateApplicationSubscriptionStatus,
            request_deserializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.UpdateApplicationSubscriptionStatusRequest.FromString,
            response_serializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.UpdateApplicationSubscriptionStatusResponse.SerializeToString,
        ),
        "GetApplicationSubscriptionStatus": grpc.unary_unary_rpc_method_handler(
            servicer.GetApplicationSubscriptionStatus,
            request_deserializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.GetApplicationSubscriptionStatusRequest.FromString,
            response_serializer=flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.GetApplicationSubscriptionStatusResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.authorization.applicationsubscription.v1beta1.ApplicationSubscriptionAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ApplicationSubscriptionAPI:
    """These APIs will be exposed as json over Http."""

    @staticmethod
    def CreateApplicationSubscription(
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
            "/flexport.authorization.applicationsubscription.v1beta1.ApplicationSubscriptionAPI/CreateApplicationSubscription",
            flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.CreateApplicationSubscriptionRequest.SerializeToString,
            flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.CreateApplicationSubscriptionResponse.FromString,
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
    def UpdateApplicationSubscriptionStatus(
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
            "/flexport.authorization.applicationsubscription.v1beta1.ApplicationSubscriptionAPI/UpdateApplicationSubscriptionStatus",
            flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.UpdateApplicationSubscriptionStatusRequest.SerializeToString,
            flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.UpdateApplicationSubscriptionStatusResponse.FromString,
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
    def GetApplicationSubscriptionStatus(
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
            "/flexport.authorization.applicationsubscription.v1beta1.ApplicationSubscriptionAPI/GetApplicationSubscriptionStatus",
            flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.GetApplicationSubscriptionStatusRequest.SerializeToString,
            flexport_dot_authorization_dot_applicationsubscription_dot_v1beta1_dot_application__subscription__api__pb2.GetApplicationSubscriptionStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )