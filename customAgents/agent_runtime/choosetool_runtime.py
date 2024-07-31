from customAgents.agent_runtime import BaseRuntime
from customAgents.agent_llm import BaseLLM
from customAgents.agent_prompt import BasePrompt
from customAgents.agent_tools import ToolKit


class ChooseToolRuntime(BaseRuntime):
    def __init__(self, llm: BaseLLM, prompt: BasePrompt, toolkit: ToolKit):
        
        super().__init__(llm, prompt, toolkit)

        self.prompt.prompt = "sepecify how to use tools"


    def step(self) -> str:
        return super().step()
    

    def loop(self, n_steps: int = 1) -> str:
        return super().loop(n_steps)