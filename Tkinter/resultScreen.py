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

database=mysql.connector.connect(
    user='root',
    password='Aekjim1998@',
    host='127.0.0.1', 
    database='sinialo',
    auth_plugin='mysql_native_password')

mycursor = database.cursor()

def main():
	root = tk.Tk()
	root.geometry("1300x800")
	root.resizable(False,False)
	frame_1 = Frame(root)
	root.title('background image')
	#root.resizable(False,False)
	image3 = ImageTk.PhotoImage(Image.open("img/resultScreen.png"))
	label3 = Label(root,image = image3)
	label3.place(x=0,y=0)
	
		
	warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

	fig = Figure( figsize=(12, 8) )
	ax1 = fig.add_subplot(111)
	m = Basemap(projection='moll',lon_0=0,resolution='c',ax=ax1)    
	m.drawcoastlines(linewidth=0.1, color="white")
	m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
	# draw parallels and meridians.

	m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
	
	canvas = FigureCanvasTkAgg(fig, root)  ## her7
	canvas.show()
	canvas.get_tk_widget().place( x = 380, y = 0,height=795, width=918)
	#pack(side=tk.TOP, fill=tk.BOTH, expand=1)
	#canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

	def cityMap(city):
	    city = city.split(' ', 1)[0]
	    city = city.split('/',1)[0]
	    city = city.split('-',1)[0]
	    lat = cityLatLong(city)[0]
	    longt = cityLatLong(city)[1]
	    #print(lat,longt)
	    x, y = m(longt, lat)
	    plt.plot(x, y, 'ok',  marker="o", markersize=8, alpha=0.6, c="blue", markeredgecolor="black", markeredgewidth=1)
	    plt.text(x, y, city, fontsize=14, color="white");



	    

	    
	root.mainloop()    
 

if __name__=="__main__":
    main()
