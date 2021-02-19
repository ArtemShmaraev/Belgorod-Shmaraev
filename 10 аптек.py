import argparse
import requests
from PIL import Image
from io import BytesIO



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

st = ""
for i in range(10):
    if i != 0:
        st += "~"

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
    organization = json_response["features"][i]
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])
    try:
        hor = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
        if "круглосуточно" in hor:
            st += f"{org_point},pm2dgl"
        else:
            st += f"{org_point},pm2bll"
    except KeyError:
        st += f"{org_point},pm2grl"

map_api_server = "http://static-maps.yandex.ru/1.x/"
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": st
}
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
