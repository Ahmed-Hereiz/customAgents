from customAgents.agent_prompt import BasePrompt
from typing import Union
from PIL import Image


class PlaceHoldersPrompt(BasePrompt):
    def __init__(self, placeholders: dict = {}, prompt_string: str = "", img: Union[str, Image.Image, None] = None):

        self.placeholders = placeholders

        super().__init__(prompt_string=prompt_string, img=img)

        self.prompt = self._generate_prompt()
        self.img = self._load_image(img)

    def _generate_prompt(self):

        prompt = self.prompt_string

        for replace in self.placeholders.keys():
            prompt = prompt.replace(replace, self.placeholders[replace])

        if self.img:
            prompt += "\n\nNote: An image is provided with this prompt. Consider it in your response if relevant."

        return prompt
