import requests
from restCountries import *

def skyScannerAirportFinder(country):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/gr-GR/"
    capital = countryNameInfo(country)[1]
    #print(capital)
    querystring = {"query":capital}
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "df61d8e863msh47948b951144384p16523djsn4b480d122f9d"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_data = response.json()
    PlaceId = response_data['Places'][0]['PlaceId']
    PlaceName = response_data['Places'][0]['PlaceName']
    return[PlaceId, PlaceName]



def skyScannerAirportFinderCity(city):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/gr-GR/"
    querystring = {"query":city}
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "df61d8e863msh47948b951144384p16523djsn4b480d122f9d"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_data = response.json()
    #print(response_data)
    PlaceId = response_data['Places'][0]['PlaceId']
    PlaceName = response_data['Places'][0]['PlaceName']
    #print("passed city",city)
    return[PlaceId, PlaceName]



def skyScannerNeighbors(country):
    airport1 = skyScannerAirportFinder(country)
    #print(airport1)
    neighbors = countryNameInfo(country)[4]
    #print(neighbors)
    limit1 = range(len(neighbors))
    airport2 = []
    for x in limit1:
        airport2.append(skyScannerAirportFinderCity(neighbors[x]))
        #print(airport2[0])
    if ['BRN-sky', 'Bern'] in airport2: airport2.remove(['BRN-sky', 'Bern'])
    limit = range(len(airport2))
    return [airport1,airport2,limit]

def getFlights(airport1,airport2):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/{}/{}/anytime".format(airport1,airport2)
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "df61d8e863msh47948b951144384p16523djsn4b480d122f9d"
        }
    response = requests.request("GET", url, headers=headers)
    response_data = response.json()
    results = response_data['Quotes']
    limit = range(2,len(results))
    #print(results)
    try:
        ticket1 = results[1]['MinPrice']
        try:
            ticket2 = results[2]['MinPrice']
            quote1 = 0
            quote2 = 0
            for x in limit:
                if results[x]['MinPrice']<ticket1:
                    ticket2 = ticket1
                    ticket1 = results[x]['MinPrice']
                    quote1 = x+1
                elif ticket2 == None or ticket2 > results[x]['MinPrice']:
                    ticket2 = results[x]['MinPrice']
                    quote2 = x+1
            #print("Incoming flight ticket prices:",quote1,ticket1,"Outgoing flight ticket prices",quote2,ticket2,"Euros")
            fullprice = ticket1+ticket2
            flights = []
            flights.append(results[quote1-1])
            flights.append(results[quote2-1])
            departuredate = flights[0]['OutboundLeg']['DepartureDate']
        except:
            fullprice = 2*ticket1
            departuredate = results[0]['OutboundLeg']['DepartureDate']
    except:
        print("No flights available between",airport1,"and",airport2)
        fullprice = "0"
        departuredate = "0"
    return [airport1,airport2,float(fullprice),departuredate]

def getNeighborFlights(country):
    skyScannerNeighbors1 = skyScannerNeighbors(country)
    airport1 = skyScannerNeighbors1[0]
    targetairports = skyScannerNeighbors1[1]
    limit = skyScannerNeighbors1[2]
    #print(skyScannerNeighbors1)
    results = []
    targetairportsfinal = []
    for x in limit:
       #print("flights from",skyScannerNeighbors1[0][1] ,"to",targetairports[x][1] ,"are:",getFlights(airport1[0],targetairports[x][0]))
       results.append(getFlights(airport1[0],targetairports[x][0]))
       targetairportsfinal.append(targetairports[x][1])
    getnflights = skyScannerNeighbors1[0][1],results,targetairportsfinal,limit
    #print(getnflights)
    limit = getnflights[3]
    fromairport = getnflights[1][0][0]
    outairports = []
    dates = []
    urls = []
    for x in limit:
        currOutAirport = (getnflights[1][x][1])[:-4]
        outairports.append((getnflights[1][x][1])[:-4])
        dates.append("{}{}{}".format(getnflights[1][x][3][2:4],getnflights[1][x][3][5:7],getnflights[1][x][3][8:10]))
        urls.append("https://gr.skyscanner.com/transport/flights/{}/{}/{}/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home".format(fromairport[:-4],currOutAirport,dates[x]))
    for x in limit:
        try:
            if results[x][2] == '0':
                del results[x]
                del targetairportsfinal[x]
                del urls[x]
        except:
            limit = range(len(results))
    limit = range(len(results))   
    return [skyScannerNeighbors1[0][1],results,targetairportsfinal,limit,urls]