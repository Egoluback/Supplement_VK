import requests, json, random

TOKEN = 'YOUR_TOKEN'
PUBLIC_ID = 0

URL_MED = 'https://models.dobro.ai/gpt2/medium/'
URL_POET = 'https://models.dobro.ai/gpt2_poetry/'

DATASETS = ["data/dataset_PrestuplenieINakazanye.txt", "data/dataset_Kolobok.txt"]

def get_sample(text):
    url = URL_MED
    if (len(text) < 50):
        if (random.randint(1, 2) == 1): url = URL_POET
    response = requests.post(url, json={"prompt": text, "length": 50})
    return json.loads(response.text)["replies"][0]
