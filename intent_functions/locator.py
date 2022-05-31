import geopy
import geocoder


class Locator:
    # gets location based on ip address
    g = geocoder.ip('me')
    # creates a geolocator based on ip address
    geolocator = geopy.Nominatim(user_agent='http')
    # gets location from latitude and longitude coordinates
    location = geolocator.reverse((g.lat, g.lng))

    # not COMPLETELY accurate results, the address it gave me was about 15 minutes
    # away from where I tested this, but the city is correct, and the zip code will
    # give accurate weather readings which is all I need at the moment.
    city = location.raw['address']['city']
    zipcode = location.raw['address']['postcode']
    lat = g.lat
    long = g.lng
