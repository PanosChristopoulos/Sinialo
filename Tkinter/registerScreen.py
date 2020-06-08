from tkinter import *
import tkinter as tk
import mysql.connector
from getpass import getpass
import loginScreen1
def main():

	root = tk.Tk()
	frame_1 = Frame(root)
	root.title('background image')
	fname = "img/register.png"
	bg_image = tk.PhotoImage(file=fname)
	w = bg_image.width()
	h = bg_image.height()
	root.geometry("%dx%d+50+30" % (w, h))
	cv = tk.Canvas(width=w, height=h)
	cv.pack(side='top', fill='both', expand='yes')
	cv.create_image(0, 0, image=bg_image, anchor='nw')
	entry_1 = Entry(root)
	entry_2 = Entry(root,show="*")
	entry_3 = Entry(root)
	entry_1.place(relx = 0.31, rely = 0.46, anchor = CENTER)
	entry_2.place(relx = 0.31, rely = 0.58, anchor = CENTER)
	entry_3.place(relx = 0.31, rely = 0.69, anchor = CENTER)

	database = mysql.connector.connect(
	user='root',
	password='Aekjim1998@',
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
	    usernameIn = entry_1.get()
	    passwordIn = entry_2.get()
	    countryISOIn = entry_3.get()
	    registerSQL(usernameIn,passwordIn,countryISOIn)
	    root.destroy()
	    loginScreen1.main()

	def loginFrame():
		root.destroy()
		loginScreen1.main()


	btn1 = tk.Button(cv,bg="seaGreen3",fg="WHITE", text="Register",width=15,command=register)
	btn1.place(relx = 0.7, rely = 0.43, anchor = CENTER)
	btn1 = tk.Button(cv,bg="tomato2",fg="WHITE", text="BACK", width=15,command=loginFrame)
	btn1.place(relx = 0.7, rely = 0.63, anchor = CENTER)
	root.mainloop()

if __name__=="__main__":
    main()