from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
            width=8E6, height=8E6, 
            lat_0=45, lon_0=-100,)
m.etopo(scale=0.5, alpha=0.5)

# Map (long, lat) to (x, y) for plotting
x, y = m(-87.879997, 41.959999)
plt.plot(x, y, 'ok', markersize=5)
plt.text(x, y, ' Chicago', fontsize=12);
plt.show()