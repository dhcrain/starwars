import requests


def print_results(response, dict_key, number):
    for number, item in enumerate(response['results'], number):
        print(number, item[dict_key])


def call_swapi(data):
    number = 1  # start the list with 1
    url, dict_key, category = data
    response = requests.get(url).json()
    if response['next']:
        print_results(response, dict_key, number)
        number += 10

        detail_choice = int(input("What item do you want to see the deatils for: "))
        url = "http://swapi.co/api/{}/{}/".format(category, detail_choice)
        response = requests.get(url).json()
        print(response[dict_key])
        exit_contiune = input("Do you want to see the rest of the list? Y/n")

        if exit_contiune != "n":
            while response['next']:
                more = input("Do you want to see more? Y/n \n").lower()
                if more != "n":
                    url = response['next']
                    response = requests.get(url).json()
                    print_results(response, dict_key, number)
                    number += 10
                else:
                    exit()
    else:
        print_results(response, dict_key, number)

def welcome():
    choice = int(input("""
Star Wars
1: Characters
2: Films
3: Vehicles
"""))

    choice_dict = {
    1: ["http://swapi.co/api/people/", "name", "people"],
    2: ["http://swapi.co/api/films/", "title", "films"],
    3: ["http://swapi.co/api/vehicles/", "name", "vehicles"],
    }

    call_swapi(choice_dict[choice])

while True:
    welcome()
