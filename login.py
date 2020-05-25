import mysql.connector
from getpass import getpass

database = mysql.connector.connect(
user='root',
password='password',
host='127.0.0.1', 
database='sinialo',
auth_plugin='mysql_native_password')

mycursor = database.cursor()


#loginSuccess=False
#userCount = 0

def loginSQL(usernameIN,passwordIN):
    mycursor.execute("SELECT username,password FROM users")
    result = mycursor.fetchall()
    exists = False
    for x in result:
        if usernameIN == x[0] and passwordIN == x[1]:
            exists = True
    if exists == True:
        #loginSuccess=True
        print("User",usernameIN, "logged in")
    else:
        print("Log in Unsuccesssful")
        #loginSuccess=False
        
def login():
    usernameIN = input("Username: ")
    passwordIN = getpass("Password: ")
    loginSQL(usernameIN,passwordIN)
    #print(loginSuccess)

