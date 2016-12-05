import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url

uhand = urllib.urlopen(url)
data = uhand.read()
print 'Retrieved',len(data),'characters'
# print data
tree = ET.fromstring(data)

sum = 0
counts = tree.findall('.//count')
for count in counts:
   sum = sum + int(count.text)
   
print 'Count:', len(counts)
print 'Sum:', sum