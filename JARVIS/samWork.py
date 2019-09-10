import geocoder
import requests
g = geocoder.ip('me')
print(g.latlng)
latitude = g.latlng[0]
longitude = g.latlng[1]
freegeoip = "http://freegeoip.net/json"
geo_r = requests.get(freegeoip)
geo_json = geo_r.json()
user_postition = [geo_json["latitude"], geo_json["longitude"]]

print(user_postition)