# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.catalog.rateitem.v1 import (
    rate_item_api_pb2 as flexport_dot_catalog_dot_rateitem_dot_v1_dot_rate__item__api__pb2,
)


class RateItemAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRateItems = channel.unary_unary(
            "/flexport.catalog.rateitem.v1.RateItemAPI/GetRateItems",
            request_serializer=flexport_dot_catalog_dot_rateitem_dot_v1_dot_rate__item__api__pb2.GetRateItemsRequest.SerializeToString,
            response_deserializer=flexport_dot_catalog_dot_rateitem_dot_v1_dot_rate__item__api__pb2.GetRateItemsResponse.FromString,
        )


class RateItemAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def GetRateItems(self, request, context):
        """Gets the rates specified by the "Default ICC" and "Default Sell" as evaluated by the input attributes against all
        active rules in Charge Management https://core.flexport.com/marketplace/charge_management. A charge and its rates
        are returned only if the input matches the charge Applicability, and a rate branch is matched.

        This API currently only returns rates that are defined in the Charge Management UI, and will not return any rates
        that may be present on the input offering. It also does not filter any rates based on the date ranges in the
        matched rate branch.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RateItemAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetRateItems": grpc.unary_unary_rpc_method_handler(
            servicer.GetRateItems,
            request_deserializer=flexport_dot_catalog_dot_rateitem_dot_v1_dot_rate__item__api__pb2.GetRateItemsRequest.FromString,
            response_serializer=flexport_dot_catalog_dot_rateitem_dot_v1_dot_rate__item__api__pb2.GetRateItemsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.catalog.rateitem.v1.RateItemAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class RateItemAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetRateItems(
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
            "/flexport.catalog.rateitem.v1.RateItemAPI/GetRateItems",
            flexport_dot_catalog_dot_rateitem_dot_v1_dot_rate__item__api__pb2.GetRateItemsRequest.SerializeToString,
            flexport_dot_catalog_dot_rateitem_dot_v1_dot_rate__item__api__pb2.GetRateItemsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )