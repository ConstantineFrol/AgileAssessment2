#!/bin/python

import datetime
import socket
import re
import sys
import urllib2
import BeautifulSoup


print("Hello world!")
now = datetime.datetime.now()
print ("Current date and time is ")
print (now.strftime("%A, %d-%m-%Y : %H:%M"))

# Get the Geo Location of an IP Address

usage = "Run the script: ./geolocate.py IPAddress"

if len(sys.argv)!=2:
    print(usage)
    sys.exit(0)

if len(sys.argv) > 1:
    ipaddr = sys.argv[1]

geody = "http://www.geody.com/geoip.php?ip=" + ipaddr
html_page = urllib2.urlopen(geody).read()
soup = BeautifulSoup.BeautifulSoup(html_page)

# Filter paragraph containing geolocation info.
paragraph = soup('p')[3]

# Remove html tags using regex.
geo_txt = re.sub(r'<.*?>', '', str(paragraph))
print geo_txt[32:].strip()


	
# This line was made by Konstantin
