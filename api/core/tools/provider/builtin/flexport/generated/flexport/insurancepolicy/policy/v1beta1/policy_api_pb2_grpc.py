# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
from flexport.insurancepolicy.policy.v1beta1 import (
    policy_api_pb2 as flexport_dot_insurancepolicy_dot_policy_dot_v1beta1_dot_policy__api__pb2,
)


class PolicyAPIStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpsertPerShipmentPolicy = channel.unary_unary(
            "/flexport.insurancepolicy.policy.v1beta1.PolicyAPI/UpsertPerShipmentPolicy",
            request_serializer=flexport_dot_insurancepolicy_dot_policy_dot_v1beta1_dot_policy__api__pb2.UpsertPerShipmentPolicyRequest.SerializeToString,
            response_deserializer=flexport_dot_insurancepolicy_dot_policy_dot_v1beta1_dot_policy__api__pb2.UpsertPerShipmentPolicyResponse.FromString,
        )


class PolicyAPIServicer:
    """Missing associated documentation comment in .proto file."""

    def UpsertPerShipmentPolicy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PolicyAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "UpsertPerShipmentPolicy": grpc.unary_unary_rpc_method_handler(
            servicer.UpsertPerShipmentPolicy,
            request_deserializer=flexport_dot_insurancepolicy_dot_policy_dot_v1beta1_dot_policy__api__pb2.UpsertPerShipmentPolicyRequest.FromString,
            response_serializer=flexport_dot_insurancepolicy_dot_policy_dot_v1beta1_dot_policy__api__pb2.UpsertPerShipmentPolicyResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexport.insurancepolicy.policy.v1beta1.PolicyAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.


class PolicyAPI:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpsertPerShipmentPolicy(
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
            "/flexport.insurancepolicy.policy.v1beta1.PolicyAPI/UpsertPerShipmentPolicy",
            flexport_dot_insurancepolicy_dot_policy_dot_v1beta1_dot_policy__api__pb2.UpsertPerShipmentPolicyRequest.SerializeToString,
            flexport_dot_insurancepolicy_dot_policy_dot_v1beta1_dot_policy__api__pb2.UpsertPerShipmentPolicyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )