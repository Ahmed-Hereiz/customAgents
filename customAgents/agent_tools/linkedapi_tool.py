from customAgents.agent_tools import BaseTool

class LinkedINApiTool(BaseTool):
    def __init__(self, description: str, tool_name: str = None):
        super().__init__(description, tool_name)