from tkinter import *
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from mpl_toolkits.basemap import Basemap
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk 
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
import profil
import resultScreen
import resultScreenCheapest
import resultScreenFavorite


def main():

	database=mysql.connector.connect(
    user='root',
    password='password',
    host='127.0.0.1', 
    database='sinialo',
    auth_plugin='mysql_native_password')
	mycursor = database.cursor()
	sessionC=loginScreen1.sess()

	def openLink(url):
		webbrowser.open_new(url)

	def resultScreenCheapestFrame():
		root.destroy()
		resultScreenCheapest.main()
	def loginScreen1Frame():
		root.destroy()
		loginScreen1.main()

	def profilFrame():
		root.destroy()
		profil.main()

	def resultScreenFrame():
		root.destroy()
		resultScreen.main()
	
	def resultScreenPopularFrame():
		root.destroy()
		main()

	def resultScreenFavoriteFrame():
		root.destroy()
		resultScreenFavorite.main() 


	root = tk.Tk()
	root.geometry("1300x800")
	root.resizable(False,False)
	frame_1 = Frame(root)
	root.title('background image')
	#root.resizable(False,False)
	image3 = ImageTk.PhotoImage(Image.open("img/resultScreen.png"))
	label3 = Label(root,image = image3)
	label3.place(x=0,y=0)
	photo=PhotoImage(file="img/button_7.png")
	photo4=PhotoImage(file="img/profile_2.png")
	photo2=PhotoImage(file="img/button_5.png")
	photo1=PhotoImage(file="img/button_6.png")
	photo5=PhotoImage(file="img/oikonomikos.png")
	btnOik = tk.Button(root,width=145,height=30,image=photo5,command=resultScreenCheapestFrame)
	btnOik.place(relx = 0.23, rely = 0.23, anchor = CENTER)
	btn1 = tk.Button(root,width=145,height=30,image=photo,command=resultScreenFrame)
	btn1.place(relx = 0.056, rely = 0.18, anchor = CENTER)
	btn2 = tk.Button(root,width=145,height=30,image=photo2,command=resultScreenPopularFrame)
	btn2.place(relx = 0.056, rely = 0.23, anchor = CENTER)
	btn3 = tk.Button(root,width=145,height=30,image=photo1,command=resultScreenFavoriteFrame)
	btn3.place(relx = 0.23, rely = 0.18, anchor = CENTER)
	btn4 = tk.Button(root, width=10,text="Return",bg = "tomato2",fg="BLACK",border="0",command=loginScreen1Frame)
	btn4.place(relx = 0.047, rely = 0.08, anchor = CENTER)
	btn5 = tk.Button(root,image=photo4,command=profilFrame,border="0")
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
	canvas.draw()
	canvas.get_tk_widget().place(bordermode="outside", x = 380, y = 0,height=795, width=918)
	toolbar = NavigationToolbar2Tk(canvas , root )
	toolbar.update()
	
	#pack(side=tk.TOP, fill=tk.BOTH, expand=1)
	#canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
	
	popularCountries  = popular.popularFinder(sessionC)
	#print(nearCountries)
	#nearCountries2 = nearCountries[2]
	#print(nearCountries2)
	popularCountries[1][1][2]

	userBudget = selectorScreen.getBudget()
	userDays = selectorScreen.getDays()
	userPeople = selectorScreen.getPeople()
	#print(userBudget,userPeople,userDays)
	
	def cityMap(city):
		lat = cityLatLong(city)[0]
		longt = cityLatLong(city)[1]
		city = city.split(' ', 1)[0]
		city = city.split('/',1)[0]
		city = city.split('-',1)[0]
		x, y = m(longt, lat)
		ax1.plot(x, y, 'ok',  marker="o", markersize=8, alpha=0.6, c="blue", markeredgecolor="black", markeredgewidth=1)
		ax1.text(x, y, city, fontsize=14, color="white");


	def suitableLocations():
		suitableLocationsList = []
		suitablePricesList = []
		suitableLinksList = []
		suitableDatesList = []
		for x in range(len(popularCountries[0])):
			#print(nearCountries[1][x][2],userBudget)
			if userBudget > popularCountries[1][x][2]:
				suitableLocationsList.append(popularCountries[0][x])
				suitablePricesList.append(popularCountries[1][x][2])
				suitableDatesList.append(popularCountries[1][x][3])
				#suitableLinksList.append(popularCountries[4][x])
		print (suitableLocationsList)
		return [suitableLocationsList,suitablePricesList,suitableDatesList]
	#, suitableLinksList

	sLocations =suitableLocations()
	print(sLocations)
	
	for x in sLocations[0]:
		time.sleep(1)
		cityMap(x)
		
	lb1 = Listbox(root,selectmode = EXTENDED)

	for y in range(len(sLocations[0])):
		#for k in range(len(nearCountries[1])):
		lb1.insert(y,("Location", sLocations[0][y] , "Price", sLocations[1][y]*userPeople, "Date",sLocations[2][y]  ))
	#, sLocations[3][y]
	
	for i in range(len(sLocations[0])):
		b = tk.Button(root,height=1 , width = 5,text= "Link {:d}".format(i+1),bg="skyBlue1",command =lambda: openLink(sLocations[3][i]))
		b.place(relx = 0.35+0.08*i, rely = 0.1, anchor = CENTER)
	

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
