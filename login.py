import mysql.connector
from getpass import getpass

database = mysql.connector.connect(
user='root',
password='password',
host='127.0.0.1', 
database='sinialo',
auth_plugin='mysql_native_password')

mycursor = database.cursor()



#userCount = 0

def loginSQL(usernameIN,passwordIN):
    loginSuccess = False
    mycursor.execute("SELECT username,password FROM users")
    result = mycursor.fetchall()
    exists = False
    for x in result:
        if usernameIN == x[0] and passwordIN == x[1]:
            exists = True
    if exists == True:
        loginSuccess=True
        print("User",usernameIN, "logged in")
    else:
        print("Log in Unsuccesssful")
        loginSuccess=False
    if loginSuccess == True:
        mycursor.execute('SELECT country_ISO FROM users where username="%s"' %usernameIN)
        result = mycursor.fetchone()
        country = result[0]
    return [usernameIN,loginSuccess,country]
        
def login():
    usernameIN = input("Username: ")
    passwordIN = getpass("Password: ")
    username = loginSQL(usernameIN,passwordIN)[0]
    loginSuccess = loginSQL(usernameIN,passwordIN)[1]
    if loginSuccess == True:
        mycursor.execute('SELECT country_ISO FROM users where username="%s"' %username)
        result = mycursor.fetchone()
        country = result[0]
    print(username)
    print(country)
    print(loginSuccess)
    return [username,loginSuccess,country]

print(loginSQL('PERIS','DES'))