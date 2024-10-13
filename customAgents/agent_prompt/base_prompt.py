from PIL import Image
from typing import Union
import os


class BasePrompt:
    def __init__(self, prompt_string: str = "", img: Union[str, Image.Image, None] = None):
        """
        Initializes the BasePrompt with the given template file and prompt string.

        :param prompt_string: The prompt string to be used.
        :param img: An optional image to be associated with the prompt. Can be a file path or a PIL Image object.
        """

        self.prompt_string = prompt_string
        self.prompt = self._generate_prompt()
        self.img = self._load_image(img)
        

    def _generate_prompt(self):
        """
        method for interfacing with runtime (used inside the runtime class), setting default to use prompt_string,
        but this needs to overwritten inside every inherited class for being customizable for the use case.
        """

        return self.prompt_string

    def _load_image(self, img: Union[str, Image.Image, None]) -> Union[Image.Image, None]:
        """
        Loads an image from a file path or returns the PIL Image object if already loaded.

        :param img: A file path to an image or a PIL Image object.
        :return: A PIL Image object or None if no image is provided.
        """
        if isinstance(img, str) and os.path.isfile(img):
            return Image.open(img)
        elif isinstance(img, Image.Image):
            return img
        return None

    def __repr__(self) -> str:
        """
        Returns a string representation of the BasePrompt instance for debugging.

        :return: A string representation of the instance.
        """
        return f"model prompt initialized with {self.prompt}"


    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the BasePrompt instance.

        :return: A string representation of the instance.
        """
        return f"model prompt initialized with {self.prompt}"


    def __add__(self, other) -> str:
        """
        Concatenates the prompt string of this instance with another BasePrompt instance.

        :param other: Another BasePrompt instance.
        :return: The concatenated prompt strings.
        """
        return self.prompt + '\n' + other.prompt

    def replace_placeholder(self, placeholder: str, value: str):
        """
        Replaces a placeholder in the prompt string with a given value.

        :param placeholder: The placeholder string to be replaced.
        :param value: The value to replace the placeholder with.
        """
        self.prompt = self.prompt.replace(placeholder, value)
        self.prompt_string = self.prompt_string.replace(placeholder, value)

    def append_to_prompt(self, additional_text: str):
        """
        Appends additional text to the end of the prompt.

        :param additional_text: The text to be appended to the prompt.
        """
        self.prompt += '\n' + additional_text
        self.prompt_string += '\n' + additional_text

    def prepend_to_prompt(self, additional_text: str):
        """
        Prepends additional text to the beginning of the prompt.

        :param additional_text: The text to be prepended to the prompt.
        """
        self.prompt = additional_text + '\n' + self.prompt
        self.prompt_string = additional_text + '\n' + self.prompt_string

    def clear_prompt(self):
        """
        Clears the current prompt, resetting it to an empty string.
        """
        self.prompt = ""
        self.prompt_string = ""

    def set_image(self, img: Union[str, Image.Image]):
        """
        Sets or updates the image associated with the prompt.

        :param img: The image to be associated with the prompt. Can be a file path or a PIL Image object.
        """
        self.img = self._load_image(img)
