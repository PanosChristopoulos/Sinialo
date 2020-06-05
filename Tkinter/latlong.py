import requests
import geocoder
def cityLatLong(city):
    g = geocoder.locationiq(city, key='07227b1db74b5a')
    latitude = g.json['lat']
    longtitude = g.json['lng']
    return [latitude,longtitude]