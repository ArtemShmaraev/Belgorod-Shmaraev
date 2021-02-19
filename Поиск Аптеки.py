import argparse
import requests
from PIL import Image
from io import BytesIO
import math

def lonlat_distance(a_lon, a_lat, b_lon, b_lat):
    degree_to_meters_factor = 111 * 1000 # 111 километров в метрах
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    distance = math.sqrt(dx * dx + dy * dy)

    return distance



parser = argparse.ArgumentParser()
parser.add_argument("adress", nargs="+")
adr = " ".join(parser.parse_args().adress)

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&" \
                   f"geocode={adr}&format=json"
response = requests.get(geocoder_request)
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")


search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"


search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
json_response = response.json()
organization = json_response["features"][0]
org_name = organization["properties"]["CompanyMetaData"]["name"]
org_address = organization["properties"]["CompanyMetaData"]["address"]
point = organization["geometry"]["coordinates"]
hor = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
org_point = "{0},{1}".format(point[0], point[1])


s = round(lonlat_distance(float(toponym_longitude), float(toponym_lattitude), float(point[0]), float(point[1])))
print(f"Aдрес аптеки: {org_address}")
print(f"Название аптеки: {org_name}")
print(f"Расстояние до аптеки {s} м")
print("Часы работы:", hor)


map_api_server = "http://static-maps.yandex.ru/1.x/"
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": "{0},pm2dgl~{1},ya_ru".format(org_point, ",".join([toponym_longitude, toponym_lattitude]),)
}
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(response.content)).show()
