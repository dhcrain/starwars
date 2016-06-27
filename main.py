import requests

# url = "http://swapi.co/api/people/"
# response = requests.get(url).json()
# print(response)

# url = "http://swapi.co/api/people/"
# response = requests.get(url).json()
# for item in response['results']:
#     print(item['name'])

choice = int(input("""
Star Wars
1: Characters
2: Films
3: Vehicles
"""))

if choice == 1:
    url = "http://swapi.co/api/people/"
    response = requests.get(url).json()
    for item in response['results']:
        print(item['name'])

if choice == 2:
    url = "http://swapi.co/api/films/"
    response = requests.get(url).json()
    for item in response['results']:
        print(item['title'])

if choice == 3:
    url = "http://swapi.co/api/vehicles/"
    response = requests.get(url).json()
    for item in response['results']:
        print(item['name'])
