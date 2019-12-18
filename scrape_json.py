import pandas as pd
import requests

url = 'https://api.github.com/orgs/fedora-infra/repos'
resp = requests.get(url)

data = pd.read_json(resp.text)

def get_total_forks(data):
    return sum(data.forks)

total_forks = get_total_forks(data)

print(total_forks)