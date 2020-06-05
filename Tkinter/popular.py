import random
from skyscanner import *


def popularFinder(country):
    popularDestinations = ["lisbon","istanbul","kobenhavn","prague","london","dublin","beijing","london","edinburgh","milan","rome","new york","dubai","hong kong","washington","los angeles","moscow","tokyo","new delhi","sao paolo","rio de janeiro","seoul","shanghai","houston","jakarta","doha","melbourne","nairobi","kabul","cape town","johannesburg","addis ababa","kuala lumpur","buenos aires"]
    selectedDestinations = []
    results = []
    destinationCities = []
    for x in range(6):
        city = random.choice(popularDestinations)
        popularDestinations.remove(city)
        selectedDestinations.append(skyScannerAirportFinderCity(city))
        destinationCities.append(selectedDestinations[x][1])

    for x in range(len(selectedDestinations)):
        results.append(getFlights(skyScannerAirportFinder(country)[0],selectedDestinations[x][0]))
    return [destinationCities,results]

#print(popularFinder("greece"))