# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.authorization.grant.v2 import (
    grant_api_pb2 as flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2,
)


class GrantAPIStub:
    """Handles role grants."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRoleGrant = channel.unary_unary(
            "/flexport.authorization.grant.v2.GrantAPI/CreateRoleGrant",
            request_serializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.CreateRoleGrantRequest.SerializeToString,
            response_deserializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.CreateRoleGrantResponse.FromString,
        )
        self.GetRoleGrants = channel.unary_unary(
            "/flexport.authorization.grant.v2.GrantAPI/GetRoleGrants",
            request_serializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRoleGrantsRequest.SerializeToString,
            response_deserializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRoleGrantsResponse.FromString,
        )
        self.RevokeRoleGrant = channel.unary_unary(
            "/flexport.authorization.grant.v2.GrantAPI/RevokeRoleGrant",
            request_serializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.RevokeRoleGrantRequest.SerializeToString,
            response_deserializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.RevokeRoleGrantResponse.FromString,
        )
        self.GetRolesForApp = channel.unary_unary(
            "/flexport.authorization.grant.v2.GrantAPI/GetRolesForApp",
            request_serializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRolesForAppRequest.SerializeToString,
            response_deserializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRolesForAppResponse.FromString,
        )
        self.ListRoleGrantsForRole = channel.unary_stream(
            "/flexport.authorization.grant.v2.GrantAPI/ListRoleGrantsForRole",
            request_serializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.ListRoleGrantsForRoleRequest.SerializeToString,
            response_deserializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.ListRoleGrantsForRoleResponse.FromString,
        )


class GrantAPIServicer:
    """Handles role grants."""

    def CreateRoleGrant(self, request, context):
        """Grant role to an actor."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetRoleGrants(self, request, context):
        """Get all role grants for an actor."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RevokeRoleGrant(self, request, context):
        """Revoke a role grant."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetRolesForApp(self, request, context):
        """Returns roles that can be granted for a particular app, e.g. Core, Transmission."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListRoleGrantsForRole(self, request, context):
        """Fetch a paginated list of actors provided a role slug"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_GrantAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateRoleGrant": grpc.unary_unary_rpc_method_handler(
            servicer.CreateRoleGrant,
            request_deserializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.CreateRoleGrantRequest.FromString,
            response_serializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.CreateRoleGrantResponse.SerializeToString,
        ),
        "GetRoleGrants": grpc.unary_unary_rpc_method_handler(
            servicer.GetRoleGrants,
            request_deserializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRoleGrantsRequest.FromString,
            response_serializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRoleGrantsResponse.SerializeToString,
        ),
        "RevokeRoleGrant": grpc.unary_unary_rpc_method_handler(
            servicer.RevokeRoleGrant,
            request_deserializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.RevokeRoleGrantRequest.FromString,
            response_serializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.RevokeRoleGrantResponse.SerializeToString,
        ),
        "GetRolesForApp": grpc.unary_unary_rpc_method_handler(
            servicer.GetRolesForApp,
            request_deserializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRolesForAppRequest.FromString,
            response_serializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRolesForAppResponse.SerializeToString,
        ),
        "ListRoleGrantsForRole": grpc.unary_stream_rpc_method_handler(
            servicer.ListRoleGrantsForRole,
            request_deserializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.ListRoleGrantsForRoleRequest.FromString,
            response_serializer=flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.ListRoleGrantsForRoleResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.authorization.grant.v2.GrantAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class GrantAPI:
    """Handles role grants."""

    @staticmethod
    def CreateRoleGrant(
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
            "/flexport.authorization.grant.v2.GrantAPI/CreateRoleGrant",
            flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.CreateRoleGrantRequest.SerializeToString,
            flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.CreateRoleGrantResponse.FromString,
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
    def GetRoleGrants(
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
            "/flexport.authorization.grant.v2.GrantAPI/GetRoleGrants",
            flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRoleGrantsRequest.SerializeToString,
            flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRoleGrantsResponse.FromString,
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
    def RevokeRoleGrant(
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
            "/flexport.authorization.grant.v2.GrantAPI/RevokeRoleGrant",
            flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.RevokeRoleGrantRequest.SerializeToString,
            flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.RevokeRoleGrantResponse.FromString,
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
    def GetRolesForApp(
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
            "/flexport.authorization.grant.v2.GrantAPI/GetRolesForApp",
            flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRolesForAppRequest.SerializeToString,
            flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.GetRolesForAppResponse.FromString,
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
    def ListRoleGrantsForRole(
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
        return grpc.experimental.unary_stream(
            request,
            target,
            "/flexport.authorization.grant.v2.GrantAPI/ListRoleGrantsForRole",
            flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.ListRoleGrantsForRoleRequest.SerializeToString,
            flexport_dot_authorization_dot_grant_dot_v2_dot_grant__api__pb2.ListRoleGrantsForRoleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )