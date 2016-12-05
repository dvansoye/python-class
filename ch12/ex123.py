import urllib

url = raw_input("Please enter URL to open (don't include the HTTP://): ")

try:
    fhand = urllib.urlopen('http://'+url)
except:
    print 'Could not open URL. Please try again'
    quit()

chars = 0
for line in fhand:
    chars = chars + len(line)
    if chars <= 3000:
        print '***BEG***',line;

print 'File size:',chars