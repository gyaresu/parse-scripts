import ParsePy
import parse.app.master
from publist import pub_list
import os
import urllib
import urllib2
try: import simplejson as json
except ImportError: import json

def get_lat_long(location):
    place = urllib.quote_plus(location.encode('utf-8'))
    #place = urllib.quote_plus(location)
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=true&region=no" % (place)
    out = urllib.urlopen(url)
    jsonResponse = json.load(out)
    pub_location = jsonResponse.get('results')[0].get('geometry').get('location')
    lat = pub_location.get('lat')
    lng = pub_location.get('lng')
    return lat, lng
 
query = ParsePy.ParseQuery("Pub")

# Add this extra query param to update single pubs. Remove the 'for pub in pubs' loop below.
#pub = query.get("UL07RiNQZP")

pubs = query.fetch()
for pub in pubs:
    pub.lat, pub.lng = get_lat_long(pub.pub_address)
    print pub.pub_name
    print pub.lat
    pub.save()

