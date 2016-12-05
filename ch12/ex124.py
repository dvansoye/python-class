# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the paragraph tags
tags = soup('p')
#print tags

count = 0 
for tag in tags:
    count = count + 1

print 'Found ' + str(count) + ' <p> tags'