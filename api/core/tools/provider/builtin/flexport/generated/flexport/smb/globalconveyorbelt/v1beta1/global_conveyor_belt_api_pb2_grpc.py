# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.smb.globalconveyorbelt.v1beta1 import (
    global_conveyor_belt_api_pb2 as flexport_dot_smb_dot_globalconveyorbelt_dot_v1beta1_dot_global__conveyor__belt__api__pb2,
)


class GlobalConveyorBeltAPIStub:
    """API for global conveyor belt data"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGcbOfferingsForRfq = channel.unary_unary(
            "/flexport.smb.globalconveyorbelt.v1beta1.GlobalConveyorBeltAPI/GetGcbOfferingsForRfq",
            request_serializer=flexport_dot_smb_dot_globalconveyorbelt_dot_v1beta1_dot_global__conveyor__belt__api__pb2.GetGcbOfferingsForRfqRequest.SerializeToString,
            response_deserializer=flexport_dot_smb_dot_globalconveyorbelt_dot_v1beta1_dot_global__conveyor__belt__api__pb2.GetGcbOfferingsForRfqResponse.FromString,
        )


class GlobalConveyorBeltAPIServicer:
    """API for global conveyor belt data"""

    def GetGcbOfferingsForRfq(self, request, context):
        """Find gcb offerings for quote request."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_GlobalConveyorBeltAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetGcbOfferingsForRfq": grpc.unary_unary_rpc_method_handler(
            servicer.GetGcbOfferingsForRfq,
            request_deserializer=flexport_dot_smb_dot_globalconveyorbelt_dot_v1beta1_dot_global__conveyor__belt__api__pb2.GetGcbOfferingsForRfqRequest.FromString,
            response_serializer=flexport_dot_smb_dot_globalconveyorbelt_dot_v1beta1_dot_global__conveyor__belt__api__pb2.GetGcbOfferingsForRfqResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.smb.globalconveyorbelt.v1beta1.GlobalConveyorBeltAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class GlobalConveyorBeltAPI:
    """API for global conveyor belt data"""

    @staticmethod
    def GetGcbOfferingsForRfq(
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
            "/flexport.smb.globalconveyorbelt.v1beta1.GlobalConveyorBeltAPI/GetGcbOfferingsForRfq",
            flexport_dot_smb_dot_globalconveyorbelt_dot_v1beta1_dot_global__conveyor__belt__api__pb2.GetGcbOfferingsForRfqRequest.SerializeToString,
            flexport_dot_smb_dot_globalconveyorbelt_dot_v1beta1_dot_global__conveyor__belt__api__pb2.GetGcbOfferingsForRfqResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )