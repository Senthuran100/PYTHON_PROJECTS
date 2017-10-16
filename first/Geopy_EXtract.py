from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Kandy")
print(location.address)