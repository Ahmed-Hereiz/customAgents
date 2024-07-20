from typing import Any
from customAgents.agent_runtime import BaseRuntime


class SimpleRuntime(BaseRuntime):
    def __init__(self, llm: Any, prompt: Any):
        """Uses default BaseRuntime step and loop methods"""
        super().__init__(llm=llm, prompt=prompt, toolkit=[])


