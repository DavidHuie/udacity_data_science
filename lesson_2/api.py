import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.

    response = requests.get(url)
    top_artists = json.loads(response.text)
    return top_artists['topartists']['artist'][0]['name']
