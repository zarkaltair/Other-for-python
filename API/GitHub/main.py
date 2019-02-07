import requests

from pprint import pprint


url = 'https://api.github.com/users/zarkaltair'

response = requests.get(url).json()

pprint(response)