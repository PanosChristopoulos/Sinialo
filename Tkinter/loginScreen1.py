import mysql.connector
from getpass import getpass
from tkinter import *
import tkinter as tk

database = mysql.connector.connect(
user='root',
password='Aekjim1998@',
host='127.0.0.1', 
database='sinialo',
auth_plugin='mysql_native_password')

mycursor = database.cursor()

root = tk.Tk()
frame_1 = Frame(root)
root.title('background image')
root.resizable(False,False)
fname = "img/login.png"
bg_image = tk.PhotoImage(file=fname)
w = bg_image.width()
h = bg_image.height()
root.geometry("%dx%d+50+30" % (w, h))
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg_image, anchor='nw')
entry_1 = tk.Entry(root, show = "*")
entry_2 = tk.Entry(root)
entry_1.place(relx = 0.3, rely = 0.6, anchor = CENTER)
entry_2.place(relx = 0.3, rely = 0.43, anchor = CENTER)




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
    return [usernameIN,loginSuccess]
        
def login():
    #usernameIN = input("Username: ")
    usernameIN = entry_2.get()
    passwordIN = entry_1.get()
    print(usernameIN)
    print(passwordIN)
    #passwordIN = getpass("Password: ")
    username = loginSQL(usernameIN,passwordIN)[0]
    loginSuccess = loginSQL(usernameIN,passwordIN)[1]
    if loginSuccess == True:
        mycursor.execute('SELECT country_ISO FROM users where username="%s"' %username)
        result = mycursor.fetchone()
        country = result[0]
    print(username)
    #print(country)
    print(loginSuccess)
    #return [username,loginSuccess,country]


btn1 = tk.Button(cv, text="Login" , command =login)
btn1.pack(side='bottom')


root.mainloop()