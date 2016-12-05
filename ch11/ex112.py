import re
fname = raw_input('Enter file: ')
fhand = open('../data/'+fname)
count = 0
total =0
for line in fhand:
    # print line
    results = re.findall('^New Revision: ([0-9]+)',line)
    if len(results) > 0:
        print line
        print results[0]
        count += 1
        total = total + int(results[0])
    # elif len(results) > 1:
    #    print 'Error: more than one revisions found in a line'
average = float(total)/float(count)
print average