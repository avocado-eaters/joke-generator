import requests
import json
from VividHues import Clr


def jokes(to_fetch):
    data = requests.get(to_fetch)
    # print(json.loads(data.text))
    response = json.loads(data.text)
    return response

  
API_URL = r"https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
a = jokes(API_URL)
print(Clr.BLUE + a["setup"] + Clr.RS)
print(Clr.LIME + a["delivery"] + Clr.RS)
