import requests


def print_results(response, dict_key, number):
    for number, item in enumerate(response['results'], number):
        print(number, item[dict_key])
        

def call_swapi(data):
    number = 1  # start the list with 1
    url, dict_key = data
    response = requests.get(url).json()
    if response['next']:
        print_results(response, dict_key, number)
        number += 10
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

choice = int(input("""
Star Wars
1: Characters
2: Films
3: Vehicles
"""))

choice_dict = {
1: ["http://swapi.co/api/people/", "name"],
2: ["http://swapi.co/api/films/", "title"],
3: ["http://swapi.co/api/vehicles/", "name"],
}

call_swapi(choice_dict[choice])
