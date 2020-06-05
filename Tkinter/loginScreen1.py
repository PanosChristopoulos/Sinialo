import mysql.connector
from getpass import getpass
from tkinter import *
from tkinter import messagebox
import selectorScreen
import tkinter as tk
import registerScreen

sessionCountry=""
sessionName = ""

def main():

    

    database=mysql.connector.connect(
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
    entry_1.place(relx = 0.5, rely = 0.68, anchor = CENTER,height=30)
    entry_2.place(relx = 0.5, rely = 0.48, anchor = CENTER ,height=30)
    #entry_1.place(relx = 0.3, rely = 0.6, anchor = CENTER)
    #entry_2.place(relx = 0.3, rely = 0.43, anchor = CENTER)

    def registerFrame():
        root.destroy()
        registerScreen.main()

    def selectorFrame():
        root.destroy()
        selectorScreen.main()

    def errorMessage():
        messagebox.showerror("Error","Invalid Username or Password")

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
            global sessionName
            sessionName = usernameIN
            print("User",usernameIN, "logged in")
            mycursor.execute('SELECT country_ISO FROM users where username="%s"' %usernameIN)
            result = mycursor.fetchone()
            country = result[0]
           
            print ( "aekk")
            print (country)
            global sessionCountry
            sessionCountry = country;
            selectorFrame()
        else:
            print("Log in Unsuccesssful")
            loginSuccess=False
            errorMessage()
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
        




    btn1 = tk.Button(cv, bg="GREEN",fg="WHITE", text="Login", width=15, command =login)
    btn1.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    btn2 = tk.Button(cv,bg="RED",fg="WHITE", text="Register", width=15, command =registerFrame)
    btn2.place(relx = 0.5, rely = 0.83, anchor = CENTER)

   

    
    
    root.mainloop()

def sessName():
    return sessionName
  
def sess():
    
    return sessionCountry

if __name__=="__main__":
    main()