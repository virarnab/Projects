from geopy.geocoders import Nominatim
from geopy import *
geolocator = Nominatim(user_agent="8.py")
from mpmath import *


city1 = input()
city2 = input()
d1 = geolocator.geocode(city1)
d2 = geolocator.geocode(city2)
lat1 = d1.latitude
lat2 = d2.latitude
long1 = d1.longitude
long2 = d2.longitude
lat1 = (pi/180)*float(lat1)
lat2 = (pi/180)*float(lat2)
long1 = (pi/180)*float(long1)
long2 = (pi/180)*float(long2)
d = 6400*acos((sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos((long2)-(long1)))
print("Distance=",d,"km")
