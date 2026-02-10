import requests 

def get_country_name(country_code):
    """ Returns a tuple of found, country name, error 
    If country is found, the tuple will be (True, country name, None)
    If country is not found, the tuple will be (False, None, None)
    If there is an error connecting to the API. the tuple will be (False, None, error message)"""

    try:
        url = create_url(country_code)
        json_response = make_api_request(url)
        if not json_response:
             return False, None, None 
        name = get_name_from_response(json_response)
        return True, name, None
    except Exception as e:
        return False, None, 'Error connecting to API'

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
