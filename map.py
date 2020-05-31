from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import warnings
import matplotlib.cbook
from latlong import *
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

fig = plt.figure(num=None, figsize=(12, 8) )
m = Basemap(projection='moll',lon_0=0,resolution='c')    
m.drawcoastlines()
m.fillcontinents(color='tan',lake_color='lightblue')
# draw parallels and meridians.

m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
m.drawcoastlines(linewidth=0.1, color="white")

# Map (long, lat) to (x, y) for plotting
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
    
cityMap('Athens')
plt.show()