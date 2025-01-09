from typing import Any, Literal, Union

from pydantic import BaseModel

from core.tools.entities.tool_entities import ToolSelector
from core.workflow.nodes.base.entities import BaseNodeData


class AgentNodeData(BaseNodeData):
    agent_strategy_provider_name: str  # redundancy
    agent_strategy_name: str
    agent_strategy_label: str  # redundancy

    class AgentInput(BaseModel):
        value: Union[list[str], list[ToolSelector], Any]
        type: Literal["mixed", "variable", "constant"]

    agent_parameters: dict[str, AgentInput]