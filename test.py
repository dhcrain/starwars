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
"""))

choice_dict = {
1: ["http://swapi.co/api/people/", "name"],
2: ["http://swapi.co/api/films/", "title"],
3: ["http://swapi.co/api/vehicles/", "name"],
}

call_swapi(choice_dict[choice])
