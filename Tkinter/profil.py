import mysql.connector
from getpass import getpass
from tkinter import *
from tkinter import messagebox
import selectorScreen
import tkinter as tk
import loginScreen1
import prefered
import resultScreenFavorite
import profil1
def main():

    database=mysql.connector.connect(
    user='root',
    password='Aekjim1998@',
    host='127.0.0.1', 
    database='sinialo',
    auth_plugin='mysql_native_password')
    sessionName = loginScreen1.sessName()
    mycursor = database.cursor()
    
    root = tk.Tk()
    frame_1 = Frame(root)
    root.title('background image')
    root.resizable(False,False)
    fname = "img/profil.png"
    bg_image = tk.PhotoImage(file=fname)
    w = bg_image.width()
    h = bg_image.height()

    def addPref():
    	prefered.addPreference(sessionName,entry.get())
    def resultScreenFavoriteFrame():
    	root.destroy()
    	resultScreenFavorite.main()


    root.geometry("%dx%d+50+30" % (w, h))
    cv = tk.Canvas(width=w, height=h)
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(0, 0, image=bg_image, anchor='nw')
    entry = Entry(root)
    entry.place(relx = 0.50, rely = 0.50, anchor = CENTER)
    btn1 = tk.Button(cv, bg="BLACK",fg="WHITE", text="Add Favorite Location", width=17, height=2,command=addPref)
    btn1.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    nameLabel = Label(text = sessionName,width=20,height=5)
    nameLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    btn1 = tk.Button(cv, bg="BLACK",fg="WHITE", text="Friend List", width=30, height=5)
    btn1.place(relx = 0.5, rely = 0.24, anchor = CENTER)
    #btn2 = tk.Button(cv,bg="BLACK",fg="WHITE", text="Favorite Locations", width=30,height=5)
    #btn2.place(relx = 0.5, rely = 0.70, anchor = CENTER)
    btn3 = tk.Button(cv, bg="BLACK",fg="WHITE", text="Show Favorite Locations", width=30,height=5,command=resultScreenFavoriteFrame)
    btn3.place(relx = 0.5, rely = 0.70, anchor = CENTER)
    
    root.mainloop()
if __name__=="__main__":
    main()