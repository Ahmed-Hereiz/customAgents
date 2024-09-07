import requests
from PIL import Image
from io import BytesIO

HUGGING_FACE_TOKEN = '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'
API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"

headers = {
    "Authorization": f"Bearer {HUGGING_FACE_TOKEN}"
}

data = {
    "inputs": "A beautiful sunset over the mountains."
}
response = requests.post(API_URL, headers=headers, json=data)

if response.status_code == 200:
    with open("generated_image.png", "wb") as f:
        f.write(response.content)
    img = Image.open('generated_image.png')
    img.show()
else:
    print(f"Error: {response.status_code}, {response.text}")

img = Image.open(BytesIO(response.content))
img.show()
print(img)
# API_URL = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech"
# headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}

# data = {"inputs": "let's find the best way to make AI agents, start by reading this documment then I will till you what to do then, by the way my name is ahmed hany hereiz and iam machine learning engineer, what is the max context length do you think for this llm ? do you thing will it be enough to read  long text like this one I have provided or may it need something more small ? let's see"}
# response = requests.post(API_URL, headers=headers, json=data)

# if response.status_code == 200:
#     with open("speech.wav", "wb") as f:
#         f.write(response.content)
# else:
#     print(f"Error: {response.status_code}, {response.text}")