# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.catalog.chargeitem.v1 import (
    charge_item_api_pb2 as flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2,
)


class ChargeItemAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetChargeItems = channel.unary_unary(
            "/flexport.catalog.chargeitem.v1.ChargeItemAPI/GetChargeItems",
            request_serializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetChargeItemsRequest.SerializeToString,
            response_deserializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetChargeItemsResponse.FromString,
        )
        self.GetUnprocessedChargeItems = channel.unary_unary(
            "/flexport.catalog.chargeitem.v1.ChargeItemAPI/GetUnprocessedChargeItems",
            request_serializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetUnprocessedChargeItemsRequest.SerializeToString,
            response_deserializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetUnprocessedChargeItemsResponse.FromString,
        )
        self.ProcessChargeItems = channel.unary_unary(
            "/flexport.catalog.chargeitem.v1.ChargeItemAPI/ProcessChargeItems",
            request_serializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.ProcessChargeItemsRequest.SerializeToString,
            response_deserializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.ProcessChargeItemsResponse.FromString,
        )
        self.GetPresentableChargeItems = channel.unary_unary(
            "/flexport.catalog.chargeitem.v1.ChargeItemAPI/GetPresentableChargeItems",
            request_serializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetPresentableChargeItemsRequest.SerializeToString,
            response_deserializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetPresentableChargeItemsResponse.FromString,
        )


class ChargeItemAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def GetChargeItems(self, request, context):
        """*
        Get the ChargeItems for the given request, typically for all the offerings on the order/shipment.

        A ChargeItem is a Commerce owned entity that represents a charge applied to a given order/shipment context. ChargeItems
        are derived from the internal Charge entity, which is a more granular concept than what most of Commerce’s systems
        customers interact with. Charges are converted to ChargeItems using ServiceItemTemplates https://core.flexport.com/service_item_templates

        ChargeItems are processed for presentation. At the time of writing, this includes
        de-duplicate ChargeItem across offerings
        filter out ChargeItems with zero rates
        bundle chargeItems based on service offering config https://core.flexport.com/marketplace/service_offerings/configure

        The ChargeItem is an attempt to represent Charges with a centralized set of mutations so that all downstream interested parties
        get a consistent view of reality which can be priced against.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetUnprocessedChargeItems(self, request, context):
        """*
        Get the UnprocessedChargeItems for the given request, typically for a set of offerings

        UnprocessedChargeItems are just ChargeItems which have not been processed for presentation.

        The UnprocessedChargeItem is an attempt to represent Charges mapped to ServiceItems so that all upstream interested parties
        can think in terms of ChargeItems which can be priced against.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ProcessChargeItems(self, request, context):
        """*
        Process ChargeItems for Presentation

        At the time of writing, this includes pure / idempotent functions which do the following:
        de-duplicate ChargeItems across offerings
        filter out ChargeItems with zero rates
        bundle chargeItems based on service offering config https://core.flexport.com/marketplace/service_offerings/configure

        To view how ChargeItems will appear on the quote (for instance), UnprocessedChargeItems should be processed by this centralized set of mutations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetPresentableChargeItems(self, request, context):
        """*
        Get Charge Items after applying any applicable invoicing presentation rules.

        This endpoint processes a list of ChargeItems based on client and transportation mode-specific presentation rules.
        It bundles, renames, and modifies these items according to predefined JSON rules before returning the adjusted list.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ChargeItemAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetChargeItems": grpc.unary_unary_rpc_method_handler(
            servicer.GetChargeItems,
            request_deserializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetChargeItemsRequest.FromString,
            response_serializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetChargeItemsResponse.SerializeToString,
        ),
        "GetUnprocessedChargeItems": grpc.unary_unary_rpc_method_handler(
            servicer.GetUnprocessedChargeItems,
            request_deserializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetUnprocessedChargeItemsRequest.FromString,
            response_serializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetUnprocessedChargeItemsResponse.SerializeToString,
        ),
        "ProcessChargeItems": grpc.unary_unary_rpc_method_handler(
            servicer.ProcessChargeItems,
            request_deserializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.ProcessChargeItemsRequest.FromString,
            response_serializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.ProcessChargeItemsResponse.SerializeToString,
        ),
        "GetPresentableChargeItems": grpc.unary_unary_rpc_method_handler(
            servicer.GetPresentableChargeItems,
            request_deserializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetPresentableChargeItemsRequest.FromString,
            response_serializer=flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetPresentableChargeItemsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.catalog.chargeitem.v1.ChargeItemAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ChargeItemAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetChargeItems(
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
            "/flexport.catalog.chargeitem.v1.ChargeItemAPI/GetChargeItems",
            flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetChargeItemsRequest.SerializeToString,
            flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetChargeItemsResponse.FromString,
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
    def GetUnprocessedChargeItems(
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
            "/flexport.catalog.chargeitem.v1.ChargeItemAPI/GetUnprocessedChargeItems",
            flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetUnprocessedChargeItemsRequest.SerializeToString,
            flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetUnprocessedChargeItemsResponse.FromString,
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
    def ProcessChargeItems(
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
            "/flexport.catalog.chargeitem.v1.ChargeItemAPI/ProcessChargeItems",
            flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.ProcessChargeItemsRequest.SerializeToString,
            flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.ProcessChargeItemsResponse.FromString,
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
    def GetPresentableChargeItems(
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
            "/flexport.catalog.chargeitem.v1.ChargeItemAPI/GetPresentableChargeItems",
            flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetPresentableChargeItemsRequest.SerializeToString,
            flexport_dot_catalog_dot_chargeitem_dot_v1_dot_charge__item__api__pb2.GetPresentableChargeItemsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )