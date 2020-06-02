import random
from skyscanner import *


def popularFinder(country):
    popularDestinations = ["lisbon","istanbul","kobenhavn","prague","london","dublin","beijing","london","edinburgh","milan","rome","new york","dubai","hong kong","washington","los angeles","moscow","tokyo","new delhi","sao paolo","rio de janeiro","seoul","houston","jakarta","doha","melbourne","nairobi","kabul","cape town","johannesburg","addis ababa","kuala lumpur","mexico city"]
    selectedDestinations = []
    results = []
    targetairports = []
    dates = []
    destinationCities = []
    urls = []
    airport1 = skyScannerAirportFinder(country)[0]
    print("airport1",airport1)
    for x in range(6):
        city = random.choice(popularDestinations)
        popularDestinations.remove(city)
        selectedDestinations.append(skyScannerAirportFinderCity(city))
        destinationCities.append(selectedDestinations[x][1])

    for x in range(len(selectedDestinations)):
        targetairport = selectedDestinations[x][0]
        getpflights = getFlights(airport1,targetairport)
        results.append(getpflights)
        print(getpflights)
        dates.append("{}{}{}".format(getpflights[3][2:4],getpflights[3][5:7],getpflights[3][8:10]))
        targetairports.append(targetairport)
        urls.append("https://gr.skyscanner.com/transport/flights/{}/{}/{}/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home".format(airport1[:-4],targetairport[:-4],dates[x]))
    
    limit = range(len(results))
    for x in limit:
        try:
            if results[x][2] == '0':
                del results[x]
                del targetairports[x]
                del destinationCities[x]
                del urls[x]
        except:
            limit = range(len(results))
    limit = range(len(results))   

    return [targetairports,destinationCities,results,urls]

print(popularFinder("belarus"))