import requests
from bs4 import BeautifulSoup

def query(query_line):
    payload = {'data': query_line}
    result = requests.get('https://lz4.overpass-api.de/api/interpreter', params=payload)
    soup = BeautifulSoup(result.content, "xml")
    return soup

def build_query(**kwargs):
    query = "node({south}, {west}, {north}, {east});->.box;".format(kwargs)
