# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.monolith.funnelmanagement.affiliation.v1beta1 import (
    affiliation_api_pb2 as flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2,
)


class AffiliationAPIStub:
    """The affiliation service definition."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Affiliate = channel.unary_unary(
            "/flexport.monolith.funnelmanagement.affiliation.v1beta1.AffiliationAPI/Affiliate",
            request_serializer=flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.AffiliateRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.AffiliateResponse.FromString,
        )
        self.VerifyAffiliation = channel.unary_unary(
            "/flexport.monolith.funnelmanagement.affiliation.v1beta1.AffiliationAPI/VerifyAffiliation",
            request_serializer=flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.VerifyAffiliationRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.VerifyAffiliationResponse.FromString,
        )


class AffiliationAPIServicer:
    """The affiliation service definition."""

    def Affiliate(self, request, context):
        """Attempts to affiliate a user with a carrier and sends a chellenge code to the carrier if the email of the user does
        not match the email of the carrier.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def VerifyAffiliation(self, request, context):
        """Verifies a challenge code sent to a carrier and entered by a user to verify that user's affiliation with that
        carrier.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AffiliationAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Affiliate": grpc.unary_unary_rpc_method_handler(
            servicer.Affiliate,
            request_deserializer=flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.AffiliateRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.AffiliateResponse.SerializeToString,
        ),
        "VerifyAffiliation": grpc.unary_unary_rpc_method_handler(
            servicer.VerifyAffiliation,
            request_deserializer=flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.VerifyAffiliationRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.VerifyAffiliationResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.monolith.funnelmanagement.affiliation.v1beta1.AffiliationAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class AffiliationAPI:
    """The affiliation service definition."""

    @staticmethod
    def Affiliate(
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
            "/flexport.monolith.funnelmanagement.affiliation.v1beta1.AffiliationAPI/Affiliate",
            flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.AffiliateRequest.SerializeToString,
            flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.AffiliateResponse.FromString,
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
    def VerifyAffiliation(
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
            "/flexport.monolith.funnelmanagement.affiliation.v1beta1.AffiliationAPI/VerifyAffiliation",
            flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.VerifyAffiliationRequest.SerializeToString,
            flexport_dot_monolith_dot_funnelmanagement_dot_affiliation_dot_v1beta1_dot_affiliation__api__pb2.VerifyAffiliationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )