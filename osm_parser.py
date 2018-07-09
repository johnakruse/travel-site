import requests
from bs4 import BeautifulSoup

def query(query_line):
    payload = {'data': query_line}
    result = requests.get('https://lz4.overpass-api.de/api/interpreter', params=payload)
    soup = BeautifulSoup(result.content, "xml")
    return soup

def build_query(**kwargs):
    #building our box here
    query = "node({south}, {west}, {north}, {east})->.box;".format(kwargs)
    if(kwargs["tourism"]):
        query = query + "(node.box[tourism];)->.results;"
    if(kwargs["food"]):
        query = query + "(node.box[amenity=restaurant]; node.box[amenity=cafe]; node.box[amenity=biergarten]; node.box[amenity=bar]; node.box[amenity=pub];)->.restaurants;"
    if(kwargs["transit"]):
        query = query + "(node.box[public_transport];node.box[amenity=bicycle_rental];node.box[amenity=bus_station];node.box[amenity=car_rental];node.box[amenity=ferry_terminal];node.box[amenity=taxi];)->.transit;"
    if(kwargs["nightlife"]):
        query = query + "(node.box[amenity=nightclub];node.box[amenity=bar] - node.restaurants)->.nightlife;"
    query = query + "(node.results, node.restaurants, node.transit, node.nightlift);out;)"
