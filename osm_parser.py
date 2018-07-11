import requests
from bs4 import BeautifulSoup

def send_query(query_line):
    payload = {'data': query_line}
    result = requests.get('https://lz4.overpass-api.de/api/interpreter', params=payload)
    return result

def build_query(**kwargs):
    #building our box here
    query = "[out:json];(node({south}, {west}, {north}, {east}))->.box;".format(kwargs)
    if "tourism" in kwargs:
        query = query + "(node.box[tourism];)->.tourism;"
    if "food" in kwargs:
        query = query + "(node.box[amenity=restaurant]; node.box[amenity=cafe]; node.box[amenity=biergarten]; node.box[amenity=bar]; node.box[amenity=pub];)->.restaurants;"
    if "transit" in kwargs:
        query = query + "(node.box[public_transport];node.box[amenity=bicycle_rental];node.box[amenity=bus_station];node.box[amenity=car_rental];node.box[amenity=ferry_terminal];node.box[amenity=taxi];)->.transit;"
    if "nightlife" in kwargs:
        query = query + "(node.box[amenity=nightclub];node.box[amenity=bar] - node.restaurants)->.nightlife;"
    query = query + "(node.tourism, node.restaurants, node.transit, node.nightlife);out;)"
    return send_query(query)
