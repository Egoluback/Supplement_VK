import requests, json

URL = 'https://models.dobro.ai/gpt2/medium/'

DATASETS = ["data/dataset_PrestuplenieINakazanye.txt", "data/dataset_Kolobok.txt"]

def get_sample(text):
    response = requests.post(URL, json={"prompt": text, "length": 50})
    return json.loads(response.text)["replies"][0]