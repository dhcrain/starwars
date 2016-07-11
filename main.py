import requests
import re
import time
from playsound import playsound


def print_results(response, dict_key):
    for item in response['results']:
        # get the number out of the URL, http://stackoverflow.com/questions/26825729/extract-number-from-string-python
        item_url = int(re.findall("\d+", item['url'])[0])
        print("{}: {}".format(item_url, item[dict_key]))

def print_details(response, responce_key1, response_key2):
    if response[responce_key1]:
        for item in response[responce_key1]:
            response = requests.get(item).json()
            print("-", response[response_key2])


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
                # url = ""
                # dict_key = 0
                # response = 0
                welcome()
                break

def welcome():
    choice = int(input("""
===============================================================
1: Characters       |   * To see more details about an item,
2: Films            |     get the index number from looking
3: Vehicles         |     at the lists in options 1, 2, & 3.
---------------------------------------------------------------
4: Character Detail             6: Vehicle Detail
5: Film Detail                  7: QUIT
===============================================================
"""))

    if choice == 7:
        exit()
    elif choice == 4:
        detail_pk = int(input("Enter item number to see details: "))
        url = "http://swapi.co/api/people/{}/".format(detail_pk)
        response = requests.get(url).json()
        print('Character Name: {}'.format(response['name']))
        # films
        responce_key1 = 'films'
        response_key2 = 'title'
        print("-Films:")
        print_details(response, responce_key1, response_key2)
        # Species
        responce_key1 = 'species'
        response_key2 = 'name'
        print("Species:")
        print_details(response, responce_key1, response_key2)
        # vehicles
        responce_key1 = 'vehicles'
        response_key2 = 'name'
        print("Vehicles:")
        print_details(response, responce_key1, response_key2)
        # Starships
        responce_key1 = 'starships'
        response_key2 = 'name'
        print("Starships:")
        print_details(response, responce_key1, response_key2)
        welcome()
    elif choice == 5:
        detail_pk = int(input("Enter item number to see details: "))
        url = "http://swapi.co/api/films/{}/".format(detail_pk)
        response = requests.get(url).json()
        print("""
Film Title: {}
Release Date: {}
Episode ID: {}
Director: {}
Opening:
        """.format(response['title'], response['release_date'], response['episode_id'], response['director']))
        playsound("Star_Wars.mp3")
        for line in response['opening_crawl'].split("\n"):
            print(line)
            time.sleep(.15)
        welcome()
    elif choice == 6:
        detail_pk = int(input("Enter item number to see details: "))
        url = "http://swapi.co/api/vehicles/{}/".format(detail_pk)
        response = requests.get(url).json()
        print("""
Vehicle Name: {}
Model: {}
Manufacturer: {}
Max Atmosphering Speed: {}""".format(response['name'], response['model'], response['manufacturer'], response['max_atmosphering_speed']))
        # films
        responce_key1 = 'films'
        response_key2 = 'title'
        print("Films: ")
        print_details(response, responce_key1, response_key2)
        welcome()
    elif choice in [1, 2, 3]:
        choice_dict = {
        1: ["http://swapi.co/api/people/", "name"],
        2: ["http://swapi.co/api/films/", "title"],
        3: ["http://swapi.co/api/vehicles/", "name"],
        }
        call_swapi(choice_dict[choice])

# http://www.pc-freak.net/ascii-art-pictures/star-wars/starwars_title.txt
print('''
     d888888888888888888  d8888b    8888888888b
     Y888888888888888888 d88PY88b   88888888888b
      Y888b    88888    ,88P  Y88.  888R    X88P
       Y888b   88888    d88'  `88b  8888bood88P
8888888888888b  88888   ,8888888888. 8888PY88888888888
8888888888888P  88888   888P    Y888 8888  Y8888888888
Y88b   d88b   d88P  d8888b    8888888888b  d8888888888
`888b d8888b d888' d88PY88b   88888888888b Y8888888888
Y888V888888V888P ,88P  Y88.  888R    X88P  Y888b
`888888PY888888' d88'  `88b  8888bood88P    Y888b
 Y8888P  Y8888P ,8888888888. 8888PY8SSt&cgmm88888b
  Y88P    Y88P  888P    Y888 8888  Y8888888888888P''')

while True:
    welcome()
