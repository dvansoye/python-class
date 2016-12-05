import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
count = 0
sum = 0 

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    count = count + 1
    sum = sum + int(tag.contents[0])

print 'Count', count
print 'Sum', sum