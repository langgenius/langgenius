# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.compliance.restrictedcountry.rpc.v1beta1 import (
    restricted_country_api_pb2 as flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2,
)


class RestrictedCountryAPIStub:
    """Restricted Country Api."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRestrictedCountryHits = channel.unary_unary(
            "/flexport.compliance.restrictedcountry.rpc.v1beta1.RestrictedCountryAPI/GetRestrictedCountryHits",
            request_serializer=flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.GetRestrictedCountryHitsRequest.SerializeToString,
            response_deserializer=flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.GetRestrictedCountryHitsResponse.FromString,
        )
        self.UpdateHitStatus = channel.unary_unary(
            "/flexport.compliance.restrictedcountry.rpc.v1beta1.RestrictedCountryAPI/UpdateHitStatus",
            request_serializer=flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.UpdateHitStatusRequest.SerializeToString,
            response_deserializer=flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.UpdateHitStatusResponse.FromString,
        )


class RestrictedCountryAPIServicer:
    """Restricted Country Api."""

    def GetRestrictedCountryHits(self, request, context):
        """Request to get the list of restricted country hits given a shipment fid"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateHitStatus(self, request, context):
        """Request to update the status of a hit"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RestrictedCountryAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetRestrictedCountryHits": grpc.unary_unary_rpc_method_handler(
            servicer.GetRestrictedCountryHits,
            request_deserializer=flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.GetRestrictedCountryHitsRequest.FromString,
            response_serializer=flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.GetRestrictedCountryHitsResponse.SerializeToString,
        ),
        "UpdateHitStatus": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateHitStatus,
            request_deserializer=flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.UpdateHitStatusRequest.FromString,
            response_serializer=flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.UpdateHitStatusResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.compliance.restrictedcountry.rpc.v1beta1.RestrictedCountryAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class RestrictedCountryAPI:
    """Restricted Country Api."""

    @staticmethod
    def GetRestrictedCountryHits(
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
            "/flexport.compliance.restrictedcountry.rpc.v1beta1.RestrictedCountryAPI/GetRestrictedCountryHits",
            flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.GetRestrictedCountryHitsRequest.SerializeToString,
            flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.GetRestrictedCountryHitsResponse.FromString,
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
    def UpdateHitStatus(
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
            "/flexport.compliance.restrictedcountry.rpc.v1beta1.RestrictedCountryAPI/UpdateHitStatus",
            flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.UpdateHitStatusRequest.SerializeToString,
            flexport_dot_compliance_dot_restrictedcountry_dot_rpc_dot_v1beta1_dot_restricted__country__api__pb2.UpdateHitStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )