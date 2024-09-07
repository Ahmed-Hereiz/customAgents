import requests
from PIL import Image
from io import BytesIO
from customAgents.agent_models import BaseModels


class HFModels(BaseModels):
    def __init__(self, hugging_face_token: str, model_api_url: str):
        
        self._hugging_face_token = hugging_face_token
        self._model_api_url = model_api_url
        self._headers = {"Authorization": f"Bearer {self._hugging_face_token}"}

        super().__init__()

    def inference(self, input_dict: dict):

        response = requests.post(self._hugging_face_token, headers=self._headers, json=input_dict)
        
        if response.status_code == 200:
            return response.content
        else: 
            raise ValueError(f"Error: {response.status_code}, {response.text}")


class HFStableDiffusionModels(HFModels):
    def __init__(self, hugging_face_token: str, model_id: str="CompVis/stable-diffusion-v1-4"):

        stable_diffusion_api_url = f"https://api-inference.huggingface.co/models/{model_id}"

        super().__init__(hugging_face_token=hugging_face_token, model_api_url=stable_diffusion_api_url)


    def inference(self, inputs: str):

        data = {"inputs": f"{inputs}"}
        response = requests.post(self._model_api_url, headers=self._headers, json=data)

        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            raise ValueError(f"Error: {response.status_code}, {response.text}")
        
    
    @property
    def get_diffusion_model_names(self) -> list:
        return [
            'CompVis/stable-diffusion-v1-4',
            'CompVis/stable-diffusion-v1-3',
            'CompVis/stable-diffusion-v1-2',
            'CompVis/stable-diffusion-v1-1',
        ]
    

