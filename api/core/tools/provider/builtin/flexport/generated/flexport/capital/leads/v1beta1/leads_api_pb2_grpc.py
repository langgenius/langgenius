# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.capital.leads.v1beta1 import (
    leads_api_pb2 as flexport_dot_capital_dot_leads_dot_v1beta1_dot_leads__api__pb2,
)


class LeadsAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RecordLead = channel.unary_unary(
            "/flexport.capital.leads.v1beta1.LeadsAPI/RecordLead",
            request_serializer=flexport_dot_capital_dot_leads_dot_v1beta1_dot_leads__api__pb2.RecordLeadRequest.SerializeToString,
            response_deserializer=flexport_dot_capital_dot_leads_dot_v1beta1_dot_leads__api__pb2.RecordLeadResponse.FromString,
        )


class LeadsAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def RecordLead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_LeadsAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "RecordLead": grpc.unary_unary_rpc_method_handler(
            servicer.RecordLead,
            request_deserializer=flexport_dot_capital_dot_leads_dot_v1beta1_dot_leads__api__pb2.RecordLeadRequest.FromString,
            response_serializer=flexport_dot_capital_dot_leads_dot_v1beta1_dot_leads__api__pb2.RecordLeadResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.capital.leads.v1beta1.LeadsAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class LeadsAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RecordLead(
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
            "/flexport.capital.leads.v1beta1.LeadsAPI/RecordLead",
            flexport_dot_capital_dot_leads_dot_v1beta1_dot_leads__api__pb2.RecordLeadRequest.SerializeToString,
            flexport_dot_capital_dot_leads_dot_v1beta1_dot_leads__api__pb2.RecordLeadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )