import requests

url = "http://swapi.co/api/species/1/"

response = requests.get(url).json()

print(response)
