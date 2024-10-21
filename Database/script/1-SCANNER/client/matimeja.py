# Extract URLs from a web page to a CSV file
# $ python extract-urls.py http://mysite.com/mypage.html myfile.csv
# By Adrian Short 6 Sep 2012
  
import sys
import os
import numpy as np
import requests
import urllib
import csv
from bs4 import BeautifulSoup
url = input(' your target twitter url ex:https://mobile.twitter.com/bjorka: ')
inurl = requests.get(url)
in_fn = open("list.txt", 'r')
out_fn = open("out.txt", 'w') # output filename for CSV file
soup = open("list.txt")
links = [open('href') for link in url]
urlparse = urllib.parse
for link in urlparse.urlparse('a'):
    if 'href' in link:
        links.append(link['href'])
        links.append(urlparse(link['href']).fragment)
        links.append(urlparse(urlparse(link['href']).fragment).fragment)

with open('out.txt') as outfile:
    writer = csv.writer(outfile)
        