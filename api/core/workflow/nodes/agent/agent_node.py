from ast import literal_eval
from collections.abc import Generator, Mapping, Sequence
from typing import Any, cast

from core.agent.entities import AgentToolEntity
from core.agent.plugin_entities import AgentStrategyParameter
from core.model_manager import ModelManager
from core.model_runtime.entities.model_entities import ModelType
from core.plugin.manager.exc import PluginDaemonClientSideError
from core.plugin.manager.plugin import PluginInstallationManager
from core.tools.entities.tool_entities import ToolProviderType
from core.tools.tool_manager import ToolManager
from core.workflow.entities.node_entities import NodeRunResult
from core.workflow.entities.variable_pool import VariablePool
from core.workflow.enums import SystemVariableKey
from core.workflow.nodes.agent.entities import AgentNodeData
from core.workflow.nodes.base.entities import BaseNodeData
from core.workflow.nodes.enums import NodeType
from core.workflow.nodes.event.event import RunCompletedEvent
from core.workflow.nodes.tool.tool_node import ToolNode
from core.workflow.utils.variable_template_parser import VariableTemplateParser
from factories.agent_factory import get_plugin_agent_strategy
from models.workflow import WorkflowNodeExecutionStatus


class AgentNode(ToolNode):
    """
    Agent Node
    """

    _node_data_cls = AgentNodeData  # type: ignore
    _node_type = NodeType.AGENT

    def _run(self) -> Generator:
        """
        Run the agent node
        """
        node_data = cast(AgentNodeData, self.node_data)

        try:
            strategy = get_plugin_agent_strategy(
                tenant_id=self.tenant_id,
                agent_strategy_provider_name=node_data.agent_strategy_provider_name,
                agent_strategy_name=node_data.agent_strategy_name,
            )
        except Exception as e:
            yield RunCompletedEvent(
                run_result=NodeRunResult(
                    status=WorkflowNodeExecutionStatus.FAILED,
                    inputs={},
                    error=f"Failed to get agent strategy: {str(e)}",
                )
            )
            return

        agent_parameters = strategy.get_parameters()

        # get parameters
        parameters = self._generate_agent_parameters(
            agent_parameters=agent_parameters,
            variable_pool=self.graph_runtime_state.variable_pool,
            node_data=node_data,
        )
        parameters_for_log = self._generate_agent_parameters(
            agent_parameters=agent_parameters,
            variable_pool=self.graph_runtime_state.variable_pool,
            node_data=node_data,
            for_log=True,
        )

        # get conversation id
        conversation_id = self.graph_runtime_state.variable_pool.get(["sys", SystemVariableKey.CONVERSATION_ID])

        try:
            message_stream = strategy.invoke(
                params=parameters,
                user_id=self.user_id,
                app_id=self.app_id,
                conversation_id=conversation_id.text if conversation_id else None,
            )
        except Exception as e:
            yield RunCompletedEvent(
                run_result=NodeRunResult(
                    status=WorkflowNodeExecutionStatus.FAILED,
                    inputs=parameters_for_log,
                    error=f"Failed to invoke agent: {str(e)}",
                )
            )
            return

        try:
            # convert tool messages

            yield from self._transform_message(
                message_stream,
                {
                    "icon": self.agent_strategy_icon,
                    "agent_strategy": cast(AgentNodeData, self.node_data).agent_strategy_name,
                },
                parameters_for_log,
            )
        except PluginDaemonClientSideError as e:
            yield RunCompletedEvent(
                run_result=NodeRunResult(
                    status=WorkflowNodeExecutionStatus.FAILED,
                    inputs=parameters_for_log,
                    error=f"Failed to transform agent message: {str(e)}",
                )
            )

    def _generate_agent_parameters(
        self,
        *,
        agent_parameters: Sequence[AgentStrategyParameter],
        variable_pool: VariablePool,
        node_data: AgentNodeData,
        for_log: bool = False,
    ) -> dict[str, Any]:
        """
        Generate parameters based on the given tool parameters, variable pool, and node data.

        Args:
            agent_parameters (Sequence[AgentParameter]): The list of agent parameters.
            variable_pool (VariablePool): The variable pool containing the variables.
            node_data (AgentNodeData): The data associated with the agent node.

        Returns:
            Mapping[str, Any]: A dictionary containing the generated parameters.

        """
        agent_parameters_dictionary = {parameter.name: parameter for parameter in agent_parameters}

        result: dict[str, Any] = {}
        for parameter_name in node_data.agent_parameters:
            parameter = agent_parameters_dictionary.get(parameter_name)
            if not parameter:
                result[parameter_name] = None
                continue
            agent_input = node_data.agent_parameters[parameter_name]
            if agent_input.type == "variable":
                variable = variable_pool.get(agent_input.value)  # type: ignore
                if variable is None:
                    raise ValueError(f"Variable {agent_input.value} does not exist")
                parameter_value = variable.value
            elif agent_input.type in {"mixed", "constant"}:
                segment_group = variable_pool.convert_template(str(agent_input.value))
                parameter_value = segment_group.log if for_log else segment_group.text
            else:
                raise ValueError(f"Unknown agent input type '{agent_input.type}'")
            value = parameter_value.strip()
            if (parameter_value.startswith("{") and parameter_value.endswith("}")) or (
                parameter_value.startswith("[") and parameter_value.endswith("]")
            ):
                value = literal_eval(parameter_value)  # transform string to python object
            if parameter.type == "array[tools]":
                value = cast(list[dict[str, Any]], value)
                value = [tool for tool in value if tool.get("enabled", False)]

            if not for_log:
                if parameter.type == "array[tools]":
                    value = cast(list[dict[str, Any]], value)
                    tool_value = []
                    for tool in value:
                        provider_type = ToolProviderType(tool.get("type", ToolProviderType.BUILT_IN.value))
                        entity = AgentToolEntity(
                            provider_id=tool.get("provider_name", ""),
                            provider_type=provider_type,
                            tool_name=tool.get("tool_name", ""),
                            tool_parameters=tool.get("parameters", {}),
                            plugin_unique_identifier=tool.get("plugin_unique_identifier", None),
                        )

                        extra = tool.get("extra", {})

                        tool_runtime = ToolManager.get_agent_tool_runtime(
                            self.tenant_id, self.app_id, entity, self.invoke_from
                        )
                        if tool_runtime.entity.description:
                            tool_runtime.entity.description.llm = (
                                extra.get("descrption", "") or tool_runtime.entity.description.llm
                            )

                        tool_value.append(
                            {
                                **tool_runtime.entity.model_dump(mode="json"),
                                "runtime_parameters": tool_runtime.runtime.runtime_parameters,
                                "provider_type": provider_type.value,
                            }
                        )
                    value = tool_value
                if parameter.type == "model-selector":
                    value = cast(dict[str, Any], value)
                    model_instance = ModelManager().get_model_instance(
                        tenant_id=self.tenant_id,
                        provider=value.get("provider", ""),
                        model_type=ModelType(value.get("model_type", "")),
                        model=value.get("model", ""),
                    )
                    models = model_instance.model_type_instance.plugin_model_provider.declaration.models
                    finded_model = next((model for model in models if model.model == value.get("model", "")), None)

                    value["entity"] = finded_model.model_dump(mode="json") if finded_model else None

            result[parameter_name] = value

        return result

    @classmethod
    def _extract_variable_selector_to_variable_mapping(
        cls,
        *,
        graph_config: Mapping[str, Any],
        node_id: str,
        node_data: BaseNodeData,
    ) -> Mapping[str, Sequence[str]]:
        """
        Extract variable selector to variable mapping
        :param graph_config: graph config
        :param node_id: node id
        :param node_data: node data
        :return:
        """
        node_data = cast(AgentNodeData, node_data)
        result: dict[str, Any] = {}
        for parameter_name in node_data.agent_parameters:
            input = node_data.agent_parameters[parameter_name]
            if input.type in ["mixed", "constant"]:
                selectors = VariableTemplateParser(str(input.value)).extract_variable_selectors()
                for selector in selectors:
                    result[selector.variable] = selector.value_selector
            elif input.type == "variable":
                result[parameter_name] = input.value

        result = {node_id + "." + key: value for key, value in result.items()}

        return result

    @property
    def agent_strategy_icon(self) -> str | None:
        """
        Get agent strategy icon
        :return:
        """
        manager = PluginInstallationManager()
        plugins = manager.list_plugins(self.tenant_id)
        try:
            current_plugin = next(
                plugin
                for plugin in plugins
                if f"{plugin.plugin_id}/{plugin.name}"
                == cast(AgentNodeData, self.node_data).agent_strategy_provider_name
            )
            icon = current_plugin.declaration.icon
        except StopIteration:
            icon = None
        return icon