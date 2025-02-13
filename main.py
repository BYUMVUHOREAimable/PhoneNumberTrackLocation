import phonenumbers
from myphone import number
import opencage
import folium
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
serviceprovider = phonenumbers.parse(number)
print(carrier.name_for_number(serviceprovider,"en"))

from opencage.geocoder import OpenCageGeocode

key = "d8e95891b19a4646a90b9ffc5c33237b"
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

myMap =folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("mylocation.html")


