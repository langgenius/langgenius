# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.authorization.policy.v1beta1 import (
    policy_api_pb2 as flexport_dot_authorization_dot_policy_dot_v1beta1_dot_policy__api__pb2,
)


class PolicyAPIStub:
    """Allows access to Authorization Service role policies."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllNonObjectLevelRolePermissions = channel.unary_unary(
            "/flexport.authorization.policy.v1beta1.PolicyAPI/GetAllNonObjectLevelRolePermissions",
            request_serializer=flexport_dot_authorization_dot_policy_dot_v1beta1_dot_policy__api__pb2.GetAllNonObjectLevelRolePermissionsRequest.SerializeToString,
            response_deserializer=flexport_dot_authorization_dot_policy_dot_v1beta1_dot_policy__api__pb2.GetAllNonObjectLevelRolePermissionsResponse.FromString,
        )


class PolicyAPIServicer:
    """Allows access to Authorization Service role policies."""

    def GetAllNonObjectLevelRolePermissions(self, request, context):
        """Gets all non-object level role -> permission mappings.
        This was original written for use in integration testing, usage may not show up in production logs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PolicyAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetAllNonObjectLevelRolePermissions": grpc.unary_unary_rpc_method_handler(
            servicer.GetAllNonObjectLevelRolePermissions,
            request_deserializer=flexport_dot_authorization_dot_policy_dot_v1beta1_dot_policy__api__pb2.GetAllNonObjectLevelRolePermissionsRequest.FromString,
            response_serializer=flexport_dot_authorization_dot_policy_dot_v1beta1_dot_policy__api__pb2.GetAllNonObjectLevelRolePermissionsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.authorization.policy.v1beta1.PolicyAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class PolicyAPI:
    """Allows access to Authorization Service role policies."""

    @staticmethod
    def GetAllNonObjectLevelRolePermissions(
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
            "/flexport.authorization.policy.v1beta1.PolicyAPI/GetAllNonObjectLevelRolePermissions",
            flexport_dot_authorization_dot_policy_dot_v1beta1_dot_policy__api__pb2.GetAllNonObjectLevelRolePermissionsRequest.SerializeToString,
            flexport_dot_authorization_dot_policy_dot_v1beta1_dot_policy__api__pb2.GetAllNonObjectLevelRolePermissionsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )