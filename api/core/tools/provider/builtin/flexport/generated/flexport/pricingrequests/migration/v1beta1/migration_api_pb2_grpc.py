# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.pricingrequests.migration.v1beta1 import (
    migration_api_pb2 as flexport_dot_pricingrequests_dot_migration_dot_v1beta1_dot_migration__api__pb2,
)


class MigrationAPIStub:
    """Specialized methods that encompass moving data from the monolith to the Pricing Requests NIS outside of normal business logic rules."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SyncBid = channel.unary_unary(
            "/flexport.pricingrequests.migration.v1beta1.MigrationAPI/SyncBid",
            request_serializer=flexport_dot_pricingrequests_dot_migration_dot_v1beta1_dot_migration__api__pb2.SyncBidRequest.SerializeToString,
            response_deserializer=flexport_dot_pricingrequests_dot_migration_dot_v1beta1_dot_migration__api__pb2.SyncBidResponse.FromString,
        )


class MigrationAPIServicer:
    """Specialized methods that encompass moving data from the monolith to the Pricing Requests NIS outside of normal business logic rules."""

    def SyncBid(self, request, context):
        """Tell the NIS to pull up-to-date Bid data specified by the fid."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MigrationAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SyncBid": grpc.unary_unary_rpc_method_handler(
            servicer.SyncBid,
            request_deserializer=flexport_dot_pricingrequests_dot_migration_dot_v1beta1_dot_migration__api__pb2.SyncBidRequest.FromString,
            response_serializer=flexport_dot_pricingrequests_dot_migration_dot_v1beta1_dot_migration__api__pb2.SyncBidResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.pricingrequests.migration.v1beta1.MigrationAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class MigrationAPI:
    """Specialized methods that encompass moving data from the monolith to the Pricing Requests NIS outside of normal business logic rules."""

    @staticmethod
    def SyncBid(
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
            "/flexport.pricingrequests.migration.v1beta1.MigrationAPI/SyncBid",
            flexport_dot_pricingrequests_dot_migration_dot_v1beta1_dot_migration__api__pb2.SyncBidRequest.SerializeToString,
            flexport_dot_pricingrequests_dot_migration_dot_v1beta1_dot_migration__api__pb2.SyncBidResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )