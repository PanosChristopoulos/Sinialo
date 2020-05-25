import mysql.connector
from getpass import getpass

database = mysql.connector.connect(
user='root',
password='password',
host='127.0.0.1', 
database='sinialo',
auth_plugin='mysql_native_password')

mycursor = database.cursor()

def registerSQL(username,password,countryISO):
    sql = "INSERT INTO users (username, password, country_ISO) VALUES (%s, %s, %s)"
    val = (username,password,countryISO)
    mycursor.execute(sql, val)
    database.commit()
    print("User",username,"added to database")

def register():
    print("Please Type your Username, Password and country_ISO")
    usernameIn = input("Username: ")
    passwordIn = getpass("Password: ")
    countryISOIn = input("Country ISO: ")
    registerSQL(usernameIn,passwordIn,countryISOIn)


