from tkinter import *
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from mpl_toolkits.basemap import Basemap
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg 
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import warnings
import matplotlib.cbook
from latlong import *
from PIL import ImageTk,Image
import loginScreen1
import popular
import selectorScreen
import time
import prefered
import skyscanner
import profil


def main():

	def profilFrame():
		root.destroy()
		profil.main()
	def resultScreenFrame():
		root.destroy()
		resultScreen.main()
	

	def resultScreenPopularFrame():
		root.destroy()
		resultScreenPopular.main()

	def resultScreenFavoriteFrame():
		root.destroy()
		resultScreenFavorite.main()

	database=mysql.connector.connect(
    user='root',
    password='Aekjim1998@',
    host='127.0.0.1', 
    database='sinialo',
    auth_plugin='mysql_native_password')
	mycursor = database.cursor()
	sessionC=loginScreen1.sess()
	sessionName = loginScreen1.sessName()
	
	root = tk.Tk()
	root.geometry("1300x800")
	#root.resizable(False,False)
	frame_1 = Frame(root)
	root.title('background image')
	root.resizable(False,False)
	image3 = ImageTk.PhotoImage(Image.open("img/resultScreen.png"))
	label3 = Label(root,image = image3)
	label3.place(x=0,y=0)
	photo=PhotoImage(file="img/button_4.png")
	photo4=PhotoImage(file="img/profile_2.png")
	photo2=PhotoImage(file="img/button_5.png")
	photo1=PhotoImage(file="img/button_6.png")
	btn1 = tk.Button(root,width=100,height=20,image=photo,command=resultScreenFrame)
	btn1.place(relx = 0.045, rely = 0.20, anchor = CENTER)
	btn2 = tk.Button(root,width=110,height=20,image=photo2,command=resultScreenPopularFrame)
	btn2.place(relx = 0.14, rely = 0.20, anchor = CENTER)
	btn3 = tk.Button(root,width=110,height=20,image=photo1,command=resultScreenFavoriteFrame)
	btn3.place(relx = 0.24, rely = 0.20, anchor = CENTER)
	btn4 = tk.Button(root, width=10,text="Return",bg = "RED",fg="BLACK")
	btn4.place(relx = 0.05, rely = 0.08, anchor = CENTER)
	btn5 = tk.Button(root,image=photo4,command=profilFrame)
	btn5.place(relx = 0.145, rely = 0.083, anchor = CENTER)
		
	warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

	fig = plt.figure(num=None, figsize=(12, 8) )
	ax1 = fig.add_subplot(111)
	m = Basemap(projection='moll',lon_0=0,resolution='c',ax=ax1)    
	m.drawcoastlines(linewidth=0.1, color="white")
	m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
	# draw parallels and meridians.

	m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
	
	
	canvas = FigureCanvasTkAgg(fig, root)  ## her7
	canvas.show()
	canvas.get_tk_widget().place( x = 380, y = 0,height=795, width=918)
	toolbar = NavigationToolbar2TkAgg(canvas , root )
	toolbar.update()
	userPeople = selectorScreen.getPeople()
	favoriteLocations = prefered.viewPreferences(sessionName)[0]
	favoriteLocationsCities = prefered.viewPreferences(sessionName)[1]
	print("jim")
	print(favoriteLocations)
	
	def cityMap(city):
		lat = cityLatLong(city)[0]
		longt = cityLatLong(city)[1]
		city = city.split(' ', 1)[0]
		city = city.split('/',1)[0]
		city = city.split('-',1)[0]
		x, y = m(longt, lat)
		ax1.plot(x, y, 'ok',  marker="o", markersize=8, alpha=0.6, c="blue", markeredgecolor="black", markeredgewidth=1)
		ax1.text(x, y, city, fontsize=14, color="white");

	userAirport = skyscanner.skyScannerAirportFinder(sessionC)
	#print("here")
	#print(userAirport)
	allLocationAttr = []
	for x in range(len(favoriteLocations)):
		#print(favoriteLocations[x])
		u = skyscanner.getFlights(userAirport[0],favoriteLocations[x])
		allLocationAttr.append(u)    
	print(allLocationAttr)	
	
	for x in favoriteLocationsCities:
		time.sleep(1)
		cityMap(x)
				
	lb1 = Listbox(root,selectmode = EXTENDED)
	#print(allLocationAttr[0])
	for y in range(len(allLocationAttr)):
		#for k in range(len(nearCountries[1])):
		lb1.insert(y,("Location", allLocationAttr[y][1] , "Price", allLocationAttr[y][2], "Date",allLocationAttr[y][3] , "Link" ))
	#, sLocations[3][y]
	

	lb1.place(x=1,y=205, width=375,height= 560)
	scrollbar = Scrollbar(lb1, orient="vertical")
	scrollbar.config(command=lb1.yview)
	scrollbar.pack(side="right", fill="y")

	scrollbar2 = Scrollbar(lb1, orient="horizontal")
	scrollbar2.config(command=lb1.xview)
	scrollbar2.pack(side="bottom", fill="x")

	lb1.config(yscrollcommand=scrollbar.set)
	lb1.config(xscrollcommand=scrollbar2.set)
	

	root.mainloop()

if __name__=="__main__":
    main()
