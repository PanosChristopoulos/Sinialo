import requests

url = "https://devru-latitude-longitude-find-v1.p.rapidapi.com/latlon.php"

def cityLatLong2(city):
    querystring = {"location":city}

    headers = {
        'x-rapidapi-host': "devru-latitude-longitude-find-v1.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_data = response.json()
    latitude = response_data["Results"][0]["lat"]
    longtitude = response_data["Results"][0]["lon"]
    #print(city,"'s latitude is",latitude,"and longtitude is",longtitude)
    return [latitude,longtitude]

def cityLatLong(city):
    g = geocoder.locationiq(city, key='')
    latitude = g.json['lat']
    longtitude = g.json['lng']
    return [latitude,longtitude]
