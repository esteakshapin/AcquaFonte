import requests


def coords_to_address(lat, lng):
    api_key = 'AIzaSyDW0ktd2_Rv-AwQu2rz2DsB5OCBrreAWI0'
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=%s" % (
        lat, lng, api_key)
    r = requests.get(url)
    return r
