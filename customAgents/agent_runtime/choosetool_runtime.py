from typing import Any
from customAgents.agent_runtime import BaseRuntime


class ChooseToolRuntime(BaseRuntime):
    def __init__(self, llm: Any, prompt: Any, toolkit: Any):
        
        super().__init__(llm, prompt, toolkit)

        self.prompt.prompt = "sepecify how to use tools"


    def step(self) -> str:
        return super().step()
    

    def loop(self, n_steps: int = 1) -> str:
        return super().loop(n_steps)