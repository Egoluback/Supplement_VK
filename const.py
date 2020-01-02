import requests, json, random

TOKEN = '47bbb34e7a81b4d1ce62dd3a4e6fbfdc9e29c6c7d6dac8a0a09b61bb3a70a4c68ae3afd50d98446f7d6ae'
PUBLIC_ID = 190299951

URL_MED = 'https://models.dobro.ai/gpt2/medium/'
URL_POET = 'https://models.dobro.ai/gpt2_poetry/'

DATASETS = ["data/dataset_PrestuplenieINakazanye.txt", "data/dataset_Kolobok.txt"]

def get_sample(text):
    url = URL_MED
    if (len(text) < 50):
        if (random.randint(1, 2) == 1): url = URL_POET
    response = requests.post(url, json={"prompt": text, "length": 50})
    return json.loads(response.text)["replies"][0]