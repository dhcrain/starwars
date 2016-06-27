# Uses Star Wars api from http://swapi.co/
import requests
import re

def print_results(response, dict_key):
    for item in response['results']:
        # get the number out of the URL, http://stackoverflow.com/questions/26825729/extract-number-from-string-python
        item_url = int((re.findall("\d+", item['url'])[0]))
        print("{}: {}".format(item_url, item[dict_key]))


def call_swapi(data):
    url, dict_key = data
    response = requests.get(url).json()

    if response['next']:
        print_results(response, dict_key)

        detail_choice = (input("""
        Number for details
        See more entries (Y)
        Main Menu (N) """))

        if isinstance(detail_choice, int ):
        # detail_choice = int(input("What item do you want to see the deatils for: "))
            url = "{}{}/".format(url, detail_choice)
            response = requests.get(url).json()
            print(response[dict_key])
        # exit_contiune = input("""  """)

        if detail_choice != "n":
            while response['next']:
                more = input("Do you want to see more? Y/n \n").lower()
                if more != "n":
                    url = response['next']
                    response = requests.get(url).json()
                    print_results(response, dict_key)
                else:
                    welcome()
    else:
        print_results(response, dict_key)


def welcome():
    choice = int(input("""
Star Wars
1: Characters
2: Films
3: Vehicles
4: Exit
------------"""))

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
