import requests
from django.conf import settings


def coords_to_address(lat, lng):
    api_key = settings.GEOCODE_API_KEY
    parameters = 'result_type=route'
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=%s&%s" % (  # noqa
        lat, lng, api_key, parameters)
    r = requests.get(url)
    return r
