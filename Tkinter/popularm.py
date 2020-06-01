from tkinter import *
import tkinter as tk
import matplotlib
import mpl_toolkits
import importlib
matplotlib.use("TkAgg")
from mpl_toolkits.basemap import Basemap
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import warnings
import matplotlib.cbook
from latlong import *
from PIL import ImageTk,Image
"""
database=mysql.connector.connect(
    user='root',
    password='Aekjim1998@',
    host='127.0.0.1', 
    database='sinialo',
    auth_plugin='mysql_native_password')

mycursor = database.cursor()
"""
def main():
    root = tk.Tk()
    root.geometry("1300x800")
    root.resizable(False,False)
    frame_1 = Frame(root)
    root.title('background image')
    photo=PhotoImage(file="img/button_4.png")
    photo4=PhotoImage(file="img/profile_2.png")
    image3 = ImageTk.PhotoImage(Image.open("img/resultScreen.png"))
    label3 = Label(root,image = image3)
    label3.place(x=0,y=0)
    photo2=PhotoImage(file="img/button_5.png")
    photo1=PhotoImage(file="img/button_6.png")
    warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
    fig = Figure( figsize=(12, 8) )
    ax1 = fig.add_subplot(111)
    m = Basemap(projection='moll',lon_0=0,resolution='c',ax=ax1)    
    m.drawcoastlines(linewidth=0.1, color="white")
    m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
    m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)	
    canvas = FigureCanvasTkAgg(fig, root)  ## her7
    canvas.get_tk_widget().place( x = 380, y = 0,height=795, width=918)
    def cityMap(city):
        city = city.split(' ', 1)[0]
        city = city.split('/',1)[0]
        city = city.split('-',1)[0]
        lat = cityLatLong(city)[0]
        longt = cityLatLong(city)[1]
        x, y = m(longt, lat)
        plt.plot(x, y, 'ok',  marker="o", markersize=8, alpha=0.6, c="blue", markeredgecolor="black", markeredgewidth=1)
        plt.text(x, y, city, fontsize=14, color="white");
    btn1 = tk.Button(root,width=100,height=20,image=photo)
    btn1.place(relx = 0.045, rely = 0.20, anchor = CENTER)
    btn2 = tk.Button(root,width=110,height=20,image=photo2)
    btn2.place(relx = 0.14, rely = 0.20, anchor = CENTER)
    btn3 = tk.Button(root,width=110,height=20,image=photo1)
    btn3.place(relx = 0.24, rely = 0.20, anchor = CENTER)
    btn4 = tk.Button(root, width=10,text="Return",bg = "RED",fg="BLACK")
    btn4.place(relx = 0.05, rely = 0.08, anchor = CENTER)
    btn5 = tk.Button(root,image=photo4)
    btn5.place(relx = 0.145, rely = 0.083, anchor = CENTER)
    
	
    root.mainloop()    
 

if __name__=="__main__":
    main()