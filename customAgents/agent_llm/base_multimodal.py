from colorama import Fore, Style
from typing import Any, List, Union
from PIL import Image
from customAgents.agent_llm.type_utils import agent_multimodal_type
import google.generativeai as genai


@agent_multimodal_type
class BaseMultiModal:
    def __init__(
            self,
            api_key: str,
            model: str,
            temperature: float = 0.7,
            safety_settings: Any = None,
            max_output_tokens: int = 1024
        ):
        
        self._api_key = api_key
        self._model = model
        self._temperature = temperature
        self._safety_settings = safety_settings
        self._max_output_tokens = max_output_tokens
        self._multi_modal = self._initialize_multimodal()

    def _initialize_multimodal(self):
        if self._model.startswith("gemini"):  # Google models
            genai.configure(api_key=self._api_key, transport="rest")
            return genai.GenerativeModel(
                model_name=self._model,
                generation_config={
                    "temperature": self._temperature,
                    "max_output_tokens": self._max_output_tokens,
                },
                safety_settings=self._safety_settings
            )
        else:
            raise ValueError('Model not supported. Currently supported models: gemini')

    def multimodal_generate(self, prompt: Union[str, List[Union[str, Any]]], stream: bool = False, output_style: str = 'default') -> str:
        if isinstance(prompt, str):
            prompt = [prompt]
        
        response = self._multi_modal.generate_content(prompt, stream=stream)
        
        if stream:
            return self._handle_stream_response(response, output_style)
        else:
            response.resolve()
            return response.text

    def _handle_stream_response(self, response, output_style: str) -> str:
        chunks = []
        for chunk in response:
            if chunk.text:
                if output_style != 'default':
                    self._print_colorized_output(chunk=chunk.text, output_style=output_style)
                chunks.append(chunk.text)
        return ''.join(chunks)

    def _print_colorized_output(self, chunk: str, output_style: str) -> None:
        """
        Method for customizing output color

        :param chunk: the output that needs to be printed.
        :param output_style: the color of the output.
        """
        allowed_styles = self.available_text_colors

        if output_style not in allowed_styles:
            raise ValueError(f"Invalid output style. Choose from {allowed_styles}")

        color_map = {
            "default": "",
            "green": Fore.LIGHTGREEN_EX,
            "blue": Fore.LIGHTBLUE_EX,
            "yellow": Fore.LIGHTYELLOW_EX,
            "cyan": Fore.LIGHTCYAN_EX,
            "red": Fore.LIGHTRED_EX,
            "magenta": Fore.LIGHTMAGENTA_EX
        }

        print(f"{color_map[output_style]}{chunk}{Style.RESET_ALL}", end='', flush=True)

    def __str__(self) -> str:
        multimodal_initialized = self._multi_modal is not None
        return f"Model used: {self._model}, with temperature: {self._temperature}, multimodal initialized: {multimodal_initialized}"

    @property
    def multimodal(self) -> Any:
        return self._multi_modal

    @property
    def available_text_colors(self) -> List[str]:
        return ['default', 'green', 'blue', 'yellow', 'cyan', 'red', 'magenta']

    def set_temperature(self, temperature: float) -> None:
        """
        Set a new temperature for the model.

        :param temperature: The new temperature value (0.0 to 1.0).
        """
        if 0.0 <= temperature <= 1.0:
            self._temperature = temperature
            self._multi_modal = self._initialize_multimodal()
        else:
            raise ValueError("Temperature must be between 0.0 and 1.0")

    def set_max_output_tokens(self, max_tokens: int) -> None:
        """
        Set a new maximum output token limit.

        :param max_tokens: The new maximum number of output tokens.
        """
        if max_tokens > 0:
            self._max_output_tokens = max_tokens
            self._multi_modal = self._initialize_multimodal()
        else:
            raise ValueError("Max output tokens must be a positive integer")