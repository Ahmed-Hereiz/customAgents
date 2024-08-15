from typing import Any
from customAgents.agent_tools import BaseTool

class LinkedINApiTool(BaseTool):
    def __init__(self, description: str, tool_name: str = None):
        super().__init__(description, tool_name)

    def execute_func(self, *params: Any) -> Any:
        """Needs to be customized !!"""

        return super().execute_func(*params)