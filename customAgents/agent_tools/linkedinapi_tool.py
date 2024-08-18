from typing import Any
from customAgents.agent_tools import BaseTool

class LinkedINApiTool(BaseTool):
    def __init__(self, linkedin_api_key: str, description: str, tool_name: str = None):
        super().__init__(description, tool_name)

        self.linkedin_api_key = linkedin_api_key

    def execute_func(self, *params: Any) -> Any:
        """Needs to be customized !!"""

        return super().execute_func(*params)