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


database=mysql.connector.connect(
user='root',
password='password',
host='127.0.0.1', 
database='sinialo',
auth_plugin='mysql_native_password')

mycursor = database.cursor()



def acceptFunct(user,userRequest):
    profil1.addFriend(user,userRequest)
    
def declineFunct(user,userRequest):
    sql = "DELETE FROM requests WHERE requestfrom = %s and requestto = %s"
    val = (userRequest,user)
    mycursor.execute(sql, val)
    database.commit()
      





def viewRequests(user):
    mycursor.execute("SELECT requestfrom FROM requests WHERE requestto='{}'".format(user))
    requests = mycursor.fetchall()
    #print(requests)
    #for x in range(len(requests)):
     #   popupmsg(user,requests[x][0])
    return requests