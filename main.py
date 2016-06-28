# Uses Star Wars api from http://swapi.co/
import requests
import re

def print_results(response, dict_key):
    for item in response['results']:
        # get the number out of the URL, http://stackoverflow.com/questions/26825729/extract-number-from-string-python
        item_url = int(re.findall("\d+", item['url'])[0])
        print("{}: {}".format(item_url, item[dict_key]))

def detail_more_menu():
    ask = (input("""
    Number for details
    See more entries (Y)
    Main Menu (N) """)).lower()
    return ask

def call_swapi(data):
    url, dict_key = data
    response = requests.get(url).json()
    print_results(response, dict_key)
    detail_choice = detail_more_menu()
    if response['next']:
        if detail_choice == "y":
            # while response['next']:
            url = response['next']
            response = requests.get(url).json()
            print_results(response, dict_key)
            detail_choice = detail_more_menu()
            detail_more_menu()
            if detail_choice == "n":
                welcome()
            if detail_choice == "y":
                call_swapi(data)
            else:
                detail_choice = int(detail_choice)
                url = "{}{}/".format(url, detail_choice)
                response = requests.get(url).json()
                print(response['name'])

        if detail_choice == "n":
            welcome()
        else:   # catches a number input
            detail_choice = int(detail_choice)
            url = "{}{}/".format(url, detail_choice)
            response = requests.get(url).json()
            print(response['name'])
    else:
        print_results(response, dict_key)
        # need the detail ask func here, when I make it....

def welcome():
    # http://www.pc-freak.net/ascii-art-pictures/star-wars/starwars_title.txt
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
What information would you like to see?
=========================================================================
1: Characters                       3: Vehicles
2: Films                            4: Exit
========================================================================="""))
    if choice == 4:
        exit()
    else:
        choice_dict = {
        1: ["http://swapi.co/api/people/", "name"],
        2: ["http://swapi.co/api/films/", "title"],
        3: ["http://swapi.co/api/vehicles/", "name"],
        }
    call_swapi(choice_dict[choice])
while True:
    welcome()
