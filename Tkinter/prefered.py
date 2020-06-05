import mysql.connector
from translate import *
from skyscanner import *
from googletrans import Translator

database = mysql.connector.connect(
user='root',
password='Aekjim1998@',
host='127.0.0.1', 
database='sinialo',
auth_plugin='mysql_native_password')

mycursor = database.cursor()

translator = Translator()
def translate(word):
    return translator.translate(word).text

def addPreference(usernameIN,cityIN):
    city = translate(cityIN)
    mycursor.execute("SELECT username FROM users")
    usernameResults = mycursor.fetchall()
    exists = False
    for x in usernameResults:
        if usernameIN == x[0]:
            exists = True
    if exists == True:
        try:
            cityAirport = skyScannerAirportFinderCity(city)[0]
            sql = "INSERT INTO preferences (username, preference, city) VALUES (%s, %s, %s)"
            val = (usernameIN,cityAirport,city)
            mycursor.execute(sql, val)
            database.commit()
            print("User",usernameIN,"added to database his prefered city:",city,"and airport",cityAirport)
        except:
            print("There is no airport available for this city")      
    else:
        print("User does not exist in database")


def viewPreferences(usernameIN):
    mycursor.execute("SELECT preference,city FROM preferences WHERE username = '{}'".format(usernameIN))
    preferenceResults = mycursor.fetchall()
    preferences = []
    cities = []
    for x in range(len(preferenceResults)):
        preferences.append(preferenceResults[x][0])
        cities.append(preferenceResults[x][1])
    preferences = list(dict.fromkeys(preferences))
    return [preferences,cities]

print(viewPreferences("ntomatozoumi"))