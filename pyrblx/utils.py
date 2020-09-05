import requests
from .exceptions import BadArgument
def sendreq(url):
    stuff = requests.get(url=url)
    if stuff.status_code == 200:
        return stuff.json()

    else:
        raise BadArgument
def direct(url):
    lol = requests.get(url)
    ee   = lol.json()
    return ee
