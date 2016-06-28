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
      Y88P    Y88P  888P    Y888 8888  Y8888888888888P
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
