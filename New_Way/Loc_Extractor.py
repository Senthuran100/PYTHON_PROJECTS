from geopy.geocoders import Nominatim
geolocator = Nominatim()
loc = geolocator.geocode('Galle')
print(loc.address)
# u'Chicago, Cook County, Illinois, United States of America'
loc = geolocator.geocode('mobile')
print(loc.address)