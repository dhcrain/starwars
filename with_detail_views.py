import requests
import re

def print_results(response, dict_key):
    for item in response['results']:
        # get the number out of the URL, http://stackoverflow.com/questions/26825729/extract-number-from-string-python
        item_url = int(re.findall("\d+", item['url'])[0])
        print("{}: {}".format(item_url, item[dict_key]))

def call_swapi(data):
    url, dict_key = data
    response = requests.get(url).json()
    print_results(response, dict_key)
    if response['next']:
        while response['next']:
            more = input("Do you want to see more? Y/n \n").lower()
            if more != "n":
                url = response['next']
                response = requests.get(url).json()
                print_results(response, dict_key)
            else:
                exit()

choice = int(input("""
Star Wars
1: Characters
2: Films
3: Vehicles
================================================
To see more details about an item get the number
from looking at the lists in 1, 2, and 3.
------------------------------------------------
4: Character Detail
5: Film Detail
6: Vehicle Detail
7: QUIT
"""))

if choice == 7:
    exit()
if choice == 4:
    detail_pk = int(input("Enter item number to see details: "))
    url = "http://swapi.co/api/people/{}/".format(detail_pk)
    response = requests.get(url).json()
    print("""
    Name: {}
    Films: {}
    Species: {}
    Vehicles: {}
    Starships: {}
    """.format(response['name'], response['films'], response['species'], response['vehicles'], response['starships']))
if choice == 5:
    detail_pk = int(input("Enter item number to see details: "))
    url = "http://swapi.co/api/films/{}/".format(detail_pk)
    response = requests.get(url).json()
    print("""
    Title: {}
    Release Date: {}
    Episode ID: {}
    Director: {}
    Opening: \n\n{}
    """.format(response['title'], response['release_date'], response['episode_id'], response['director'], response['opening_crawl']))
if choice == 6:
    detail_pk = int(input("Enter item number to see details: "))
    url = "http://swapi.co/api/vehicles/{}/".format(detail_pk)
    response = requests.get(url).json()
    print("""
    Name: {}
    Model: {}
    Manufacturer: {}
    Max Atmosphering Speed: {}
    Films: {}
    """.format(response['name'], response['model'], response['manufacturer'], response['max_atmosphering_speed'], response['films']))
else:
    choice_dict = {
    1: ["http://swapi.co/api/people/", "name"],
    2: ["http://swapi.co/api/films/", "title"],
    3: ["http://swapi.co/api/vehicles/", "name"],
    }
    call_swapi(choice_dict[choice])
