import requests, json

URL = 'https://models.dobro.ai/gpt2/medium/'

DATASETS = ["data/datasetPrestuplenie_i_nakazanye.txt"]

def get_sample(text):
    response = requests.post(URL, json={"prompt": text, "length": 50})
    return json.loads(response.text)["replies"][0]