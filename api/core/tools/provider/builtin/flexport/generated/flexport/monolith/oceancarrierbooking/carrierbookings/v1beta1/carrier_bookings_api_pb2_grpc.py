# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.monolith.oceancarrierbooking.carrierbookings.v1beta1 import (
    carrier_bookings_api_pb2 as flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2,
)


class CarrierBookingsAPIStub:
    """This API will be deprecated soon in favor of OEX NIS, please do not add anything here."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindCarrierBookingByFid = channel.unary_unary(
            "/flexport.monolith.oceancarrierbooking.carrierbookings.v1beta1.CarrierBookingsAPI/FindCarrierBookingByFid",
            request_serializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByFidRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByFidResponse.FromString,
        )
        self.ListCarrierBookingsByExecutionTaskFid = channel.unary_unary(
            "/flexport.monolith.oceancarrierbooking.carrierbookings.v1beta1.CarrierBookingsAPI/ListCarrierBookingsByExecutionTaskFid",
            request_serializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.ListCarrierBookingsByExecutionTaskFidRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.ListCarrierBookingsByExecutionTaskFidResponse.FromString,
        )
        self.FindCarrierBookingByDocumentableFid = channel.unary_unary(
            "/flexport.monolith.oceancarrierbooking.carrierbookings.v1beta1.CarrierBookingsAPI/FindCarrierBookingByDocumentableFid",
            request_serializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByDocumentableFidRequest.SerializeToString,
            response_deserializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByDocumentableFidResponse.FromString,
        )


class CarrierBookingsAPIServicer:
    """This API will be deprecated soon in favor of OEX NIS, please do not add anything here."""

    def FindCarrierBookingByFid(self, request, context):
        """Find carrier booking by carrier booking fid."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListCarrierBookingsByExecutionTaskFid(self, request, context):
        """Get all carrier bookings of a shipment."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FindCarrierBookingByDocumentableFid(self, request, context):
        """Find carrier booking by document fid."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CarrierBookingsAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "FindCarrierBookingByFid": grpc.unary_unary_rpc_method_handler(
            servicer.FindCarrierBookingByFid,
            request_deserializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByFidRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByFidResponse.SerializeToString,
        ),
        "ListCarrierBookingsByExecutionTaskFid": grpc.unary_unary_rpc_method_handler(
            servicer.ListCarrierBookingsByExecutionTaskFid,
            request_deserializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.ListCarrierBookingsByExecutionTaskFidRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.ListCarrierBookingsByExecutionTaskFidResponse.SerializeToString,
        ),
        "FindCarrierBookingByDocumentableFid": grpc.unary_unary_rpc_method_handler(
            servicer.FindCarrierBookingByDocumentableFid,
            request_deserializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByDocumentableFidRequest.FromString,
            response_serializer=flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByDocumentableFidResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.monolith.oceancarrierbooking.carrierbookings.v1beta1.CarrierBookingsAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class CarrierBookingsAPI:
    """This API will be deprecated soon in favor of OEX NIS, please do not add anything here."""

    @staticmethod
    def FindCarrierBookingByFid(
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
            "/flexport.monolith.oceancarrierbooking.carrierbookings.v1beta1.CarrierBookingsAPI/FindCarrierBookingByFid",
            flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByFidRequest.SerializeToString,
            flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByFidResponse.FromString,
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
    def ListCarrierBookingsByExecutionTaskFid(
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
            "/flexport.monolith.oceancarrierbooking.carrierbookings.v1beta1.CarrierBookingsAPI/ListCarrierBookingsByExecutionTaskFid",
            flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.ListCarrierBookingsByExecutionTaskFidRequest.SerializeToString,
            flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.ListCarrierBookingsByExecutionTaskFidResponse.FromString,
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
    def FindCarrierBookingByDocumentableFid(
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
            "/flexport.monolith.oceancarrierbooking.carrierbookings.v1beta1.CarrierBookingsAPI/FindCarrierBookingByDocumentableFid",
            flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByDocumentableFidRequest.SerializeToString,
            flexport_dot_monolith_dot_oceancarrierbooking_dot_carrierbookings_dot_v1beta1_dot_carrier__bookings__api__pb2.FindCarrierBookingByDocumentableFidResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )