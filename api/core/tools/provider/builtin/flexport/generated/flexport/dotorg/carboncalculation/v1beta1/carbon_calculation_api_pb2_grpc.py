# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.dotorg.carboncalculation.v1beta1 import (
    carbon_calculation_api_pb2 as flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2,
)


class CarbonCalculationAPIStub:
    """The API for all carbon calulcations."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CalculateCarbonEmissions = channel.unary_unary(
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculateCarbonEmissions",
            request_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsRequest.SerializeToString,
            response_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsResponse.FromString,
        )
        self.CalculatePredictedCarbonEmissions = channel.unary_unary(
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculatePredictedCarbonEmissions",
            request_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculatePredictedCarbonEmissionsRequest.SerializeToString,
            response_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculatePredictedCarbonEmissionsResponse.FromString,
        )
        self.GetExecutionOrderCarbonEmissions = channel.unary_unary(
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/GetExecutionOrderCarbonEmissions",
            request_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderCarbonEmissionsRequest.SerializeToString,
            response_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderCarbonEmissionsResponse.FromString,
        )
        self.GetExecutionOrderLegCarbonEmissions = channel.unary_unary(
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/GetExecutionOrderLegCarbonEmissions",
            request_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderLegCarbonEmissionsRequest.SerializeToString,
            response_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderLegCarbonEmissionsResponse.FromString,
        )
        self.GetShipmentLegCarbonCalculatorRequestLegs = channel.unary_unary(
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/GetShipmentLegCarbonCalculatorRequestLegs",
            request_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetShipmentLegCarbonCalculatorRequestLegsRequest.SerializeToString,
            response_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetShipmentLegCarbonCalculatorRequestLegsResponse.FromString,
        )
        self.CalculateRequestLegCarbonEmissions = channel.unary_unary(
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculateRequestLegCarbonEmissions",
            request_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateRequestLegCarbonEmissionsRequest.SerializeToString,
            response_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateRequestLegCarbonEmissionsResponse.FromString,
        )
        self.CalculateDataPreparationRequestLeg = channel.unary_unary(
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculateDataPreparationRequestLeg",
            request_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateDataPreparationRequestLegRequest.SerializeToString,
            response_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateDataPreparationRequestLegResponse.FromString,
        )
        self.CalculateIpbCarbonEmissions = channel.unary_unary(
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculateIpbCarbonEmissions",
            request_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateIpbCarbonEmissionsRequest.SerializeToString,
            response_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateIpbCarbonEmissionsResponse.FromString,
        )
        self.CalculateCarbonEmissionsUsingOfferings = channel.unary_unary(
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculateCarbonEmissionsUsingOfferings",
            request_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsUsingOfferingsRequest.SerializeToString,
            response_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsUsingOfferingsResponse.FromString,
        )


class CarbonCalculationAPIServicer:
    """The API for all carbon calulcations."""

    def CalculateCarbonEmissions(self, request, context):
        """Calculate the carbon emissions given an execution order and execution plan."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CalculatePredictedCarbonEmissions(self, request, context):
        """Calculate the predicted carbon emissions given a transit execution offering and its shipment cargo."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetExecutionOrderCarbonEmissions(self, request, context):
        """Fetch the carbon emission data for an execution order."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetExecutionOrderLegCarbonEmissions(self, request, context):
        """Fetch leg-level carbon emission data for an execution order."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetShipmentLegCarbonCalculatorRequestLegs(self, request, context):
        """Fetch leg-level carbon emission data for a shipment."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CalculateRequestLegCarbonEmissions(self, request, context):
        """Calculates carbon emissions given a list of request legs."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CalculateDataPreparationRequestLeg(self, request, context):
        """Returns data preparation values for request legs."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CalculateIpbCarbonEmissions(self, request, context):
        """Returns data preparation values for request legs."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CalculateCarbonEmissionsUsingOfferings(self, request, context):
        """calculate carbon emissions using offerings"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CarbonCalculationAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CalculateCarbonEmissions": grpc.unary_unary_rpc_method_handler(
            servicer.CalculateCarbonEmissions,
            request_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsRequest.FromString,
            response_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsResponse.SerializeToString,
        ),
        "CalculatePredictedCarbonEmissions": grpc.unary_unary_rpc_method_handler(
            servicer.CalculatePredictedCarbonEmissions,
            request_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculatePredictedCarbonEmissionsRequest.FromString,
            response_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculatePredictedCarbonEmissionsResponse.SerializeToString,
        ),
        "GetExecutionOrderCarbonEmissions": grpc.unary_unary_rpc_method_handler(
            servicer.GetExecutionOrderCarbonEmissions,
            request_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderCarbonEmissionsRequest.FromString,
            response_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderCarbonEmissionsResponse.SerializeToString,
        ),
        "GetExecutionOrderLegCarbonEmissions": grpc.unary_unary_rpc_method_handler(
            servicer.GetExecutionOrderLegCarbonEmissions,
            request_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderLegCarbonEmissionsRequest.FromString,
            response_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderLegCarbonEmissionsResponse.SerializeToString,
        ),
        "GetShipmentLegCarbonCalculatorRequestLegs": grpc.unary_unary_rpc_method_handler(
            servicer.GetShipmentLegCarbonCalculatorRequestLegs,
            request_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetShipmentLegCarbonCalculatorRequestLegsRequest.FromString,
            response_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetShipmentLegCarbonCalculatorRequestLegsResponse.SerializeToString,
        ),
        "CalculateRequestLegCarbonEmissions": grpc.unary_unary_rpc_method_handler(
            servicer.CalculateRequestLegCarbonEmissions,
            request_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateRequestLegCarbonEmissionsRequest.FromString,
            response_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateRequestLegCarbonEmissionsResponse.SerializeToString,
        ),
        "CalculateDataPreparationRequestLeg": grpc.unary_unary_rpc_method_handler(
            servicer.CalculateDataPreparationRequestLeg,
            request_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateDataPreparationRequestLegRequest.FromString,
            response_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateDataPreparationRequestLegResponse.SerializeToString,
        ),
        "CalculateIpbCarbonEmissions": grpc.unary_unary_rpc_method_handler(
            servicer.CalculateIpbCarbonEmissions,
            request_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateIpbCarbonEmissionsRequest.FromString,
            response_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateIpbCarbonEmissionsResponse.SerializeToString,
        ),
        "CalculateCarbonEmissionsUsingOfferings": grpc.unary_unary_rpc_method_handler(
            servicer.CalculateCarbonEmissionsUsingOfferings,
            request_deserializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsUsingOfferingsRequest.FromString,
            response_serializer=flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsUsingOfferingsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class CarbonCalculationAPI:
    """The API for all carbon calulcations."""

    @staticmethod
    def CalculateCarbonEmissions(
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
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculateCarbonEmissions",
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsRequest.SerializeToString,
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsResponse.FromString,
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
    def CalculatePredictedCarbonEmissions(
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
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculatePredictedCarbonEmissions",
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculatePredictedCarbonEmissionsRequest.SerializeToString,
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculatePredictedCarbonEmissionsResponse.FromString,
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
    def GetExecutionOrderCarbonEmissions(
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
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/GetExecutionOrderCarbonEmissions",
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderCarbonEmissionsRequest.SerializeToString,
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderCarbonEmissionsResponse.FromString,
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
    def GetExecutionOrderLegCarbonEmissions(
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
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/GetExecutionOrderLegCarbonEmissions",
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderLegCarbonEmissionsRequest.SerializeToString,
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetExecutionOrderLegCarbonEmissionsResponse.FromString,
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
    def GetShipmentLegCarbonCalculatorRequestLegs(
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
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/GetShipmentLegCarbonCalculatorRequestLegs",
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetShipmentLegCarbonCalculatorRequestLegsRequest.SerializeToString,
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.GetShipmentLegCarbonCalculatorRequestLegsResponse.FromString,
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
    def CalculateRequestLegCarbonEmissions(
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
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculateRequestLegCarbonEmissions",
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateRequestLegCarbonEmissionsRequest.SerializeToString,
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateRequestLegCarbonEmissionsResponse.FromString,
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
    def CalculateDataPreparationRequestLeg(
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
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculateDataPreparationRequestLeg",
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateDataPreparationRequestLegRequest.SerializeToString,
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateDataPreparationRequestLegResponse.FromString,
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
    def CalculateIpbCarbonEmissions(
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
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculateIpbCarbonEmissions",
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateIpbCarbonEmissionsRequest.SerializeToString,
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateIpbCarbonEmissionsResponse.FromString,
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
    def CalculateCarbonEmissionsUsingOfferings(
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
            "/flexport.dotorg.carboncalculation.v1beta1.CarbonCalculationAPI/CalculateCarbonEmissionsUsingOfferings",
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsUsingOfferingsRequest.SerializeToString,
            flexport_dot_dotorg_dot_carboncalculation_dot_v1beta1_dot_carbon__calculation__api__pb2.CalculateCarbonEmissionsUsingOfferingsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )