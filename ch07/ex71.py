try:
    mbox = open('../data/mbox-short.txt')
except:
    print "Could not open file"

for line in mbox:
    line = line.upper()
    print line
