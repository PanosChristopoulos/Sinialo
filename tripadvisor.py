import requests
from countryinfo import *

def airportCode(country):
    city = getCapital(country)
    url = "https://tripadvisor1.p.rapidapi.com/airports/search"
    querystring = {"locale":"en_US","query":city}
    headers = {
    'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
    'x-rapidapi-key': ""
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_data = response.json()
    code = response_data[0]['code']
    name = response_data[0]['name']
    city_name = response_data[0]['cityname']

airportCode("usa")
    
