from customAgents.agent_prompt import BasePrompt
from typing import Union
from PIL import Image


class SimplePrompt(BasePrompt):
    def __init__(self, prompt_string: str = "", img: Union[str, Image.Image, None] = None):

        super().__init__(prompt_string, img)

        self.prompt = self._generate_prompt()
        self.img = self._load_image(img)
        
    def _generate_prompt(self):
        prompt = self.prompt_string

        if self.img:
            prompt += "\n\nNote: An image is provided with this prompt. Consider it in your response if relevant."

        return prompt