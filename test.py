# from urllib.parse import urlparse
# o = urlparse('http://swapi.co/api/people/4/')
# print(o)

# uid = filter(str.isdigit, u)
# uid = (list(filter(str.isdigit, u)))
# print((uid))


import re

u = "http://swapi.co/api/people/41/"
print(int((re.findall("\d+", u)[0])))
