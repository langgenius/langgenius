# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.integrationtest.authorization.v1 import (
    authorization_test_with_auth_api_pb2 as flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2,
)


class AuthorizationTestWithAuthAPIStub:
    """The API for authorization integration tests."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ServerInterceptorTestRegularWithAuthCheck = channel.unary_unary(
            "/flexport.integrationtest.authorization.v1.AuthorizationTestWithAuthAPI/ServerInterceptorTestRegularWithAuthCheck",
            request_serializer=flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorTestRegularWithAuthCheckRequest.SerializeToString,
            response_deserializer=flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorTestRegularWithAuthCheckResponse.FromString,
        )
        self.ServerInterceptorNoMandatoryAuthWithAuthCheck = channel.unary_unary(
            "/flexport.integrationtest.authorization.v1.AuthorizationTestWithAuthAPI/ServerInterceptorNoMandatoryAuthWithAuthCheck",
            request_serializer=flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorNoMandatoryAuthWithAuthCheckRequest.SerializeToString,
            response_deserializer=flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorNoMandatoryAuthWithAuthCheckResponse.FromString,
        )


class AuthorizationTestWithAuthAPIServicer:
    """The API for authorization integration tests."""

    def ServerInterceptorTestRegularWithAuthCheck(self, request, context):
        """Test endpoint for authorization integration test, not included on the dont_enforce_mandatory_auth_for_methods list. This endpoint also enforces auth check by calling the CheckAuth module in ruby SDK"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ServerInterceptorNoMandatoryAuthWithAuthCheck(self, request, context):
        """Test endpoint for authorization integration test, included on the dont_enforce_mandatory_auth_for_methods list. This endpoint also enforces auth check by calling the CheckAuth module in ruby SDK"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AuthorizationTestWithAuthAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ServerInterceptorTestRegularWithAuthCheck": grpc.unary_unary_rpc_method_handler(
            servicer.ServerInterceptorTestRegularWithAuthCheck,
            request_deserializer=flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorTestRegularWithAuthCheckRequest.FromString,
            response_serializer=flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorTestRegularWithAuthCheckResponse.SerializeToString,
        ),
        "ServerInterceptorNoMandatoryAuthWithAuthCheck": grpc.unary_unary_rpc_method_handler(
            servicer.ServerInterceptorNoMandatoryAuthWithAuthCheck,
            request_deserializer=flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorNoMandatoryAuthWithAuthCheckRequest.FromString,
            response_serializer=flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorNoMandatoryAuthWithAuthCheckResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.integrationtest.authorization.v1.AuthorizationTestWithAuthAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class AuthorizationTestWithAuthAPI:
    """The API for authorization integration tests."""

    @staticmethod
    def ServerInterceptorTestRegularWithAuthCheck(
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
            "/flexport.integrationtest.authorization.v1.AuthorizationTestWithAuthAPI/ServerInterceptorTestRegularWithAuthCheck",
            flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorTestRegularWithAuthCheckRequest.SerializeToString,
            flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorTestRegularWithAuthCheckResponse.FromString,
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
    def ServerInterceptorNoMandatoryAuthWithAuthCheck(
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
            "/flexport.integrationtest.authorization.v1.AuthorizationTestWithAuthAPI/ServerInterceptorNoMandatoryAuthWithAuthCheck",
            flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorNoMandatoryAuthWithAuthCheckRequest.SerializeToString,
            flexport_dot_integrationtest_dot_authorization_dot_v1_dot_authorization__test__with__auth__api__pb2.ServerInterceptorNoMandatoryAuthWithAuthCheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )