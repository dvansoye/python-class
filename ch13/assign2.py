import urllib
import json

url = raw_input('Enter location: ')
print 'Retrieving', url

uhand = urllib.urlopen(url)
data = uhand.read()
print 'Retrieved',len(data),'characters'
js = json.loads(str(data))
# print json.dumps(js, indent=4)

sum = 0
lst = js['comments']
for item in lst:
   sum = sum + int(item['count'])
   
print 'Count:', len(lst)
print 'Sum:', sum