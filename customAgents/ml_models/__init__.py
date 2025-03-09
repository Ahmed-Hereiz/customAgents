from .base_models import BaseModels
from .gradioclient_models import GradioClientModels
from .huggingface_models import (
    HFModels,
    HFTxt2ImgModels,
    HFImg2ImgModels,
    HFImg2TxtModels,
    HFTxt2SpeechModels,
    HFSpeech2TxtModels
)
from .sklearn_models import SklearnModels



__all__ = [
    'BaseModels',
    'HFModels',
    'HFTxt2ImgModels',
    'HFImg2ImgModels',
    'HFImg2TxtModels',
    'HFTxt2SpeechModels',
    'HFSpeech2TxtModels',
    'GradioClientModels',
    "SklearnModels"
]

__name__ = "customAgents.ml_models"

__package__ = "customAgents"

__file__ = __file__

__path__ = __path__

__version__ = "1.0.0"  
