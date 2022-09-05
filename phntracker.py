import phonenumbers



from myNumber import number #this another .py to import phonenumber
#this contains only mobile number with variable number
#u should also create this

from phonenumbers import geocoder

import folium

#api key
key=' '#here u should paste ur api key winthin quotes

samNumber= phonenumbers.parse(number)

yourLocation=geocoder.description_for_number(samNumber,"en")

print(yourLocation)

#get service provider Name
from phonenumbers import carrier
service_provider= phonenumbers.parse(number)
x=carrier.name_for_number(service_provider,"en")
print(x)

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)
query=str(yourLocation)
results=geocoder.geocode(query)
#print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)


#myMap=folium.Map(location=[lat,lng],zoom_start=9)

myMap=folium.Map(location=[lat,lng])

folium.Marker([lat,lng],popup="Marker is utilized")

myMap.save("myLocation.html")
