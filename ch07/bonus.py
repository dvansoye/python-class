# Use http://www.pythonlearn.com/code/words.txt as the file name
import urllib2
fname = raw_input("Enter file name: ")
fh = urllib2.urlopen(fname)
for line in fh:
    print line.upper().rstrip()