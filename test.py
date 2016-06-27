
import requests

# url = "http://swapi.co/api/films/7/"
# response = requests.request("GET", url).json()
# print(response)


detail_choice = int(input("What item do you want to see the deatils for: "))
url = "http://swapi.co/api/people/{}/".format(detail_choice)
response = requests.get(url).json()
print(response['name'])
