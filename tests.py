import matplotlib.pyplot as plt
from matplotlib import animation
import cartopy.crs as ccrs

fig, ax = plt.subplots()

#SET AXES FOR PLOTTING AREA
ax=plt.axes(projection=ccrs.PlateCarree())
ax.set_ylim(40.6051,40.6825)
ax.set_xlim(-73.8288,-73.7258)

#ADD OSM BASEMAP
#ax.add_image(osm_tiles,13) #Zoom level 13

#PLOT JFK INTL AIRPORT
ax.text(-73.778889,40.639722,'JFK Intl',horizontalalignment='right',size='large')
ax.plot([-73.778889],[40.639722],'bo') #Plot a point in blue color
plt.show()