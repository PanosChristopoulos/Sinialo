import requests




def countryCodeInfo(countryCode):
    url = "https://restcountries-v1.p.rapidapi.com/alpha/{}".format(countryCode)
    headers = {
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
        'x-rapidapi-key': "df61d8e863msh47948b951144384p16523djsn4b480d122f9d"
        }
    response = requests.request("GET", url, headers=headers)
    response_data = response.json()
    name = response_data['name']
    capital = response_data['capital']
    borders = response_data['borders']
    bordercount = range(len(borders))
    return [name,capital,borders,bordercount]




def countryNameInfo(country):
    url = "https://restcountries-v1.p.rapidapi.com/name/{}".format(country)

    headers = {
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
        'x-rapidapi-key': "df61d8e863msh47948b951144384p16523djsn4b480d122f9d"
        }

    response = requests.request("GET", url, headers=headers)
    response_data = response.json()
    name = response_data[0]['name']
    capital = response_data[0]['capital']
    borders = response_data[0]['borders']
    bordercount = range(len(borders))
    neighborCapitalList = []
    for x in bordercount:
        neighborCapitalList.append(countryCodeInfo(borders[x])[1])
    while '' in neighborCapitalList: neighborCapitalList.remove('')
    if "Thimphu" in neighborCapitalList: neighborCapitalList.remove("Thimphu")
    if "City of Victoria" in neighborCapitalList: neighborCapitalList.remove("City of Victoria")
  

    return [name,capital,borders,bordercount,neighborCapitalList]

