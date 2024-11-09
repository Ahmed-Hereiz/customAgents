from customAgents.agent_prompt import BasePrompt, SimplePrompt, ReActPrompt
from customAgents.agent_llm import BaseMultiModal
from PIL import Image
import numpy as np
from pydub import AudioSegment
import os
import json

with open("../config/llm.json", "r") as f:
    llm_config = json.load(f)

mp3_file_path = "/home/ahmed-hereiz/self/customAgents/tests/crowd-talking-138493.mp3"
audio = AudioSegment.from_mp3(mp3_file_path)
audio = audio[:200]  
# print(audio)

width, height = 100, 100
red_color = (255, 0, 0)  
image = Image.new('RGB', (width, height), color=red_color)

# multimodal = BaseMultiModal(api_key=llm_config["api_key"],model=llm_config["model"])
# prompt = BasePrompt(text="what is in this audio?", audio=audio)
# prompt.construct_prompt()

# print(multimodal.multimodal_generate(prompt.prompt, audio=audio))

import google.generativeai as genai
import pathlib

genai.configure(api_key=llm_config["api_key"])
model = genai.GenerativeModel(llm_config["model"])

myfile = genai.upload_file(mp3_file_path)
print(f"{myfile=}")

# prompt = "can you relate this image to the audio?"
# response = model.generate_content([
#     prompt,image,myfile,
#     # {
#     #     "mime_type": "audio/mp3",
#     #     "data": pathlib.Path(mp3_file_path).read_bytes()
#     # },
# ])

# print(response.text)