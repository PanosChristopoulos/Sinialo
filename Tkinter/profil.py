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
import popup
import resultScreenCheapest
def main():

    database=mysql.connector.connect(
    user='root',
    password='password',
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
    photo4=PhotoImage(file="img/profile_2.png")
    def addPref():
    	prefered.addPreference(sessionName,entry2.get())
    def resultScreenCheapestFrame():
    	root.destroy()
    	resultScreenCheapest.main()
    def resultScreenFavoriteFrame():
    	root.destroy()
    	resultScreenFavorite.main()
    def profilFrame():
    	root.destroy()
    	profil.main()
    root.geometry("%dx%d+50+30" % (w, h))
    cv = tk.Canvas(width=w, height=h)
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(0, 0, image=bg_image, anchor='nw')
    nameLabel = Label(text = sessionName,width=20,height=5)
    nameLabel.place(relx = 0.5, rely = 0.24, anchor = CENTER)
    entry = Entry(root)
    entry.place(relx = 0.50, rely = 0.35, anchor = CENTER)
    print(popup.viewRequests(sessionName))
    def sendRequest():
    	print(sessionName,entry.get())	
    	profil1.addFriend(sessionName,entry.get())

    def friendList():
    	popupmsg(sessionName,popup.viewRequests(sessionName))
 	
    def acceptReq(x):
    	popup.acceptFunct(sessionName,popup.viewRequests(sessionName)[x][0])
    def declineReq(x):
    	popup.declineFunct(sessionName,popup.viewRequests(sessionName)[x][0])

    def popupmsg(user,userRequest):
        popup = tk.Tk()
        popup.wm_title(userRequest)
        print(userRequest)
        for x in range(len(userRequest)):
        	label = tk.Label(popup, text = "Έχετε αίτημα φιλίας από το χρήστη "+userRequest[x][0], font = NORMAL)
        	label.place(relx = 0.15, rely = 0.1+(x*0.25), anchor = CENTER)
        	B1 = tk.Button(popup,text="Αποδοχή",command = lambda i=x:acceptReq(i))
        	B1.place(relx = 0.07, rely = 0.2+(x*0.25), anchor = CENTER)
        	B2 = tk.Button(popup,text="Απόρριψη",command = lambda i=x:declineReq(i))
        	B2.place(relx = 0.15, rely = 0.2+(x*0.25), anchor = CENTER)
        popup.mainloop()
    btn4 = tk.Button(root, width=10,text="Return",bg = "tomato2",fg="BLACK",border="0",command=resultScreenCheapestFrame)
    btn4.place(relx = 0.15, rely = 0.08, anchor = CENTER)    
    btn = tk.Button(cv, bg="BLACK",fg="WHITE", text="Add Friend", width=17, height=2,command=sendRequest)
    btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    btn1 = tk.Button(cv, bg="BLACK",fg="WHITE", text="Friend List", width=30, height=5,command=friendList)
    btn1.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    entry2 = Entry(root)
    entry2.place(relx = 0.50, rely = 0.65, anchor = CENTER)
    btn1 = tk.Button(cv, bg="BLACK",fg="WHITE", text="Add Favorite Location", width=17, height=2,command=addPref)
    btn1.place(relx = 0.5, rely = 0.70, anchor = CENTER)
    btn3 = tk.Button(cv, bg="BLACK",fg="WHITE", text="Show Favorite Locations", width=30,height=5,command=resultScreenFavoriteFrame)
    btn3.place(relx = 0.5, rely = 0.86, anchor = CENTER)
    btn5 = tk.Button(root,image=photo4,command=profilFrame,border="0")
    btn5.place(relx = 0.5, rely = 0.083, anchor = CENTER)
    
    


    root.mainloop()
if __name__=="__main__":
    main()