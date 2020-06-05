import requests
from skyscanner import *


def cheapestFlightsCountry(country):
    airport = skyScannerAirportFinder(country)[0]
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/{}/anywhere/anytime".format(airport)

    querystring = {"inboundpartialdate":"anytime"}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_data = response.json()
    places = response_data['Places']
    cities = []
    cheapestFlights =[]
    placesdictionary = {}
    for x in range(len(places)):
        if places[x]['Type'] == 'Station':
            cities.append(places[x])
    for x in range(len(cities)):
        placesdictionary[cities[x]['PlaceId']] = [cities[x]['SkyscannerCode']+'-sky',cities[x]['CityName']]
    #print(placesdictionary)
    quotes=response_data["Quotes"]
    prices = []
    #print(quotes)
    for x in range(len(quotes)):
        prices.append(quotes[x]['MinPrice'])
    for x in range(5):
        minpos = prices.index(min(prices))
        #print(minpos)
        #print(quotes[minpos])
        destinationid=quotes[minpos]['OutboundLeg']['DestinationId']
        #print(destinationid)
        #print(placesdictionary[destinationid])
        date = quotes[minpos]['OutboundLeg']['DepartureDate'][:10]
        urldate = date[2:4]+date[5:7]+date[8:10]
        #cities[x]['SkyscannerCode']
        url = "https://gr.skyscanner.com/transport/flights/{}/{}/{}/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home".format(airport[:-4],placesdictionary[destinationid][0][:-4],urldate)
        cheapestFlights.append([quotes[minpos]['MinPrice'],date,placesdictionary[destinationid][0],placesdictionary[destinationid][1],url])
        del places[minpos]
        del quotes[minpos]
        del prices[minpos]
    print(cheapestFlights)

cheapestFlightsCountry("qatar")
