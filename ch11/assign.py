import re
fname = raw_input('Enter filename: ')
if len(fname) == 0: fname = 'regex_sum_42.txt'
try:
    fhand = open(fname)
except:
    print "Can't open file. Please try again."
    exit()

total = 0
for line in fhand:
    results = re.findall('[0-9]+', line)
    # print results
    total = total + sum([int(i) for i in results])

print 'Sum',total