import requests

def skyScannerNeighbors(country):
    airport1 = skyScannerAirportFinder(country)
    #print(airport1)
    neighbors = countryNameInfo(country)[4]
    #print(neighbors)
    limit = range(len(neighbors))
    airport2 = []
    for x in limit:
        airport2.append(skyScannerAirportFinderCity(neighbors[x]))
        #print(airport2[0])
    return [airport1,airport2,limit]


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

    print(nearCities , "nearCities")
    return [skyScannerNeighbors1[0][1],results,targetairportsfinal,limit,urls]
