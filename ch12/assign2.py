import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))
i = 0

while i <= count:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    print ' Retrieveing:', url
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    
    # Locate the one indicated by the position param
    url = tags[position-1].get('href', None)
    i = i + 1