from customAgents.agent_prompt import BasePrompt
from typing import Union
from PIL import Image


class ChooseToolsPrompt(BasePrompt):
    def __init__(self, task: str, prompt_string: str = "", img: Union[str, Image.Image, None] = None):
        self.task = task
        super().__init__(prompt_string, img)
        self.prompt = self._generate_prompt()

    def _generate_prompt(self):
        choose_tools_prompt = """
{prompt_string}
You are an LLM tool user expert. Your task is to choose the most useful tools to solve this task:
{task}

The available tools you have:
{tools}
"""

        choose_tools_prompt = choose_tools_prompt.format(
            prompt_string=self.prompt_string,
            task=self.task,
            tools="{tools}"  # Placeholder for tools, to be filled later
        )

        if self.img:
            choose_tools_prompt += "\n\nNote: An image is provided with this prompt. Consider visual analysis tools if they might be relevant to the task."

        return choose_tools_prompt

    def set_tools(self, tools: str):
        """
        Set the available tools after initialization.
        
        :param tools: A string containing the list of available tools.
        """
        self.prompt = self.prompt.replace("{tools}", tools)
