import requests

url = "https://devru-latitude-longitude-find-v1.p.rapidapi.com/latlon.php"

def cityLatLong(city):
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
    return latitude,longtitude
