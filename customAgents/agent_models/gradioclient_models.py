from customAgents.agent_models import BaseModels
from gradio_client import Client


class GradioClientModels(BaseModels):
    def __init__(self, gradio_client_id : str, api_name : str = None):
        
        self.client = Client(gradio_client_id)
        self.api_name = api_name

        super().__init__()

    def inference(self, input_prompt):

        return self.client.predict(
            input_prompt,
            api_name=self.api_name
        )