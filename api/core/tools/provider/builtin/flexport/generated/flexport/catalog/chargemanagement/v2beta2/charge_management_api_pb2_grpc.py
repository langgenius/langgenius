# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.catalog.chargemanagement.v2beta2 import (
    charge_management_api_pb2 as flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2,
)


class ChargeManagementAPIStub:
    """The charge-management service definition."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCharges = channel.unary_unary(
            "/flexport.catalog.chargemanagement.v2beta2.ChargeManagementAPI/GetCharges",
            request_serializer=flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetChargesRequest.SerializeToString,
            response_deserializer=flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetChargesResponse.FromString,
        )
        self.GetMarkups = channel.unary_unary(
            "/flexport.catalog.chargemanagement.v2beta2.ChargeManagementAPI/GetMarkups",
            request_serializer=flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetMarkupsRequest.SerializeToString,
            response_deserializer=flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetMarkupsResponse.FromString,
        )


class ChargeManagementAPIServicer:
    """The charge-management service definition."""

    def GetCharges(self, request, context):
        """Endpoint for fetching charges that apply to one or more offerings."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetMarkups(self, request, context):
        """Endpoint for fetching markups that apply to one or more offerings."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ChargeManagementAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetCharges": grpc.unary_unary_rpc_method_handler(
            servicer.GetCharges,
            request_deserializer=flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetChargesRequest.FromString,
            response_serializer=flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetChargesResponse.SerializeToString,
        ),
        "GetMarkups": grpc.unary_unary_rpc_method_handler(
            servicer.GetMarkups,
            request_deserializer=flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetMarkupsRequest.FromString,
            response_serializer=flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetMarkupsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.catalog.chargemanagement.v2beta2.ChargeManagementAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ChargeManagementAPI:
    """The charge-management service definition."""

    @staticmethod
    def GetCharges(
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
            "/flexport.catalog.chargemanagement.v2beta2.ChargeManagementAPI/GetCharges",
            flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetChargesRequest.SerializeToString,
            flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetChargesResponse.FromString,
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
    def GetMarkups(
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
            "/flexport.catalog.chargemanagement.v2beta2.ChargeManagementAPI/GetMarkups",
            flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetMarkupsRequest.SerializeToString,
            flexport_dot_catalog_dot_chargemanagement_dot_v2beta2_dot_charge__management__api__pb2.GetMarkupsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )