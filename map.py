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

m.drawmapboundary(fill_color='lightblue')


# Map (long, lat) to (x, y) for plotting
def cityMap(city):
    lat = cityLatLong(city)[0]
    longt = cityLatLong(city)[1]
    print(lat,longt)
    x, y = m(longt, lat)
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y, city, fontsize=10);
cityMap('Agrinio')
cityMap('Dublin')
cityMap('Guantanamo')
cityMap('Tirana')
cityMap('Ouagadougou')
cityMap('Kingali')
plt.show()