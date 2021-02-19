from io import BytesIO


import requests
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("adress", nargs="+")
toponym_to_find = " ".join(parser.parse_args().adress)

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:

    pass

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
maxm = list(map(float, toponym["boundedBy"]["Envelope"]["upperCorner"].split(" ")))
minim = list(map(float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split(" ")))
d = str(maxm[0] - minim[0])
sh = str(maxm[1] - minim[1])
s = [d, sh]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

delta = "0.005"


map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "l": "map",
    "pt": ",".join([toponym_longitude, toponym_lattitude]) + ",pm2pnl",
    "spn": ",".join(s)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
print(response.url)

Image.open(BytesIO(
    response.content)).show()
