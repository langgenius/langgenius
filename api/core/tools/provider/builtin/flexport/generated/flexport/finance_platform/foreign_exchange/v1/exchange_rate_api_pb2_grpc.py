# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.finance_platform.foreign_exchange.v1 import (
    exchange_rate_api_pb2 as flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2,
)


class ExchangeRateAPIStub:
    """The protocol for all foreign exchange rate API."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCurrentExchangeRate = channel.unary_unary(
            "/flexport.finance_platform.foreign_exchange.v1.ExchangeRateAPI/GetCurrentExchangeRate",
            request_serializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetCurrentExchangeRateRequest.SerializeToString,
            response_deserializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetCurrentExchangeRateResponse.FromString,
        )
        self.GetExchangeRateAsOf = channel.unary_unary(
            "/flexport.finance_platform.foreign_exchange.v1.ExchangeRateAPI/GetExchangeRateAsOf",
            request_serializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetExchangeRateAsOfRequest.SerializeToString,
            response_deserializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetExchangeRateAsOfResponse.FromString,
        )
        self.FindExchangeRate = channel.unary_unary(
            "/flexport.finance_platform.foreign_exchange.v1.ExchangeRateAPI/FindExchangeRate",
            request_serializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FindExchangeRateRequest.SerializeToString,
            response_deserializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FindExchangeRateResponse.FromString,
        )
        self.FetchAndStoreExchangeRate = channel.unary_unary(
            "/flexport.finance_platform.foreign_exchange.v1.ExchangeRateAPI/FetchAndStoreExchangeRate",
            request_serializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FetchAndStoreExchangeRateRequest.SerializeToString,
            response_deserializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FetchAndStoreExchangeRateResponse.FromString,
        )


class ExchangeRateAPIServicer:
    """The protocol for all foreign exchange rate API."""

    def GetCurrentExchangeRate(self, request, context):
        """Get the latest exchange rate dto. A custom FX source may optionally be
        specified to fetch rates retreived from that source, else the Flexport
        company default source will be used.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetExchangeRateAsOf(self, request, context):
        """Get the latest exchange rate dto before a specific time, return the
        exchange rate with earliest time otherwise. A custom FX source may
        optionally be specified to fetch rates retreived from that source, else the
        Flexport company default source will be used.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FindExchangeRate(self, request, context):
        """Get exchange rate dto with core database id."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FetchAndStoreExchangeRate(self, request, context):
        """Fetch new exchange rate from openexchangerate api."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ExchangeRateAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetCurrentExchangeRate": grpc.unary_unary_rpc_method_handler(
            servicer.GetCurrentExchangeRate,
            request_deserializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetCurrentExchangeRateRequest.FromString,
            response_serializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetCurrentExchangeRateResponse.SerializeToString,
        ),
        "GetExchangeRateAsOf": grpc.unary_unary_rpc_method_handler(
            servicer.GetExchangeRateAsOf,
            request_deserializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetExchangeRateAsOfRequest.FromString,
            response_serializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetExchangeRateAsOfResponse.SerializeToString,
        ),
        "FindExchangeRate": grpc.unary_unary_rpc_method_handler(
            servicer.FindExchangeRate,
            request_deserializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FindExchangeRateRequest.FromString,
            response_serializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FindExchangeRateResponse.SerializeToString,
        ),
        "FetchAndStoreExchangeRate": grpc.unary_unary_rpc_method_handler(
            servicer.FetchAndStoreExchangeRate,
            request_deserializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FetchAndStoreExchangeRateRequest.FromString,
            response_serializer=flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FetchAndStoreExchangeRateResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.finance_platform.foreign_exchange.v1.ExchangeRateAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class ExchangeRateAPI:
    """The protocol for all foreign exchange rate API."""

    @staticmethod
    def GetCurrentExchangeRate(
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
            "/flexport.finance_platform.foreign_exchange.v1.ExchangeRateAPI/GetCurrentExchangeRate",
            flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetCurrentExchangeRateRequest.SerializeToString,
            flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetCurrentExchangeRateResponse.FromString,
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
    def GetExchangeRateAsOf(
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
            "/flexport.finance_platform.foreign_exchange.v1.ExchangeRateAPI/GetExchangeRateAsOf",
            flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetExchangeRateAsOfRequest.SerializeToString,
            flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.GetExchangeRateAsOfResponse.FromString,
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
    def FindExchangeRate(
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
            "/flexport.finance_platform.foreign_exchange.v1.ExchangeRateAPI/FindExchangeRate",
            flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FindExchangeRateRequest.SerializeToString,
            flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FindExchangeRateResponse.FromString,
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
    def FetchAndStoreExchangeRate(
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
            "/flexport.finance_platform.foreign_exchange.v1.ExchangeRateAPI/FetchAndStoreExchangeRate",
            flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FetchAndStoreExchangeRateRequest.SerializeToString,
            flexport_dot_finance__platform_dot_foreign__exchange_dot_v1_dot_exchange__rate__api__pb2.FetchAndStoreExchangeRateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )