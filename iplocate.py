import os
import sys
from urllib2 import urlopen
import urllib2
import json


while True:
    ip = raw_input("ip address: ")
    url = "https://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    os.system("clear")
    os.system("figlet Scanning")
    print "\n"
    print "Query: ", values["query"]
    print "status: ", values["status"]
    print "Country:", value["country"]
    print "City: ", values["city"]
    print "regionName: ", values["regionName"]
    print "timeZone: ", values["timezone"]
    print "lat: ", str(values["lat"]) + "lon: ", str(values["lon"])
    print "as: ", values["as"]
    print "zipcode: ", str(values["zip"])
    print "\n"
    print "EASY AS FUCK :P"

