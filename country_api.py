import requests
from collections import namedtuple

CountryInfo = namedtuple('CountryInfo', ['found', 'name', 'capital', 'error'])

def get_country_name(country_code):
    """ Returns a CountryInfo namedtuple with found, name, capital, error fields 
    If country is found: CountryInfo(found=True, name=..., capital=..., error=None)
    If country is not found: CountryInfo(found=False, name=None, capital=None, error=None)
    If there is an error: CountryInfo(found=False, name=None, capital=None, error=...)"""

    try:
        url = create_url(country_code)
        json_response = make_api_request(url)
        if not json_response:
             return CountryInfo(False, None, None, None)
        name = get_name_from_response(json_response)
        capital = get_capital_from_response(json_response)
        return CountryInfo(True, name, capital, None)
    except Exception as e:
        return CountryInfo(False, None, None, 'Error connecting to API')

def create_url(country_code):
    url = f'https://restcountries.com/v3.1/alpha/{country_code}'
    return url


def make_api_request(url):
    response = requests.get(url)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    json = response.json()  
    return json


def get_name_from_response(json_response):
    name = json_response[0]['name']['official']
    return name


def get_capital_from_response(json_response):
    capital = json_response[0].get('capital')
    if capital:
        return capital[0]
    return 'N/A'
